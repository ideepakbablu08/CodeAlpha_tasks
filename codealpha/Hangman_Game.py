import tkinter as tk
from tkinter import messagebox
from random import choice

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x400")
        self.root.resizable(0, 0)
        self.root.configure(bg="#000000")

        self.player_score = 0
        self.computer_score = 0

        self.dictionary = ["cat", "dog", "bird", "nest", "sun", "tree"]

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.hangman_canvas = tk.Canvas(self.root, width=200, height=300, bg="#000000", highlightthickness=0)
        self.hangman_canvas.grid(row=0, column=0, rowspan=7, padx=10, pady=10)

        self.label_title = tk.Label(self.root, text="Hangman Game", font=("Helvetica", 18, "bold"), bg="#000000", fg="#FF0000")
        self.label_title.grid(row=0, column=0, pady=10, padx=20)

        self.label_clue = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"), bg="#000000", fg="#FF0000")
        self.label_clue.grid(row=1, column=1, pady=10, sticky="w")

        self.entry_letter = tk.Entry(self.root, font=("Helvetica", 14, "bold"), width=3, fg="#FF0000", bg="#000000", insertbackground="#FF0000")
        self.entry_letter.grid(row=2, column=1, sticky="w")

        self.button_guess = tk.Button(self.root, text="Guess", font=("Helvetica", 12, "bold"), command=self.guess_letter, fg="#FF0000", bg="#000000")
        self.button_guess.grid(row=3, column=1, pady=5, sticky="w")

        self.label_guesses = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"), bg="#000000", fg="#FF0000")
        self.label_guesses.grid(row=4, column=1, pady=5, sticky="w")

        self.button_play_again = tk.Button(self.root, text="Play Again", font=("Helvetica", 12, "bold"), command=self.start_game, fg="#FF0000", bg="#000000")
        self.button_play_again.grid(row=5, column=1, pady=5, sticky="w")

        self.label_score = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"), bg="#000000", fg="#FF0000")
        self.label_score.grid(row=6, column=1, pady=5, sticky="w")

    def start_game(self):
        self.word = choice(self.dictionary)
        self.word_length = len(self.word)
        self.clue = ["_"] * self.word_length
        self.tries = 6
        self.letters_tried = ""
        self.letters_wrong = 0

        self.update_display()

    def guess_letter(self):
        letter = self.entry_letter.get().lower()
        self.entry_letter.delete(0, tk.END)

        if len(letter) == 1 and letter.isalpha():
            if letter in self.letters_tried:
                messagebox.showinfo("Hangman", f"You've already picked '{letter}'")
            else:
                self.letters_tried += letter
                if letter in self.word:
                    for i in range(self.word_length):
                        if self.word[i] == letter:
                            self.clue[i] = letter
                else:
                    self.letters_wrong += 1
        else:
            messagebox.showwarning("Hangman", "Please enter a valid letter.")

        self.update_display()

        if self.letters_wrong == self.tries:
            messagebox.showinfo("Hangman", f"Game Over! The word was '{self.word}'")
            self.computer_score += 1
            self.update_score()
        elif "_" not in self.clue:
            messagebox.showinfo("Hangman", f"You win! The word was '{self.word}'")
            self.player_score += 1
            self.update_score()

    def update_display(self):
        self.label_clue.config(text=" ".join(self.clue))
        self.label_guesses.config(text=f"Guesses: {self.letters_tried}")
        self.update_hangman_graphic()

    def update_hangman_graphic(self):
        self.hangman_canvas.delete("all")
        graphics = [
            """
                +-------+
                |
                |
                | 
                |
                |
             ==============
            """,
            """
                +-------+
                |       |
                |       0
                | 
                |
                |
             ==============
            """,
            """
                +-------+
                |       |
                |       0
                |       |
                |
                |
             ==============
            """,
            """
                +-------+
                |       |
                |       0
                |      -|
                |
                |
             ==============
            """,
            """
                +-------+
                |       |
                |       0
                |      -|-
                |
                |
             ==============
            """,
            """
                +-------+
                |       |
                |       0
                |      -|-
                |      /
                |
             ==============
            """,
            """
                +-------+
                |       |
                |       0
                |      -|-
                |      / \\
                |
             ==============
            """
        ]
        self.hangman_canvas.create_text(60, 180, text=graphics[self.letters_wrong], font=("Courier", 10), fill="#FF0000")

    def update_score(self):
        self.label_score.config(text=f"Player: {self.player_score} | Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
