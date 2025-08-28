from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Iterable, Union
import hashlib, json, time

from .metadata import UploadMeta
from .storage_local import LocalFSStorage  # default; swap with S3Storage in prod

class BaseUploader(ABC):
    """validate → stream_iter → stage → store"""

    STAGING_ROOT = Path("data/staging")
    OUTPUT_NAME = "normalized.ndjson"

    def __init__(
        self,
        upload_id: str,
        source_path: Union[str, Path],
        meta: UploadMeta,
        storage=None,
        bucket: str = "ingestion",
    ):
        self.upload_id = upload_id
        self.source_path = Path(source_path)
        self.meta = meta
        self.bucket = bucket
        self.storage = storage or LocalFSStorage()
        self._start_ts = time.time()
        self.staging_dir = self.STAGING_ROOT / upload_id
        self.staging_dir.mkdir(parents=True, exist_ok=True)

    # hooks
    @abstractmethod
    def validate_source(self) -> None: ...

    @abstractmethod
    def stream_iter(self) -> Iterable[Dict]: ...

    # shared impl
    def write_staging(self) -> Path:
        out_path = self.staging_dir / self.OUTPUT_NAME
        with out_path.open("w", encoding="utf-8") as f:
            for rec in self.stream_iter():
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        return out_path

    def _sha256(self, path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as fp:
            for chunk in iter(lambda: fp.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()

    def finalize(self, staged_path: Path) -> Dict:
        # Per-bot namespacing
        key = f"{self.meta.bot_name}/{self.upload_id}/{staged_path.name}"
        uri = self.storage.put_object(
            bucket=self.bucket,
            key=key,
            file_path=staged_path,
            content_type="application/x-ndjson",
        )
        return {
            "upload_id": self.upload_id,
            "bot_name": self.meta.bot_name,
            "artifact_uri": uri,
            "records_file": staged_path.name,
            "sha256": self._sha256(staged_path),
            "duration_s": round(time.time() - self._start_ts, 3),
        }

    def run(self) -> Dict:
        self.validate_source()
        staged = self.write_staging()
        return self.finalize(staged)
