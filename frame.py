from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title = "frame app"

new_frame = LabelFrame(root, text="check this dope fram", padx=5, pady=5)
new_frame.pack(padx=10, pady=10)

b = Button(frame, text="don't click here")
b.pack()





root.mainloop()
