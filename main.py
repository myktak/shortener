from tkinter import *
import pyshorteners

def shorten():
    if shorty.get():
        shorty.delete(0, END)
    if entry.get():
        url = pyshorteners.Shortener().tinyurl.short(entry.get())
        shorty.insert(END, url)

root = Tk()
root.title('Shortener(tkinter)')
root.attributes('-type', 'dialog')

label = Label(root, text="Enter link:", font=30)
label.pack(pady=(10, 0))

entry = Entry(root, font=80)
entry.pack(padx=20)

button = Button(root, text="Shorten link", font=50, command=shorten)
button.pack(pady=20, padx=30)

shorty_label = Label(root, text="Shortened link:", font=30)
shorty_label.pack()

shorty = Entry(root, font=80)
shorty.pack(pady=(0, 10))

root.mainloop()