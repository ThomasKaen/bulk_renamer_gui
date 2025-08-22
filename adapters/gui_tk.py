import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from ..core import RenameOptions, RenameRule, RenameService
from ..core.io_utils import list_files

class BulkRenamerGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Bulk Renamer App")
        self.root.geometry("700x540")

        # State
        self.folder = tk.StringVar()
        self.prefix = tk.StringVar()
        self.suffix = tk.StringVar()
        self.find_text = tk.StringVar()
        self.replace_text = tk.StringVar()
        self.skip_existing = tk.BooleanVar(value=True)

        self._build()
        self.files: list[str] = []

    def _build(self):
        top = tk.Frame(self.root); top.pack(fill="x", padx=10, pady=(10,6))
        tk.Label(top, text="Folder:").pack(side="left")
        tk.Entry(top, textvariable=self.folder, width=60).pack(side="left", padx=6)
        tk.Button(top, text="Browse", command=self._choose_folder).pack(side="left")

        grid = tk.Frame(self.root); grid.pack(padx=10, pady=8)
        tk.Label(grid, text="Prefix").grid(row=0, column=0, sticky="e", padx=6, pady=3)
        tk.Entry(grid, textvariable=self.prefix, width=24).grid(row=0, column=1, pady=3)
        tk.Label(grid, text="Suffix").grid(row=1, column=0, sticky="e", padx=6, pady=3)
        tk.Entry(grid, textvariable=self.suffix, width=24).grid(row=1, column=1, pady=3)
        tk.Label(grid, text="Find").grid(row=2, column=0, sticky="e", padx=6, pady=3)
        tk.Entry(grid, textvariable=self.find_text, width=24).grid(row=2, column=1, pady=3)
        tk.Label(grid, text="Replace with").grid(row=3, column=0, sticky="e", padx=6, pady=3)
        tk.Entry(grid, textvariable=self.replace_text, width=24).grid(row=3, column=1, pady=3)

        opts = tk.Frame(self.root); opts.pack(fill="x", padx=10)
        tk.Checkbutton(opts, text="Skip existing / avoid overwrite", variable=self.skip_existing).pack(side="left")

        actions = tk.Frame(self.root); actions.pack(padx=10, pady=8)
        tk.Button(actions, text="Preview", command=self._preview).pack(side="left", padx=6)
        tk.Button(actions, text="Rename Files", command=self._rename).pack(side="left", padx=6)

        self.preview_box = tk.Text(self.root, height=16, wrap="none"); self.preview_box.pack(fill="both", expand=True, padx=10, pady=(4,10))

    def _choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder.set(folder)
            self._load_files()

    def _load_files(self):
        self.files = list_files(self.folder.get())
        self.preview_box.delete("1.0", tk.END)
        self.preview_box.insert(tk.END, f"Loaded {len(self.files)} files.\n")

    def _make_opts(self, dry: bool) -> RenameOptions:
        rule = RenameRule(
            prefix=self.prefix.get(),
            suffix=self.suffix.get(),
            find_text=self.find_text.get(),
            replace_text=self.replace_text.get(),
        )
        return RenameOptions(rule=rule, dry_run=dry, skip_existing=self.skip_existing.get())

    def _preview(self):
        if not self.folder.get():
            messagebox.showwarning("Choose folder", "Please select a folder first.")
            return
        service = RenameService(self.folder.get())
        opts = self._make_opts(dry=True)
        res = service.preview(self.files, opts)
        self.preview_box.delete("1.0", tk.END)
        for r in res:
            self.preview_box.insert(tk.END, f"{r.src_name} -> {r.dst_name}\n")

    def _rename(self):
        if not self.folder.get():
            messagebox.showwarning("Choose folder", "Please select a folder first.")
            return
        if not self.files:
            messagebox.showwarning("No files", "Folder appears empty.")
            return
        service = RenameService(self.folder.get(), log=lambda m: self.preview_box.insert(tk.END, m + "\n"))
        opts = self._make_opts(dry=False)
        res = service.execute(self.files, opts)
        ok = sum(1 for r in res if r.ok)
        err = sum(1 for r in res if not r.ok)
        messagebox.showinfo("Done", f"Renamed {ok} files. Errors: {err}")
        self._load_files()

if __name__ == "__main__":
    root = tk.Tk()
    app = BulkRenamerGUI(root)
    root.mainloop()
