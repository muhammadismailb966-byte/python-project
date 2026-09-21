import tkinter as tk
import random

sentences = [
    "Python is easy to learn",
    "Practice makes you a better programmer",
    "Typing fast requires regular practice",
    "Tkinter is useful for GUI applications",
    "Never stop learning new things"
]

time_left = 30
running = False
score = 0

def start():
    global time_left, running, score

    time_left = 30
    score = 0
    running = True

    sentence.config(text=random.choice(sentences))
    text.delete("1.0", tk.END)
    result.config(text="Start typing...")
    timer.config(text="Time: 30s")
    text.focus()

    countdown()

def countdown():
    global time_left, running

    if time_left > 0 and running:
        time_left -= 1
        timer.config(text=f"Time: {time_left}s")
        root.after(1000, countdown)
    else:
        running = False
        calculate()

def calculate():
    global score

    typed = text.get("1.0", tk.END).strip()
    target = sentence.cget("text")

    correct = sum(
        1 for a, b in zip(typed, target) if a == b
    )

    accuracy = (correct / len(target) * 100) if target else 0
    words = len(typed.split())
    wpm = words * 2

    score = correct

    result.config(
        text=f"🏆 Score: {score}   |   ⚡ WPM: {wpm}   |   🎯 Accuracy: {accuracy:.0f}%"
    )

root = tk.Tk()
root.title("⌨️ Typing Tutor")
root.geometry("650x550")
root.configure(bg="#0f172a")

tk.Label(
    root,
    text="⌨️ TYPING TUTOR",
    font=("Arial", 26, "bold"),
    bg="#0f172a",
    fg="white"
).pack(pady=20)

timer = tk.Label(
    root,
    text="Time: 30s",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
timer.pack()

sentence = tk.Label(
    root,
    text="Press Start to begin",
    font=("Arial", 16, "bold"),
    bg="#1e293b",
    fg="white",
    wraplength=550,
    padx=20,
    pady=20
)
sentence.pack(pady=25)

text = tk.Text(
    root,
    height=6,
    font=("Arial", 15),
    bg="#334155",
    fg="white",
    insertbackground="white"
)
text.pack(padx=40, fill="x")

tk.Button(
    root,
    text="▶ Start / Restart",
    command=start,
    font=("Arial", 13, "bold"),
    bg="#38bdf8",
    padx=30,
    pady=10
).pack(pady=20)

result = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="#22c55e"
)
result.pack(pady=10)

root.mainloop()