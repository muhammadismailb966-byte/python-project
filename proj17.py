import tkinter as tk
from tkinter import messagebox
import math


# =========================
# MAIN WINDOW
# =========================

window = tk.Tk()
window.title("Scientific Calculator Pro")
window.geometry("850x600")
window.resizable(False, False)
window.configure(bg="#10141c")


# =========================
# COLORS
# =========================

BG = "#10141c"
CARD = "#181e29"
DISPLAY = "#0d1117"
TEXT = "#ffffff"
SECONDARY = "#9aa4b2"
ACCENT = "#00d4ff"
BUTTON = "#242c3a"
OPERATOR = "#303b4d"
DANGER = "#ff4757"


# =========================
# VARIABLES
# =========================

expression = ""
display_var = tk.StringVar()


# =========================
# HEADER
# =========================

header = tk.Frame(window, bg=BG)
header.pack(fill="x", padx=25, pady=(20, 10))

title = tk.Label(
    header,
    text="🧮 SCIENTIFIC CALCULATOR",
    font=("Arial", 18, "bold"),
    bg=BG,
    fg=TEXT
)
title.pack(side="left")

status = tk.Label(
    header,
    text="● READY",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg="#00e676"
)
status.pack(side="right")


# =========================
# MAIN AREA
# =========================

main_frame = tk.Frame(window, bg=BG)
main_frame.pack(fill="both", expand=True, padx=25, pady=10)


# =========================
# CALCULATOR CARD
# =========================

calculator = tk.Frame(
    main_frame,
    bg=CARD,
    highlightbackground="#2b3444",
    highlightthickness=1
)

calculator.pack(
    side="left",
    fill="both",
    expand=True
)


# =========================
# DISPLAY
# =========================

display = tk.Entry(
    calculator,
    textvariable=display_var,
    font=("Arial", 30, "bold"),
    justify="right",
    bg=DISPLAY,
    fg=ACCENT,
    insertbackground=TEXT,
    relief="flat",
    bd=0
)

display.pack(
    padx=20,
    pady=20,
    fill="x",
    ipady=15
)


# =========================
# BUTTON FUNCTIONS
# =========================

def press(value):
    global expression

    expression += str(value)
    display_var.set(expression)


def clear():
    global expression

    expression = ""
    display_var.set("")


def backspace():
    global expression

    expression = expression[:-1]
    display_var.set(expression)


def calculate():
    global expression

    if not expression:
        return

    try:
        # Basic calculation
        result = eval(
            expression,
            {"__builtins__": None},
            {
                "sqrt": math.sqrt,
                "pow": pow
            }
        )

        add_history(
            f"{expression} = {result}"
        )

        expression = str(result)
        display_var.set(expression)

    except ZeroDivisionError:
        messagebox.showerror(
            "Error",
            "Cannot divide by zero."
        )

    except Exception:
        messagebox.showerror(
            "Error",
            "Invalid calculation."
        )


def square_root():
    global expression

    try:
        value = float(expression)

        if value < 0:
            raise ValueError

        result = math.sqrt(value)

        add_history(
            f"√{value} = {result}"
        )

        expression = str(result)
        display_var.set(expression)

    except:
        messagebox.showerror(
            "Error",
            "Enter a valid positive number."
        )


def power():
    global expression

    try:
        value = float(expression)

        result = value ** 2

        add_history(
            f"{value}² = {result}"
        )

        expression = str(result)
        display_var.set(expression)

    except:
        messagebox.showerror(
            "Error",
            "Enter a valid number."
        )


def percentage():
    global expression

    try:
        value = float(expression)

        result = value / 100

        add_history(
            f"{value}% = {result}"
        )

        expression = str(result)
        display_var.set(expression)

    except:
        messagebox.showerror(
            "Error",
            "Enter a valid number."
        )


# =========================
# BUTTON CREATOR
# =========================

def create_button(
    parent,
    text,
    command,
    bg=BUTTON
):

    return tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 13, "bold"),
        bg=bg,
        fg=TEXT,
        activebackground="#3b4658",
        activeforeground=TEXT,
        relief="flat",
        bd=0,
        cursor="hand2"
    )


