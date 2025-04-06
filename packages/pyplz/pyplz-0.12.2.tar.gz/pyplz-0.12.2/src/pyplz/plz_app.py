from __future__ import annotations

import importlib.util
import inspect
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

from dotenv import dotenv_values, load_dotenv
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from pyplz.command import Command
from pyplz.console_utils import ConsoleUtils
from pyplz.task import Task
from pyplz.types import CallableWithArgs

console = Console()


class PlzApp:
    def __init__(self) -> None:
        self._tasks: dict[str, Task] = dict()
        self._user_configured = False
        self._configured_envs: list[list[str]] = []

    def _reset(self):
        self._tasks = dict()
        self._user_configured = False

    def configure(self, env: dict[str, str] | None = None):
        self._user_configured = True
        self._dotenv = self._load_env_dotenv()

        if env:
            env_vars = [[k, v] for k, v in env.items()]
            self._configured_envs = env_vars
            self._load_env_vars(env_vars)

    def list_tasks(self):
        """List all available tasks."""
        if all(t.is_builtin for t in self._tasks.values()):
            self.print_error("No tasks have been registered. plz expects at least one `@plz.task` in your plzfile.py")
            return

        max_command_length = max(len(t.name) + 5 for t in self._tasks.values())
        max_command_length = min(max_command_length, 25)

        max_desc_length = max(len(t.desc) * 2 for t in self._tasks.values() if t.desc is not None)
        max_desc_length = min(max_desc_length, 50)

        table = Table(show_header=False, box=None, show_edge=False)
        table.add_column("Tasks", style="orange1", no_wrap=True, width=max_command_length + 2)
        table.add_column("Description", style="white", no_wrap=True, width=max_desc_length + 2)

        for t in self._tasks.values():
            desc = t.desc or ""
            name = t.name
            if t.is_default:
                name = f"[bold]{name}[/bold]"
                desc = f"[bold]{desc}\t(default)[/bold]"
            table.add_row(f"{name}", desc)

        panel_width = max_command_length + max_desc_length + 4

        # Ensure the panel width does not exceed terminal width
        terminal_width = console.size.width

        final_width = min(panel_width, terminal_width)

        panel = Panel(
            table,
            title="Tasks",
            title_align="left",
            border_style="dark_orange3",
            padding=(0, 1),
            box=box.ROUNDED,
            width=final_width,
        )
        console.print(panel)

    def _get_dotenv_path(self) -> Path:
        return Path(os.getcwd()) / ".env"

    def _load_env_dotenv(self) -> list[list[str]]:
        env_path = self._get_dotenv_path()

        # Load the .env file if it exists
        if env_path.exists():
            # capture the env variables
            load_dotenv(env_path)
            # Load the environment variables into a variable
            env_vars_dict = dotenv_values(env_path)
            env_vars_list = [[k, v] for k, v in env_vars_dict.items() if v is not None]
            return env_vars_list

        return []

    def _try_execute_utility_commands(self, command: Command) -> bool:
        if command.has_task_specified():
            return False

        if command.list:
            self.list_tasks()
            return True

        if command.show_env:
            self._print_env(cmd=command)
            return True

        if command.show_env_all:
            self._print_env(cmd=command, all=True)
            return True

        return False

    def _get_default_task(self) -> Task | None:
        default_tasks = [t for t in self._tasks.values() if t.is_default]

        if len(default_tasks) > 1:
            self.fail("More than one default task found: " + ", ".join(t.name for t in default_tasks))

        if len(default_tasks) == 0:
            return None
        return default_tasks[0]

    def _try_execute_default_task(self, command: Command) -> bool:
        if command.has_task_specified():
            return False

        if not command.is_default():
            return False

        default_task = self._get_default_task()
        if default_task is None:
            self.list_tasks()
            return True
        else:
            default_task()
            return True

    def _try_execute_task(self, command: Command) -> bool:
        if not command.has_task_specified():
            return False

        assert command.task is not None

        if command.show_env:
            self._print_env(cmd=command)
            return True

        kwargs = command.task_kwargs or {}
        command.task(**kwargs)
        return True

    def _load_env_cli(self, command: Command):
        self._load_env_vars(command.env)

    def _load_env_vars(self, env_vars: list[list[str]]):
        for k, v in env_vars:
            os.environ[k] = v

    def _load_plzfile(self):
        # wrapping with internal to make mocking possible in tests
        # test_import for example would need to actually import
        # while most other tests won't
        self._internal_load_plzfile()

    def _internal_load_plzfile(self):
        plzfile_path = os.path.join(os.getcwd(), "plzfile.py")
        spec = importlib.util.spec_from_file_location("plzfile", plzfile_path)
        plzfile = importlib.util.module_from_spec(spec)  # type: ignore

        # plz loads the CWD to the sys.path to allow plzfile to import freely
        sys.path.append(os.path.join(os.getcwd()))

        spec.loader.exec_module(plzfile)  # type: ignore

    def _main_execute(self, command: Command):
        if not self._user_configured:
            self.configure()

        self._load_env_cli(command)

        if self._try_execute_utility_commands(command):
            return

        if self._try_execute_default_task(command):
            return

        if self._try_execute_task(command):
            return

        self.fail("Execution failed for unknown reason.")

    def task(
        self,
        name: str | None = None,
        desc: str | None = None,
        default: bool = False,
        requires: Callable | list[Callable | CallableWithArgs] | None = None,
        env: dict[str, Any] | None = None,
    ) -> Callable:
        """Defines a plz task that can be executed from the command line.

        Functions decorated with `plz.task` will be registered as tasks that can be executed from the command line.
        They can also accept arguments which will get documented in the task's help message.
        Also, you can declare *args to accept any number of positional arguments.

        Args:
            name (str, optional): _description_. Defaults to the method name (with underscores replaced with hyphens).
            desc (str, optional): _description_. Defaults to the method's docstring.
            default (bool, optional): _description_. Defaults to False. If True, this task will be executed if no task
                explicilty specified.
            requires (Callable | list[Callable  |  CallableWithArgs] | None, optional): _description_. Defaults to None.
                Defines the required tasks that will be executed before this task. Can be a single task (functions),
                or a list of tasks (optionally with arguments). See examples below, or refrence the docs for more
                information.
            env (dict[str, Any] | None, optional): _description_. Defaults to None. Defines task-level environment
                variables that will be set before the task is executed.
        """

        def decorator(func) -> Callable:
            t_name: str = name or func.__name__
            # Replace underscores with hyphens to use kebab-case
            t_name = t_name.replace("_", "-")

            t_desc = desc
            if desc is None:
                t_desc = inspect.cleandoc(func.__doc__) if func.__doc__ else ""

            # Nomralize requires to list of tuples
            _required = requires
            required_funcs: list[CallableWithArgs]
            if _required is None:
                required_funcs = []
            elif isinstance(_required, list):
                # Normalize callable with args to tuple as well
                required_funcs = [r if isinstance(r, tuple) else (r, ()) for r in _required]
            else:
                required_funcs = [(_required, ())]
            required_tasks = [(self._tasks[r.__name__], args) for r, args in required_funcs]

            self._tasks[t_name] = Task(
                func=func, name=t_name, desc=t_desc, is_default=default, requires=required_tasks, task_env_vars=env
            )

            return func

        return decorator

    @staticmethod
    def print_error(msg: str, silent: bool = False, exit: bool = False):
        PlzApp.print(msg, "red", silent=silent)
        if exit:
            sys.exit(1)

    @staticmethod
    def print_warning(msg: str, silent: bool = False):
        PlzApp.print(msg, "yellow", silent=silent)

    @staticmethod
    def print_weak(msg: str, silent: bool = False):
        PlzApp.print(msg, "bright_black", silent=silent)

    @staticmethod
    def print(msg: str, color: str | None = None, silent: bool = False):
        if silent:
            return

        if color:
            msg = f"[{color}]{msg}[/]"
        console.print(msg)

    @staticmethod
    def fail(msg: str | None = None):
        if msg is not None:
            PlzApp.print_error(msg)
        sys.exit(1)

    def _print_env(self, cmd: Command, all: bool = False):
        """
        prints the environment variable
        """
        ConsoleUtils.print_box(title=".env", rows=self._dotenv, sort=True)
        if self._configured_envs:
            ConsoleUtils.print_box(title="configured", rows=self._configured_envs, sort=True)
        if cmd.task is not None:
            task_envs = [[key, value] for key, value in cmd.task.task_env_vars.items()]
            ConsoleUtils.print_box(title="task-definition", rows=task_envs, sort=True)
        ConsoleUtils.print_box(title="in-line", rows=cmd.env, sort=True)
        if all:
            env_vars = os.environ
            rows = [[key, value] for key, value in env_vars.items()]
            rows = [row for row in rows if row not in self._dotenv]
            ConsoleUtils.print_box(title="All (rest)", rows=rows, sort=True)

    def run(
        self,
        command: str,
        env: dict[str, str] | None = None,
        dry_run: bool = False,
        echo: bool = True,
        raise_error: bool = True,
    ) -> int:
        """
        Executes a shell command with optional environment variables, timeout, and dry run mode, and more.
        Args:
            command (str): The shell command to execute.
            env (dict[str, str], optional): A dictionary of environment variables to set for the command.
                Defaults to None.
            dry_run (bool): If True, the command will not be executed, and a dry run message will be printed.
                Defaults to False.
            echo (bool): If True, the command will be printed before execution (with environment variables replaced).
                Defaults to True.
            raise_error (bool): If True, a CalledProcessError will be raised if the command returns a non-zero
                exit status. Defaults to True.
        Returns:
            The standard output of the command if it was successful or the standard error if it failed.
        Raises:
            subprocess.CalledProcessError: If the command returns a non-zero exit status.
        """
        # Merge provided env with the current environment variables
        env = {**os.environ, **(env or {})}

        # replace env variables in the command
        def replace_env_var(match):
            var_name = match.group(1)
            return env.get(var_name, f"${{{var_name}}}")

        command_w_vars = re.sub(r"\$(\w+)", replace_env_var, command)

        if echo and not dry_run:
            self.print_weak(f"Executing: `{command_w_vars}`")

        if dry_run:
            self.print_warning(f"Dry run: `{command_w_vars}`")
            return 0

        ec = os.system(command_w_vars)

        if raise_error and ec != 0:
            raise subprocess.CalledProcessError(ec, command)

        return ec

    def ask(self, question: str | None = None, silent: bool = False) -> bool:
        """
        Asks the user a yes/no question and returns a boolean based on the response.

        Args:
            question (str): The question to ask the user. Defaults to "Are you sure [y] / [n]".
            silent (bool): If True, response will not be declared. Defaults to False.
        Returns:
            bool: True if the user responds with 'y' or 'Y', False otherwise.
        """
        if question is None:
            question = "Are you sure you want to proceed? (y/n) [n]:"
        while True:
            response = input(f"{question} ").strip().lower()
            if response in ["y", "n", "Y", "N", ""]:
                if response.lower() == "y":
                    self.print_weak("Accepted", silent=silent)
                    return True
                else:
                    self.print_weak("Declined", silent=silent)
                    return False
            self.print_warning("Please respond with 'y' or 'n'. Enter will default to 'n'.")


plz = PlzApp()
