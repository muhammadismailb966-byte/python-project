import tkinter as tk
from tkinter import ttk


# Offline fixed exchange rates (1 USD = ...)
RATES = {
    "USD": 1.00,
    "PKR": 280.00,
    "EUR": 0.92,
    "GBP": 0.78,
    "AED": 3.67,
    "SAR": 3.75,
    "INR": 83.00,
    "CAD": 1.36,
    "AUD": 1.52,
    "JPY": 149.00
}


class CurrencyConverter:

    def __init__(self, root):
        self.root = root

        self.root.title("Currency Converter")
        self.root.geometry("620x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")

        self.setup_style()
        self.create_gui()
        
        # ⭐ IMPORTANT: Delay initial conversion until GUI is fully ready
        self.root.after(200, self.initial_convert)

    # ---------------- STYLE ----------------

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            font=("Segoe UI", 12, "bold"),
            padding=10,
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
            foreground=[("readonly", "white")],
            bordercolor=[("focus", "#38bdf8")]
        )

    # ---------------- GUI ----------------

    def create_gui(self):
        # Header
        tk.Label(
            self.root, text="💱", font=("Segoe UI Emoji", 36),
            bg="#0f172a", fg="white"
        ).pack(pady=(20, 0))

        tk.Label(
            self.root, text="CURRENCY CONVERTER",
            font=("Segoe UI", 22, "bold"), bg="#0f172a", fg="#38bdf8"
        ).pack()

        tk.Label(
            self.root, text="Offline Currency Conversion",
            font=("Segoe UI", 10), bg="#0f172a", fg="#94a3b8"
        ).pack(pady=(3, 12))

        # Main Card
        card = tk.Frame(
            self.root, bg="#1e293b",
            highlightbackground="#334155", highlightthickness=1
        )
        card.pack(padx=40, fill="both", expand=True)

        # Amount
        tk.Label(
            card, text="Amount", font=("Segoe UI", 11, "bold"),
            bg="#1e293b", fg="#cbd5e1"
        ).pack(anchor="w", padx=30, pady=(20, 5))

        self.amount = tk.Entry(
            card, font=("Segoe UI", 16, "bold"), bg="#111827", fg="white",
            insertbackground="white", relief="flat",
            highlightthickness=2, highlightbackground="#334155", 
            highlightcolor="#38bdf8"
        )
        self.amount.pack(padx=30, fill="x", ipady=12)
        self.amount.insert(0, "1")
        
        # Bindings
        self.amount.bind("<KeyRelease>", self.on_amount_change)
        self.amount.bind("<Return>", lambda e: self.convert())

        # Currency Row
        currency_row = tk.Frame(card, bg="#1e293b")
        currency_row.pack(padx=30, pady=18, fill="x")

        # From
        from_box = tk.Frame(currency_row, bg="#1e293b")
        from_box.pack(side="left", fill="x", expand=True)

        tk.Label(
            from_box, text="From Currency", font=("Segoe UI", 10, "bold"),
            bg="#1e293b", fg="#cbd5e1"
        ).pack(anchor="w", pady=(0, 5))

        self.from_currency = ttk.Combobox(
            from_box, values=list(RATES.keys()), state="readonly",
            font=("Segoe UI", 12, "bold")
        )
        self.from_currency.pack(fill="x")
        self.from_currency.set("USD")
        self.from_currency.bind("<<ComboboxSelected>>", lambda e: self.convert())

        # Swap Button
        swap_btn = tk.Button(
            currency_row, text="⇄", command=self.swap_currency,
            font=("Segoe UI", 20, "bold"), bg="#334155", fg="#38bdf8",
            activebackground="#475569", activeforeground="white",
            relief="flat", cursor="hand2", width=3
        )
        swap_btn.pack(side="left", padx=10, pady=25)
        self.add_hover_effect(swap_btn, "#334155", "#475569")

        # To
        to_box = tk.Frame(currency_row, bg="#1e293b")
        to_box.pack(side="left", fill="x", expand=True)

        tk.Label(
            to_box, text="To Currency", font=("Segoe UI", 10, "bold"),
            bg="#1e293b", fg="#cbd5e1"
        ).pack(anchor="w", pady=(0, 5))

        self.to_currency = ttk.Combobox(
            to_box, values=list(RATES.keys()), state="readonly",
            font=("Segoe UI", 12, "bold")
        )
        self.to_currency.pack(fill="x")
        self.to_currency.set("PKR")
        self.to_currency.bind("<<ComboboxSelected>>", lambda e: self.convert())

        # Convert Button
        convert_btn = tk.Button(
            card, text="🔄 CONVERT NOW", command=self.convert,
            font=("Segoe UI", 12, "bold"), bg="#0284c7", fg="white",
            activebackground="#0369a1", activeforeground="white",
            relief="flat", cursor="hand2", pady=12
        )
        convert_btn.pack(padx=30, fill="x")
        self.add_hover_effect(convert_btn, "#0284c7", "#0369a1")

        # ⭐ RESULT BOX - Bigger and more visible
        result_box = tk.Frame(
            card, bg="#0c1220",
            highlightbackground="#38bdf8", highlightthickness=2
        )
        result_box.pack(padx=30, pady=18, fill="x")

        tk.Label(
            result_box, text="▼ CONVERTED AMOUNT ▼",
            font=("Segoe UI", 10, "bold"), bg="#0c1220", fg="#38bdf8"
        ).pack(pady=(12, 5))

        # ⭐ Main result label - VERY BIG and BOLD
        self.result = tk.Label(
            result_box, text="0.00",
            font=("Segoe UI", 36, "bold"), bg="#0c1220", fg="#22d3ee"
        )
        self.result.pack(pady=(0, 2))
        
        # Currency name below the amount
        self.result_currency = tk.Label(
            result_box, text="PKR",
            font=("Segoe UI", 14, "bold"), bg="#0c1220", fg="#94a3b8"
        )
        self.result_currency.pack(pady=(0, 10))

        # ⭐ Status indicator - shows when last conversion happened
        self.status = tk.Label(
            result_box, text="● Ready",
            font=("Segoe UI", 9), bg="#0c1220", fg="#22c55e"
        )
        self.status.pack(pady=(0, 8))

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
            self.root, text="Fixed offline rates • No internet required",
            font=("Segoe UI", 9), bg="#0f172a", fg="#64748b"
        ).pack(pady=8)

    # ---------------- INITIAL CONVERT (Delayed) ----------------
    
    def initial_convert(self):
        """Call convert after GUI is fully loaded"""
        try:
            self.convert()
        except Exception as e:
            print(f"Initial convert error: {e}")
            # Force set a default result
            self.result.config(text="280.00", fg="#22d3ee")
            self.result_currency.config(text="PKR")

    # ---------------- AMOUNT CHANGE HANDLER ----------------
    
    def on_amount_change(self, event=None):
        """Only allow numbers and dots in amount field"""
        current = self.amount.get()
        # Filter out non-numeric characters (except dot and minus)
        filtered = "".join(c for c in current if c.isdigit() or c == '.' or c == '-')
        if filtered != current:
            self.amount.delete(0, tk.END)
            self.amount.insert(0, filtered)
        self.convert()

    # ---------------- CONVERT ----------------

    def convert(self, event=None):
        try:
            amount_str = self.amount.get().strip()
            
            # Handle empty input
            if not amount_str or amount_str == '.' or amount_str == '-':
                self.result.config(text="0.00", fg="#f59e0b")
                self.result_currency.config(text="Enter amount...")
                self.status.config(text="● Waiting for input", fg="#f59e0b")
                return

            amount = float(amount_str)
            
            if amount < 0:
                self.result.config(text="Error", fg="#ef4444")
                self.result_currency.config(text="Negative not allowed")
                self.status.config(text="● Invalid input", fg="#ef4444")
                return

            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()

            # ⭐ Safety check - make sure currencies are valid
            if from_currency not in RATES or to_currency not in RATES:
                self.result.config(text="Error", fg="#ef4444")
                self.result_currency.config(text="Invalid currency")
                self.status.config(text="● Select currencies", fg="#ef4444")
                return

            # Convert to USD first, then to target currency
            usd_amount = amount / RATES[from_currency]
            converted = usd_amount * RATES[to_currency]

            # ⭐ Format with commas for readability
            formatted = f"{converted:,.2f}"

            # Update result - BIG and VISIBLE
            self.result.config(text=formatted, fg="#22d3ee")
            self.result_currency.config(text=to_currency, fg="#94a3b8")
            self.status.config(text="● Converted successfully", fg="#22c55e")

        except ValueError:
            self.result.config(text="Error", fg="#ef4444")
            self.result_currency.config(text="Invalid number")
            self.status.config(text="● Invalid input", fg="#ef4444")
            
        except KeyError as e:
            self.result.config(text="Error", fg="#ef4444")
            self.result_currency.config(text=f"Missing: {e}")
            self.status.config(text="● Key error", fg="#ef4444")
            
        except Exception as e:
            self.result.config(text="Error", fg="#ef4444")
            self.result_currency.config(text=str(e)[:30])
            self.status.config(text="● Unexpected error", fg="#ef4444")

    # ---------------- SWAP ----------------

    def swap_currency(self):
        from_value = self.from_currency.get()
        to_value = self.to_currency.get()

        self.from_currency.set(to_value)
        self.to_currency.set(from_value)
        self.convert()

    # ---------------- CLEAR ----------------

    def clear(self):
        self.amount.delete(0, tk.END)
        self.amount.insert(0, "1")
        self.from_currency.set("USD")
        self.to_currency.set("PKR")
        self.convert()

    # ---------------- HOVER EFFECT ----------------
    
    def add_hover_effect(self, widget, normal_color, hover_color):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
        widget.bind("<Leave>", lambda e: widget.config(bg=normal_color))


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()