import tkinter as tk

# creating a simple window
window = tk.Tk()


def onClick():
    clicked = tk.Label(window, text='Clicked on a button!')
    clicked.pack()


# creating a button with a function being passed
firstButton = tk.Button(window, text='Click me!', padx=50, pady=25, command=onClick)

# packing button to the window
firstButton.pack()

# keep the window open
window.mainloop()