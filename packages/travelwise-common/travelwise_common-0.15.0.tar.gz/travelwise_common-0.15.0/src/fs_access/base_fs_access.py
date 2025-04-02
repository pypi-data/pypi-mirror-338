import glob
import os
import re
from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import IO, Optional, Any


class BaseFSAccess(ABC):
    @property
    def file_type(self) -> str:
        raise NotImplementedError()

    def get_file_paths(
        self, directory: str, file_regex: Optional[str] = None
    ) -> list[str]:
        file_paths = glob.glob(
            os.path.join(directory, "**", f"*.{self.file_type.lower()}"),
            recursive=True,
        )

        if file_regex:
            pattern = re.compile(file_regex)
            file_paths = [
                path for path in file_paths if pattern.search(os.path.basename(path))
            ]

        return file_paths

    @contextmanager
    def open(self, path: str, mode: str = "r") -> IO:
        with open(path, mode) as f:
            yield f

    @abstractmethod
    def read(self, path: str) -> Any:
        """
        :param path: the file path to read from
        :return: a python object representing the data (e.g. dictionary, list, etc.) as appropriate
        """
        raise NotImplementedError()

    @abstractmethod
    def save(self, data: Any, path: str) -> None:
        """
        :param data: the data to save to the file path (python objects)
        :param path: the path to save to
        """
        raise NotImplementedError()
