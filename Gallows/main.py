import tkinter as tk
from Model.model import HangmanModel
from View.view import HangmanView
from Controller.controller import HangmanController

def main():
    root = tk.Tk()
    model = HangmanModel()
    view = HangmanView(root)
    controller = HangmanController(model, view)
    root.mainloop()

if __name__ == "__main__":
    main()
