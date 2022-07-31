import tkinter as tk

# creating a simple window
window = tk.Tk()

# creating a label, but now let's pass the window created
greetings = tk.Label(window, text='Hello World!')
name = tk.Label(window, text="My name is Eric!")

# adding window to the label makes this next line unnecessarily
# greetings.pack()

# positioning
greetings.grid(row=0, column=0)
name.grid(row=1, column=0)

# keep the window open
window.mainloop()