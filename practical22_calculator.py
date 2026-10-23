"""
Practical No. 22: Generate a simple calculator desktop application using AI coding tools.
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar
"""

import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("Practical 22: Simple Calculator")
    root.geometry("340x460")
    root.configure(bg="#1e1e2e")
    root.resizable(False, False)

    expression = ""

    # 1. Display Screen Frame & Entry Widget
    display_frame = tk.Frame(root, bg="#1e1e2e", padx=15, pady=15)
    display_frame.pack(fill="x")

    display_var = tk.StringVar(value="0")
    display_entry = tk.Entry(
        display_frame,
        textvariable=display_var,
        font=("Segoe UI", 26, "bold"),
        bg="#181825",
        fg="#cdd6f4",
        justify="right",
        relief="flat",
        bd=10
    )
    display_entry.pack(fill="x", ipady=8)

    # 2. Calculator Logic Functions
    def button_click(value):
        nonlocal expression
        if display_var.get() == "0" and value not in ["+", "-", "*", "/", "%", "."]:
            expression = str(value)
        else:
            expression += str(value)
        display_var.set(expression)

    def calculate():
        nonlocal expression
        try:
            # Handle percentage conversion
            clean_expr = expression.replace("%", "/100")
            result = eval(clean_expr)
            # Format integer results without trailing .0
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            display_var.set(str(result))
            expression = str(result)
        except ZeroDivisionError:
            display_var.set("Error: Div by 0")
            expression = ""
        except Exception:
            display_var.set("Error")
            expression = ""

    def clear():
        nonlocal expression
        expression = ""
        display_var.set("0")

    def backspace():
        nonlocal expression
        expression = expression[:-1]
        display_var.set(expression if expression else "0")

    # 3. Calculator Buttons Layout Matrix
    buttons = [
        ("C", clear, "#f38ba8", "#11111b"),
        ("⌫", backspace, "#fab387", "#11111b"),
        ("%", lambda: button_click("%"), "#89b4fa", "#11111b"),
        ("/", lambda: button_click("/"), "#89b4fa", "#11111b"),
        
        ("7", lambda: button_click("7"), "#313244", "#cdd6f4"),
        ("8", lambda: button_click("8"), "#313244", "#cdd6f4"),
        ("9", lambda: button_click("9"), "#313244", "#cdd6f4"),
        ("*", lambda: button_click("*"), "#89b4fa", "#11111b"),
        
        ("4", lambda: button_click("4"), "#313244", "#cdd6f4"),
        ("5", lambda: button_click("5"), "#313244", "#cdd6f4"),
        ("6", lambda: button_click("6"), "#313244", "#cdd6f4"),
        ("-", lambda: button_click("-"), "#89b4fa", "#11111b"),
        
        ("1", lambda: button_click("1"), "#313244", "#cdd6f4"),
        ("2", lambda: button_click("2"), "#313244", "#cdd6f4"),
        ("3", lambda: button_click("3"), "#313244", "#cdd6f4"),
        ("+", lambda: button_click("+"), "#89b4fa", "#11111b"),
        
        ("0", lambda: button_click("0"), "#313244", "#cdd6f4"),
        (".", lambda: button_click("."), "#313244", "#cdd6f4"),
        ("=", calculate, "#a6e3a1", "#11111b", 2)
    ]

    # 4. Buttons Grid Frame
    btn_frame = tk.Frame(root, bg="#1e1e2e", padx=12, pady=5)
    btn_frame.pack(fill="both", expand=True)

    row_val = 0
    col_val = 0
    for item in buttons:
        text = item[0]
        cmd = item[1]
        bg_col = item[2]
        fg_col = item[3]
        colspan = item[4] if len(item) > 4 else 1

        btn = tk.Button(
            btn_frame,
            text=text,
            font=("Segoe UI", 13, "bold"),
            bg=bg_col,
            fg=fg_col,
            activebackground="#cdd6f4",
            activeforeground="#11111b",
            relief="flat",
            cursor="hand2",
            command=cmd
        )
        btn.grid(row=row_val, column=col_val, columnspan=colspan, sticky="nsew", padx=4, pady=4)

        col_val += colspan
        if col_val >= 4:
            col_val = 0
            row_val += 1

    # Configure grid weights for responsive resizing inside frame
    for r in range(5):
        btn_frame.rowconfigure(r, weight=1)
    for c in range(4):
        btn_frame.columnconfigure(c, weight=1)

    # 5. Keyboard Bindings
    root.bind("<Return>", lambda e: calculate())
    root.bind("<Escape>", lambda e: clear())

    root.mainloop()

if __name__ == "__main__":
    main()
