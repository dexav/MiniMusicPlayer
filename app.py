import tkinter as tk
from tkinter import messagebox

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title('Mini Music Player')

<<<<<<< Updated upstream
        self.play_button = tk.Button(master, text='Play', command=self.play_music)
        self.play_button.pack(pady=10)
=======
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Variables
        self.current_song = ""
        self.paused = False
        self.playlist = []
        self.current_index = 0
        self.shuffle_mode = False
        
        # Create main frames
        self.create_header_frame()
        self.create_playlist_frame()
        self.create_control_frame()
        self.create_info_frame()
        
        # Bind events
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_header_frame(self):
        self.header_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        self.header_frame.pack(fill=tk.X)
        
        # App title
        title_label = tk.Label(
            self.header_frame, 
            text="Musik-Player", 
            font=("Helvetica", 18, "bold"),
            fg="white",
            bg="#2c3e50"
        )
        title_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Add music button
        self.add_btn = tk.Button(
            self.header_frame,
            text="Musik hinzufügen",
            font=("Helvetica", 10),
            bg="#3498db",
            fg="white",
            command=self.add_songs
        )
        self.add_btn.pack(side=tk.RIGHT, padx=20, pady=15)
        
    def create_playlist_frame(self):
        playlist_container = tk.Frame(self.root, bg="#f5f5f5")
        playlist_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Playlist label
        playlist_label = tk.Label(
            playlist_container,
            text="Playlist",
            font=("Helvetica", 14, "bold"),
            bg="#f5f5f5"
        )
        playlist_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Create a frame for the playlist with scrollbar
        playlist_frame = tk.Frame(playlist_container, bg="#f5f5f5")
        playlist_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(playlist_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Playlist listbox
        self.playlist_box = tk.Listbox(
            playlist_frame,
            bg="white",
            fg="#333333",
            width=60,
            height=15,
            selectbackground="#3498db",
            selectforeground="white",
            font=("Helvetica", 10),
            yscrollcommand=scrollbar.set
        )
        self.playlist_box.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        scrollbar.config(command=self.playlist_box.yview)
        
        # Bind double-click to play selected song
        self.playlist_box.bind("<Double-1>", self.play_selected_song)
        
        # Button frame for playlist actions
        btn_frame = tk.Frame(playlist_container, bg="#f5f5f5")
        btn_frame.pack(fill=tk.X, pady=10)
        
        # Remove song button
        self.remove_btn = tk.Button(
            btn_frame,
            text="Entfernen",
            font=("Helvetica", 10),
            bg="#e74c3c",
            fg="white",
            command=self.remove_song
        )
        self.remove_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Shuffle button
        self.shuffle_btn = tk.Button(
            btn_frame,
            text="Zufällige Wiedergabe",
            font=("Helvetica", 10),
            bg="#9b59b6",
            fg="white",
            command=self.toggle_shuffle
        )
        self.shuffle_btn.pack(side=tk.LEFT)
        
    def create_control_frame(self):
        control_frame = tk.Frame(self.root, bg="#ecf0f1", height=100)
        control_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Progress bar
        self.progress_frame = tk.Frame(control_frame, bg="#ecf0f1")
        self.progress_frame.pack(fill=tk.X, padx=20, pady=(10, 0))
        
        self.progress_label = tk.Label(
            self.progress_frame,
            text="00:00 / 00:00",
            bg="#ecf0f1",
            font=("Helvetica", 8)
        )
        self.progress_label.pack(side=tk.RIGHT)
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            orient=tk.HORIZONTAL,
            length=100,
            mode="determinate"
        )
        self.progress_bar.pack(fill=tk.X, padx=(0, 10), side=tk.LEFT, expand=True)
        
        # Control buttons
        buttons_frame = tk.Frame(control_frame, bg="#ecf0f1")
        buttons_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Previous button
        self.prev_btn = tk.Button(
            buttons_frame,
            text="⏮",
            font=("Helvetica", 16),
            bg="#ecf0f1",
            command=self.play_prev
        )
        self.prev_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Play/Pause button
        self.play_btn = tk.Button(
            buttons_frame,
            text="▶",
            font=("Helvetica", 16),
            bg="#2ecc71",
            fg="white",
            width=8,
            command=self.play_pause
        )
        self.play_btn.pack(side=tk.LEFT, padx=10)
        
        # Next button
        self.next_btn = tk.Button(
            buttons_frame,
            text="⏭",
            font=("Helvetica", 16),
            bg="#ecf0f1",
            command=self.play_next
        )
        self.next_btn.pack(side=tk.LEFT, padx=10)
        
        # Volume frame
        volume_frame = tk.Frame(buttons_frame, bg="#ecf0f1")
        volume_frame.pack(side=tk.RIGHT)
        
        # Volume icon
        volume_label = tk.Label(
            volume_frame,
            text="🔊",
            font=("Helvetica", 12),
            bg="#ecf0f1"
        )
        volume_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Volume slider
        self.volume_slider = ttk.Scale(
            volume_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            value=70,
            command=self.set_volume
        )
        self.volume_slider.pack(side=tk.RIGHT)
        
        # Set initial volume
        self.set_volume(70)
        
    def create_info_frame(self):
        self.info_frame = tk.Frame(self.root, bg="#ecf0f1", height=60)
        self.info_frame.pack(fill=tk.X)
        
        # Now playing label
        self.now_playing_var = tk.StringVar()
        self.now_playing_var.set("Bereit zum Abspielen")
        
        now_playing_label = tk.Label(
            self.info_frame,
            textvariable=self.now_playing_var,
            font=("Helvetica", 10, "italic"),
            bg="#ecf0f1"
        )
        now_playing_label.pack(pady=10)
        
        # Song duration label
        self.duration_var = tk.StringVar()
        self.duration_var.set("")
        
        duration_label = tk.Label(
            self.info_frame,
            textvariable=self.duration_var,
            font=("Helvetica", 9),
            bg="#ecf0f1",
            fg="#7f8c8d"
        )
        duration_label.pack(pady=(0, 10))
        
    
>>>>>>> Stashed changes

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
