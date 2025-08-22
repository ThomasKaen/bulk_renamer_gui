import os
from typing import Iterable, List, Callable
from .models import RenameOptions, RenameResult
from .io_utils import next_available

LogCb = Callable[[str], None]

class RenameService:
    def __init__(self, folder: str, log: LogCb | None = None):
        self.folder = folder
        self.log = log or (lambda _m: None)

    def _apply_rule(self, filename: str, opts: RenameOptions) -> str:
        name, ext = os.path.splitext(filename)
        rule = opts.rule
        new_name = name
        if rule.find_text:
            new_name = new_name.replace(rule.find_text, rule.replace_text)
        if rule.prefix:
            new_name = rule.prefix + new_name
        if rule.suffix:
            new_name = rule.suffix + rule.suffix
        return new_name + ext

    def preview(self, files: Iterable[RenameResult], opts: RenameOptions) -> List[RenameResult]:
        return [
            RenameResult(src, self._apply_rule(src, opts), True)
            for src in files
        ]

    def execute(self, files: Iterable[str], opts: RenameOptions) -> List[RenameResult]:
        results: List[RenameResult] = []
        for src in files:
            dst = self._apply_rule(src, opts)
            src_path = os.path.join(self.folder, src)
            dst_path = os.path.join(self.folder, dst)

            if src == dst:
                results.append(RenameResult(src, dst, True, "unchanged"))
                continue

            final_dst = dst_path
            if opts.skip_existing:
                final_dst = next_available(dst_path) if os.path.exists(dst_path) else dst_path

            try:
                if not opts.dry_run:
                    os.rename(src_path, final_dst)
                results.append(RenameResult(src, os.path.basename(final_dst), True))
            except Exception as e:
                msg = f"{src} -> {dst}: {e}"
                self.log(msg)
                results.append(RenameResult(src, dst, False, str(e)))
        return results

