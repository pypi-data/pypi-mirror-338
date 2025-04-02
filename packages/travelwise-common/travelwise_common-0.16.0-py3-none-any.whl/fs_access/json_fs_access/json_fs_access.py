import json
from typing import Any

from fs_access.base_fs_access import BaseFSAccess


class JSONFSAccess(BaseFSAccess):
    @property
    def file_type(self) -> str:
        return "json"

    def read(self, path: str) -> Any:
        with self.open(path) as f:
            json_data = json.load(f)
        return json_data

    def save(self, data: Any, path: str) -> None:
        with self.open(path, "w") as f:
            json.dump(data, f, indent=4)
