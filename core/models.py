from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class RenameRule:
    prefix: str = ""
    suffix: str = ""
    find_text: str = ""
    replace_text: str = ""

@dataclass(frozen=True)
class RenameOptions:
    rule: RenameRule
    dry_run: bool = True
    skip_existing: bool = True

@dataclass
class RenameResult:
    src_name: str
    dst_name: str
    ok: bool
    reason: Optional[str] = None