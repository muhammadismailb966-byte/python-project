import tkinter as tk
from tkinter import messagebox


expenses = []


def add_expense():
    item = item_entry.get().strip()

    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")
        return

    if not item:
        messagebox.showwarning("Warning", "Enter expense name")
        return

    expenses.append((item, amount))

    listbox.insert(
        tk.END,
        f"{item}  -  Rs. {amount:.2f}"
    )

    total.set(
        f"Total: Rs. {sum(x[1] for x in expenses):.2f}"
    )

    item_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


def clear_all():
    expenses.clear()
    listbox.delete(0, tk.END)
    total.set("Total: Rs. 0.00")


root = tk.Tk()
root.title("Expense Tracker Pro")
root.geometry("550x600")
root.configure(bg="#0f172a")

tk.Label(
    root,
    text="💰 Expense Tracker Pro",
    font=("Arial", 22, "bold"),
    bg="#0f172a",
    fg="white"
).pack(pady=20)

frame = tk.Frame(root, bg="#0f172a")
frame.pack(padx=30, fill="x")

item_entry = tk.Entry(
    frame,
    font=("Arial", 12)
)
item_entry.pack(
    fill="x",
    pady=5,
    ipady=8
)
item_entry.insert(0, "Expense name")

amount_entry = tk.Entry(
    frame,
    font=("Arial", 12)
)
amount_entry.pack(
    fill="x",
    pady=5,
    ipady=8
)
amount_entry.insert(0, "Amount")

tk.Button(
    frame,
    text="Add Expense",
    command=add_expense,
    bg="#38bdf8",
    font=("Arial", 11, "bold")
).pack(
    fill="x",
    pady=10
)

listbox = tk.Listbox(
    root,
    bg="#1e293b",
    fg="white",
    font=("Arial", 12)
)
listbox.pack(
    padx=30,
    pady=15,
    fill="both",
    expand=True
)

total = tk.StringVar(
    value="Total: Rs. 0.00"
)

tk.Label(
    root,
    textvariable=total,
    font=("Arial", 16, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
).pack(pady=10)

tk.Button(
    root,
    text="Clear All",
    command=clear_all,
    bg="#334155",
    fg="white",
    font=("Arial", 11, "bold")
).pack(
    pady=15
)

root.mainloop()

