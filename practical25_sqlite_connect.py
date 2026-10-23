"""
Practical No. 25: Create an SQLite database and connect it with a Python desktop application.
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3
import os

DB_NAME = "vibe_college.db"

def init_database():
    """Create database and initial tables if they do not exist."""
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
    root = tk.Tk()
    root.title("Practical 25: SQLite Database Connection")
    root.geometry("560x480")
    root.configure(bg="#f8fafc")
    root.resizable(False, False)

    # 1. Header Banner
    header = tk.Label(
        root,
        text="SQLite Database Integration",
        font=("Segoe UI", 16, "bold"),
        bg="#1e3a8a",
        fg="#ffffff",
        pady=12
    )
    header.pack(fill="x")

    # 2. Connection Info Card
    info_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=15, relief="solid", bd=1)
    info_frame.pack(padx=20, pady=15, fill="x")

    db_path = os.path.abspath(DB_NAME)

    tk.Label(info_frame, text="Database File:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=0, column=0, sticky="w", pady=3)
    tk.Label(info_frame, text=DB_NAME, font=("Consolas", 10, "bold"), bg="#ffffff", fg="#2563eb").grid(row=0, column=1, sticky="w", padx=10, pady=3)

    tk.Label(info_frame, text="SQLite Version:", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").grid(row=1, column=0, sticky="w", pady=3)
    tk.Label(info_frame, text=sqlite3.sqlite_version, font=("Consolas", 10), bg="#ffffff", fg="#16a34a").grid(row=1, column=1, sticky="w", padx=10, pady=3)

    status_var = tk.StringVar(value="Status: Click 'Test Connection' to verify")
    status_label = tk.Label(info_frame, textvariable=status_var, font=("Segoe UI", 9, "italic"), bg="#f1f5f9", fg="#475569", pady=5)
    status_label.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10, 0))

    # 3. Output Log Text Area
    log_area = scrolledtext.ScrolledText(root, height=10, font=("Consolas", 9), relief="solid", bd=1, padx=8, pady=8)
    log_area.pack(padx=20, pady=5, fill="both", expand=True)

    def log(msg):
        log_area.insert(tk.END, msg + "\n")
        log_area.see(tk.END)

    # 4. Database Action Callbacks
    def test_connection():
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("SELECT datetime('now', 'localtime')")
            server_time = cursor.fetchone()[0]
            conn.close()

            status_var.set("🟢 Status: Connected Successfully!")
            log(f"[SUCCESS] Connected to '{DB_NAME}'")
            log(f"          SQLite Engine Time: {server_time}")
            log(f"          Absolute Path: {db_path}")
            messagebox.showinfo("Connection Verified", f"Connected to SQLite Database successfully!\n\nEngine Time: {server_time}")
        except Exception as e:
            status_var.set("🔴 Status: Connection Failed")
            log(f"[ERROR] Failed to connect: {e}")
            messagebox.showerror("Error", str(e))

    def create_table_schema():
        try:
            init_database()
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(students)")
            columns = cursor.fetchall()
            conn.close()

            status_var.set("🟢 Table 'students' Verified / Created!")
            log("\n[SCHEMA] Table 'students' structure:")
            log("---------------------------------------------------------")
            log(f"{'Col ID':<8} {'Column Name':<18} {'Data Type':<12} {'NotNull':<8}")
            log("---------------------------------------------------------")
            for col in columns:
                log(f"{col[0]:<8} {col[1]:<18} {col[2]:<12} {bool(col[3])}")
            log("---------------------------------------------------------")
            messagebox.showinfo("Schema Ready", "Table 'students' created and schema verified successfully!")
        except Exception as e:
            log(f"[ERROR] Schema creation failed: {e}")
            messagebox.showerror("Error", str(e))

    # 5. Buttons Toolbar
    btn_frame = tk.Frame(root, bg="#f8fafc")
    btn_frame.pack(pady=12)

    btn_test = tk.Button(
        btn_frame,
        text="🔌 Test DB Connection",
        font=("Segoe UI", 10, "bold"),
        bg="#2563eb",
        fg="#ffffff",
        padx=12,
        pady=6,
        relief="flat",
        cursor="hand2",
        command=test_connection
    )
    btn_test.pack(side="left", padx=8)

    btn_schema = tk.Button(
        btn_frame,
        text="🛠️ Create / Inspect Table",
        font=("Segoe UI", 10, "bold"),
        bg="#16a34a",
        fg="#ffffff",
        padx=12,
        pady=6,
        relief="flat",
        cursor="hand2",
        command=create_table_schema
    )
    btn_schema.pack(side="left", padx=8)

    # Initial Welcome Log
    log("Practical 25: SQLite Database Connectivity")
    log("Click 'Test DB Connection' or 'Create / Inspect Table' below.\n")

    root.mainloop()

if __name__ == "__main__":
    main()
