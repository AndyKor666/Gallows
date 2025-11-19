import random

class HangmanModel:
    def __init__(self):
        self.words=["dachau", "buchenwald", "auschwitz", "belzek", "gulag", "school"]
        self.word=""
        self.hidden=""
        self.attempts=6
    def new_game(self):
        self.word=random.choice(self.words)
        self.hidden="_"*len(self.word)
        self.attempts=6
    def guess(self, letter):
        letter=letter.lower()
        if letter in self.word:
            self.hidden = "".join(
                [letter if self.word[i]==letter else self.hidden[i] for i in range(len(self.word))]
            )
            return True
        else:
            self.attempts-=1
            return False
    def is_won(self):
        return self.hidden==self.word
    def is_lost(self):
        return self.attempts<= 0
