import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
import calendar


class AgeCalculator:

    def __init__(self, root):
        self.root = root

        self.root.title("Age Calculator")
        self.root.geometry("900x850")
        self.root.resizable(True, True)
        self.root.minsize(800, 750)
        self.root.configure(bg="#0f172a")
        
        self.setup_style()
        self.create_gui()

    # ---------------- STYLE ----------------

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            font=("Segoe UI", 12, "bold"),
            padding=8,
            fieldbackground="#111827",
            background="#111827",
            foreground="white",
            selectbackground="#0284c7",
            selectforeground="white",
            arrowcolor="#38bdf8"
        )

        style.map(
            "TCombobox",
            fieldbackground=[("readonly", "#111827")],
            foreground=[("readonly", "white")]
        )

    # ---------------- GUI ----------------

    def create_gui(self):
        # Header
        tk.Label(
            self.root, text="🎂", font=("Segoe UI Emoji", 40),
            bg="#0f172a", fg="white"
        ).pack(pady=(20, 0))

        tk.Label(
            self.root, text="AGE CALCULATOR",
            font=("Segoe UI", 22, "bold"), bg="#0f172a", fg="#f472b6"
        ).pack()

        tk.Label(
            self.root, text="Find your exact age in years, months, days & more",
            font=("Segoe UI", 10), bg="#0f172a", fg="#94a3b8"
        ).pack(pady=(3, 12))

        # Main Card
        card = tk.Frame(
            self.root, bg="#1e293b",
            highlightbackground="#334155", highlightthickness=1
        )
        card.pack(padx=40, fill="both", expand=True)

        # Date of Birth Section
        tk.Label(
            card, text="📅 Date of Birth", font=("Segoe UI", 12, "bold"),
            bg="#1e293b", fg="#cbd5e1"
        ).pack(anchor="w", padx=30, pady=(20, 10))

        # Date Row (Day, Month, Year)
        date_row = tk.Frame(card, bg="#1e293b")
        date_row.pack(padx=30, fill="x")

        # Day
        day_frame = tk.Frame(date_row, bg="#1e293b")
        day_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))

        tk.Label(
            day_frame, text="Day", font=("Segoe UI", 9, "bold"),
            bg="#1e293b", fg="#94a3b8"
        ).pack(anchor="w", pady=(0, 3))

        self.day_combo = ttk.Combobox(
            day_frame, values=[str(i) for i in range(1, 32)],
            state="readonly", font=("Segoe UI", 11, "bold")
        )
        self.day_combo.pack(fill="x")
        self.day_combo.set("1")

        # Month
        month_frame = tk.Frame(date_row, bg="#1e293b")
        month_frame.pack(side="left", fill="x", expand=True, padx=5)

        tk.Label(
            month_frame, text="Month", font=("Segoe UI", 9, "bold"),
            bg="#1e293b", fg="#94a3b8"
        ).pack(anchor="w", pady=(0, 3))

        months = [
            "01 - January", "02 - February", "03 - March", "04 - April",
            "05 - May", "06 - June", "07 - July", "08 - August",
            "09 - September", "10 - October", "11 - November", "12 - December"
        ]
        self.month_combo = ttk.Combobox(
            month_frame, values=months,
            state="readonly", font=("Segoe UI", 11, "bold")
        )
        self.month_combo.pack(fill="x")
        self.month_combo.set("01 - January")

        # Year
        year_frame = tk.Frame(date_row, bg="#1e293b")
        year_frame.pack(side="left", fill="x", expand=True, padx=(5, 0))

        tk.Label(
            year_frame, text="Year", font=("Segoe UI", 9, "bold"),
            bg="#1e293b", fg="#94a3b8"
        ).pack(anchor="w", pady=(0, 3))

        current_year = datetime.now().year
        years = [str(i) for i in range(current_year, 1900, -1)]
        self.year_combo = ttk.Combobox(
            year_frame, values=years,
            state="readonly", font=("Segoe UI", 11, "bold")
        )
        self.year_combo.pack(fill="x")
        self.year_combo.set("2000")

        # Calculate Button
        calc_btn = tk.Button(
            card, text="🎯 CALCULATE MY AGE", command=self.calculate_age,
            font=("Segoe UI", 12, "bold"), bg="#db2777", fg="white",
            activebackground="#be185d", activeforeground="white",
            relief="flat", cursor="hand2", pady=12
        )
        calc_btn.pack(padx=30, pady=20, fill="x")
        self.add_hover_effect(calc_btn, "#db2777", "#be185d")

        # Result Box
        result_box = tk.Frame(
            card, bg="#0c1220",
            highlightbackground="#f472b6", highlightthickness=2
        )
        result_box.pack(padx=30, pady=(0, 15), fill="x")

        tk.Label(
            result_box, text="▼ YOUR AGE ▼",
            font=("Segoe UI", 10, "bold"), bg="#0c1220", fg="#f472b6"
        ).pack(pady=(12, 5))

        # Main Age Display
        self.age_main = tk.Label(
            result_box, text="-- Years, -- Months, -- Days",
            font=("Segoe UI", 18, "bold"), bg="#0c1220", fg="#22d3ee"
        )
        self.age_main.pack(pady=(0, 10))

        # Detailed Stats Grid
        stats_grid = tk.Frame(result_box, bg="#0c1220")
        stats_grid.pack(fill="x", padx=20, pady=(0, 12))

        # Row 1
        row1 = tk.Frame(stats_grid, bg="#0c1220")
        row1.pack(fill="x", pady=3)

        self.stat_months = self.create_stat_box(row1, "Total Months", "--", "#a78bfa")
        self.stat_days = self.create_stat_box(row1, "Total Days", "--", "#34d399")

        # Row 2
        row2 = tk.Frame(stats_grid, bg="#0c1220")
        row2.pack(fill="x", pady=3)

        self.stat_hours = self.create_stat_box(row2, "Total Hours", "--", "#fbbf24")
        self.stat_minutes = self.create_stat_box(row2, "Total Minutes", "--", "#fb923c")

        # Row 3
        row3 = tk.Frame(stats_grid, bg="#0c1220")
        row3.pack(fill="x", pady=3)

        self.stat_seconds = self.create_stat_box(row3, "Total Seconds", "--", "#f87171")
        self.stat_weeks = self.create_stat_box(row3, "Total Weeks", "--", "#60a5fa")

        # Extra Info Section
        info_box = tk.Frame(card, bg="#1e293b")
        info_box.pack(padx=30, pady=(0, 15), fill="x")

        # Born on day
        self.born_day = tk.Label(
            info_box, text="🗓 Born on: ---",
            font=("Segoe UI", 11), bg="#1e293b", fg="#cbd5e1",
            anchor="w"
        )
        self.born_day.pack(fill="x", pady=2)

        # Next Birthday
        self.next_birthday = tk.Label(
            info_box, text="🎉 Next Birthday: ---",
            font=("Segoe UI", 11), bg="#1e293b", fg="#fbbf24",
            anchor="w"
        )
        self.next_birthday.pack(fill="x", pady=2)

        # Zodiac Sign
        self.zodiac = tk.Label(
            info_box, text="⭐ Zodiac Sign: ---",
            font=("Segoe UI", 11), bg="#1e293b", fg="#a78bfa",
            anchor="w"
        )
        self.zodiac.pack(fill="x", pady=2)

        # Bottom Buttons
        buttons = tk.Frame(card, bg="#1e293b")
        buttons.pack(padx=30, pady=(0, 18), fill="x")

        clear_btn = tk.Button(
            buttons, text="🗑 CLEAR", command=self.clear,
            font=("Segoe UI", 10, "bold"), bg="#334155", fg="white",
            activebackground="#475569", relief="flat", cursor="hand2", padx=20, pady=8
        )
        clear_btn.pack(side="left")
        self.add_hover_effect(clear_btn, "#334155", "#475569")

        exit_btn = tk.Button(
            buttons, text="✕ EXIT", command=self.root.destroy,
            font=("Segoe UI", 10, "bold"), bg="#991b1b", fg="white",
            activebackground="#b91c1c", relief="flat", cursor="hand2", padx=20, pady=8
        )
        exit_btn.pack(side="right")
        self.add_hover_effect(exit_btn, "#991b1b", "#b91c1c")

        # Footer
        tk.Label(
            self.root, text="Made with ❤️ • Calculate your age precisely",
            font=("Segoe UI", 9), bg="#0f172a", fg="#64748b"
        ).pack(pady=8)

    # ---------------- HELPER: Create Stat Box ----------------

    def create_stat_box(self, parent, label, value, color):
        box = tk.Frame(parent, bg="#111827", highlightbackground=color, highlightthickness=1)
        box.pack(side="left", fill="x", expand=True, padx=3)

        tk.Label(
            box, text=label, font=("Segoe UI", 8, "bold"),
            bg="#111827", fg="#94a3b8"
        ).pack(pady=(6, 2))

        value_label = tk.Label(
            box, text=value, font=("Segoe UI", 13, "bold"),
            bg="#111827", fg=color
        )
        value_label.pack(pady=(0, 6))

        return value_label

    # ---------------- CALCULATE AGE ----------------

    def calculate_age(self):
        try:
            # Get selected values
            day = int(self.day_combo.get())
            month_str = self.month_combo.get()
            month = int(month_str.split(" - ")[0])
            year = int(self.year_combo.get())

            # Validate date
            try:
                birth_date = date(year, month, day)
            except ValueError:
                messagebox.showerror(
                    "Invalid Date",
                    f"{day}/{month}/{year} ایک درست تاریخ نہیں ہے!\n\nبراہ کرم صحیح تاریخ منتخب کریں۔"
                )
                return

            # Today's date
            today = date.today()

            # Check if birth date is in future
            if birth_date > today:
                messagebox.showerror(
                    "Future Date",
                    "تاریخ پیدائش آج کی تاریخ سے بعد میں نہیں ہو سکتی!"
                )
                return

            # Calculate exact age
            years = today.year - birth_date.year
            months = today.month - birth_date.month
            days = today.day - birth_date.day

            if days < 0:
                months -= 1
                # Get days in previous month
                prev_month = today.month - 1 if today.month > 1 else 12
                prev_year = today.year if today.month > 1 else today.year - 1
                days_in_month = calendar.monthrange(prev_year, prev_month)[1]
                days += days_in_month

            if months < 0:
                years -= 1
                months += 12

            # Update main age display
            self.age_main.config(
                text=f"{years} Years, {months} Months, {days} Days"
            )

            # Calculate total stats
            delta = today - birth_date
            total_days = delta.days
            total_weeks = total_days // 7
            total_months = years * 12 + months
            total_hours = total_days * 24
            total_minutes = total_hours * 60
            total_seconds = total_minutes * 60

            # Update stat boxes
            self.stat_months.config(text=f"{total_months:,}")
            self.stat_days.config(text=f"{total_days:,}")
            self.stat_hours.config(text=f"{total_hours:,}")
            self.stat_minutes.config(text=f"{total_minutes:,}")
            self.stat_seconds.config(text=f"{total_seconds:,}")
            self.stat_weeks.config(text=f"{total_weeks:,}")

            # Born on which day
            day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                        "Friday", "Saturday", "Sunday"]
            born_day_name = day_names[birth_date.weekday()]
            self.born_day.config(
                text=f"🗓 Born on: {born_day_name}, {birth_date.strftime('%d %B %Y')}"
            )

            # Next Birthday calculation
            next_bday = date(today.year, birth_date.month, birth_date.day)
            if next_bday < today:
                next_bday = date(today.year + 1, birth_date.month, birth_date.day)

            days_until_bday = (next_bday - today).days

            if days_until_bday == 0:
                self.next_birthday.config(
                    text="🎉 آج آپ کی سالگرہ ہے! مبارک ہو! 🎂",
                    fg="#22c55e"
                )
            else:
                self.next_birthday.config(
                    text=f"🎉 Next Birthday: {days_until_bday} days remaining ({next_bday.strftime('%d %B %Y')})",
                    fg="#fbbf24"
                )

            # Zodiac Sign
            zodiac_sign = self.get_zodiac_sign(month, day)
            self.zodiac.config(text=f"⭐ Zodiac Sign: {zodiac_sign}")

        except Exception as e:
            messagebox.showerror("Error", f"کیلکولیشن میں مسئلہ: {str(e)}")

    # ---------------- ZODIAC SIGN ----------------

    def get_zodiac_sign(self, month, day):
        zodiac_dates = [
            ((1, 20), "Capricorn ♑"),
            ((2, 19), "Aquarius ♒"),
            ((3, 20), "Pisces ♓"),
            ((4, 20), "Aries ♈"),
            ((5, 21), "Taurus ♉"),
            ((6, 21), "Gemini ♊"),
            ((7, 22), "Cancer ♋"),
            ((8, 23), "Leo ♌"),
            ((9, 23), "Virgo ♍"),
            ((10, 23), "Libra ♎"),
            ((11, 22), "Scorpio ♏"),
            ((12, 22), "Sagittarius ♐"),
            ((12, 31), "Capricorn ♑")
        ]

        for end_date, sign in zodiac_dates:
            if (month, day) <= end_date:
                return sign
        return "Capricorn ♑"

    # ---------------- CLEAR ----------------

    def clear(self):
        self.day_combo.set("1")
        self.month_combo.set("01 - January")
        self.year_combo.set("2000")

        self.age_main.config(text="-- Years, -- Months, -- Days")
        self.stat_months.config(text="--")
        self.stat_days.config(text="--")
        self.stat_hours.config(text="--")
        self.stat_minutes.config(text="--")
        self.stat_seconds.config(text="--")
        self.stat_weeks.config(text="--")

        self.born_day.config(text="🗓 Born on: ---")
        self.next_birthday.config(text="🎉 Next Birthday: ---", fg="#fbbf24")
        self.zodiac.config(text="⭐ Zodiac Sign: ---")

    # ---------------- HOVER EFFECT ----------------

    def add_hover_effect(self, widget, normal_color, hover_color):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
        widget.bind("<Leave>", lambda e: widget.config(bg=normal_color))


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculator(root)
    root.mainloop()