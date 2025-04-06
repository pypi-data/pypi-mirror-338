import argparse

from pyplz.command import Command
from pyplz.exceptions import TaskNotFoundError
from pyplz.plz_app import PlzApp
from pyplz.task import Task
from pyplz.task_parser import TaskParser


class PlzParser:
    def __init__(self, plz_app: PlzApp, task_parser: TaskParser):
        self.plz_app = plz_app
        self.task_parser = task_parser
        self.parser = argparse.ArgumentParser(description="plz - A python-first task runner.", add_help=True)
        self.parser.add_argument("-l", "--list", action="store_true", help="List all available tasks.")
        self.parser.add_argument(
            "-e", "--env", action="append", help="Inline environment variable (KEY=VALUE). Can be used multiple times."
        )
        self.parser.add_argument("--show-env", action="store_true", help="Show all pyplz environment variables.")
        self.parser.add_argument(
            "--show-env-all", action="store_true", help="Show all available environment variables."
        )
        self.parser.add_argument("task", nargs=argparse.REMAINDER, help="The task to run. Use -l to list tasks.")

    def parse(self, args: list[str]) -> Command:
        parsed_args = self.parser.parse_args(args)

        # Parse inline environment variables if provided.
        if parsed_args.task:
            cmd = self.parse_task(parsed_args.task)
            cmd._env = parsed_args.env
        else:
            cmd = Command(
                list=parsed_args.list,
                _env=parsed_args.env,
                show_env=parsed_args.show_env,
                show_env_all=parsed_args.show_env_all,
            )

        return cmd

    def list_tasks(self):
        # Implement the logic to list all available tasks
        print("Listing all available tasks...")

    def parse_task(self, task_with_args: list[str]) -> Command:
        task_name = task_with_args[0]
        if "_" in task_name:
            # allowing user to input snake_case instead of kebab-case
            task_name = task_name.replace("_", "-")
        if task_name not in self.plz_app._tasks:
            raise TaskNotFoundError(task_name=task_name)
        if len(task_with_args) > 1:
            task_args = task_with_args[1:]
        else:
            task_args = []

        task: Task = self.plz_app._tasks[task_name]
        # Implement the logic to run the task with the provided arguments

        cmd = self.task_parser.parse(task=task, args=task_args)

        return cmd
