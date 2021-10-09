"""
Create a memory match game!
"""
import random
import time
import tkinter as tk
from tkinter import messagebox


# TODO: First, run this code. You should see a grid with 52 buttons.
#   Your task is to:
#   1. Create a dictionary with each button as a key and a number from 1 to 13
#      as the corresponding value. There are 52 buttons, so there should be EXACTLY
#      4 copies of each number from 1 ot 13.
#   2. Show the value of the button (a number from 1 to 13) when it's clicked.
#   3. After the second button is clicked, check if the number from the first button
#      matches the number of the second button.
#      a. If they match, show the two numbers and disable them so they can't be clicked again.
#         There is an example of how to disable the button in the code below.
#      b. If they don't match, remove the text from the two buttons. The two buttons should
#         still be clickable.
#   4. End the game with a congratulations message when all the numbers have been matched.
#   5. See 'memory_match_example.png' in this folder for an example of what the game should
#      look like.
class MemoryMatch(tk.Tk):
    WIDTH = 1090
    HEIGHT = 500
    TOTAL_BUTTONS = 52

    def __init__(self):
        super().__init__()

        # 4 copies of each value
        num_copies_each_value = 4
        buttons_per_row = MemoryMatch.TOTAL_BUTTONS / 4
        button_width, button_height = self.setup_buttons(buttons_per_row)
        self.dictionary = dict()
        self.buttons_pressed = list()
        numbers_used = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(MemoryMatch.TOTAL_BUTTONS):
            row_num = int(i / buttons_per_row)
            col_num = int(i % buttons_per_row)
            row_y = row_num * button_height
            col_x = col_num * button_width
            button = tk.Button(self, text='', fg='black', font=('arial', 24, 'bold'))
            button.place(x=col_x, y=row_y, width=button_width, height=button_height)
            button.bind('<ButtonPress>', self.on_button_press)
            rand = random.randint(1, 13)
            while numbers_used[rand - 1] >= 4:
                rand = random.randint(1, 13)
            numbers_used[rand - 1] += 1
            self.dictionary[button] = rand
        self.matches = 0
        self.matches_label = tk.Label(self, text='Matches: 0', font=('arial', 36, 'bold'))
        self.matches_label.place(x=0, y=MemoryMatch.HEIGHT)
        self.attempts = 0
        self.attempts_label = tk.Label(self, text='Attempts: 0', font=('arial', 36, 'bold'))
        self.attempts_label.place(x=400, y=MemoryMatch.HEIGHT)

    def on_button_press(self, event):
        button_pressed = event.widget
        button_pressed.configure(text=str(self.dictionary[button_pressed]))
        if not self.buttons_pressed.__contains__(button_pressed) and not button_pressed['state'] == tk.DISABLED:
            self.buttons_pressed.append(button_pressed)
        if len(self.buttons_pressed) == 2:
            if self.dictionary[self.buttons_pressed[0]] == self.dictionary[self.buttons_pressed[1]]:
                self.buttons_pressed[0].configure(state=tk.DISABLED, text=self.dictionary[self.buttons_pressed[0]])
                self.buttons_pressed[1].configure(state=tk.DISABLED, text=self.dictionary[self.buttons_pressed[1]])
                self.buttons_pressed.clear()
                self.matches += 1
            self.attempts += 1
        if len(self.buttons_pressed) == 3:
            self.buttons_pressed[0].configure(text='')
            self.buttons_pressed[1].configure(text='')
            self.buttons_pressed.clear()
            self.buttons_pressed.append(button_pressed)

        self.matches_label.configure(text='Matches: ' + str(self.matches))
        self.attempts_label.configure(text='Attempts: ' + str(self.attempts))
        if self.matches == 26:
            messagebox.showinfo(None, message="Congratulations! You won!")

        #if button_pressed['state'] == tk.DISABLED:
        #    button_pressed.configure(state=tk.NORMAL, text='ON')
        #elif button_pressed['state'] == tk.NORMAL:
        #    button_pressed.configure(state=tk.DISABLED, text='OFF')

    def setup_buttons(self, buttons_per_row):
        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('%sx%s' % (MemoryMatch.WIDTH, MemoryMatch.HEIGHT))
        self.update_idletasks()

        num_rows = int(MemoryMatch.TOTAL_BUTTONS / buttons_per_row)
        if MemoryMatch.TOTAL_BUTTONS % buttons_per_row != 0:
            num_rows += 1

        button_width = int(self.winfo_width() / buttons_per_row)
        button_height = int(self.winfo_height() / num_rows)
        self.geometry('%sx%s' % (MemoryMatch.WIDTH, MemoryMatch.HEIGHT + 100))

        return button_width, button_height

if __name__ == '__main__':
    game = MemoryMatch()
    game.title('League Python Memory Game')
    game.mainloop()
