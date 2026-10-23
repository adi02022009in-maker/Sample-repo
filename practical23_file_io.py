"""
Practical No. 23: Implement file read/write operations in a desktop application.
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os

def main():
    root = tk.Tk()
    root.title("Practical 23: File Read & Write Operations")
    root.geometry("580x480")
    root.configure(bg="#f8fafc")
    root.resizable(False, False)

    current_file_path = None

    # 1. Header Banner
    header = tk.Label(
        root,
        text="Desktop File Manager (Read / Write)",
        font=("Segoe UI", 16, "bold"),
        bg="#0f766e",
        fg="#ffffff",
        pady=12
    )
    header.pack(fill="x")

    # 2. Controls / Toolbar Frame
    toolbar = tk.Frame(root, bg="#ffffff", padx=15, pady=10, relief="solid", bd=1)
    toolbar.pack(fill="x", padx=15, pady=(15, 5))

    # 3. Text Area with Scrollbar
    text_frame = tk.Frame(root, padx=15, pady=5, bg="#f8fafc")
    text_frame.pack(fill="both", expand=True)

    text_area = scrolledtext.ScrolledText(
        text_frame,
        wrap=tk.WORD,
        font=("Consolas", 11),
        relief="solid",
        bd=1,
        padx=10,
        pady=10
    )
    text_area.pack(fill="both", expand=True)

    # 4. Status Bar
    status_var = tk.StringVar(value="Status: Ready | No file loaded")
    status_bar = tk.Label(
        root,
        textvariable=status_var,
        font=("Segoe UI", 9),
        bg="#e2e8f0",
        fg="#334155",
        anchor="w",
        padx=12,
        pady=5
    )
    status_bar.pack(fill="x", side="bottom")

    # 5. File Operations Logic
    def open_file():
        nonlocal current_file_path
        filepath = filedialog.askopenfilename(
            title="Open Text File",
            filetypes=[("Text Files (*.txt)", "*.txt"), ("All Files (*.*)", "*.*")]
        )
        if filepath:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                text_area.delete("1.0", tk.END)
                text_area.insert("1.0", content)
                current_file_path = filepath
                filename = os.path.basename(filepath)
                status_var.set(f"Loaded: {filename} | Length: {len(content)} chars")
                messagebox.showinfo("File Read Success", f"Successfully read '{filename}'!")
            except Exception as e:
                messagebox.showerror("Read Error", f"Failed to read file: {e}")

    def save_file():
        nonlocal current_file_path
        filepath = filedialog.asksaveasfilename(
            title="Save Text File",
            defaultextension=".txt",
            filetypes=[("Text Files (*.txt)", "*.txt"), ("All Files (*.*)", "*.*")]
        )
        if filepath:
            try:
                content = text_area.get("1.0", tk.END).rstrip("\n")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                current_file_path = filepath
                filename = os.path.basename(filepath)
                status_var.set(f"Saved: {filename} | Total characters: {len(content)}")
                messagebox.showinfo("File Write Success", f"File saved successfully as '{filename}'!")
            except Exception as e:
                messagebox.showerror("Write Error", f"Failed to save file: {e}")

    def clear_text():
        text_area.delete("1.0", tk.END)
        status_var.set("Text area cleared. Ready for new input.")

    # Add Buttons to Toolbar
    btn_open = tk.Button(toolbar, text="📂 Open & Read", font=("Segoe UI", 10, "bold"), bg="#0284c7", fg="#fff", padx=10, pady=5, relief="flat", cursor="hand2", command=open_file)
    btn_open.pack(side="left", padx=5)

    btn_save = tk.Button(toolbar, text="💾 Write & Save", font=("Segoe UI", 10, "bold"), bg="#16a34a", fg="#fff", padx=10, pady=5, relief="flat", cursor="hand2", command=save_file)
    btn_save.pack(side="left", padx=5)

    btn_clear = tk.Button(toolbar, text="🗑️ Clear Text", font=("Segoe UI", 10), bg="#ef4444", fg="#fff", padx=10, pady=5, relief="flat", cursor="hand2", command=clear_text)
    btn_clear.pack(side="left", padx=5)

    # Insert default helper text
    sample_text = (
        "Practical 23: File Read/Write Operations in Python Tkinter\n"
        "----------------------------------------------------------\n"
        "Student Name: Rahul Sharma\n"
        "Enrollment No: 246250307086\n"
        "Branch: Computer Engineering\n"
        "Subject: Application Design & Development using Vibe Coding\n\n"
        "You can edit this text and click 'Write & Save' to write to disk,\n"
        "or click 'Open & Read' to open any existing file."
    )
    text_area.insert("1.0", sample_text)
    status_var.set(f"Ready: Sample content loaded ({len(sample_text)} characters)")

    root.mainloop()

if __name__ == "__main__":
    main()
