"""
Practical No. 19: Configure Python environment with Tkinter and generate a basic GUI window.
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar
"""

import tkinter as tk
from tkinter import ttk

def main():
    # 1. Create the main application window
    root = tk.Tk()
    root.title("Practical 19: Basic Tkinter GUI Window")
    root.geometry("500x350")
    root.configure(bg="#f1f5f9")
    root.resizable(False, False)

    # 2. Main Title Label
    title_label = tk.Label(
        root,
        text="⚡ Vibe Coding - Tkinter Desktop App",
        font=("Segoe UI", 16, "bold"),
        bg="#1e1b4b",
        fg="#ffffff",
        pady=15
    )
    title_label.pack(fill="x")

    # 3. Content Frame
    frame = tk.Frame(root, bg="#ffffff", padx=25, pady=25, relief="groove", bd=1)
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    desc_label = tk.Label(
        frame,
        text="Welcome to Python GUI Programming!\n\nThis basic desktop window was generated using\nAI prompts in VS Code using Tkinter.",
        font=("Segoe UI", 11),
        bg="#ffffff",
        fg="#334155",
        justify="center"
    )
    desc_label.pack(pady=10)

    # 4. Status and Close Button
    status_label = tk.Label(
        frame,
        text="Status: Python 3.13 + Tkinter 8.6 Ready",
        font=("Segoe UI", 9, "italic"),
        bg="#ffffff",
        fg="#16a34a"
    )
    status_label.pack(pady=5)

    close_btn = tk.Button(
        frame,
        text="Exit Application",
        font=("Segoe UI", 10, "bold"),
        bg="#ef4444",
        fg="#ffffff",
        activebackground="#dc2626",
        activeforeground="#ffffff",
        padx=15,
        pady=5,
        relief="flat",
        cursor="hand2",
        command=root.destroy
    )
    close_btn.pack(pady=10)

    # 5. Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
