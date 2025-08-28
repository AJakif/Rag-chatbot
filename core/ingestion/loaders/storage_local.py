import shutil
from pathlib import Path
from typing import Union

class LocalFSStorage:
    """Simple local storage (good for dev/tests)."""
    def __init__(self, root: Union[str, Path] = "data/outputs"):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def put_object(self, bucket: str, key: str, file_path: Union[str, Path], content_type: str) -> str:
        dest = self.root / bucket / key
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, dest)
        return f"file://{dest.resolve()}"
