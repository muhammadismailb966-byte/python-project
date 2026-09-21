import tkinter as tk
from collections import Counter


# =========================
# WINDOW
# =========================

window = tk.Tk()
window.title("Word & Character Counter")
window.geometry("750x600")
window.resizable(False, False)
window.configure(bg="#10141c")


BG = "#10141c"
CARD = "#181e29"
TEXT = "#ffffff"
SECONDARY = "#9aa4b2"
ACCENT = "#00d4ff"
BUTTON = "#242c3a"


# =========================
# HEADER
# =========================

tk.Label(
    window,
    text="🔎 WORD & CHARACTER COUNTER",
    font=("Arial", 20, "bold"),
    bg=BG,
    fg=TEXT
).pack(pady=(25, 5))


tk.Label(
    window,
    text="Enter your text below",
    font=("Arial", 11),
    bg=BG,
    fg=SECONDARY
).pack(pady=5)


# =========================
# TEXT AREA
# =========================

card = tk.Frame(
    window,
    bg=CARD,
    highlightbackground="#2b3444",
    highlightthickness=1
)

card.pack(
    padx=30,
    pady=20,
    fill="x"
)


text_box = tk.Text(
    card,
    height=10,
    font=("Arial", 12),
    bg="#0d1117",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    bd=0,
    wrap="word"
)

text_box.pack(
    padx=15,
    pady=15,
    fill="x"
)


# =========================
# STATISTICS
# =========================

stats = tk.Frame(window, bg=BG)
stats.pack(pady=10)


word_label = tk.Label(
    stats,
    text="Words: 0",
    font=("Arial", 12, "bold"),
    bg=BUTTON,
    fg=TEXT,
    padx=25,
    pady=12
)

word_label.grid(row=0, column=0, padx=5)


character_label = tk.Label(
    stats,
    text="Characters: 0",
    font=("Arial", 12, "bold"),
    bg=BUTTON,
    fg=TEXT,
    padx=25,
    pady=12
)

character_label.grid(row=0, column=1, padx=5)


space_label = tk.Label(
    stats,
    text="Spaces: 0",
    font=("Arial", 12, "bold"),
    bg=BUTTON,
    fg=TEXT,
    padx=25,
    pady=12
)

space_label.grid(row=0, column=2, padx=5)


line_label = tk.Label(
    stats,
    text="Lines: 0",
    font=("Arial", 12, "bold"),
    bg=BUTTON,
    fg=TEXT,
    padx=25,
    pady=12
)

line_label.grid(row=1, column=0, padx=5, pady=8)


no_space_label = tk.Label(
    stats,
    text="Without Spaces: 0",
    font=("Arial", 12, "bold"),
    bg=BUTTON,
    fg=TEXT,
    padx=25,
    pady=12
)

no_space_label.grid(row=1, column=1, padx=5, pady=8)


repeated_label = tk.Label(
    stats,
    text="Most Repeated: -",
    font=("Arial", 12, "bold"),
    bg=BUTTON,
    fg=TEXT,
    padx=25,
    pady=12
)

repeated_label.grid(row=1, column=2, padx=5, pady=8)


# =========================
# ANALYZE
# =========================

def analyze_text():

    text = text_box.get("1.0", tk.END).strip()

    words = text.split()

    characters = len(text)

    characters_without_spaces = len(
        text.replace(" ", "")
    )

    spaces = text.count(" ")

    lines = len(
        text.splitlines()
    )

    word_count = Counter(
        word.lower().strip(".,!?;:")
        for word in words
    )

    if word_count:
        most_repeated = word_count.most_common(1)[0]

        repeated_text = (
            f"{most_repeated[0]} "
            f"({most_repeated[1]} times)"
        )

    else:
        repeated_text = "-"

    word_label.config(
        text=f"Words: {len(words)}"
    )

    character_label.config(
        text=f"Characters: {characters}"
    )

    space_label.config(
        text=f"Spaces: {spaces}"
    )

    line_label.config(
        text=f"Lines: {lines}"
    )

    no_space_label.config(
        text=f"Without Spaces: {characters_without_spaces}"
    )

    repeated_label.config(
        text=f"Most Repeated: {repeated_text}"
    )


# =========================
# CLEAR
# =========================

def clear_text():

    text_box.delete(
        "1.0",
        tk.END
    )

    word_label.config(text="Words: 0")
    character_label.config(text="Characters: 0")
    space_label.config(text="Spaces: 0")
    line_label.config(text="Lines: 0")
    no_space_label.config(text="Without Spaces: 0")
    repeated_label.config(text="Most Repeated: -")


# =========================
# BUTTONS
# =========================

button_frame = tk.Frame(
    window,
    bg=BG
)

button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="🔎 Analyze Text",
    command=analyze_text,
    font=("Arial", 11, "bold"),
    bg=ACCENT,
    fg=BG,
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2"
).grid(row=0, column=0, padx=8)


tk.Button(
    button_frame,
    text="🧹 Clear",
    command=clear_text,
    font=("Arial", 11, "bold"),
    bg=BUTTON,
    fg=TEXT,
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2"
).grid(row=0, column=1, padx=8)


tk.Button(
    button_frame,
    text="EXIT",
    command=window.destroy,
    font=("Arial", 11, "bold"),
    bg=BUTTON,
    fg=TEXT,
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2"
).grid(row=0, column=2, padx=8)


window.mainloop()