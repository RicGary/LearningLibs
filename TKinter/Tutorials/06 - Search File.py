import tkinter as tk
from tkinter import filedialog

# let's make a little project
window = tk.Tk()

# a simple title
window.title('WordDoc word changing.')

# open a box and returns the path
window.filename = filedialog.askopenfilename(initialdir='/', title='Select the directory:')

window.mainloop()