# =========================
# BUTTON FRAME
# =========================

buttons_frame = tk.Frame(
    calculator,
    bg=CARD
)

buttons_frame.pack(
    padx=20,
    pady=5,
    fill="both",
    expand=True
)


# =========================
# BUTTONS
# =========================

buttons = [
    ("C", clear, DANGER),
    ("⌫", backspace, BUTTON),
    ("%", percentage, OPERATOR),
    ("÷", lambda: press("/"), OPERATOR),

    ("7", lambda: press("7"), BUTTON),
    ("8", lambda: press("8"), BUTTON),
    ("9", lambda: press("9"), BUTTON),
    ("×", lambda: press("*"), OPERATOR),

    ("4", lambda: press("4"), BUTTON),
    ("5", lambda: press("5"), BUTTON),
    ("6", lambda: press("6"), BUTTON),
    ("−", lambda: press("-"), OPERATOR),

    ("1", lambda: press("1"), BUTTON),
    ("2", lambda: press("2"), BUTTON),
    ("3", lambda: press("3"), BUTTON),
    ("+", lambda: press("+"), OPERATOR),

    ("√", square_root, OPERATOR),
    ("x²", power, OPERATOR),
    ("0", lambda: press("0"), BUTTON),
    (".", lambda: press("."), BUTTON),

    ("(", lambda: press("("), BUTTON),
    (")", lambda: press(")"), BUTTON),
    ("=", calculate, ACCENT),
]


# =========================
# PLACE BUTTONS
# =========================

row = 0
column = 0

for text, command, color in buttons:

    button = create_button(
        buttons_frame,
        text,
        command,
        color
    )

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4,
        sticky="nsew"
    )

    column += 1

    if column == 4:
        column = 0
        row += 1


# Make grid responsive
for i in range(4):
    buttons_frame.columnconfigure(
        i,
        weight=1
    )

for i in range(6):
    buttons_frame.rowconfigure(
        i,
        weight=1
    )


# =========================
# HISTORY PANEL
# =========================

history_frame = tk.Frame(
    main_frame,
    bg=CARD,
    width=250,
    highlightbackground="#2b3444",
    highlightthickness=1
)

history_frame.pack(
    side="right",
    fill="y",
    padx=(15, 0)
)

history_frame.pack_propagate(False)


history_title = tk.Label(
    history_frame,
    text="🕘 HISTORY",
    font=("Arial", 14, "bold"),
    bg=CARD,
    fg=TEXT
)

history_title.pack(
    pady=15
)


history_list = tk.Listbox(
    history_frame,
    font=("Arial", 10),
    bg=DISPLAY,
    fg=TEXT,
    selectbackground=ACCENT,
    selectforeground="#10141c",
    relief="flat",
    bd=0
)

history_list.pack(
    padx=12,
    pady=5,
    fill="both",
    expand=True
)


# =========================
# ADD HISTORY
# =========================

def add_history(item):

    history_list.insert(
        tk.END,
        item
    )


# =========================
# CLEAR HISTORY
# =========================

def clear_history():

    history_list.delete(
        0,
        tk.END
    )


clear_history_button = tk.Button(
    history_frame,
    text="Clear History",
    command=clear_history,
    font=("Arial", 10, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=DANGER,
    relief="flat",
    bd=0,
    cursor="hand2"
)

clear_history_button.pack(
    pady=12,
    padx=12,
    fill="x",
    ipady=7
)


# =========================
# KEYBOARD SUPPORT
# =========================

def keyboard_input(event):

    key = event.char

    if key in "0123456789+-*/().":
        press(key)

    elif event.keysym == "Return":
        calculate()

    elif event.keysym == "BackSpace":
        backspace()

    elif event.keysym == "Escape":
        clear()


window.bind(
    "<Key>",
    keyboard_input
)


# =========================
# START APPLICATION
# =========================

window.mainloop()