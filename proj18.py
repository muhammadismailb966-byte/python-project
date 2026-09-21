import tkinter as tk
from tkinter import messagebox


# =========================
# QUESTIONS
# =========================

questions = [
    {
        "question": "Which language is used to create this application?",
        "options": ["Java", "Python", "C++", "PHP"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "define", "def", "func"],
        "answer": "def"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "<!--"],
        "answer": "#"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["String", "Integer", "Boolean", "Float"],
        "answer": "Boolean"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["display()", "echo()", "print()", "show()"],
        "answer": "print()"
    }
]


# =========================
# WINDOW
# =========================

window = tk.Tk()
window.title("Python Quiz")
window.geometry("700x500")
window.resizable(False, False)
window.configure(bg="#10141c")


BG = "#10141c"
CARD = "#181e29"
TEXT = "#ffffff"
SECONDARY = "#9aa4b2"
ACCENT = "#00d4ff"
BUTTON = "#242c3a"
GREEN = "#00e676"
RED = "#ff4757"


# =========================
# VARIABLES
# =========================

current_question = 0
score = 0
selected_answer = tk.StringVar()


# =========================
# HEADER
# =========================

header = tk.Frame(window, bg=BG)
header.pack(fill="x", padx=30, pady=25)

title = tk.Label(
    header,
    text="📝 PYTHON QUIZ",
    font=("Arial", 20, "bold"),
    bg=BG,
    fg=TEXT
)
title.pack(side="left")

progress = tk.Label(
    header,
    text="Question 1/5",
    font=("Arial", 11, "bold"),
    bg=BG,
    fg=ACCENT
)
progress.pack(side="right")


# =========================
# CARD
# =========================

card = tk.Frame(
    window,
    bg=CARD,
    highlightbackground="#2b3444",
    highlightthickness=1
)

card.pack(
    padx=30,
    pady=5,
    fill="both",
    expand=True
)


# =========================
# QUESTION
# =========================

question_label = tk.Label(
    card,
    text="",
    font=("Arial", 17, "bold"),
    bg=CARD,
    fg=TEXT,
    wraplength=580
)

question_label.pack(
    pady=(35, 25)
)


# =========================
# OPTIONS
# =========================

options_frame = tk.Frame(card, bg=CARD)
options_frame.pack(fill="x", padx=60)


# =========================
# LOAD QUESTION
# =========================

def load_question():

    selected_answer.set("")

    question = questions[current_question]

    question_label.config(
        text=question["question"]
    )

    progress.config(
        text=f"Question {current_question + 1}/{len(questions)}"
    )

    for widget in options_frame.winfo_children():
        widget.destroy()

    for option in question["options"]:

        radio = tk.Radiobutton(
            options_frame,
            text=option,
            variable=selected_answer,
            value=option,
            font=("Arial", 12),
            bg=CARD,
            fg=TEXT,
            selectcolor="#0d1117",
            activebackground=CARD,
            activeforeground=TEXT,
            anchor="w",
            padx=15,
            pady=8
        )

        radio.pack(
            fill="x",
            pady=4
        )


# =========================
# NEXT QUESTION
# =========================

def next_question():

    global current_question
    global score

    answer = selected_answer.get()

    if not answer:
        messagebox.showwarning(
            "Select Answer",
            "Please select an answer first."
        )
        return

    correct_answer = questions[current_question]["answer"]

    if answer == correct_answer:
        score += 1
        messagebox.showinfo(
            "Correct!",
            "✓ Your answer is correct!"
        )
    else:
        messagebox.showerror(
            "Wrong Answer",
            f"✗ Correct answer: {correct_answer}"
        )

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        show_result()


# =========================
# FINAL RESULT
# =========================

def show_result():

    for widget in window.winfo_children():
        widget.destroy()

    result_card = tk.Frame(
        window,
        bg=CARD,
        highlightbackground="#2b3444",
        highlightthickness=1
    )

    result_card.pack(
        padx=60,
        pady=50,
        fill="both",
        expand=True
    )

    tk.Label(
        result_card,
        text="🎉 QUIZ COMPLETED!",
        font=("Arial", 24, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(pady=(60, 25))

    percentage = (score / len(questions)) * 100

    tk.Label(
        result_card,
        text=f"Your Score: {score}/{len(questions)}",
        font=("Arial", 20, "bold"),
        bg=CARD,
        fg=ACCENT
    ).pack(pady=10)

    tk.Label(
        result_card,
        text=f"Percentage: {percentage:.0f}%",
        font=("Arial", 15),
        bg=CARD,
        fg=SECONDARY
    ).pack(pady=5)

    tk.Button(
        result_card,
        text="EXIT",
        command=window.destroy,
        font=("Arial", 11, "bold"),
        bg=BUTTON,
        fg=TEXT,
        relief="flat",
        padx=30,
        pady=10,
        cursor="hand2"
    ).pack(pady=35)


# =========================
# NEXT BUTTON
# =========================

next_button = tk.Button(
    card,
    text="NEXT →",
    command=next_question,
    font=("Arial", 11, "bold"),
    bg=ACCENT,
    fg=BG,
    relief="flat",
    padx=30,
    pady=10,
    cursor="hand2"
)

next_button.pack(pady=30)


# =========================
# START
# =========================

load_question()

window.mainloop()