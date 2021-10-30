"""
Create an anagram game!
"""
import random
import tkinter as tk
from tkinter import messagebox

# TODO Use this dictionary of anagrams to create an anagrams GUI word game.
#  Look at 'anagrams_game_example.png' in this folder for an example.
word_anagrams = {
    "action": ["cation"],
    "agree": ["eager"],
    "calm": ["clam"],
    "charming": ["marching"],
    "clean": ["lance"],
    "cool": ["loco"],
    "creative": ["reactive"],
    "delight": ["lighted"],
    "earnest": ["eastern", "nearest"],
    "easy": ["ayes", "yeas"],
    "free": ["reef"],
    "great": ["grate"],
    "green": ["genre"],
    "grin": ["ring"],
    "hearty": ["earthy"],
    "idea": ["aide"],
    "ideal": ["ailed"],
    "keen": ["knee"],
    "lively": ["evilly", "vilely"],
    "lovely": ["volley"],
    "merit": ["miter", "remit", "timer"],
    "open": ["nope", "peon", "pone"],
    "prepared": ["dapperer"],
    "quiet": ["quite"],
    "refined": ["definer"],
    "restored": ["resorted", "rostered"],
    "reward": ["drawer", "redraw", "warder", "warred"],
    "rewarding": ["redrawing", "wardering"],
    "right": ["girth"],
    "secure": ["rescue"],
    "simple": ["impels"],
    "smile": ["limes", "miles", "slime"],
    "super": ["puers", "purse"],
    "tops": ["opts", "post", "pots", "spot", "stop"],
    "unreal": ["neural"],
    "wonderful": ["underflow"],
    "zeal": ["laze"]}


class Anagrams(tk.Tk):
    def __init__(self):
        super().__init__()
        self.guesses_remaining = 5
        self.guesses_remaining_label = tk.Label(self, text="Guesses Remaining:   " + str(self.guesses_remaining), font=('arial', 12))
        self.guesses_remaining_label.place(relx=0, rely=0.4, relwidth=0.4, relheight=0.3)
        self.guesses = list()
        self.guesses_label = tk.Label(self, text="")
        self.guesses_label.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)
        self.words_used = list()
        self.word = self.rand_word()
        self.word_label = tk.Label(self, text=self.word)
        self.word_label.place(relx=0.5, rely=0, relwidth=0.2, relheight=0.3)
        self.instructions = tk.Label(self, text="Guess the " + str(len(word_anagrams[self.word])) + " anagram(s) for the word: ")
        self.instructions.place(relx=0, rely=0, relwidth=0.54, relheight=0.3)
        self.new_word = tk.Button(self, text="Get New Word!")
        self.new_word.bind("<ButtonPress>", self.get_new_word)
        self.new_word.place(relx=0.7, rely=0.03, relwidth=0.25, relheight=0.2)
        self.guess_box = tk.Entry(self)
        self.guess_box.place(relx=0.43, rely=0.45, relwidth=0.3, relheight=0.2)
        self.guess_button = tk.Button(self, text="Guess")
        self.guess_button.place(relx=0.77, rely=0.45, relwidth=0.2, relheight=0.2)
        self.guess_button.bind("<ButtonPress>", self.guess_word)

    def get_new_word(self, event):
        self.guesses.clear()
        self.guesses_label.configure(text="")
        self.word = self.rand_word()
        self.word_label.configure(text=self.word)
        self.guesses_remaining = 5
        self.guesses_remaining_label.configure(text="Guesses Remaining:   " + str(self.guesses_remaining))
        self.instructions.configure(text="Guess the " + str(len(word_anagrams[self.word])) + " anagram(s) for the word: ")
        return


    def rand_word(self):
        size = len(word_anagrams)
        rand = random.randint(0, size-1)
        word = list(word_anagrams)[rand]
        while word in self.words_used:
            rand = random.randint(0, size - 1)
            word = list(word_anagrams)[rand]
        self.words_used.append(word)
        return word

    def guess_word(self, event):
        guess = self.guess_box.get()
        words = word_anagrams[self.word]
        if guess in words:
            if guess not in self.guesses:
                messagebox.showinfo(None, "Correct!")
                self.guesses.append(guess)
                thing = ""
                for g in self.guesses:
                    thing+=g+", "
                self.guesses_label.configure(text=thing)
        elif self.guesses_remaining == 0:
            messagebox.showinfo(None, "You don't have any more guesses remaining! Get a new word!")
        else:
            self.guesses_remaining -= 1
            self.guesses_remaining_label.configure(text="Guesses Remaining:   " + str(self.guesses_remaining))
            messagebox.showinfo(None, "incorrect!")
        self.guess_box.delete(0, tk.END)


if __name__ == '__main__':
    AnnaGram = Anagrams()
    AnnaGram.geometry("500x200")
    AnnaGram.mainloop()




