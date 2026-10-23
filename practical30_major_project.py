"""
Practical No. 30: MAJOR PROJECT – II
Title: College Fee Collection & Finance Management System
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar

Specifications:
- Multi-frame GUI with Menu Bar (Dashboard, Students, Collect Fee, Ledger, Reports, Export/Import)
- SQLite Database with 3 relational tables: students, fee_structures, fee_payments
- Full CRUD Operations with Validation and Confirmation Dialogs
- Dynamic Search & Filter Facility
- Data Export (CSV, JSON, Text Receipt) and CSV Import Capability
- Packaged as a Distributable Executable (.exe)
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
import json
import os
from datetime import datetime

DB_NAME = "vibe_fees.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Table 1: Students
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            enrollment_no TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            branch TEXT NOT NULL,
            semester INTEGER NOT NULL,
            contact TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Table 2: Fee Structures
    cur.execute("""
        CREATE TABLE IF NOT EXISTS fee_structures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT UNIQUE NOT NULL,
            total_fee REAL NOT NULL,
            academic_year TEXT NOT NULL
        )
    """)

    # Table 3: Fee Payments (Child Table with FKs)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS fee_payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            receipt_no TEXT UNIQUE NOT NULL,
            student_id INTEGER NOT NULL,
            fee_structure_id INTEGER NOT NULL,
            amount_paid REAL NOT NULL,
            payment_mode TEXT NOT NULL,
            payment_date TEXT NOT NULL,
            remarks TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY(fee_structure_id) REFERENCES fee_structures(id)
        )
    """)

    # Seed initial fee structures if empty
    cur.execute("SELECT COUNT(*) FROM fee_structures")
    if cur.fetchone()[0] == 0:
        cur.executemany("""
            INSERT INTO fee_structures (category, total_fee, academic_year) VALUES (?, ?, ?)
        """, [
            ("Tuition Fee (Regular)", 15000.0, "2026-2027"),
            ("Exam & Lab Fee", 3500.0, "2026-2027"),
            ("Hostel & Mess Fee", 22000.0, "2026-2027"),
            ("Library & Sports Fee", 1500.0, "2026-2027")
        ])

    # Seed sample students if empty
    cur.execute("SELECT COUNT(*) FROM students")
    if cur.fetchone()[0] == 0:
        cur.executemany("""
            INSERT INTO students (enrollment_no, name, branch, semester, contact) VALUES (?, ?, ?, ?, ?)
        """, [
            ("246250307086", "Rahul Sharma", "Computer Engineering", 5, "9876543210"),
            ("246250307087", "Priya Patel", "Information Technology", 5, "9876543211"),
            ("246250307088", "Amit Varma", "Mechanical Engineering", 3, "9876543212")
        ])

    # Seed sample payment if empty
    cur.execute("SELECT COUNT(*) FROM fee_payments")
    if cur.fetchone()[0] == 0:
        cur.execute("""
            INSERT INTO fee_payments (receipt_no, student_id, fee_structure_id, amount_paid, payment_mode, payment_date, remarks)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ("REC-1001", 1, 1, 15000.0, "UPI / Online", "2026-10-23", "Full Semester 5 Tuition Paid"))

    conn.commit()
    conn.close()

class FeeManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fee Collection & Financial Records System - Practical 30")
        self.geometry("960x640")
        self.configure(bg="#f8fafc")
        self.resizable(False, False)

        init_db()

        # Build Menu Bar
        self.build_menu()

        # Top Banner
        header = tk.Frame(self, bg="#0f172a", height=50)
        header.pack(fill="x")
        tk.Label(header, text="🏛️ Govt. Polytechnic College, Jamnagar — Fee Collection System", font=("Segoe UI", 13, "bold"), bg="#0f172a", fg="#ffffff", padx=15, pady=10).pack(side="left")
        tk.Label(header, text="Major Project II | DI05000121", font=("Segoe UI", 9), bg="#0f172a", fg="#94a3b8", padx=15).pack(side="right")

        # Main Layout: Sidebar + Dynamic Content
        container = tk.Frame(self, bg="#f8fafc")
        container.pack(fill="both", expand=True)

        sidebar = tk.Frame(container, bg="#1e293b", width=220, padx=10, pady=15)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="NAVIGATION", font=("Segoe UI", 8, "bold"), bg="#1e293b", fg="#94a3b8", pady=5).pack(anchor="w")

        nav_items = [
            ("📊 Dashboard", self.show_dashboard),
            ("👨‍🎓 Students (CRUD)", self.show_students),
            ("💳 Collect Fee (CRUD)", self.show_collect_fee),
            ("📑 Transactions Ledger", self.show_ledger),
            ("📈 Revenue Reports", self.show_reports),
            ("💾 Export / Import Data", self.show_export_import),
            ("ℹ️ About Project", self.show_about)
        ]

        for label, command in nav_items:
            btn = tk.Button(
                sidebar, text=label, font=("Segoe UI", 10, "bold"),
                bg="#334155", fg="#f8fafc", activebackground="#2563eb", activeforeground="#ffffff",
                relief="flat", anchor="w", padx=12, pady=7, cursor="hand2", command=command
            )
            btn.pack(fill="x", pady=3)

        self.content_area = tk.Frame(container, bg="#f8fafc", padx=20, pady=15)
        self.content_area.pack(side="right", fill="both", expand=True)

        self.show_dashboard()

    def build_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="Dashboard", command=self.show_dashboard)
        file_menu.add_command(label="Collect Fee", command=self.show_collect_fee)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

        tools_menu = tk.Menu(menubar, tearoff=False)
        tools_menu.add_command(label="Export to CSV", command=self.show_export_import)
        tools_menu.add_command(label="Import from CSV", command=self.show_export_import)
        menubar.add_cascade(label="Tools", menu=tools_menu)

        help_menu = tk.Menu(menubar, tearoff=False)
        help_menu.add_command(label="About Project", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

    def clear_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    # --- SCREEN 1: Dashboard Overview ---
    def show_dashboard(self):
        self.clear_content()
        tk.Label(self.content_area, text="Executive Fee Collection Dashboard", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w", pady=(0, 15))

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT COALESCE(SUM(amount_paid), 0) FROM fee_payments")
        total_collected = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM fee_payments")
        total_receipts = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM students")
        total_students = cur.fetchone()[0]
        conn.close()

        cards_frame = tk.Frame(self.content_area, bg="#f8fafc")
        cards_frame.pack(fill="x", pady=10)

        stats = [
            ("TOTAL FEES COLLECTED", f"₹ {total_collected:,.2f}", "#059669"),
            ("RECEIPTS ISSUED", f"{total_receipts} Receipts", "#2563eb"),
            ("ACTIVE STUDENTS", f"{total_students} Students", "#7c3aed")
        ]

        for title, val, color in stats:
            c = tk.Frame(cards_frame, bg="#ffffff", padx=20, pady=15, relief="solid", bd=1)
            c.pack(side="left", fill="both", expand=True, padx=8)
            tk.Label(c, text=title, font=("Segoe UI", 8, "bold"), bg="#ffffff", fg="#64748b").pack(anchor="w")
            tk.Label(c, text=val, font=("Segoe UI", 20, "bold"), bg="#ffffff", fg=color).pack(anchor="w", pady=5)

        summary_box = tk.LabelFrame(self.content_area, text=" Quick Launch & Verification ", font=("Segoe UI", 10, "bold"), bg="#ffffff", padx=15, pady=15, relief="solid", bd=1)
        summary_box.pack(fill="both", expand=True, pady=15)

        tk.Label(summary_box, text="System Features & Specifications:\n\n"
                                   "1. 3 Relational SQLite Tables: 'students', 'fee_structures', 'fee_payments' with foreign keys\n"
                                   "2. Module 1: Student Records CRUD (Create, Read, Update, Delete with confirmation)\n"
                                   "3. Module 2: Fee Collection & Instant Receipt Generation\n"
                                   "4. Dynamic Multi-field Search Filter in Transaction Ledger\n"
                                   "5. Complete Data Export (CSV, JSON, Text Receipt) and CSV Import Capability\n"
                                   "6. Compiled as a Standalone Executable (.exe) for distribution",
                 font=("Segoe UI", 10), bg="#ffffff", fg="#334155", justify="left").pack(anchor="w")

    # --- SCREEN 2: Student Management (CRUD 1) ---
    def show_students(self):
        self.clear_content()
        tk.Label(self.content_area, text="Student Enrollment & Accounts Management", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w", pady=(0, 10))

        form_frame = tk.LabelFrame(self.content_area, text=" Add / Edit Student ", font=("Segoe UI", 9, "bold"), bg="#ffffff", padx=15, pady=10, relief="solid", bd=1)
        form_frame.pack(fill="x", pady=5)

        tk.Label(form_frame, text="Enrollment No:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w", pady=4)
        enr_in = tk.Entry(form_frame, font=("Segoe UI", 9), width=20)
        enr_in.grid(row=0, column=1, padx=6, pady=4)

        tk.Label(form_frame, text="Full Name:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=0, column=2, sticky="w", pady=4)
        name_in = tk.Entry(form_frame, font=("Segoe UI", 9), width=24)
        name_in.grid(row=0, column=3, padx=6, pady=4)

        tk.Label(form_frame, text="Branch:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=1, column=0, sticky="w", pady=4)
        branch_cb = ttk.Combobox(form_frame, values=["Computer Engineering", "Information Technology", "Mechanical Engineering", "Civil Engineering"], width=18, state="readonly")
        branch_cb.grid(row=1, column=1, padx=6, pady=4); branch_cb.current(0)

        tk.Label(form_frame, text="Semester:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=1, column=2, sticky="w", pady=4)
        sem_cb = ttk.Combobox(form_frame, values=["1", "2", "3", "4", "5", "6"], width=6, state="readonly")
        sem_cb.grid(row=1, column=3, padx=6, pady=4, sticky="w"); sem_cb.current(4)

        selected_student_id = [None]

        # Table
        cols = ("id", "enr", "name", "branch", "sem", "contact")
        tree = ttk.Treeview(self.content_area, columns=cols, show="headings", height=8)
        for c, h, w in zip(cols, ["ID", "Enrollment No", "Full Name", "Branch", "Sem", "Contact"], [40, 120, 180, 160, 50, 110]):
            tree.heading(c, text=h)
            tree.column(c, width=w, anchor="center" if c in ["id", "enr", "sem", "contact"] else "w")
        tree.pack(fill="both", expand=True, pady=10)

        def refresh_table():
            tree.delete(*tree.get_children())
            conn = sqlite3.connect(DB_NAME)
            cur = conn.cursor()
            cur.execute("SELECT id, enrollment_no, name, branch, semester, contact FROM students ORDER BY id ASC")
            for r in cur.fetchall():
                tree.insert("", "end", values=r)
            conn.close()

        def on_select(e):
            sel = tree.selection()
            if sel:
                row = tree.item(sel[0], "values")
                selected_student_id[0] = row[0]
                enr_in.delete(0, tk.END); enr_in.insert(0, row[1])
                name_in.delete(0, tk.END); name_in.insert(0, row[2])
                branch_cb.set(row[3])
                sem_cb.set(row[4])

        tree.bind("<<TreeviewSelect>>", on_select)

        def add_student():
            enr, name, b, s = enr_in.get().strip(), name_in.get().strip(), branch_cb.get(), sem_cb.get()
            if not enr or not name:
                messagebox.showwarning("Validation", "Enrollment and Name are required!")
                return
            try:
                conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
                cur.execute("INSERT INTO students (enrollment_no, name, branch, semester, contact) VALUES (?, ?, ?, ?, ?)", (enr, name, b, int(s), "9876543210"))
                conn.commit(); conn.close()
                messagebox.showinfo("Success", f"Student '{name}' added successfully!")
                refresh_table()
            except sqlite3.IntegrityError:
                messagebox.showerror("Duplicate", "Enrollment number already exists!")

        def update_student():
            if not selected_student_id[0]:
                messagebox.showwarning("Select", "Select a student row to update!")
                return
            conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
            cur.execute("UPDATE students SET enrollment_no=?, name=?, branch=?, semester=? WHERE id=?",
                        (enr_in.get().strip(), name_in.get().strip(), branch_cb.get(), int(sem_cb.get()), selected_student_id[0]))
            conn.commit(); conn.close()
            messagebox.showinfo("Updated", "Student record updated successfully!")
            refresh_table()

        def delete_student():
            if not selected_student_id[0]:
                messagebox.showwarning("Select", "Select a student to delete!")
                return
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student and their payments?"):
                conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
                cur.execute("DELETE FROM students WHERE id=?", (selected_student_id[0],))
                conn.commit(); conn.close()
                messagebox.showinfo("Deleted", "Student record deleted.")
                refresh_table()

        btn_bar = tk.Frame(form_frame, bg="#ffffff")
        btn_bar.grid(row=2, column=0, columnspan=4, pady=8)
        tk.Button(btn_bar, text="➕ Add Student", bg="#059669", fg="#fff", font=("Segoe UI", 9, "bold"), relief="flat", padx=10, command=add_student).pack(side="left", padx=4)
        tk.Button(btn_bar, text="✏️ Update Selected", bg="#d97706", fg="#fff", font=("Segoe UI", 9, "bold"), relief="flat", padx=10, command=update_student).pack(side="left", padx=4)
        tk.Button(btn_bar, text="🗑️ Delete Student", bg="#dc2626", fg="#fff", font=("Segoe UI", 9, "bold"), relief="flat", padx=10, command=delete_student).pack(side="left", padx=4)

        refresh_table()

    # --- SCREEN 3: Fee Payment Entry (CRUD 2) ---
    def show_collect_fee(self):
        self.clear_content()
        tk.Label(self.content_area, text="Collect Student Fee & Issue Receipt", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w", pady=(0, 15))

        card = tk.Frame(self.content_area, bg="#ffffff", padx=25, pady=20, relief="solid", bd=1)
        card.pack(fill="x")

        conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
        cur.execute("SELECT id, enrollment_no, name FROM students")
        students = cur.fetchall()
        cur.execute("SELECT id, category, total_fee FROM fee_structures")
        structures = cur.fetchall()
        conn.close()

        receipt_num = f"REC-{datetime.now().strftime('%y%m%d%H%M%S')[-6:]}"

        tk.Label(card, text="Receipt No:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w", pady=6)
        r_entry = tk.Entry(card, font=("Segoe UI", 9, "bold"), width=28)
        r_entry.grid(row=0, column=1, padx=10, pady=6); r_entry.insert(0, receipt_num)

        tk.Label(card, text="Student:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=1, column=0, sticky="w", pady=6)
        student_cb = ttk.Combobox(card, values=[f"{s[0]} - {s[1]} ({s[2]})" for s in students], width=35, state="readonly")
        student_cb.grid(row=1, column=1, padx=10, pady=6)
        if students: student_cb.current(0)

        tk.Label(card, text="Fee Category:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=2, column=0, sticky="w", pady=6)
        fee_cb = ttk.Combobox(card, values=[f"{f[0]} - {f[1]} (₹{f[2]})" for f in structures], width=35, state="readonly")
        fee_cb.grid(row=2, column=1, padx=10, pady=6)
        if structures: fee_cb.current(0)

        tk.Label(card, text="Amount Paid (₹):", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=3, column=0, sticky="w", pady=6)
        amt_entry = tk.Entry(card, font=("Segoe UI", 9), width=28)
        amt_entry.grid(row=3, column=1, padx=10, pady=6); amt_entry.insert(0, "15000.0")

        tk.Label(card, text="Payment Mode:", bg="#ffffff", font=("Segoe UI", 9, "bold")).grid(row=4, column=0, sticky="w", pady=6)
        mode_cb = ttk.Combobox(card, values=["UPI / Online", "Cash", "Net Banking", "Demand Draft"], width=26, state="readonly")
        mode_cb.grid(row=4, column=1, padx=10, pady=6); mode_cb.current(0)

        def process_payment():
            r_no = r_entry.get().strip()
            amt = amt_entry.get().strip()
            if not student_cb.get() or not fee_cb.get() or not amt:
                messagebox.showwarning("Error", "All fields are required!")
                return
            s_id = int(student_cb.get().split(" - ")[0])
            f_id = int(fee_cb.get().split(" - ")[0])
            try:
                conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
                cur.execute("""
                    INSERT INTO fee_payments (receipt_no, student_id, fee_structure_id, amount_paid, payment_mode, payment_date, remarks)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (r_no, s_id, f_id, float(amt), mode_cb.get(), datetime.now().strftime("%Y-%m-%d"), "Paid in Full"))
                conn.commit(); conn.close()
                messagebox.showinfo("Payment Successful", f"Payment of ₹{float(amt):,.2f} recorded!\nReceipt: {r_no}")
                self.show_ledger()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", f"Receipt {r_no} already exists!")

        tk.Button(card, text="💳 Confirm & Save Payment", bg="#059669", fg="#fff", font=("Segoe UI", 10, "bold"), relief="flat", padx=15, pady=8, command=process_payment).grid(row=5, column=1, sticky="e", pady=15)

    # --- SCREEN 4: Transaction Ledger & Search ---
    def show_ledger(self):
        self.clear_content()
        tk.Label(self.content_area, text="Fee Transactions Ledger & Receipts", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w")

        # Search bar
        sf = tk.Frame(self.content_area, bg="#f8fafc", pady=8)
        sf.pack(fill="x")
        tk.Label(sf, text="Search (Receipt / Student / Mode):", font=("Segoe UI", 9, "bold"), bg="#f8fafc").pack(side="left")
        q_ent = tk.Entry(sf, font=("Segoe UI", 9), width=24)
        q_ent.pack(side="left", padx=8)

        cols = ("rec", "student", "enr", "category", "amount", "mode", "date")
        tree = ttk.Treeview(self.content_area, columns=cols, show="headings", height=13)
        for c, h in zip(cols, ["Receipt No", "Student Name", "Enrollment", "Fee Category", "Amount Paid", "Mode", "Date"]):
            tree.heading(c, text=h)
        tree.pack(fill="both", expand=True, pady=5)

        def load(query=None):
            tree.delete(*tree.get_children())
            conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
            base = """
                SELECT p.receipt_no, s.name, s.enrollment_no, f.category, p.amount_paid, p.payment_mode, p.payment_date
                FROM fee_payments p
                JOIN students s ON p.student_id = s.id
                JOIN fee_structures f ON p.fee_structure_id = f.id
            """
            if query:
                base += " WHERE p.receipt_no LIKE ? OR s.name LIKE ? OR s.enrollment_no LIKE ? OR p.payment_mode LIKE ?"
                cur.execute(base, (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%"))
            else:
                base += " ORDER BY p.id DESC"
                cur.execute(base)
            for r in cur.fetchall():
                tree.insert("", "end", values=(r[0], r[1], r[2], r[3], f"₹ {r[4]:,.2f}", r[5], r[6]))
            conn.close()

        tk.Button(sf, text="🔍 Search", bg="#2563eb", fg="#fff", font=("Segoe UI", 9, "bold"), relief="flat", padx=10, command=lambda: load(q_ent.get().strip())).pack(side="left")
        tk.Button(sf, text="Reset", bg="#e2e8f0", relief="flat", padx=10, command=lambda: load()).pack(side="left", padx=5)

        load()

    # --- SCREEN 5: Reports & Analytics ---
    def show_reports(self):
        self.clear_content()
        tk.Label(self.content_area, text="Financial Revenue Reports & Summary", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w", pady=(0, 15))

        box = tk.LabelFrame(self.content_area, text=" Branch-Wise Fee Collection Summary ", font=("Segoe UI", 10, "bold"), bg="#ffffff", padx=15, pady=15, relief="solid", bd=1)
        box.pack(fill="both", expand=True)

        conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
        cur.execute("""
            SELECT s.branch, COUNT(p.id) as receipts, SUM(p.amount_paid) as total
            FROM students s
            LEFT JOIN fee_payments p ON s.id = p.student_id
            GROUP BY s.branch
        """)
        rows = cur.fetchall()
        conn.close()

        cols = ("branch", "tx_count", "total_rev")
        tree = ttk.Treeview(box, columns=cols, show="headings", height=8)
        tree.heading("branch", text="Department / Branch")
        tree.heading("tx_count", text="Total Transactions")
        tree.heading("total_rev", text="Total Revenue Collected")
        for r in rows:
            tree.insert("", "end", values=(r[0], f"{r[1]} payments", f"₹ {r[2] if r[2] else 0:,.2f}"))
        tree.pack(fill="both", expand=True)

    # --- SCREEN 6: Export / Import Center ---
    def show_export_import(self):
        self.clear_content()
        tk.Label(self.content_area, text="Data Export & Import Center", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w", pady=(0, 15))

        card = tk.Frame(self.content_area, bg="#ffffff", padx=25, pady=25, relief="solid", bd=1)
        card.pack(fill="both", expand=True)

        tk.Label(card, text="File Operations (CSV, JSON & Text Receipts):", font=("Segoe UI", 11, "bold"), bg="#ffffff").pack(anchor="w", pady=(0, 15))

        def export_csv():
            path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV (*.csv)", "*.csv")], title="Export Fee Payments to CSV")
            if path:
                conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
                cur.execute("SELECT receipt_no, student_id, fee_structure_id, amount_paid, payment_mode, payment_date FROM fee_payments")
                rows = cur.fetchall(); conn.close()
                with open(path, "w", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    w.writerow(["receipt_no", "student_id", "fee_structure_id", "amount_paid", "payment_mode", "payment_date"])
                    w.writerows(rows)
                messagebox.showinfo("Export Success", f"Exported {len(rows)} payment records to {os.path.basename(path)}!")

        def export_json():
            path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON (*.json)", "*.json")], title="Export Records to JSON")
            if path:
                conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
                cur.execute("SELECT receipt_no, amount_paid, payment_mode, payment_date FROM fee_payments")
                data = [{"receipt_no": r[0], "amount": r[1], "mode": r[2], "date": r[3]} for r in cur.fetchall()]
                conn.close()
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
                messagebox.showinfo("Export Success", f"Successfully exported JSON data!")

        def import_csv():
            path = filedialog.askopenfilename(filetypes=[("CSV (*.csv)", "*.csv")], title="Import Fee Records CSV")
            if path:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        r = csv.reader(f); next(r)
                        conn = sqlite3.connect(DB_NAME); cur = conn.cursor()
                        count = 0
                        for row in r:
                            cur.execute("INSERT OR IGNORE INTO fee_payments (receipt_no, student_id, fee_structure_id, amount_paid, payment_mode, payment_date) VALUES (?, ?, ?, ?, ?, ?)", row)
                            count += 1
                        conn.commit(); conn.close()
                    messagebox.showinfo("Import Success", f"Successfully read & imported {count} records back into application!")
                    self.show_ledger()
                except Exception as e:
                    messagebox.showerror("Import Error", f"Failed to import: {e}")

        tk.Button(card, text="📥 Export Payments to CSV File", font=("Segoe UI", 10, "bold"), bg="#059669", fg="#fff", padx=15, pady=8, relief="flat", command=export_csv).pack(anchor="w", pady=6)
        tk.Button(card, text="📦 Export Payments to JSON File", font=("Segoe UI", 10, "bold"), bg="#2563eb", fg="#fff", padx=15, pady=8, relief="flat", command=export_json).pack(anchor="w", pady=6)
        tk.Button(card, text="📤 Import Records back from CSV File", font=("Segoe UI", 10, "bold"), bg="#7c3aed", fg="#fff", padx=15, pady=8, relief="flat", command=import_csv).pack(anchor="w", pady=6)

    # --- SCREEN 7: About System ---
    def show_about(self):
        self.clear_content()
        tk.Label(self.content_area, text="About Major Project – II", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w", pady=(0, 15))

        box = tk.Frame(self.content_area, bg="#ffffff", padx=25, pady=25, relief="solid", bd=1)
        box.pack(fill="both", expand=True)

        details = [
            ("Project Theme:", "College Fee Collection & Financial Accounting System"),
            ("Course:", "Application Design & Development using Vibe Coding (DI05000121)"),
            ("Institute:", "Govt. Polytechnic College, Jamnagar"),
            ("Student Enrollment:", "246250307086 (Diploma Computer Engineering - Sem 5)"),
            ("Database Engine:", "SQLite3 with 3 Normalized Relational Tables"),
            ("Executable Build:", "Compiled Standalone Windows Executable (.exe) via PyInstaller"),
            ("Repository:", "https://github.com/adi02022009in-maker/Sample-Vibe")
        ]

        for k, v in details:
            row = tk.Frame(box, bg="#ffffff", pady=6)
            row.pack(fill="x")
            tk.Label(row, text=k, font=("Segoe UI", 10, "bold"), bg="#ffffff", width=22, anchor="w").pack(side="left")
            tk.Label(row, text=v, font=("Segoe UI", 10), bg="#ffffff", fg="#334155").pack(side="left")

if __name__ == "__main__":
    app = FeeManagementApp()
    app.mainloop()
