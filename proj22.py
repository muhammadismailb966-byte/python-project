import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time


class PomodoroTimer:

    def __init__(self, root):
        self.root = root

        self.root.title("Pomodoro Timer")
        self.root.geometry("620x720")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")

        # Timer settings (in minutes)
        self.work_time = 25
        self.short_break = 5
        self.long_break = 15
        self.sessions_before_long = 4

        # Timer state
        self.current_mode = "work"  # work, short_break, long_break
        self.time_left = self.work_time * 60  # in seconds
        self.total_time = self.work_time * 60
        self.is_running = False
        self.is_paused = False
        self.session_count = 0
        self.total_sessions = 0
        self.timer_thread = None

        self.setup_style()
        self.create_gui()
        self.update_display()

    # ---------------- STYLE ----------------

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Progress.Horizontal.TProgressbar",
            troughcolor="#1e293b",
            background="#ef4444",
            thickness=20
        )

    # ---------------- GUI ----------------

    def create_gui(self):
        # Header
        tk.Label(
            self.root, text="🍅", font=("Segoe UI Emoji", 40),
            bg="#0f172a", fg="white"
        ).pack(pady=(20, 0))

        tk.Label(
            self.root, text="POMODORO TIMER",
            font=("Segoe UI", 22, "bold"), bg="#0f172a", fg="#ef4444"
        ).pack()

        tk.Label(
            self.root, text="Stay focused • Work smarter • Take breaks",
            font=("Segoe UI", 10), bg="#0f172a", fg="#94a3b8"
        ).pack(pady=(3, 12))

        # Main Card
        card = tk.Frame(
            self.root, bg="#1e293b",
            highlightbackground="#334155", highlightthickness=1
        )
        card.pack(padx=40, fill="both", expand=True)

        # Mode Selection Buttons
        mode_frame = tk.Frame(card, bg="#1e293b")
        mode_frame.pack(padx=30, pady=(20, 15), fill="x")

        self.work_btn = tk.Button(
            mode_frame, text="🎯 WORK\n25 min",
            command=lambda: self.switch_mode("work"),
            font=("Segoe UI", 10, "bold"), bg="#ef4444", fg="white",
            activebackground="#dc2626", relief="flat", cursor="hand2",
            pady=10
        )
        self.work_btn.pack(side="left", fill="x", expand=True, padx=2)

        self.short_break_btn = tk.Button(
            mode_frame, text="☕ SHORT BREAK\n5 min",
            command=lambda: self.switch_mode("short_break"),
            font=("Segoe UI", 10, "bold"), bg="#334155", fg="white",
            activebackground="#475569", relief="flat", cursor="hand2",
            pady=10
        )
        self.short_break_btn.pack(side="left", fill="x", expand=True, padx=2)

        self.long_break_btn = tk.Button(
            mode_frame, text="🌴 LONG BREAK\n15 min",
            command=lambda: self.switch_mode("long_break"),
            font=("Segoe UI", 10, "bold"), bg="#334155", fg="white",
            activebackground="#475569", relief="flat", cursor="hand2",
            pady=10
        )
        self.long_break_btn.pack(side="left", fill="x", expand=True, padx=2)

        # Mode Indicator
        self.mode_label = tk.Label(
            card, text="🎯 WORK SESSION",
            font=("Segoe UI", 14, "bold"), bg="#1e293b", fg="#ef4444"
        )
        self.mode_label.pack(pady=(0, 10))

        # Timer Display
        timer_box = tk.Frame(
            card, bg="#0c1220",
            highlightbackground="#ef4444", highlightthickness=3
        )
        timer_box.pack(padx=30, pady=(0, 15), fill="x")

        self.timer_display = tk.Label(
            timer_box, text="25:00",
            font=("Segoe UI", 72, "bold"), bg="#0c1220", fg="#ef4444"
        )
        self.timer_display.pack(pady=30)

        # Progress Bar
        self.progress_var = tk.DoubleVar(value=100)
        self.progress_bar = ttk.Progressbar(
            timer_box, variable=self.progress_var, maximum=100,
            style="Progress.Horizontal.TProgressbar"
        )
        self.progress_bar.pack(fill="x", padx=20, pady=(0, 20))

        # Control Buttons
        control_frame = tk.Frame(card, bg="#1e293b")
        control_frame.pack(padx=30, pady=(0, 15), fill="x")

        self.start_btn = tk.Button(
            control_frame, text="▶ START",
            command=self.start_timer,
            font=("Segoe UI", 12, "bold"), bg="#22c55e", fg="white",
            activebackground="#16a34a", relief="flat", cursor="hand2",
            pady=12
        )
        self.start_btn.pack(side="left", fill="x", expand=True, padx=2)

        self.pause_btn = tk.Button(
            control_frame, text="⏸ PAUSE",
            command=self.pause_timer,
            font=("Segoe UI", 12, "bold"), bg="#f59e0b", fg="white",
            activebackground="#d97706", relief="flat", cursor="hand2",
            pady=12, state="disabled"
        )
        self.pause_btn.pack(side="left", fill="x", expand=True, padx=2)

        self.reset_btn = tk.Button(
            control_frame, text="⏹ RESET",
            command=self.reset_timer,
            font=("Segoe UI", 12, "bold"), bg="#64748b", fg="white",
            activebackground="#475569", relief="flat", cursor="hand2",
            pady=12
        )
        self.reset_btn.pack(side="left", fill="x", expand=True, padx=2)

        # Skip Button
        self.skip_btn = tk.Button(
            card, text="⏭ SKIP TO NEXT",
            command=self.skip_to_next,
            font=("Segoe UI", 10, "bold"), bg="#334155", fg="white",
            activebackground="#475569", relief="flat", cursor="hand2",
            pady=8
        )
        self.skip_btn.pack(padx=30, pady=(0, 15), fill="x")
        self.add_hover_effect(self.skip_btn, "#334155", "#475569")

        # Session Stats
        stats_box = tk.Frame(
            card, bg="#111827",
            highlightbackground="#334155", highlightthickness=1
        )
        stats_box.pack(padx=30, pady=(0, 15), fill="x")

        tk.Label(
            stats_box, text="📊 SESSION STATISTICS",
            font=("Segoe UI", 10, "bold"), bg="#111827", fg="#94a3b8"
        ).pack(pady=(10, 5))

        stats_grid = tk.Frame(stats_box, bg="#111827")
        stats_grid.pack(fill="x", padx=20, pady=(0, 10))

        # Current Cycle
        cycle_frame = tk.Frame(stats_grid, bg="#111827")
        cycle_frame.pack(side="left", fill="x", expand=True, padx=5)

        tk.Label(
            cycle_frame, text="Current Cycle",
            font=("Segoe UI", 9, "bold"), bg="#111827", fg="#64748b"
        ).pack()

        self.cycle_label = tk.Label(
            cycle_frame, text="0 / 4",
            font=("Segoe UI", 18, "bold"), bg="#111827", fg="#38bdf8"
        )
        self.cycle_label.pack()

        # Total Sessions
        total_frame = tk.Frame(stats_grid, bg="#111827")
        total_frame.pack(side="left", fill="x", expand=True, padx=5)

        tk.Label(
            total_frame, text="Total Sessions",
            font=("Segoe UI", 9, "bold"), bg="#111827", fg="#64748b"
        ).pack()

        self.total_label = tk.Label(
            total_frame, text="0",
            font=("Segoe UI", 18, "bold"), bg="#111827", fg="#22c55e"
        )
        self.total_label.pack()

        # Total Time
        time_frame = tk.Frame(stats_grid, bg="#111827")
        time_frame.pack(side="left", fill="x", expand=True, padx=5)

        tk.Label(
            time_frame, text="Focus Time",
            font=("Segoe UI", 9, "bold"), bg="#111827", fg="#64748b"
        ).pack()

        self.focus_time_label = tk.Label(
            time_frame, text="0 min",
            font=("Segoe UI", 18, "bold"), bg="#111827", fg="#f472b6"
        )
        self.focus_time_label.pack()

        # Bottom Buttons
        buttons = tk.Frame(card, bg="#1e293b")
        buttons.pack(padx=30, pady=(0, 18), fill="x")

        settings_btn = tk.Button(
            buttons, text="⚙ SETTINGS",
            command=self.open_settings,
            font=("Segoe UI", 10, "bold"), bg="#334155", fg="white",
            activebackground="#475569", relief="flat", cursor="hand2", padx=20, pady=8
        )
        settings_btn.pack(side="left")
        self.add_hover_effect(settings_btn, "#334155", "#475569")

        exit_btn = tk.Button(
            buttons, text="✕ EXIT",
            command=self.root.destroy,
            font=("Segoe UI", 10, "bold"), bg="#991b1b", fg="white",
            activebackground="#b91c1c", relief="flat", cursor="hand2", padx=20, pady=8
        )
        exit_btn.pack(side="right")
        self.add_hover_effect(exit_btn, "#991b1b", "#b91c1c")

        # Footer
        tk.Label(
            self.root, text="🍅 Pomodoro Technique • Stay productive!",
            font=("Segoe UI", 9), bg="#0f172a", fg="#64748b"
        ).pack(pady=8)

    # ---------------- MODE SWITCHING ----------------

    def switch_mode(self, mode):
        if self.is_running:
            if not messagebox.askyesno(
                "Switch Mode",
                "Timer is running. Switch mode anyway?"
            ):
                return

        self.stop_timer()

        self.current_mode = mode

        if mode == "work":
            self.time_left = self.work_time * 60
            self.total_time = self.work_time * 60
            self.mode_label.config(text="🎯 WORK SESSION", fg="#ef4444")
            self.timer_display.config(fg="#ef4444")
            self.work_btn.config(bg="#ef4444")
            self.short_break_btn.config(bg="#334155")
            self.long_break_btn.config(bg="#334155")
            timer_box = self.timer_display.master
            timer_box.config(highlightbackground="#ef4444")
            self.progress_bar.configure(style="Progress.Horizontal.TProgressbar")

        elif mode == "short_break":
            self.time_left = self.short_break * 60
            self.total_time = self.short_break * 60
            self.mode_label.config(text="☕ SHORT BREAK", fg="#22c55e")
            self.timer_display.config(fg="#22c55e")
            self.work_btn.config(bg="#334155")
            self.short_break_btn.config(bg="#22c55e")
            self.long_break_btn.config(bg="#334155")
            timer_box = self.timer_display.master
            timer_box.config(highlightbackground="#22c55e")
            self.progress_bar.configure(style="Green.Horizontal.TProgressbar")

        elif mode == "long_break":
            self.time_left = self.long_break * 60
            self.total_time = self.long_break * 60
            self.mode_label.config(text="🌴 LONG BREAK", fg="#38bdf8")
            self.timer_display.config(fg="#38bdf8")
            self.work_btn.config(bg="#334155")
            self.short_break_btn.config(bg="#334155")
            self.long_break_btn.config(bg="#38bdf8")
            timer_box = self.timer_display.master
            timer_box.config(highlightbackground="#38bdf8")
            self.progress_bar.configure(style="Blue.Horizontal.TProgressbar")

        self.update_display()

    # ---------------- TIMER CONTROL ----------------

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.is_paused = False
            self.start_btn.config(state="disabled")
            self.pause_btn.config(state="normal")
            self.timer_thread = threading.Thread(target=self.run_timer, daemon=True)
            self.timer_thread.start()

    def pause_timer(self):
        if self.is_running:
            self.is_running = False
            self.is_paused = True
            self.start_btn.config(state="normal", text="▶ RESUME")
            self.pause_btn.config(state="disabled")

    def stop_timer(self):
        self.is_running = False
        self.is_paused = False
        self.start_btn.config(state="normal", text="▶ START")
        self.pause_btn.config(state="disabled")

    def reset_timer(self):
        self.stop_timer()
        self.switch_mode(self.current_mode)

    def skip_to_next(self):
        if self.is_running:
            self.stop_timer()

        if self.current_mode == "work":
            self.session_count += 1
            self.total_sessions += 1
            self.update_stats()

            if self.session_count >= self.sessions_before_long:
                self.session_count = 0
                self.switch_mode("long_break")
            else:
                self.switch_mode("short_break")
        else:
            self.switch_mode("work")

    # ---------------- TIMER LOOP ----------------

    def run_timer(self):
        while self.is_running and self.time_left > 0:
            time.sleep(1)
            if self.is_running:
                self.time_left -= 1
                self.root.after(0, self.update_display)

        if self.time_left <= 0 and self.is_running:
            self.root.after(0, self.timer_complete)

    def timer_complete(self):
        self.stop_timer()
        self.play_sound()

        if self.current_mode == "work":
            self.session_count += 1
            self.total_sessions += 1
            self.update_stats()

            if self.session_count >= self.sessions_before_long:
                self.session_count = 0
                messagebox.showinfo(
                    "Great Work! 🎉",
                    f"You completed {self.sessions_before_long} sessions!\n\nTime for a LONG BREAK (15 min)"
                )
                self.switch_mode("long_break")
            else:
                messagebox.showinfo(
                    "Session Complete! ✅",
                    f"Session {self.session_count}/{self.sessions_before_long} done!\n\nTime for a SHORT BREAK (5 min)"
                )
                self.switch_mode("short_break")
        else:
            messagebox.showinfo(
                "Break Over! ☕",
                "Break is over!\n\nReady to focus again?"
            )
            self.switch_mode("work")

        self.start_timer()

    # ---------------- DISPLAY UPDATE ----------------

    def update_display(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_display.config(text=f"{minutes:02d}:{seconds:02d}")

        # Update progress bar
        if self.total_time > 0:
            progress = (self.time_left / self.total_time) * 100
            self.progress_var.set(progress)

    def update_stats(self):
        self.cycle_label.config(text=f"{self.session_count} / {self.sessions_before_long}")
        self.total_label.config(text=str(self.total_sessions))
        focus_minutes = self.total_sessions * self.work_time
        if focus_minutes >= 60:
            hours = focus_minutes // 60
            mins = focus_minutes % 60
            self.focus_time_label.config(text=f"{hours}h {mins}m")
        else:
            self.focus_time_label.config(text=f"{focus_minutes} min")

    # ---------------- SOUND ----------------

    def play_sound(self):
        try:
            # Try winsound for Windows
            import winsound
            for _ in range(3):
                winsound.Beep(1000, 500)
                time.sleep(0.2)
        except ImportError:
            # Fallback for other platforms
            self.root.bell()

    # ---------------- SETTINGS ----------------

    def open_settings(self):
        if self.is_running:
            messagebox.showwarning(
                "Timer Running",
                "Please stop the timer before changing settings."
            )
            return

        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("400x350")
        settings_window.configure(bg="#0f172a")
        settings_window.resizable(False, False)

        tk.Label(
            settings_window, text="⚙ TIMER SETTINGS",
            font=("Segoe UI", 16, "bold"), bg="#0f172a", fg="#38bdf8"
        ).pack(pady=20)

        # Work Time
        tk.Label(
            settings_window, text="Work Duration (minutes):",
            font=("Segoe UI", 11), bg="#0f172a", fg="#cbd5e1"
        ).pack(pady=(10, 5))

        work_entry = tk.Entry(
            settings_window, font=("Segoe UI", 14),
            bg="#111827", fg="white", insertbackground="white",
            relief="flat", justify="center"
        )
        work_entry.pack(ipady=8, ipadx=20)
        work_entry.insert(0, str(self.work_time))

        # Short Break
        tk.Label(
            settings_window, text="Short Break (minutes):",
            font=("Segoe UI", 11), bg="#0f172a", fg="#cbd5e1"
        ).pack(pady=(10, 5))

        short_entry = tk.Entry(
            settings_window, font=("Segoe UI", 14),
            bg="#111827", fg="white", insertbackground="white",
            relief="flat", justify="center"
        )
        short_entry.pack(ipady=8, ipadx=20)
        short_entry.insert(0, str(self.short_break))

        # Long Break
        tk.Label(
            settings_window, text="Long Break (minutes):",
            font=("Segoe UI", 11), bg="#0f172a", fg="#cbd5e1"
        ).pack(pady=(10, 5))

        long_entry = tk.Entry(
            settings_window, font=("Segoe UI", 14),
            bg="#111827", fg="white", insertbackground="white",
            relief="flat", justify="center"
        )
        long_entry.pack(ipady=8, ipadx=20)
        long_entry.insert(0, str(self.long_break))

        # Save Button
        def save_settings():
            try:
                self.work_time = int(work_entry.get())
                self.short_break = int(short_entry.get())
                self.long_break = int(long_entry.get())

                if self.work_time < 1 or self.short_break < 1 or self.long_break < 1:
                    raise ValueError

                self.work_btn.config(text=f"🎯 WORK\n{self.work_time} min")
                self.short_break_btn.config(text=f"☕ SHORT BREAK\n{self.short_break} min")
                self.long_break_btn.config(text=f"🌴 LONG BREAK\n{self.long_break} min")

                self.switch_mode(self.current_mode)
                settings_window.destroy()

            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter valid positive numbers."
                )

        save_btn = tk.Button(
            settings_window, text="💾 SAVE SETTINGS",
            command=save_settings,
            font=("Segoe UI", 11, "bold"), bg="#22c55e", fg="white",
            activebackground="#16a34a", relief="flat", cursor="hand2",
            pady=10
        )
        save_btn.pack(pady=20, padx=30, fill="x")

    # ---------------- HOVER EFFECT ----------------

    def add_hover_effect(self, widget, normal_color, hover_color):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
        widget.bind("<Leave>", lambda e: widget.config(bg=normal_color))


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()