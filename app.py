import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Hello World").pack()
root.title("Mini Music Player")
root.minsize(width=500, height=500)
root.maxsize(width=1000, height=1000)
root.resizable(width=True, height=True)

root.mainloop()


