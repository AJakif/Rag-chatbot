from pathlib import Path
from typing import Union
from .metadata import UploadMeta
from .base_loader import BaseUploader
from .json_loader import JSONUploader
from .xml_loader import XMLUploader
from .pdf_loader import PDFUploader

EXT_MAP = {
    ".json": JSONUploader,
    ".ndjson": JSONUploader,
    ".xml": XMLUploader,
    ".pdf": PDFUploader,
}

def get_uploader(upload_id: str, source_path: Union[str, Path], meta: UploadMeta, storage=None) -> BaseUploader:
    ext = Path(source_path).suffix.lower()
    cls = EXT_MAP.get(ext)
    if not cls:
        raise ValueError(f"Unsupported file extension: {ext}")
    return cls(upload_id, source_path, meta, storage=storage)
