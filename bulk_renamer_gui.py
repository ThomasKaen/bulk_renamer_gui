import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk Renamer App")
        self.root.geometry("600x500")

        self.folder_path = tk.StringVar()
        self.prefix = tk.StringVar()
        self.suffix = tk.StringVar()
        self.find_text = tk.StringVar()
        self.replace_text = tk.StringVar()

        self.create_widgets()
        self.files = []

    def create_widgets(self):
        # Folder selection
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=10, fill="x")

        tk.Label(folder_frame, text="Select Folder:").pack(side="left", padx=5)
        tk.Entry(folder_frame, textvariable=self.folder_path, width=50).pack(side="left", padx=5)
        tk.Button(folder_frame, text="Browse", command=self.browse_folder).pack(side="left")

        # Rename options
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=10)

        tk.Label(options_frame, text="Prefix:").grid(row=0, column=0, padx=5, pady=2)
        tk.Entry(options_frame, textvariable=self.prefix).grid(row=0, column=1, padx=5)

        tk.Label(options_frame, text="Suffix:").grid(row=1, column=0, padx=5, pady=2)
        tk.Entry(options_frame, textvariable=self.suffix).grid(row=1, column=1, padx=5)

        tk.Label(options_frame, text="Find:").grid(row=2, column=0, padx=5, pady=2)
        tk.Entry(options_frame, textvariable=self.find_text).grid(row=2, column=1, padx=5)

        tk.Label(options_frame, text="Replace with:").grid(row=3, column=0, padx=5, pady=2)
        tk.Entry(options_frame, textvariable=self.prefix).grid(row=3, column=1, padx=5)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Preview", command=self.preview_renaming).pack(side="left", padx=10)
        tk.Button(button_frame, text="Rename Files", command=self.rename_files).pack(side="left", padx=10)

        # Preview area
        self.preview_box = tk.Text(self.root, height=15, wrap="none")
        self.preview_box.pack(padx=10, pady=10, fill="both", expand=True)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
            self.load_files()

    def load_files(self):
        self.files = [f for f in os.listdir(self.folder_path.get()) if os.path.isfile(os.path.join(self.folder_path.get(), f))]
        self.preview_box.delete("1.0", tk.END)
        self.preview_box.insert(tk.END, f"Loaded {len(self.files)} files.\n")

    def preview_renaming(self):
        self.preview_box.delete("1.0", tk.END)
        for filename in self.files:
            name, ext = os.path.splitext(filename)
            new_name = name

            # Apply rules
            if self.find_text.get():
                new_name = new_name.replace(self.find_text.get(), self.replace_text.get())
            if self.prefix.get():
                new_name = self.prefix.get() + new_name
            if self.suffix.get():
                new_name = new_name + self.suffix.get()

            new_filename = new_name + ext
            self.preview_box.insert(tk.END, f"{filename} -> {new_filename}\n")

    def rename_files(self):
        folder = self.folder_path.get()
        count = 0
        for filename in os.listdir(folder):
            name, ext = os.path.splitext(filename)
            new_name = name

            if self.find_text.get():
                new_name = new_name.replace(self.find_text.get(), self.replace_text.get())
            if self.prefix.get():
                new_name = self.prefix.get() + new_name
            if self.suffix.get():
                new_name = new_name + self.suffix.get()

            new_filename = new_name + ext
            src = os.path.join(folder, filename)
            dst = os.path.join(folder, new_filename)

            if not os.path.exists(dst):
                os.rename(src, dst)
                count += 1

        messagebox.showinfo("Done", f"Renamed {count} files.")
        self.load_files()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()













