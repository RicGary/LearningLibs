"""
If you want to learn more: https://www.youtube.com/watch?v=YXPyB4XeYLA&t
"""

import tkinter as tk

# creating a simple window
window = tk.Tk()

# creating a label
greetings = tk.Label(text='Hello World!')

# here you can add the label to the window created earlier
greetings.pack()

# keep the window open
window.mainloop()