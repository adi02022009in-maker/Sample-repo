"""
Practical No. 27: Display, update, and delete records in a desktop GUI using SQLite.
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
    root.title("Practical 27: SQLite Display, Update & Delete")
    root.geometry("780x560")
    root.configure(bg="#f8fafc")

    selected_id = None

    # 1. Header Banner
    header = tk.Label(
        root,
        text="Student Records Manager (R-U-D)",
        font=("Segoe UI", 16, "bold"),
        bg="#4f46e5",
        fg="#ffffff",
        pady=10
    )
    header.pack(fill="x")

    # 2. Main Content Split: Form (Left) & Treeview Table (Right)
    main_frame = tk.Frame(root, bg="#f8fafc", padx=15, pady=10)
    main_frame.pack(fill="both", expand=True)

    # --- Left Panel: Edit / Form Frame ---
    edit_frame = tk.LabelFrame(main_frame, text=" Manage Student Record ", font=("Segoe UI", 10, "bold"), bg="#ffffff", padx=15, pady=12, relief="solid", bd=1)
    edit_frame.pack(side="left", fill="y", padx=(0, 10))

    tk.Label(edit_frame, text="Full Name:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
    name_entry = tk.Entry(edit_frame, font=("Segoe UI", 10), width=24, relief="groove", bd=2)
    name_entry.grid(row=1, column=0, pady=(0, 8), sticky="w")

    tk.Label(edit_frame, text="Enrollment No:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
    enroll_entry = tk.Entry(edit_frame, font=("Segoe UI", 10), width=24, relief="groove", bd=2)
    enroll_entry.grid(row=3, column=0, pady=(0, 8), sticky="w")

    tk.Label(edit_frame, text="Branch:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=4, column=0, sticky="w", pady=5)
    branch_combo = ttk.Combobox(
        edit_frame,
        values=["Computer Engineering", "Information Technology", "Mechanical Engineering", "Civil Engineering"],
        state="readonly",
        font=("Segoe UI", 9),
        width=22
    )
    branch_combo.grid(row=5, column=0, pady=(0, 8), sticky="w")
    branch_combo.current(0)

    tk.Label(edit_frame, text="Semester:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=6, column=0, sticky="w", pady=5)
    sem_combo = ttk.Combobox(
        edit_frame,
        values=["1", "2", "3", "4", "5", "6"],
        state="readonly",
        font=("Segoe UI", 9),
        width=22
    )
    sem_combo.grid(row=7, column=0, pady=(0, 15), sticky="w")
    sem_combo.current(4)

    # --- Right Panel: Treeview Table ---
    table_frame = tk.LabelFrame(main_frame, text=" Database Records Directory ", font=("Segoe UI", 10, "bold"), bg="#ffffff", padx=10, pady=10, relief="solid", bd=1)
    table_frame.pack(side="right", fill="both", expand=True)

    columns = ("id", "name", "enrollment_no", "branch", "semester")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse", height=14)

    tree.heading("id", text="ID")
    tree.heading("name", text="Full Name")
    tree.heading("enrollment_no", text="Enrollment No")
    tree.heading("branch", text="Branch")
    tree.heading("semester", text="Sem")

    tree.column("id", width=45, anchor="center")
    tree.column("name", width=140)
    tree.column("enrollment_no", width=110, anchor="center")
    tree.column("branch", width=150)
    tree.column("semester", width=50, anchor="center")

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # 3. Database CRUD Logic
    def load_records():
        tree.delete(*tree.get_children())
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, enrollment_no, branch, semester FROM students ORDER BY id ASC")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            tree.insert("", "end", values=row)

    def on_row_select(event):
        nonlocal selected_id
        selected_item = tree.selection()
        if not selected_item:
            return
        row = tree.item(selected_item[0], "values")
        selected_id = row[0]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, row[1])
        enroll_entry.delete(0, tk.END)
        enroll_entry.insert(0, row[2])
        branch_combo.set(row[3])
        sem_combo.set(str(row[4]))

    tree.bind("<<TreeviewSelect>>", on_row_select)

    def update_record():
        nonlocal selected_id
        if not selected_id:
            messagebox.showwarning("Selection Required", "Please select a record from the table to update!")
            return

        name = name_entry.get().strip()
        enroll = enroll_entry.get().strip()
        branch = branch_combo.get()
        sem = sem_combo.get()

        if not name or not enroll:
            messagebox.showwarning("Validation Error", "Name and Enrollment cannot be empty!")
            return

        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE students SET name = ?, enrollment_no = ?, branch = ?, semester = ? WHERE id = ?",
                (name, enroll, branch, int(sem), selected_id)
            )
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", f"Student ID #{selected_id} updated successfully!")
            load_records()
            clear_form()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Enrollment number must be unique!")
        except Exception as e:
            messagebox.showerror("Update Error", str(e))

    def delete_record():
        nonlocal selected_id
        if not selected_id:
            messagebox.showwarning("Selection Required", "Please select a student from the table to delete!")
            return

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to permanently delete Student ID #{selected_id}?")
        if confirm:
            try:
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM students WHERE id = ?", (selected_id,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Deleted", f"Student ID #{selected_id} was removed from the database.")
                load_records()
                clear_form()
            except Exception as e:
                messagebox.showerror("Delete Error", str(e))

    def clear_form():
        nonlocal selected_id
        selected_id = None
        name_entry.delete(0, tk.END)
        enroll_entry.delete(0, tk.END)
        branch_combo.current(0)
        sem_combo.current(4)
        name_entry.focus_set()

    # 4. Action Buttons (Update, Delete, Clear)
    btn_update = tk.Button(edit_frame, text="✏️ Update Record", font=("Segoe UI", 9, "bold"), bg="#f59e0b", fg="#ffffff", padx=10, pady=5, relief="flat", cursor="hand2", command=update_record)
    btn_update.grid(row=8, column=0, sticky="ew", pady=4)

    btn_delete = tk.Button(edit_frame, text="🗑️ Delete Record", font=("Segoe UI", 9, "bold"), bg="#ef4444", fg="#ffffff", padx=10, pady=5, relief="flat", cursor="hand2", command=delete_record)
    btn_delete.grid(row=9, column=0, sticky="ew", pady=4)

    btn_clear = tk.Button(edit_frame, text="🔄 Clear Selection", font=("Segoe UI", 9), bg="#e2e8f0", fg="#334155", padx=10, pady=5, relief="flat", cursor="hand2", command=clear_form)
    btn_clear.grid(row=10, column=0, sticky="ew", pady=4)

    # Load records initially
    load_records()
    root.mainloop()

if __name__ == "__main__":
    main()
