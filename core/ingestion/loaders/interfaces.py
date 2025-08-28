from pathlib import Path
from typing import Protocol, Union

class StorageBackend(Protocol):
    def put_object(self, bucket: str, key: str, file_path: Union[str, Path], content_type: str) -> str:
        """Upload a file to storage and return a URI (e.g., s3://bucket/key)."""
        ...
