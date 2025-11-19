from Model.model import HangmanModel
from View.view import HangmanView

class HangmanController:
    def __init__(self, model: HangmanModel, view: HangmanView):
        self.model=model
        self.view=view
        self.view.button.config(command=self.on_guess)
        self.view.restart_button.config(command=self.new_game)
        self.new_game()
    def new_game(self):
        self.model.new_game()
        self.view.set_word(self.model.hidden)
        self.view.set_status(f"Attempts left: {self.model.attempts}")
        self.view.show_message("Start guessing!", "#333")
    def on_guess(self):
        letter = self.view.entry.get().strip().lower()
        if not letter or len(letter) != 1 or not letter.isalpha():
            self.view.show_message("Enter one letter!", "darkred")
            return
        correct=self.model.guess(letter)
        self.view.set_word(self.model.hidden)
        self.view.set_status(f"Attempts left: {self.model.attempts}")
        if correct:
            self.view.show_message("Good guess!", "green")
        else:
            self.view.show_message("Wrong!", "red")
        if self.model.is_won():
            self.view.show_message(f"You won! Word: {self.model.word.upper()}", "darkgreen")
        elif self.model.is_lost():
            self.view.show_message(f"Game over\n\nYOU'RE DEAD.\nWord was: {self.model.word.upper()}", "darkred")
