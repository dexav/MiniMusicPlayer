import tkinter as tk
from tkinter import messagebox

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title('Mini Music Player')

        self.play_button = tk.Button(master, text='Play', command=self.play_music)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(master, text='Pause', command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(master, text='Stop', command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.exit_button = tk.Button(master, text='Exit', command=self.exit_app)
        self.exit_button.pack(pady=10)

    def play_music(self):
        messagebox.showinfo('Info', 'Playing music...')

    def pause_music(self):
        messagebox.showinfo('Info', 'Music paused.')

    def stop_music(self):
        messagebox.showinfo('Info', 'Music stopped.')

    def exit_app(self):
        messagebox.showinfo('Info', 'Exiting app...')
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(width=500, height=500)
    root.maxsize(width=1000, height=1000)
    root.resizable(width=True, height=True)
    player = MusicPlayer(root)
    root.mainloop()
