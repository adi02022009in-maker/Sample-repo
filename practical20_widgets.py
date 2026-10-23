"""
Practical No. 20: Create a desktop application interface with labels, buttons and input fields.
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar
"""

import tkinter as tk
from tkinter import ttk, messagebox

def main():
    root = tk.Tk()
    root.title("Practical 20: GUI Labels, Buttons & Entry Fields")
    root.geometry("520x450")
    root.configure(bg="#f8fafc")
    root.resizable(False, False)

    # 1. Header Banner Label
    header = tk.Label(
        root,
        text="Student Information Form",
        font=("Segoe UI", 16, "bold"),
        bg="#0284c7",
        fg="#ffffff",
        pady=12
    )
    header.pack(fill="x")

    # 2. Main Form Frame
    form_frame = tk.Frame(root, bg="#ffffff", padx=25, pady=20, relief="solid", bd=1)
    form_frame.pack(padx=25, pady=20, fill="both", expand=True)

    # Form Fields using Grid layout
    # Field 1: Student Name
    tk.Label(form_frame, text="Full Name:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=0, column=0, sticky="w", pady=8)
    name_entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=30, relief="groove", bd=2)
    name_entry.grid(row=0, column=1, pady=8, padx=10)

    # Field 2: Enrollment Number
    tk.Label(form_frame, text="Enrollment No:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=1, column=0, sticky="w", pady=8)
    enroll_entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=30, relief="groove", bd=2)
    enroll_entry.grid(row=1, column=1, pady=8, padx=10)

    # Field 3: Branch / Department
    tk.Label(form_frame, text="Branch:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=2, column=0, sticky="w", pady=8)
    branch_entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=30, relief="groove", bd=2)
    branch_entry.grid(row=2, column=1, pady=8, padx=10)

    # Field 4: Email Address
    tk.Label(form_frame, text="Email Address:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=3, column=0, sticky="w", pady=8)
    email_entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=30, relief="groove", bd=2)
    email_entry.grid(row=3, column=1, pady=8, padx=10)

    # Output Display Label
    result_var = tk.StringVar(value="Ready for data input.")
    result_label = tk.Label(form_frame, textvariable=result_var, font=("Segoe UI", 9, "italic"), bg="#f0f9ff", fg="#0369a1", wraplength=420, pady=8, relief="flat")
    result_label.grid(row=4, column=0, columnspan=2, sticky="ew", pady=15)

    # 3. Button Callbacks
    def on_submit():
        name = name_entry.get().strip()
        enroll = enroll_entry.get().strip()
        branch = branch_entry.get().strip()
        email = email_entry.get().strip()

        if not name or not enroll or not branch or not email:
            messagebox.showwarning("Incomplete Data", "Please fill in all input fields!")
            return

        result_var.set(f"Submitted: {name} | Enr: {enroll} | {branch} | {email}")
        messagebox.showinfo("Success", f"Data received successfully for {name}!")

    def on_clear():
        name_entry.delete(0, tk.END)
        enroll_entry.delete(0, tk.END)
        branch_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        result_var.set("Fields cleared. Ready for new entry.")
        name_entry.focus_set()

    # 4. Buttons Container Frame
    btn_frame = tk.Frame(form_frame, bg="#ffffff")
    btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

    submit_btn = tk.Button(
        btn_frame,
        text="Submit Details",
        font=("Segoe UI", 10, "bold"),
        bg="#0284c7",
        fg="#ffffff",
        padx=15,
        pady=6,
        relief="flat",
        cursor="hand2",
        command=on_submit
    )
    submit_btn.pack(side="left", padx=8)

    clear_btn = tk.Button(
        btn_frame,
        text="Clear Form",
        font=("Segoe UI", 10),
        bg="#e2e8f0",
        fg="#334155",
        padx=15,
        pady=6,
        relief="flat",
        cursor="hand2",
        command=on_clear
    )
    clear_btn.pack(side="left", padx=8)

    name_entry.focus_set()
    root.mainloop()

if __name__ == "__main__":
    main()
