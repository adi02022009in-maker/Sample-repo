"""
Practical No. 28: Develop a complete desktop CRUD application (mini project with 6-7 modules).
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar
Theme: Student College ERP & Records Management System
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
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
            email TEXT,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Seed sample records if empty
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ("Rahul Sharma", "246250307086", "Computer Engineering", 5, "rahul@example.com", "9876543210"),
            ("Priya Patel", "246250307087", "Information Technology", 5, "priya@example.com", "9876543211"),
            ("Amit Varma", "246250307088", "Mechanical Engineering", 3, "amit@example.com", "9876543212"),
            ("Neha Joshi", "246250307089", "Computer Engineering", 5, "neha@example.com", "9876543213")
        ]
        cursor.executemany("INSERT INTO students (name, enrollment_no, branch, semester, email, phone) VALUES (?, ?, ?, ?, ?, ?)", sample_data)
    conn.commit()
    conn.close()

class StudentERPApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Practical 28: Student Management ERP Mini Project")
        self.geometry("900x600")
        self.configure(bg="#f1f5f9")
        self.resizable(False, False)

        init_db()

        # Top Header
        header = tk.Frame(self, bg="#1e1b4b", height=50)
        header.pack(fill="x")
        tk.Label(header, text="🎓 Vibe College ERP - Student Management System", font=("Segoe UI", 14, "bold"), bg="#1e1b4b", fg="#ffffff", padx=15, pady=10).pack(side="left")
        tk.Label(header, text="Semester 5 | DI05000121", font=("Segoe UI", 10), bg="#1e1b4b", fg="#94a3b8", padx=15).pack(side="right")

        # Container for Sidebar + Pages
        body = tk.Frame(self, bg="#f1f5f9")
        body.pack(fill="both", expand=True)

        # 1. Sidebar Navigation (6 Modules + About)
        sidebar = tk.Frame(body, bg="#0f172a", width=220, padx=10, pady=15)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="NAVIGATION", font=("Segoe UI", 9, "bold"), bg="#0f172a", fg="#64748b", pady=5).pack(anchor="w")

        self.frames = {}
        pages = [
            ("📊 Dashboard", self.show_dashboard),
            ("➕ Register Student", self.show_create),
            ("📋 Student Directory", self.show_directory),
            ("✏️ Edit Record", self.show_update),
            ("🗑️ Delete Record", self.show_delete),
            ("📈 Reports & Export", self.show_reports),
            ("ℹ️ About System", self.show_about)
        ]

        for text, cmd in pages:
            btn = tk.Button(
                sidebar,
                text=text,
                font=("Segoe UI", 10, "bold"),
                bg="#1e293b",
                fg="#f8fafc",
                activebackground="#3b82f6",
                activeforeground="#ffffff",
                relief="flat",
                anchor="w",
                padx=12,
                pady=8,
                cursor="hand2",
                command=cmd
            )
            btn.pack(fill="x", pady=4)

        # Main Page Container Area
        self.content_area = tk.Frame(body, bg="#f8fafc", padx=20, pady=20)
        self.content_area.pack(side="right", fill="both", expand=True)

        # Show Dashboard initially
        self.show_dashboard()

    def clear_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    # --- Module 1: Dashboard ---
    def show_dashboard(self):
        self.clear_content()
        tk.Label(self.content_area, text="Executive Dashboard", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#1e293b").pack(anchor="w", pady=(0, 15))

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM students")
        total_students = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT branch) FROM students")
        total_branches = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM students WHERE branch = 'Computer Engineering'")
        ce_students = cur.fetchone()[0]
        conn.close()

        cards_frame = tk.Frame(self.content_area, bg="#f8fafc")
        cards_frame.pack(fill="x", pady=10)

        stats = [
            ("Total Registered", str(total_students), "#3b82f6"),
            ("Academic Branches", str(total_branches), "#10b981"),
            ("Computer Dept", str(ce_students), "#8b5cf6")
        ]

        for title, val, col in stats:
            card = tk.Frame(cards_frame, bg="#ffffff", padx=20, pady=15, relief="solid", bd=1)
            card.pack(side="left", fill="both", expand=True, padx=8)
            tk.Label(card, text=title, font=("Segoe UI", 9, "bold"), bg="#ffffff", fg="#64748b").pack(anchor="w")
            tk.Label(card, text=val, font=("Segoe UI", 24, "bold"), bg="#ffffff", fg=col).pack(anchor="w", pady=5)

        info_box = tk.LabelFrame(self.content_area, text=" System Overview ", font=("Segoe UI", 10, "bold"), bg="#ffffff", padx=15, pady=15, relief="solid", bd=1)
        info_box.pack(fill="both", expand=True, pady=15)
        tk.Label(info_box, text="Welcome to the Vibe College Student ERP System.\n\n"
                                "• Integrated CRUD Modules (Create, Read, Update, Delete)\n"
                                "• Instant Search by Enrollment Number or Student Name\n"
                                "• Branch-wise Analytics and CSV Report Export\n"
                                "• SQLite Relational Database Engine with Transaction Safety",
                 font=("Segoe UI", 10), bg="#ffffff", fg="#334155", justify="left").pack(anchor="w")

    # --- Module 2: Register Student (Create) ---
    def show_create(self):
        self.clear_content()
        tk.Label(self.content_area, text="Register New Student", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#1e293b").pack(anchor="w", pady=(0, 15))

        form = tk.Frame(self.content_area, bg="#ffffff", padx=25, pady=20, relief="solid", bd=1)
        form.pack(fill="x")

        tk.Label(form, text="Full Name:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=6)
        name_ent = tk.Entry(form, font=("Segoe UI", 10), width=32, relief="groove", bd=2)
        name_ent.grid(row=0, column=1, padx=10, pady=6)

        tk.Label(form, text="Enrollment No:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=6)
        enr_ent = tk.Entry(form, font=("Segoe UI", 10), width=32, relief="groove", bd=2)
        enr_ent.grid(row=1, column=1, padx=10, pady=6)

        tk.Label(form, text="Branch:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=6)
        branch_cb = ttk.Combobox(form, values=["Computer Engineering", "Information Technology", "Mechanical Engineering", "Civil Engineering"], state="readonly", width=30)
        branch_cb.grid(row=2, column=1, padx=10, pady=6)
        branch_cb.current(0)

        tk.Label(form, text="Semester:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=3, column=0, sticky="w", pady=6)
        sem_cb = ttk.Combobox(form, values=["1", "2", "3", "4", "5", "6"], state="readonly", width=30)
        sem_cb.grid(row=3, column=1, padx=10, pady=6)
        sem_cb.current(4)

        tk.Label(form, text="Email Address:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=4, column=0, sticky="w", pady=6)
        email_ent = tk.Entry(form, font=("Segoe UI", 10), width=32, relief="groove", bd=2)
        email_ent.grid(row=4, column=1, padx=10, pady=6)

        tk.Label(form, text="Phone Number:", font=("Segoe UI", 9, "bold"), bg="#ffffff").grid(row=5, column=0, sticky="w", pady=6)
        phone_ent = tk.Entry(form, font=("Segoe UI", 10), width=32, relief="groove", bd=2)
        phone_ent.grid(row=5, column=1, padx=10, pady=6)

        def save_student():
            name = name_ent.get().strip()
            enr = enr_ent.get().strip()
            branch = branch_cb.get()
            sem = sem_cb.get()
            email = email_ent.get().strip()
            phone = phone_ent.get().strip()

            if not name or not enr:
                messagebox.showwarning("Validation Error", "Name and Enrollment Number are required!")
                return

            try:
                conn = sqlite3.connect(DB_NAME)
                cur = conn.cursor()
                cur.execute("INSERT INTO students (name, enrollment_no, branch, semester, email, phone) VALUES (?, ?, ?, ?, ?, ?)",
                            (name, enr, branch, int(sem), email, phone))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", f"Student '{name}' registered successfully!")
                self.show_directory()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Enrollment Number already exists in the database!")

        btn_save = tk.Button(form, text="💾 Register Student", font=("Segoe UI", 10, "bold"), bg="#10b981", fg="#fff", padx=15, pady=6, relief="flat", cursor="hand2", command=save_student)
        btn_save.grid(row=6, column=1, sticky="e", pady=15)

    # --- Module 3: Student Directory (Read & Search) ---
    def show_directory(self):
        self.clear_content()
        tk.Label(self.content_area, text="Student Records Directory", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#1e293b").pack(anchor="w")

        # Search Bar
        search_frame = tk.Frame(self.content_area, bg="#f8fafc", pady=10)
        search_frame.pack(fill="x")

        tk.Label(search_frame, text="Search (Name / Enr):", font=("Segoe UI", 9, "bold"), bg="#f8fafc").pack(side="left")
        search_entry = tk.Entry(search_frame, font=("Segoe UI", 9), width=24)
        search_entry.pack(side="left", padx=8)

        def do_search():
            q = search_entry.get().strip()
            populate_tree(q)

        tk.Button(search_frame, text="🔍 Search", font=("Segoe UI", 9, "bold"), bg="#3b82f6", fg="#fff", relief="flat", padx=10, command=do_search).pack(side="left")
        tk.Button(search_frame, text="Reset", font=("Segoe UI", 9), bg="#e2e8f0", relief="flat", padx=10, command=lambda: populate_tree()).pack(side="left", padx=5)

        # Table
        cols = ("id", "name", "enr", "branch", "sem", "phone")
        tree = ttk.Treeview(self.content_area, columns=cols, show="headings", height=12)
        tree.heading("id", text="ID")
        tree.heading("name", text="Full Name")
        tree.heading("enr", text="Enrollment No")
        tree.heading("branch", text="Branch")
        tree.heading("sem", text="Sem")
        tree.heading("phone", text="Phone")

        tree.column("id", width=40, anchor="center")
        tree.column("name", width=160)
        tree.column("enr", width=120, anchor="center")
        tree.column("branch", width=160)
        tree.column("sem", width=50, anchor="center")
        tree.column("phone", width=100, anchor="center")
        tree.pack(fill="both", expand=True)

        def populate_tree(query=None):
            tree.delete(*tree.get_children())
            conn = sqlite3.connect(DB_NAME)
            cur = conn.cursor()
            if query:
                cur.execute("SELECT id, name, enrollment_no, branch, semester, phone FROM students WHERE name LIKE ? OR enrollment_no LIKE ?", (f"%{query}%", f"%{query}%"))
            else:
                cur.execute("SELECT id, name, enrollment_no, branch, semester, phone FROM students ORDER BY id ASC")
            for r in cur.fetchall():
                tree.insert("", "end", values=r)
            conn.close()

        populate_tree()

    # --- Module 4: Edit Record (Update) ---
    def show_update(self):
        self.clear_content()
        tk.Label(self.content_area, text="Edit Student Record", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#1e293b").pack(anchor="w", pady=(0, 15))

        top_search = tk.Frame(self.content_area, bg="#f8fafc")
        top_search.pack(fill="x", pady=5)
        tk.Label(top_search, text="Enter Enrollment No to Edit:", font=("Segoe UI", 10, "bold"), bg="#f8fafc").pack(side="left")
        enr_in = tk.Entry(top_search, font=("Segoe UI", 10), width=20)
        enr_in.pack(side="left", padx=8)

        form = tk.Frame(self.content_area, bg="#ffffff", padx=20, pady=20, relief="solid", bd=1)
        form.pack(fill="x", pady=10)

        name_e = tk.Entry(form, font=("Segoe UI", 10), width=30)
        branch_e = ttk.Combobox(form, values=["Computer Engineering", "Information Technology", "Mechanical Engineering", "Civil Engineering"], width=28)
        sem_e = ttk.Combobox(form, values=["1", "2", "3", "4", "5", "6"], width=28)
        phone_e = tk.Entry(form, font=("Segoe UI", 10), width=30)
        curr_id = None

        tk.Label(form, text="Name:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        name_e.grid(row=0, column=1, pady=5, padx=8)
        tk.Label(form, text="Branch:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=1, column=0, sticky="w", pady=5)
        branch_e.grid(row=1, column=1, pady=5, padx=8)
        tk.Label(form, text="Semester:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=2, column=0, sticky="w", pady=5)
        sem_e.grid(row=2, column=1, pady=5, padx=8)
        tk.Label(form, text="Phone:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=3, column=0, sticky="w", pady=5)
        phone_e.grid(row=3, column=1, pady=5, padx=8)

        def fetch():
            nonlocal curr_id
            enr = enr_in.get().strip()
            conn = sqlite3.connect(DB_NAME)
            cur = conn.cursor()
            cur.execute("SELECT id, name, branch, semester, phone FROM students WHERE enrollment_no = ?", (enr,))
            row = cur.fetchone()
            conn.close()
            if row:
                curr_id = row[0]
                name_e.delete(0, tk.END); name_e.insert(0, row[1])
                branch_e.set(row[2])
                sem_e.set(str(row[3]))
                phone_e.delete(0, tk.END); phone_e.insert(0, row[4] if row[4] else "")
                messagebox.showinfo("Loaded", f"Record for '{row[1]}' loaded successfully.")
            else:
                messagebox.showwarning("Not Found", "No student found with that Enrollment Number!")

        tk.Button(top_search, text="Fetch Record", font=("Segoe UI", 9, "bold"), bg="#3b82f6", fg="#fff", relief="flat", command=fetch).pack(side="left")

        def update():
            if not curr_id:
                messagebox.showwarning("No Record", "Please fetch a valid record first!")
                return
            conn = sqlite3.connect(DB_NAME)
            cur = conn.cursor()
            cur.execute("UPDATE students SET name = ?, branch = ?, semester = ?, phone = ? WHERE id = ?",
                        (name_e.get().strip(), branch_e.get(), int(sem_e.get()), phone_e.get().strip(), curr_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Updated", "Student record updated successfully in database!")
            self.show_directory()

        tk.Button(form, text="✏️ Save Updates", font=("Segoe UI", 10, "bold"), bg="#f59e0b", fg="#fff", relief="flat", padx=15, pady=5, command=update).grid(row=4, column=1, sticky="e", pady=15)

    # --- Module 5: Delete Record ---
    def show_delete(self):
        self.clear_content()
        tk.Label(self.content_area, text="Delete Student Record", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#ef4444").pack(anchor="w", pady=(0, 15))

        box = tk.Frame(self.content_area, bg="#ffffff", padx=25, pady=25, relief="solid", bd=1)
        box.pack(fill="x")

        tk.Label(box, text="Enter Enrollment Number to Delete:", font=("Segoe UI", 10, "bold"), bg="#ffffff").pack(anchor="w")
        del_enr = tk.Entry(box, font=("Segoe UI", 11), width=30)
        del_enr.pack(anchor="w", pady=10)

        def do_delete():
            enr = del_enr.get().strip()
            if not enr:
                messagebox.showwarning("Required", "Please enter an Enrollment Number!")
                return
            conn = sqlite3.connect(DB_NAME)
            cur = conn.cursor()
            cur.execute("SELECT id, name FROM students WHERE enrollment_no = ?", (enr,))
            row = cur.fetchone()
            if not row:
                conn.close()
                messagebox.showerror("Not Found", "No student found with that enrollment number!")
                return

            if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to PERMANENTLY delete record for:\n\n{row[1]} (Enr: {enr})?"):
                cur.execute("DELETE FROM students WHERE id = ?", (row[0],))
                conn.commit()
                conn.close()
                messagebox.showinfo("Deleted", f"Record for {row[1]} removed from database.")
                self.show_directory()
            else:
                conn.close()

        tk.Button(box, text="🗑️ Delete Record Permanently", font=("Segoe UI", 10, "bold"), bg="#ef4444", fg="#fff", relief="flat", padx=15, pady=6, cursor="hand2", command=do_delete).pack(anchor="w", pady=10)

    # --- Module 6: Reports & Export ---
    def show_reports(self):
        self.clear_content()
        tk.Label(self.content_area, text="Reports & CSV Data Export", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#1e293b").pack(anchor="w", pady=(0, 15))

        rep_frame = tk.Frame(self.content_area, bg="#ffffff", padx=20, pady=20, relief="solid", bd=1)
        rep_frame.pack(fill="both", expand=True)

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT branch, COUNT(*) FROM students GROUP BY branch")
        branch_stats = cur.fetchall()
        conn.close()

        tk.Label(rep_frame, text="Branch-Wise Student Enrollment Summary:", font=("Segoe UI", 11, "bold"), bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(0, 10))

        for branch, count in branch_stats:
            row_f = tk.Frame(rep_frame, bg="#f8fafc", padx=12, pady=6)
            row_f.pack(fill="x", pady=3)
            tk.Label(row_f, text=branch, font=("Segoe UI", 10), bg="#f8fafc").pack(side="left")
            tk.Label(row_f, text=f"{count} Student(s)", font=("Segoe UI", 10, "bold"), bg="#f8fafc", fg="#3b82f6").pack(side="right")

        def export_csv():
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files (*.csv)", "*.csv")], title="Export Student Records")
            if file_path:
                conn = sqlite3.connect(DB_NAME)
                cur = conn.cursor()
                cur.execute("SELECT id, name, enrollment_no, branch, semester, email, phone FROM students")
                rows = cur.fetchall()
                conn.close()

                with open(file_path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["ID", "Full Name", "Enrollment No", "Branch", "Semester", "Email", "Phone"])
                    writer.writerows(rows)
                messagebox.showinfo("Export Complete", f"Successfully exported {len(rows)} records to:\n{file_path}")

        tk.Button(rep_frame, text="📥 Export All Records to CSV", font=("Segoe UI", 10, "bold"), bg="#10b981", fg="#fff", padx=15, pady=8, relief="flat", cursor="hand2", command=export_csv).pack(pady=20)

    # --- Module 7: About System ---
    def show_about(self):
        self.clear_content()
        tk.Label(self.content_area, text="About This Application", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#1e293b").pack(anchor="w", pady=(0, 15))

        box = tk.Frame(self.content_area, bg="#ffffff", padx=25, pady=25, relief="solid", bd=1)
        box.pack(fill="both", expand=True)

        details = [
            ("Course:", "Application Design & Development using Vibe Coding (DI05000121)"),
            ("Practical:", "Practical No. 28 - Complete Desktop CRUD Mini Project (7 Modules)"),
            ("Institute:", "Govt. Polytechnic College, Jamnagar"),
            ("Technologies:", "Python 3.13, Tkinter GUI, SQLite Relational Database Engine"),
            ("Student Roll / Enr:", "246250307086 (Diploma Computer Engineering - Sem 5)")
        ]

        for k, v in details:
            row = tk.Frame(box, bg="#ffffff", pady=6)
            row.pack(fill="x")
            tk.Label(row, text=k, font=("Segoe UI", 10, "bold"), bg="#ffffff", width=18, anchor="w").pack(side="left")
            tk.Label(row, text=v, font=("Segoe UI", 10), bg="#ffffff", fg="#334155").pack(side="left")

if __name__ == "__main__":
    app = StudentERPApp()
    app.mainloop()
