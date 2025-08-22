import os
from typing import List

def list_files(folder: str) -> List[str]:
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def next_available(dst_path: str) -> str:
    """Append _2, _3, ... to avoid collision if needed"""
    if not os.path.exists(dst_path):
        return dst_path
    base, ext = os.path.splitext(dst_path)
    i = 2
    while True:
        candidate = f"{base}_{i}{ext}"
        if not os.path.exists(candidate):
            return candidate
        i += 1