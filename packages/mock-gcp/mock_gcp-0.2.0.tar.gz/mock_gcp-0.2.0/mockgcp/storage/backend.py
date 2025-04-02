from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from mockgcp.storage.blob import MockBlob
    from mockgcp.storage.bucket import MockBucket


class StorageBackend:
    _projects: ClassVar[dict[str, StorageBackend]] = {}

    def __new__(cls, project):
        if project not in cls._projects:
            cls._projects[project] = super().__new__(cls)
        return cls._projects[project]

    def __init__(self, project) -> None:
        if not hasattr(self, "project"):
            self.project = project

            self._tmp = TemporaryDirectory()
            self.data_dir = Path(self._tmp.name)
            self.buckets: dict[str, MockBucket] = {}
            self.blobs: dict[str, dict[str, MockBlob]] = {}

    def __del__(self) -> None:
        self._tmp.cleanup()
