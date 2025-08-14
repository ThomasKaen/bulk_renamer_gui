# 🖥️ Bulk File Renamer — GUI (Windows)

A simple Windows app to **bulk-rename files** with a friendly interface.  
Pick a folder → set rules (prefix, suffix, find/replace) → **Preview** → **Rename**.

Perfect for cleaning messy downloads, photo sets, scans, exports, or client deliverables.

---

## ✨ Features
- Prefix / Suffix (e.g. add `IMG_` or `_final`)
- Find & Replace inside filenames (e.g. remove `_copy`)
- Live **Preview** of the new names before applying
- Skips files if the target name already exists (no overwrite)
- No command line needed — **double-click app**

---

## 📦 Run from Source

1) Install Python 3.10+ (Windows): https://www.python.org/downloads/  
2) Open PowerShell in the project folder and create a venv:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
3) Run the app:
   ```powershell
   python bulk_file_renamer_gui.py
   ```

> `tkinter` ships with most Windows Python installers. If you’re missing it, reinstall Python using the official installer and check “tcl/tk”.

---

## 🛠 How to Use
1. **Browse** → choose the folder with the files you want to rename  
2. Fill any of: **Prefix**, **Suffix**, **Find**, **Replace with**  
3. Click **Preview** to see `old → new` names  
4. Click **Rename Files** to apply changes

Notes:
- The app only renames **files** in the selected folder (not subfolders)
- If a target filename already exists, that file is **skipped** safely

---

## 🚀 Build a Standalone `.exe` (Windows)

Create/activate venv (if not done):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install PyInstaller:
```powershell
pip install pyinstaller
```

Build:
```powershell
pyinstaller --onefile --windowed bulk_file_renamer_gui.py
```

Optional with an icon:
```powershell
pyinstaller --onefile --windowed --icon icon.ico bulk_file_renamer_gui.py
```

Result: `dist\bulk_file_renamer_gui.exe`

If you need a clean rebuild:
```powershell
rmdir /s /q build dist
del *.spec
pyinstaller --onefile --windowed bulk_file_renamer_gui.py
```

---

## 🧩 Roadmap / Ideas
- Recursive mode (include subfolders)
- Date/timestamp stamping
- Case options (lower/UPPER)
- CSV log of renames
- Config presets

---

## 🐞 Troubleshooting
- **SmartScreen warning**: Click *More info* → *Run anyway* (unsigned apps trigger this).
- **Missing `tkinter`**: Reinstall Python from python.org (Windows installer includes Tcl/Tk).
- **Paths with spaces**: Wrap paths in quotes in PowerShell.
- **Permission errors**: Make sure files aren’t open/locked by another app.

---

## 📄 License
MIT — free to use and modify.

---

## 👋 Hire / Contact
I build small, useful tools that make messy workflows simple.  
If you want a custom version or extra features, reach out via my Fiverr profile.
