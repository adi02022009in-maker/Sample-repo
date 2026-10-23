"""
Practical No. 24: Develop a notes or text editor GUI application using AI prompts.
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os

def main():
    root = tk.Tk()
    root.title("Untitled - Vibe Notes")
    root.geometry("680x520")

    file_path = None

    # 1. Main Text Area with Undo Support
    text_area = scrolledtext.ScrolledText(
        root,
        wrap=tk.WORD,
        undo=True,
        font=("Segoe UI", 11),
        relief="flat",
        padx=12,
        pady=10
    )
    text_area.pack(fill="both", expand=True)

    # 2. Status Bar for Line & Column Info
    status_bar = tk.Label(
        root,
        text="Ln 1, Col 1 | Words: 0 | UTF-8",
        font=("Segoe UI", 9),
        bg="#f1f5f9",
        fg="#475569",
        anchor="e",
        padx=15,
        pady=4,
        relief="groove"
    )
    status_bar.pack(fill="x", side="bottom")

    # 3. Text Editor Functions
    def update_status(event=None):
        cursor_pos = text_area.index(tk.INSERT)
        line, col = cursor_pos.split(".")
        content = text_area.get("1.0", tk.END).strip()
        word_count = len(content.split()) if content else 0
        status_bar.config(text=f"Ln {line}, Col {int(col)+1} | Words: {word_count} | UTF-8")

    text_area.bind("<KeyRelease>", update_status)
    text_area.bind("<ButtonRelease-1>", update_status)

    def new_file(event=None):
        nonlocal file_path
        if messagebox.askyesno("New File", "Start a new document? Unsaved changes will be lost."):
            text_area.delete("1.0", tk.END)
            file_path = None
            root.title("Untitled - Vibe Notes")
            update_status()

    def open_file(event=None):
        nonlocal file_path
        path = filedialog.askopenfilename(
            title="Open Note",
            filetypes=[("Text Documents (*.txt)", "*.txt"), ("Markdown (*.md)", "*.md"), ("All Files (*.*)", "*.*")]
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                text_area.delete("1.0", tk.END)
                text_area.insert("1.0", content)
                file_path = path
                root.title(f"{os.path.basename(path)} - Vibe Notes")
                update_status()
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(event=None):
        nonlocal file_path
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text_area.get("1.0", tk.END).rstrip("\n"))
                messagebox.showinfo("Saved", "Note saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
        else:
            save_as_file()

    def save_as_file():
        nonlocal file_path
        path = filedialog.asksaveasfilename(
            title="Save Note As",
            defaultextension=".txt",
            filetypes=[("Text Documents (*.txt)", "*.txt"), ("Markdown (*.md)", "*.md"), ("All Files (*.*)", "*.*")]
        )
        if path:
            file_path = path
            save_file()
            root.title(f"{os.path.basename(path)} - Vibe Notes")

    def show_about():
        messagebox.showinfo(
            "About Vibe Notes",
            "Vibe Notes Application\n"
            "Developed using Python 3.13 & Tkinter\n"
            "Subject: Vibe Coding (DI05000121)\n"
            "Govt. Polytechnic College, Jamnagar"
        )

    # 4. Create Standard Menu Bar
    menu_bar = tk.Menu(root)

    # File Menu
    file_menu = tk.Menu(menu_bar, tearoff=False)
    file_menu.add_command(label="New", accelerator="Ctrl+N", command=new_file)
    file_menu.add_command(label="Open...", accelerator="Ctrl+O", command=open_file)
    file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
    file_menu.add_command(label="Save As...", command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Edit Menu
    edit_menu = tk.Menu(menu_bar, tearoff=False)
    edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=lambda: text_area.event_generate("<<Undo>>"))
    edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=lambda: text_area.event_generate("<<Redo>>"))
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: text_area.event_generate("<<Cut>>"))
    edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: text_area.event_generate("<<Copy>>"))
    edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: text_area.event_generate("<<Paste>>"))
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=lambda: text_area.tag_add("sel", "1.0", "end"))
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    # Help Menu
    help_menu = tk.Menu(menu_bar, tearoff=False)
    help_menu.add_command(label="About Vibe Notes", command=show_about)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    root.config(menu=menu_bar)

    # 5. Keyboard Shortcuts
    root.bind("<Control-n>", new_file)
    root.bind("<Control-N>", new_file)
    root.bind("<Control-o>", open_file)
    root.bind("<Control-O>", open_file)
    root.bind("<Control-s>", save_file)
    root.bind("<Control-S>", save_file)

    # Sample default note
    initial_note = (
        "WELCOME TO VIBE NOTES\n"
        "=====================\n\n"
        "This full-featured desktop text editor was built using Python and Tkinter.\n\n"
        "Features:\n"
        "• Native File Menu (New, Open, Save, Save As, Exit)\n"
        "• Edit Menu (Cut, Copy, Paste, Undo, Redo, Select All)\n"
        "• Keyboard Shortcuts (Ctrl+N, Ctrl+O, Ctrl+S)\n"
        "• Real-time Line, Column, and Word Count in Status Bar\n"
    )
    text_area.insert("1.0", initial_note)
    update_status()

    root.mainloop()

if __name__ == "__main__":
    main()
