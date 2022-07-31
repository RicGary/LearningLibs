import tkinter as tk

# creating a simple window
window = tk.Tk()

# putting data on our window
entry = tk.Entry(window, width=50, borderwidth=5)
entry.insert(0, 'Enter your name:')
entry.pack()


def onClick():
    text = 'Hello ' + entry.get()
    clicked = tk.Label(window, text=text)
    clicked.pack()


# creating a button with a function being passed
firstButton = tk.Button(window, text='Click me!', padx=50, pady=25, command=onClick)

# packing button to the window
firstButton.pack()

# keep the window open
window.mainloop()