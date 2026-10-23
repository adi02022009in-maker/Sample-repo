"""
Practical No. 26: Develop a data entry form that stores records into SQLite database.
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

DB_NAME = "vibe_college.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            enrollment_no TEXT UNIQUE NOT NULL,
            branch TEXT NOT NULL,
            semester INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def main():
    init_db()

    root = tk.Tk()
    root.title("Practical 26: SQLite Data Entry Form")
    root.geometry("560x520")
    root.configure(bg="#f8fafc")
    root.resizable(False, False)

    # 1. Header Banner
    header = tk.Label(
        root,
        text="Student Database Entry Form",
        font=("Segoe UI", 16, "bold"),
        bg="#047857",
        fg="#ffffff",
        pady=12
    )
    header.pack(fill="x")

    # 2. Form Container Frame
    form_frame = tk.Frame(root, bg="#ffffff", padx=25, pady=20, relief="solid", bd=1)
    form_frame.pack(padx=25, pady=15, fill="x")

    # Field 1: Name
    tk.Label(form_frame, text="Full Name:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=0, column=0, sticky="w", pady=8)
    name_entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=32, relief="groove", bd=2)
    name_entry.grid(row=0, column=1, pady=8, padx=10)

    # Field 2: Enrollment Number
    tk.Label(form_frame, text="Enrollment No:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=1, column=0, sticky="w", pady=8)
    enroll_entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=32, relief="groove", bd=2)
    enroll_entry.grid(row=1, column=1, pady=8, padx=10)

    # Field 3: Branch
    tk.Label(form_frame, text="Branch / Dept:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=2, column=0, sticky="w", pady=8)
    branch_combo = ttk.Combobox(
        form_frame,
        values=["Computer Engineering", "Information Technology", "Mechanical Engineering", "Civil Engineering"],
        state="readonly",
        font=("Segoe UI", 10),
        width=30
    )
    branch_combo.grid(row=2, column=1, pady=8, padx=10)
    branch_combo.current(0)

    # Field 4: Semester
    tk.Label(form_frame, text="Semester:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=3, column=0, sticky="w", pady=8)
    sem_combo = ttk.Combobox(
        form_frame,
        values=["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"],
        state="readonly",
        font=("Segoe UI", 10),
        width=30
    )
    sem_combo.grid(row=3, column=1, pady=8, padx=10)
    sem_combo.current(4)  # Semester 5 default

    # 3. Status and Count Display
    count_var = tk.StringVar()

    def update_count():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM students")
        cnt = cursor.fetchone()[0]
        conn.close()
        count_var.set(f"Database Total: {cnt} Student Record(s) Stored")

    status_label = tk.Label(form_frame, textvariable=count_var, font=("Segoe UI", 9, "italic"), bg="#ecfdf5", fg="#065f46", pady=6)
    status_label.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(10, 0))

    # 4. Save Record Callback
    def save_record():
        name = name_entry.get().strip()
        enroll = enroll_entry.get().strip()
        branch = branch_combo.get()
        sem = sem_combo.get().replace("Semester ", "").strip()

        if not name or not enroll:
            messagebox.showwarning("Validation Error", "Please provide both Name and Enrollment Number!")
            return

        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, enrollment_no, branch, semester) VALUES (?, ?, ?, ?)",
                (name, enroll, branch, int(sem))
            )
            conn.commit()
            record_id = cursor.lastrowid
            conn.close()

            messagebox.showinfo("Success", f"Student '{name}' saved successfully with Database ID #{record_id}!")
            # Reset fields
            name_entry.delete(0, tk.END)
            enroll_entry.delete(0, tk.END)
            name_entry.focus_set()
            update_count()
        except sqlite3.IntegrityError:
            messagebox.showerror("Duplicate Record", f"Enrollment number '{enroll}' already exists in database!")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to store record: {e}")

    def reset_fields():
        name_entry.delete(0, tk.END)
        enroll_entry.delete(0, tk.END)
        name_entry.focus_set()

    # 5. Buttons Toolbar
    btn_frame = tk.Frame(root, bg="#f8fafc")
    btn_frame.pack(pady=12)

    btn_save = tk.Button(
        btn_frame,
        text="💾 Save to Database",
        font=("Segoe UI", 10, "bold"),
        bg="#047857",
        fg="#ffffff",
        padx=15,
        pady=7,
        relief="flat",
        cursor="hand2",
        command=save_record
    )
    btn_save.pack(side="left", padx=8)

    btn_reset = tk.Button(
        btn_frame,
        text="🔄 Reset Fields",
        font=("Segoe UI", 10),
        bg="#e2e8f0",
        fg="#334155",
        padx=15,
        pady=7,
        relief="flat",
        cursor="hand2",
        command=reset_fields
    )
    btn_reset.pack(side="left", padx=8)

    # Initialize count and focus
    update_count()
    name_entry.focus_set()

    root.mainloop()

if __name__ == "__main__":
    main()
