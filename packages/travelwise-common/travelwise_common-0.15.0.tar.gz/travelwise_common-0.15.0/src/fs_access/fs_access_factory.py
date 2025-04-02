from enum import Enum

from src.fs_access.base_fs_access import BaseFSAccess
from src.fs_access.json_fs_access.json_fs_access import JSONFSAccess


class FileType(Enum):
    JSON = "json"


class FSAccessFactory:
    @staticmethod
    def create_fs_access(file_type: FileType) -> BaseFSAccess:
        if file_type == FileType.JSON:
            return JSONFSAccess()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
