from __future__ import annotations

import inspect
import os

from typing import Any, Callable

from rich.console import Console


console = Console()


class Task:
    def __init__(
        self,
        func: Callable,
        name: str | None = None,
        desc: str | None = None,
        requires: list[tuple[Task, tuple]] | None = None,  # List of tuples of tasks and their arguments
        is_default: bool = False,
        is_builtin: bool = False,
        task_env_vars: dict[str, Any] | None = None,
    ) -> None:
        self.func = func
        self.name = name or func.__name__
        desc = desc or ""
        if len(desc) == 0 and func.__doc__ is not None:
            desc = inspect.cleandoc(func.__doc__)
        self.desc = desc
        self.is_default = is_default
        self.is_builtin = is_builtin

        # normalize requires
        if requires is None:
            requires = []
        self.requires = requires

        # normalize task-scope environment variables
        if task_env_vars is None:
            task_env_vars = {}
        self.task_env_vars = task_env_vars

    def __call__(self, *args, **kwargs) -> Any:
        """
        Call the task function and return the result.
        If the task function has any required functions, they will be called first (recursively).
        #"""
        # load task-level environment variables
        for key, value in self.task_env_vars.items():
            os.environ[key] = value

        # Invoke required tasks first
        for r_task, r_args in self.requires:
            r_task(*r_args)

        ret = self.func(*args, **kwargs)
        if ret is not None:
            console.print(ret)

    def __str__(self) -> str:
        tags = []
        if self.is_default:
            tags.append("[default]")
        if self.is_builtin:
            tags.append("[builtin]")
        tags_str = (" " + " ".join(tags)) if tags else ""
        return self.name + tags_str

    def __repr__(self) -> str:
        return self.__str__()
