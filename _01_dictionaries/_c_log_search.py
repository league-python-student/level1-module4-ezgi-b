"""
Log Search using a Id-Name Dictionary
"""

# TODO: Create a dictionary of integers for the keys and strings for the values.
#  Create a GUI app with three buttons. Look at 'log_search_example.png' in this
#  folder for an example of what your program should look like.
#
#  Button 1: Add Entry
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      After an ID is entered, use another input dialog to ask the user
#      to enter a name. Add this information as a new entry to your
#      dictionary.

#  Button 2: Search by ID
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      If that ID exists, display that name to the user.
#      Otherwise, tell the user that that entry does not exist.
#
# Button 3: View List
#      When this button is clicked, display the entire list in a message
#      dialog in the following format:
#      ID: 123  Name: Harry Howard
#      ID: 245  Name: Polly Powers
#      ID: 433  Name: Oliver Ortega
#      etc...
#
# When this is complete, add a fourth button to your window.
# Button 4: Remove Entry
#      When this button is clicked, prompt the user to enter an ID using
#      an input dialog.
#      If this ID exists in the dictionary, remove it. Otherwise, notify the
#      user that the ID is not in the list.
#
import tkinter as tk
from tkinter import simpledialog, messagebox

class log_search(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dictionary = dict()

        self.button_1 = tk.Button(text='Add Entry')
        self.button_1.place(relx=0, rely=0, relwidth=0.25, relheight=1)
        self.button_1.bind('<ButtonPress>', self.add_entry)

        self.button_2 = tk.Button(text='Search by ID')
        self.button_2.place(relx=0.25, rely=0, relwidth=0.25, relheight=1)
        self.button_2.bind('<ButtonPress>', self.search_by_id)

        self.button_3 = tk.Button(text='View List')
        self.button_3.place(relx=0.5, rely=0, relwidth=0.25, relheight=1)
        self.button_3.bind('<ButtonPress>', self.view_list)

        self.button_4 = tk.Button(text='Remove Entry')
        self.button_4.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)
        self.button_4.bind('<ButtonPress>', self.remove_entry)

    def add_entry(self, event):
        key = simpledialog.askinteger(None, prompt="What is the ID?")
        value = simpledialog.askstring(None, prompt="What is the name?")
        self.dictionary[key] = value

    def search_by_id(self, event):
        key = simpledialog.askinteger(None, prompt="What is the ID?")
        if key in self.dictionary:
            messagebox.showinfo(message="The person with that ID is " + self.dictionary[key])
        else:
            messagebox.showinfo(message="No one with that ID exists")

    def view_list(self, event):
        list = ""
        for key in self.dictionary:
            list += "ID: " + str(key) + ", Name: " + self.dictionary[key] + "\n";
        messagebox.showinfo(message=list)

    def remove_entry(self, event):
        key = simpledialog.askinteger(None, prompt="What is the ID?")
        if key in self.dictionary:
            messagebox.showinfo(message="The person with that ID is " + self.dictionary[key]+ ". That user had been removed.")
            del self.dictionary[key]
        else:
            messagebox.showinfo(message="No one with that ID exists")


if __name__ == '__main__':
    search = log_search()
    search.geometry("400x100")
    search.mainloop()


