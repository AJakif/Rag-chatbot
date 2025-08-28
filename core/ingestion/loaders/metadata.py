from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class UploadMeta:
    filename: str
    content_type: str
    bot_name: str
    size_bytes: Optional[int] = None
    extra: Optional[Dict] = None
