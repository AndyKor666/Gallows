import tkinter as tk

class HangmanView:
    def __init__(self, root):
        self.root = root
        self.bg = "#0b0b0b"
        self.main = "#d2c29d"
        self.blood = "#8b0000"
        self.dim = "#6e6e6e"
        self.root.title("HANGMAN")
        self.root.geometry("500x400")
        self.root.configure(bg=self.bg)
        self.title = tk.Label(
            root,
            text="H A N G M A N",
            font=("Consolas", 22, "bold"),
            bg=self.bg,
            fg=self.blood
        )
        self.title.pack(pady=15)
        self.word_label = tk.Label(
            root,
            text="_ _ _ _ _",
            font=("Consolas", 28, "bold"),
            bg=self.bg,
            fg=self.main
        )
        self.word_label.pack(pady=10)
        self.entry = tk.Entry(
            root,
            font=("Consolas", 18),
            justify="center",
            width=4,
            bg="#1c1c1c",
            fg=self.main,
            insertbackground=self.main
        )
        self.entry.pack(pady=10)
        self.button = tk.Button(
            root,
            text="TRY LETTER",
            font=("Consolas", 14),
            bg="#2b2b2b",
            fg=self.main,
            activebackground="#3b1c1c",
            activeforeground=self.main,
            relief="raised",
            borderwidth=2
        )
        self.button.pack(pady=10)
        self.status_label = tk.Label(
            root,
            text="Attempts left: 6",
            font=("Consolas", 14),
            bg=self.bg,
            fg=self.main
        )
        self.status_label.pack(pady=10)
        self.message_label = tk.Label(
            root,
            text="Good luck in GULAG...",
            font=("Consolas", 13, "italic"),
            bg=self.bg,
            fg=self.dim
        )
        self.message_label.pack(pady=10)
        self.restart_button = tk.Button(
            root,
            text="New Game",
            font=("Consolas", 12),
            bg="#2b2b2b",
            fg=self.main,
            activebackground="#3b1c1c",
            activeforeground=self.main,
            relief="ridge",
            borderwidth=2
        )
        self.restart_button.pack(pady=10)

    def set_word(self, text):
        spaced = " ".join(text.upper())
        self.word_label.config(text=spaced)

    def set_status(self, text):
        self.status_label.config(text=text)

    def show_message(self, text, color=None):
        if color is None:
            color = self.main
        self.message_label.config(text=text, fg=color)

    def clear_input(self):
        self.entry.delete(0, tk.END)
