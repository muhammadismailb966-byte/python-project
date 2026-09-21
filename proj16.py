import tkinter as tk
from tkinter import messagebox
import string
import secrets


# =========================
# MAIN WINDOW
# =========================

window = tk.Tk()
window.title("Password Generator Pro")
window.geometry("650x500")
window.resizable(False, False)
window.configure(bg="#10141c")


# =========================
# COLORS
# =========================

BG = "#10141c"
CARD = "#181e29"
TEXT = "#ffffff"
SECONDARY = "#9aa4b2"
ACCENT = "#00d4ff"
BUTTON = "#242c3a"
SUCCESS = "#00e676"
DANGER = "#ff4757"


# =========================
# HEADER
# =========================

header = tk.Frame(window, bg=BG)
header.pack(fill="x", padx=30, pady=(25, 10))

title = tk.Label(
    header,
    text="🔐 PASSWORD GENERATOR",
    font=("Arial", 18, "bold"),
    bg=BG,
    fg=TEXT
)
title.pack(side="left")

status = tk.Label(
    header,
    text="● SECURE",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=SUCCESS
)
status.pack(side="right")


# =========================
# MAIN CARD
# =========================

card = tk.Frame(
    window,
    bg=CARD,
    highlightbackground="#2b3444",
    highlightthickness=1
)

card.pack(
    padx=30,
    pady=15,
    fill="both",
    expand=True
)


# =========================
# PASSWORD DISPLAY
# =========================

password_var = tk.StringVar()

password_entry = tk.Entry(
    card,
    textvariable=password_var,
    font=("Arial", 20, "bold"),
    justify="center",
    bg="#0d1117",
    fg=ACCENT,
    insertbackground=TEXT,
    relief="flat",
    bd=0
)

password_entry.pack(
    padx=30,
    pady=(30, 10),
    ipady=12,
    fill="x"
)


# =========================
# STRENGTH
# =========================

strength_label = tk.Label(
    card,
    text="Password Strength: -",
    font=("Arial", 12, "bold"),
    bg=CARD,
    fg=SECONDARY
)

strength_label.pack(pady=5)


# =========================
# LENGTH
# =========================

length_frame = tk.Frame(card, bg=CARD)
length_frame.pack(pady=15)

length_label = tk.Label(
    length_frame,
    text="Password Length:",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=TEXT
)
length_label.pack(side="left", padx=10)

length_var = tk.IntVar(value=16)

length_spinbox = tk.Spinbox(
    length_frame,
    from_=6,
    to=50,
    textvariable=length_var,
    width=5,
    font=("Arial", 12),
    justify="center"
)
length_spinbox.pack(side="left")


# =========================
# OPTIONS
# =========================

options_frame = tk.Frame(card, bg=CARD)
options_frame.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)


def create_checkbox(text, variable):
    return tk.Checkbutton(
        options_frame,
        text=text,
        variable=variable,
        font=("Arial", 10),
        bg=CARD,
        fg=TEXT,
        selectcolor="#0d1117",
        activebackground=CARD,
        activeforeground=TEXT
    )


create_checkbox("Uppercase", uppercase_var).grid(
    row=0, column=0, padx=8
)

create_checkbox("Lowercase", lowercase_var).grid(
    row=0, column=1, padx=8
)

create_checkbox("Numbers", numbers_var).grid(
    row=0, column=2, padx=8
)

create_checkbox("Symbols", symbols_var).grid(
    row=0, column=3, padx=8
)


# =========================
# STRENGTH CHECK
# =========================

def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        strength_label.config(
            text="Password Strength: WEAK",
            fg=DANGER
        )

    elif score <= 4:
        strength_label.config(
            text="Password Strength: MEDIUM",
            fg="#ffa502"
        )

    else:
        strength_label.config(
            text="Password Strength: STRONG",
            fg=SUCCESS
        )


# =========================
# GENERATE PASSWORD
# =========================

def generate_password():

    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Length",
            "Please enter a valid password length."
        )
        return

    characters = ""

    if uppercase_var.get():
        characters += string.ascii_uppercase

    if lowercase_var.get():
        characters += string.ascii_lowercase

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning(
            "No Options Selected",
            "Please select at least one character type."
        )
        return

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    password_var.set(password)

    check_strength(password)


# =========================
# COPY PASSWORD
# =========================

def copy_password():

    password = password_var.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Please generate a password first."
        )
        return

    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )


# =========================
# CLEAR
# =========================

def clear_password():

    password_var.set("")

    strength_label.config(
        text="Password Strength: -",
        fg=SECONDARY
    )


# =========================
# BUTTONS
# =========================

button_frame = tk.Frame(card, bg=CARD)
button_frame.pack(pady=20)


generate_button = tk.Button(
    button_frame,
    text="🔄 Generate",
    font=("Arial", 11, "bold"),
    bg=ACCENT,
    fg="#10141c",
    activebackground="#00b8d9",
    relief="flat",
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2",
    command=generate_password
)

generate_button.grid(
    row=0, column=0, padx=6
)


copy_button = tk.Button(
    button_frame,
    text="📋 Copy",
    font=("Arial", 11, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground="#303b4d",
    relief="flat",
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2",
    command=copy_password
)

copy_button.grid(
    row=0, column=1, padx=6
)


clear_button = tk.Button(
    button_frame,
    text="🧹 Clear",
    font=("Arial", 11, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground="#303b4d",
    relief="flat",
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2",
    command=clear_password
)

clear_button.grid(
    row=0, column=2, padx=6
)


# =========================
# EXIT BUTTON
# =========================

exit_button = tk.Button(
    window,
    text="EXIT",
    font=("Arial", 10, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=DANGER,
    activeforeground=TEXT,
    relief="flat",
    bd=0,
    padx=25,
    pady=8,
    cursor="hand2",
    command=window.destroy
)

exit_button.pack(pady=(0, 20))


# =========================
# START APPLICATION
# =========================

generate_password()

window.mainloop()