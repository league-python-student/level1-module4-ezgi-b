"""
Create an anagram game!
"""
import random
import tkinter as tk

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
        self.guesses_label = tk.Label(self, text="testest")
        self.guesses_label.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)
        self.words_used = list()
        self.instructions = tk.Label(self, text="Guess the # anagram(s) for the word: ")
        self.instructions.place(relx=0, rely=0, relwidth=0.54, relheight=0.3)
        self.word_label = tk.Label(self, text=self.word)
        self.word = self.rand_word()
        self.word_label.place(relx=0.5, rely=0, relwidth=0.2, relheight=0.3)
        self.new_word = tk.Button(self, text="Get New Word!")
        self.new_word.bind("<KeyPress>", self.rand_word)
        self.new_word.place(relx=0.7, rely=0.03, relwidth=0.25, relheight=0.2)
        self.guess_box = tk.Entry(self)
        self.guess_box.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.2)

    def rand_word(self):
        size = len(word_anagrams)
        rand = random.randint(0, size-1)
        word = list(word_anagrams)[rand]
        while word in self.words_used:
            rand = random.randint(0, size - 1)
            word = list(word_anagrams)[rand]
        self.words_used.append(word)
        self.word_label.configure(self, text=word)
        return word


if __name__ == '__main__':
    AnnaGram = Anagrams()
    AnnaGram.geometry("500x200")
    AnnaGram.mainloop()




