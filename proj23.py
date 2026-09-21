import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import os


class AdvancedNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Notepad - Untitled")
        self.root.geometry("1000x700")
        self.root.minsize(750, 550)
        self.root.configure(bg="#0f172a")

        self.current_file = None
        self.modified = False
        self.dark_mode = True

        self.bg = "#0f172a"
        self.card = "#1e293b"
        self.editor_bg = "#111827"
        self.text_color = "#f8fafc"
        self.muted = "#94a3b8"
        self.accent = "#38bdf8"
        self.border = "#334155"

        self.create_menu()
        self.create_toolbar()
        self.create_editor()
        self.create_statusbar()

        self.bind_shortcuts()
        self.update_status()

    # =========================================================
    # MENU
    # =========================================================

    def create_menu(self):
        menu_bar = tk.Menu(
            self.root,
            bg=self.card,
            fg=self.text_color,
            activebackground=self.accent,
            activeforeground="#0f172a"
        )

        # File
        file_menu = tk.Menu(
            menu_bar,
            tearoff=0,
            bg=self.card,
            fg=self.text_color
        )

        file_menu.add_command(
            label="New",
            accelerator="Ctrl+N",
            command=self.new_file
        )
        file_menu.add_command(
            label="Open",
            accelerator="Ctrl+O",
            command=self.open_file
        )
        file_menu.add_command(
            label="Save",
            accelerator="Ctrl+S",
            command=self.save_file
        )
        file_menu.add_command(
            label="Save As",
            accelerator="Ctrl+Shift+S",
            command=self.save_as
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit",
            command=self.exit_app
        )

        menu_bar.add_cascade(
            label="File",
            menu=file_menu
        )

        # Edit
        edit_menu = tk.Menu(
            menu_bar,
            tearoff=0,
            bg=self.card,
            fg=self.text_color
        )

        edit_menu.add_command(
            label="Undo",
            accelerator="Ctrl+Z",
            command=self.undo
        )
        edit_menu.add_command(
            label="Redo",
            accelerator="Ctrl+Y",
            command=self.redo
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Cut",
            accelerator="Ctrl+X",
            command=self.cut
        )
        edit_menu.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            command=self.copy
        )
        edit_menu.add_command(
            label="Paste",
            accelerator="Ctrl+V",
            command=self.paste
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Select All",
            accelerator="Ctrl+A",
            command=self.select_all
        )

        menu_bar.add_cascade(
            label="Edit",
            menu=edit_menu
        )

        # Search
        search_menu = tk.Menu(
            menu_bar,
            tearoff=0,
            bg=self.card,
            fg=self.text_color
        )

        search_menu.add_command(
            label="Find",
            accelerator="Ctrl+F",
            command=self.show_find
        )
        search_menu.add_command(
            label="Replace",
            accelerator="Ctrl+H",
            command=self.show_replace
        )

        menu_bar.add_cascade(
            label="Search",
            menu=search_menu
        )

        # Format
        format_menu = tk.Menu(
            menu_bar,
            tearoff=0,
            bg=self.card,
            fg=self.text_color
        )

        format_menu.add_command(
            label="Increase Font",
            accelerator="Ctrl++",
            command=lambda: self.change_font_size(2)
        )

        format_menu.add_command(
            label="Decrease Font",
            accelerator="Ctrl+-",
            command=lambda: self.change_font_size(-2)
        )

        format_menu.add_command(
            label="Text Color",
            command=self.choose_text_color
        )

        menu_bar.add_cascade(
            label="Format",
            menu=format_menu
        )

        # View
        view_menu = tk.Menu(
            menu_bar,
            tearoff=0,
            bg=self.card,
            fg=self.text_color
        )

        view_menu.add_command(
            label="Toggle Dark Mode",
            command=self.toggle_theme
        )

        menu_bar.add_cascade(
            label="View",
            menu=view_menu
        )

        self.root.config(menu=menu_bar)

    # =========================================================
    # TOOLBAR
    # =========================================================

    def create_toolbar(self):
        self.toolbar = tk.Frame(
            self.root,
            bg=self.card,
            height=55
        )
        self.toolbar.pack(
            fill="x"
        )

        buttons = [
            ("New", self.new_file),
            ("Open", self.open_file),
            ("Save", self.save_file),
            ("Undo", self.undo),
            ("Redo", self.redo),
            ("Find", self.show_find),
            ("Replace", self.show_replace)
        ]

        for text, command in buttons:
            tk.Button(
                self.toolbar,
                text=text,
                command=command,
                font=("Segoe UI", 10, "bold"),
                bg=self.card,
                fg=self.text_color,
                activebackground=self.accent,
                activeforeground="#0f172a",
                relief="flat",
                cursor="hand2",
                padx=12,
                pady=8
            ).pack(
                side="left",
                padx=2,
                pady=7
            )

        # Font size
        tk.Label(
            self.toolbar,
            text="Font:",
            font=("Segoe UI", 10, "bold"),
            bg=self.card,
            fg=self.muted
        ).pack(
            side="left",
            padx=(15, 5)
        )

        self.font_size = tk.IntVar(value=14)

        self.font_spin = tk.Spinbox(
            self.toolbar,
            from_=8,
            to=40,
            textvariable=self.font_size,
            width=4,
            command=self.apply_font,
            bg=self.editor_bg,
            fg=self.text_color,
            buttonbackground=self.border,
            relief="flat"
        )
        self.font_spin.pack(
            side="left",
            padx=5
        )

        tk.Button(
            self.toolbar,
            text="A",
            command=self.choose_text_color,
            font=("Segoe UI", 11, "bold"),
            bg=self.card,
            fg=self.text_color,
            activebackground=self.accent,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=7
        ).pack(
            side="left",
            padx=3
        )

        # Theme button
        tk.Button(
            self.toolbar,
            text="☾ Theme",
            command=self.toggle_theme,
            font=("Segoe UI", 10, "bold"),
            bg=self.card,
            fg=self.text_color,
            activebackground=self.accent,
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=7
        ).pack(
            side="right",
            padx=8
        )

    # =========================================================
    # EDITOR
    # =========================================================

    def create_editor(self):
        editor_frame = tk.Frame(
            self.root,
            bg=self.bg
        )
        editor_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # Line numbers
        self.line_numbers = tk.Text(
            editor_frame,
            width=5,
            padx=8,
            pady=12,
            font=("Consolas", 14),
            bg=self.card,
            fg=self.muted,
            relief="flat",
            state="disabled",
            takefocus=0
        )
        self.line_numbers.pack(
            side="left",
            fill="y"
        )

        # Main text editor
        self.text_area = tk.Text(
            editor_frame,
            undo=True,
            wrap="none",
            font=("Consolas", 14),
            bg=self.editor_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            selectbackground="#2563eb",
            selectforeground="#ffffff",
            relief="flat",
            padx=15,
            pady=12
        )
        self.text_area.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Vertical scrollbar
        scrollbar_y = tk.Scrollbar(
            editor_frame,
            command=self.text_area.yview
        )
        scrollbar_y.pack(
            side="right",
            fill="y"
        )

        self.text_area.config(
            yscrollcommand=self.on_scroll
        )

        # Horizontal scrollbar
        scrollbar_x = tk.Scrollbar(
            self.root,
            orient="horizontal",
            command=self.text_area.xview
        )
        scrollbar_x.pack(
            fill="x",
            padx=15
        )

        self.text_area.config(
            xscrollcommand=scrollbar_x.set
        )

        self.text_area.bind(
            "<<Modified>>",
            self.on_modified
        )

        self.text_area.bind(
            "<KeyRelease>",
            self.update_status
        )

        self.text_area.bind(
            "<ButtonRelease>",
            self.update_status
        )

    # =========================================================
    # STATUS BAR
    # =========================================================

    def create_statusbar(self):
        self.statusbar = tk.Frame(
            self.root,
            bg=self.card,
            height=30
        )
        self.statusbar.pack(
            fill="x"
        )

        self.status_label = tk.Label(
            self.statusbar,
            text="Ready",
            font=("Segoe UI", 9),
            bg=self.card,
            fg=self.muted,
            anchor="w"
        )
        self.status_label.pack(
            side="left",
            padx=12
        )

        self.file_label = tk.Label(
            self.statusbar,
            text="Untitled",
            font=("Segoe UI", 9),
            bg=self.card,
            fg=self.muted
        )
        self.file_label.pack(
            side="right",
            padx=12
        )

    # =========================================================
    # FILE OPERATIONS
    # =========================================================

    def new_file(self):
        if not self.check_unsaved():
            return

        self.text_area.delete(
            "1.0",
            tk.END
        )

        self.current_file = None
        self.modified = False

        self.root.title(
            "Advanced Notepad - Untitled"
        )

        self.file_label.config(
            text="Untitled"
        )

        self.update_line_numbers()
        self.update_status()

    def open_file(self):
        if not self.check_unsaved():
            return

        file_path = filedialog.askopenfilename(
            title="Open File",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("HTML Files", "*.html"),
                ("CSS Files", "*.css"),
                ("JavaScript Files", "*.js"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return

        try:
            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:
                content = file.read()

            self.text_area.delete(
                "1.0",
                tk.END
            )

            self.text_area.insert(
                "1.0",
                content
            )

            self.current_file = file_path
            self.modified = False

            self.root.title(
                f"Advanced Notepad - {os.path.basename(file_path)}"
            )

            self.file_label.config(
                text=os.path.basename(file_path)
            )

            self.text_area.edit_reset()
            self.update_line_numbers()
            self.update_status()

        except Exception as error:
            messagebox.showerror(
                "Open Error",
                f"Could not open file.\n\n{error}"
            )

    def save_file(self):
        if self.current_file is None:
            return self.save_as()

        try:
            content = self.text_area.get(
                "1.0",
                tk.END
            )

            with open(
                self.current_file,
                "w",
                encoding="utf-8"
            ) as file:
                file.write(content)

            self.modified = False

            self.root.title(
                f"Advanced Notepad - "
                f"{os.path.basename(self.current_file)}"
            )

            self.status_label.config(
                text="File saved successfully"
            )

            return True

        except Exception as error:
            messagebox.showerror(
                "Save Error",
                f"Could not save file.\n\n{error}"
            )
            return False

    def save_as(self):
        file_path = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("HTML Files", "*.html"),
                ("CSS Files", "*.css"),
                ("JavaScript Files", "*.js"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return False

        self.current_file = file_path
        return self.save_file()

    # =========================================================
    # UNSAVED CHECK
    # =========================================================

    def check_unsaved(self):
        if not self.modified:
            return True

        answer = messagebox.askyesnocancel(
            "Unsaved Changes",
            "You have unsaved changes.\n\n"
            "Do you want to save them?"
        )

        if answer is None:
            return False

        if answer:
            return self.save_file()

        return True

    # =========================================================
    # EDIT OPERATIONS
    # =========================================================

    def undo(self):
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass

        self.update_line_numbers()

    def redo(self):
        try:
            self.text_area.edit_redo()
        except tk.TclError:
            pass

        self.update_line_numbers()

    def cut(self):
        self.text_area.event_generate(
            "<<Cut>>"
        )

    def copy(self):
        self.text_area.event_generate(
            "<<Copy>>"
        )

    def paste(self):
        self.text_area.event_generate(
            "<<Paste>>"
        )

    def select_all(self):
        self.text_area.tag_add(
            "sel",
            "1.0",
            tk.END
        )

        self.text_area.mark_set(
            tk.INSERT,
            "1.0"
        )

        self.text_area.see(
            tk.INSERT
        )

    # =========================================================
    # FIND
    # =========================================================

    def show_find(self):
        window = tk.Toplevel(self.root)
        window.title("Find")
        window.geometry("400x150")
        window.configure(bg=self.card)
        window.resizable(False, False)

        tk.Label(
            window,
            text="Find Text",
            font=("Segoe UI", 11, "bold"),
            bg=self.card,
            fg=self.text_color
        ).pack(
            pady=(20, 5)
        )

        entry = tk.Entry(
            window,
            font=("Segoe UI", 12),
            bg=self.editor_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            relief="flat"
        )
        entry.pack(
            padx=25,
            fill="x",
            ipady=8
        )

        def find_text():
            self.text_area.tag_remove(
                "find",
                "1.0",
                tk.END
            )

            word = entry.get()

            if not word:
                return

            start = "1.0"

            while True:
                position = self.text_area.search(
                    word,
                    start,
                    stopindex=tk.END
                )

                if not position:
                    break

                end = f"{position}+{len(word)}c"

                self.text_area.tag_add(
                    "find",
                    position,
                    end
                )

                start = end

            self.text_area.tag_config(
                "find",
                background="#facc15",
                foreground="#000000"
            )

        tk.Button(
            window,
            text="Find All",
            command=find_text,
            font=("Segoe UI", 10, "bold"),
            bg=self.accent,
            fg="#0f172a",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        ).pack(
            pady=15
        )

        entry.focus()

    # =========================================================
    # REPLACE
    # =========================================================

    def show_replace(self):
        window = tk.Toplevel(self.root)
        window.title("Find & Replace")
        window.geometry("450x230")
        window.configure(bg=self.card)
        window.resizable(False, False)

        tk.Label(
            window,
            text="Find",
            font=("Segoe UI", 10, "bold"),
            bg=self.card,
            fg=self.text_color
        ).pack(
            pady=(15, 3)
        )

        find_entry = tk.Entry(
            window,
            font=("Segoe UI", 11),
            bg=self.editor_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            relief="flat"
        )
        find_entry.pack(
            padx=25,
            fill="x",
            ipady=7
        )

        tk.Label(
            window,
            text="Replace With",
            font=("Segoe UI", 10, "bold"),
            bg=self.card,
            fg=self.text_color
        ).pack(
            pady=(10, 3)
        )

        replace_entry = tk.Entry(
            window,
            font=("Segoe UI", 11),
            bg=self.editor_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            relief="flat"
        )
        replace_entry.pack(
            padx=25,
            fill="x",
            ipady=7
        )

        def replace_all():
            find_text = find_entry.get()
            replace_text = replace_entry.get()

            if not find_text:
                return

            content = self.text_area.get(
                "1.0",
                tk.END
            )

            new_content = content.replace(
                find_text,
                replace_text
            )

            self.text_area.delete(
                "1.0",
                tk.END
            )

            self.text_area.insert(
                "1.0",
                new_content
            )

            self.update_line_numbers()

            messagebox.showinfo(
                "Replace",
                "Replacement completed."
            )

        tk.Button(
            window,
            text="Replace All",
            command=replace_all,
            font=("Segoe UI", 10, "bold"),
            bg=self.accent,
            fg="#0f172a",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        ).pack(
            pady=15
        )

        find_entry.focus()

    # =========================================================
    # FONT
    # =========================================================

    def apply_font(self):
        try:
            size = int(
                self.font_size.get()
            )

            self.text_area.config(
                font=("Consolas", size)
            )

            self.line_numbers.config(
                font=("Consolas", size)
            )

        except ValueError:
            pass

    def change_font_size(self, amount):
        new_size = self.font_size.get() + amount

        if 8 <= new_size <= 40:
            self.font_size.set(new_size)
            self.apply_font()

    # =========================================================
    # TEXT COLOR
    # =========================================================

    def choose_text_color(self):
        color = colorchooser.askcolor(
            title="Choose Text Color"
        )

        if color[1]:
            self.text_area.config(
                fg=color[1]
            )

    # =========================================================
    # THEME
    # =========================================================

    def toggle_theme(self):
        if self.dark_mode:
            self.dark_mode = False

            self.bg = "#f1f5f9"
            self.card = "#e2e8f0"
            self.editor_bg = "#ffffff"
            self.text_color = "#0f172a"
            self.muted = "#475569"

        else:
            self.dark_mode = True

            self.bg = "#0f172a"
            self.card = "#1e293b"
            self.editor_bg = "#111827"
            self.text_color = "#f8fafc"
            self.muted = "#94a3b8"

        self.apply_theme()

    def apply_theme(self):
        self.root.configure(
            bg=self.bg
        )

        self.toolbar.configure(
            bg=self.card
        )

        self.text_area.configure(
            bg=self.editor_bg,
            fg=self.text_color,
            insertbackground=self.text_color
        )

        self.line_numbers.configure(
            bg=self.card,
            fg=self.muted
        )

        self.statusbar.configure(
            bg=self.card
        )

        self.status_label.configure(
            bg=self.card,
            fg=self.muted
        )

        self.file_label.configure(
            bg=self.card,
            fg=self.muted
        )

        self.update_status()

    # =========================================================
    # LINE NUMBERS
    # =========================================================

    def update_line_numbers(self):
        self.line_numbers.config(
            state="normal"
        )

        self.line_numbers.delete(
            "1.0",
            tk.END
        )

        lines = self.text_area.index(
            "end-1c"
        ).split(".")[0]

        line_numbers = "\n".join(
            str(i)
            for i in range(1, int(lines) + 1)
        )

        self.line_numbers.insert(
            "1.0",
            line_numbers
        )

        self.line_numbers.config(
            state="disabled"
        )

    def on_scroll(self, *args):
        self.line_numbers.yview_moveto(
            args[0]
        )

        self.text_area.yview(*args)

    # =========================================================
    # STATUS
    # =========================================================

    def update_status(self, event=None):
        self.update_line_numbers()

        cursor = self.text_area.index(
            tk.INSERT
        )

        line, column = cursor.split(".")

        content = self.text_area.get(
            "1.0",
            tk.END
        ).strip()

        words = len(
            content.split()
        ) if content else 0

        characters = len(
            content
        )

        self.status_label.config(
            text=(
                f"Ln {line}, Col {int(column) + 1}"
                f"   |   Words: {words}"
                f"   |   Characters: {characters}"
            )
        )

    # =========================================================
    # MODIFIED
    # =========================================================

    def on_modified(self, event=None):
        if self.text_area.edit_modified():
            self.modified = True

            title = (
                os.path.basename(self.current_file)
                if self.current_file
                else "Untitled"
            )

            self.root.title(
                f"Advanced Notepad - {title} *"
            )

            self.text_area.edit_modified(False)

        self.update_line_numbers()

    # =========================================================
    # KEYBOARD SHORTCUTS
    # =========================================================

    def bind_shortcuts(self):
        self.root.bind(
            "<Control-n>",
            lambda e: self.new_file()
        )

        self.root.bind(
            "<Control-o>",
            lambda e: self.open_file()
        )

        self.root.bind(
            "<Control-s>",
            lambda e: self.save_file()
        )

        self.root.bind(
            "<Control-Shift-S>",
            lambda e: self.save_as()
        )

        self.root.bind(
            "<Control-f>",
            lambda e: self.show_find()
        )

        self.root.bind(
            "<Control-h>",
            lambda e: self.show_replace()
        )

        self.root.bind(
            "<Control-plus>",
            lambda e: self.change_font_size(2)
        )

        self.root.bind(
            "<Control-minus>",
            lambda e: self.change_font_size(-2)
        )

    # =========================================================
    # EXIT
    # =========================================================

    def exit_app(self):
        if self.check_unsaved():
            self.root.destroy()


# =============================================================
# RUN
# =============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedNotepad(root)

    root.protocol(
        "WM_DELETE_WINDOW",
        app.exit_app
    )

    root.mainloop()