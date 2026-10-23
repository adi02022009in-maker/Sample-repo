"""
Practical No. 21: Implement event handling (button click actions) in a GUI application.
Subject: Application Design & Development using Vibe Coding (DI05000121)
Govt. Polytechnic College, Jamnagar
"""

import tkinter as tk
from datetime import datetime

def main():
    root = tk.Tk()
    root.title("Practical 21: Tkinter Event Handling")
    root.geometry("520x480")
    root.configure(bg="#f8fafc")
    root.resizable(False, False)

    # 1. Header Banner
    header = tk.Label(
        root,
        text="Interactive Event Handling Demo",
        font=("Segoe UI", 16, "bold"),
        bg="#4338ca",
        fg="#ffffff",
        pady=12
    )
    header.pack(fill="x")

    # 2. State Variable & Counter Display Frame
    count = 0

    counter_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=15, relief="solid", bd=1)
    counter_frame.pack(padx=20, pady=15, fill="x")

    tk.Label(counter_frame, text="Current Counter Value:", font=("Segoe UI", 11), bg="#ffffff", fg="#64748b").pack()
    value_label = tk.Label(counter_frame, text="0", font=("Segoe UI", 32, "bold"), bg="#ffffff", fg="#4338ca")
    value_label.pack(pady=5)

    # 3. Event Log Frame
    log_frame = tk.Frame(root, bg="#ffffff", padx=15, pady=10, relief="solid", bd=1)
    log_frame.pack(padx=20, pady=5, fill="both", expand=True)

    tk.Label(log_frame, text="Live Event Log (Button clicks & Key presses):", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")

    log_listbox = tk.Listbox(log_frame, font=("Consolas", 9), height=7, relief="groove", bd=1)
    log_listbox.pack(fill="both", expand=True, pady=5)

    def log_event(message):
        now = datetime.now().strftime("%H:%M:%S")
        log_listbox.insert(0, f"[{now}] {message}")

    # Initial log entry
    log_event("Application initialized. Ready for user events.")

    # 4. Event Handler Functions
    def increment(event=None):
        nonlocal count
        count += 1
        value_label.config(text=str(count))
        source = "Key Press (Up)" if event else "Button Click"
        log_event(f"{source} -> Incremented to {count}")

    def decrement(event=None):
        nonlocal count
        count -= 1
        value_label.config(text=str(count))
        source = "Key Press (Down)" if event else "Button Click"
        log_event(f"{source} -> Decremented to {count}")

    def reset(event=None):
        nonlocal count
        count = 0
        value_label.config(text="0")
        source = "Key Press (R)" if event else "Button Click"
        log_event(f"{source} -> Counter Reset to 0")

    # 5. Buttons with command= event binding
    btn_frame = tk.Frame(root, bg="#f8fafc")
    btn_frame.pack(pady=15)

    btn_inc = tk.Button(
        btn_frame,
        text="➕ Increment (+1)",
        font=("Segoe UI", 10, "bold"),
        bg="#16a34a",
        fg="#ffffff",
        padx=12,
        pady=6,
        relief="flat",
        cursor="hand2",
        command=increment
    )
    btn_inc.pack(side="left", padx=6)

    btn_dec = tk.Button(
        btn_frame,
        text="➖ Decrement (-1)",
        font=("Segoe UI", 10, "bold"),
        bg="#ea580c",
        fg="#ffffff",
        padx=12,
        pady=6,
        relief="flat",
        cursor="hand2",
        command=decrement
    )
    btn_dec.pack(side="left", padx=6)

    btn_reset = tk.Button(
        btn_frame,
        text="🔄 Reset (0)",
        font=("Segoe UI", 10, "bold"),
        bg="#64748b",
        fg="#ffffff",
        padx=12,
        pady=6,
        relief="flat",
        cursor="hand2",
        command=reset
    )
    btn_reset.pack(side="left", padx=6)

    # 6. Keyboard Event Bindings (binds keys to event handlers)
    root.bind("<Up>", increment)
    root.bind("<Down>", decrement)
    root.bind("<r>", reset)
    root.bind("<R>", reset)

    root.mainloop()

if __name__ == "__main__":
    main()
