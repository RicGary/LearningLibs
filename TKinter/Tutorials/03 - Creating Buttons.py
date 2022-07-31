import tkinter as tk

# creating a simple window
window = tk.Tk()

# creating a button with sizes -> pad
firstButton = tk.Button(window, text='Click me!', padx=50, pady=25)

# packing button to the window
firstButton.pack()

# keep the window open
window.mainloop()