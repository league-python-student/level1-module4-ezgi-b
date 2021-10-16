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
        self.guesses = 5
        self.guesses_label = tk.Label(self, text="bljglref")
        self.guesses_label.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.3)
        self.instructions = tk.Label(self, text="")
        self.word_label = tk.Label(self, text="")
        self.word = ""
        self.new_word = tk.Button(self, text="Get New Word!")
        self.guess_box = tk.Entry(self)
        self.guess_box.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.3)
        self.guess_box.bind("<KeyPress>")


if __name__ == '__main__':
    AnnaGram = Anagrams()
    AnnaGram.geometry("500x200")
    AnnaGram.mainloop()




