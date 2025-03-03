import os
import tkinter as tk
from tkinter import filedialog, ttk
import pygame
import random
from PIL import Image, ImageTk
import io
import urllib.request
from mutagen.mp3 import MP3

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Musik-Player")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")
        self.root.resizable(True, True)

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
        
    def add_songs(self):
        # Open file dialog to select music files
        songs = filedialog.askopenfilenames(
            title="Musikdateien auswählen",
            filetypes=(("MP3 Files", "*.mp3"), ("All Files", "*.*"))
        )
        
        # Add songs to playlist
        for song in songs:
            song_name = os.path.basename(song)
            if song not in self.playlist:
                self.playlist.append(song)
                self.playlist_box.insert(tk.END, song_name)
    
    def play_selected_song(self, event=None):
        # Get selected song index
        try:
            index = self.playlist_box.curselection()[0]
            self.current_index = index
            self.play_song()
        except:
            pass
    
    def play_song(self):
        # Stop current song if playing
        pygame.mixer.music.stop()
        
        # Get selected song
        if not self.playlist:
            return
            
        self.current_song = self.playlist[self.current_index]
        song_name = os.path.basename(self.current_song)
        
        # Update now playing info
        self.now_playing_var.set(f"Spielt: {song_name}")
        
        # Load and play song
        pygame.mixer.music.load(self.current_song)
        pygame.mixer.music.play()
        
        # Update play button text
        self.play_btn.config(text="⏸")
        self.paused = False
        
        # Get song info
        try:
            audio = MP3(self.current_song)
            song_length = audio.info.length
            mins, secs = divmod(song_length, 60)
            mins = round(mins)
            secs = round(secs)
            self.duration_var.set(f"Dauer: {mins:02d}:{secs:02d}")
            
            # Start progress bar update
            self.update_progress(song_length)
        except:
            self.duration_var.set("Dauer: Unbekannt")
        
        # Highlight current song in playlist
        self.playlist_box.selection_clear(0, tk.END)
        self.playlist_box.selection_set(self.current_index)
        self.playlist_box.activate(self.current_index)
        self.playlist_box.see(self.current_index)
    
    def play_pause(self):
        if not self.playlist:
            return
            
        if self.paused:
            # Resume playing
            pygame.mixer.music.unpause()
            self.play_btn.config(text="⏸")
            self.paused = False
        else:
            # Check if music is playing
            if pygame.mixer.music.get_busy():
                # Pause music
                pygame.mixer.music.pause()
                self.play_btn.config(text="▶")
                self.paused = True
            else:
                # Start playing if nothing is playing
                self.play_song()
    
    def play_next(self):
        if not self.playlist:
            return
            
        if self.shuffle_mode:
            # Play random song
            next_index = random.randint(0, len(self.playlist) - 1)
            while next_index == self.current_index and len(self.playlist) > 1:
                next_index = random.randint(0, len(self.playlist) - 1)
            self.current_index = next_index
        else:
            # Play next song in order
            self.current_index = (self.current_index + 1) % len(self.playlist)
            
        self.play_song()
    
    def play_prev(self):
        if not self.playlist:
            return
            
        if self.shuffle_mode:
            # Play random song
            prev_index = random.randint(0, len(self.playlist) - 1)
            while prev_index == self.current_index and len(self.playlist) > 1:
                prev_index = random.randint(0, len(self.playlist) - 1)
            self.current_index = prev_index
        else:
            # Play previous song in order
            self.current_index = (self.current_index - 1) % len(self.playlist)
            
        self.play_song()
    
    def remove_song(self):
        # Remove selected song from playlist
        try:
            selected_index = self.playlist_box.curselection()[0]
            self.playlist_box.delete(selected_index)
            self.playlist.pop(selected_index)
            
            # If removed song was playing, play next song
            if selected_index == self.current_index:
                if self.playlist:
                    if selected_index < len(self.playlist):
                        self.current_index = selected_index
                    else:
                        self.current_index = 0
                    self.play_song()
                else:
                    pygame.mixer.music.stop()
                    self.now_playing_var.set("Bereit zum Abspielen")
                    self.duration_var.set("")
                    self.play_btn.config(text="▶")
            elif selected_index < self.current_index:
                self.current_index -= 1
        except:
            pass
    
    def set_volume(self, val):
        # Set volume
        volume = float(val) / 100
        pygame.mixer.music.set_volume(volume)
    
    def toggle_shuffle(self):
        # Toggle shuffle mode
        self.shuffle_mode = not self.shuffle_mode
        if self.shuffle_mode:
            self.shuffle_btn.config(bg="#8e44ad")
        else:
            self.shuffle_btn.config(bg="#9b59b6")
    
    def update_progress(self, total_length):
        # Update progress bar
        current_time = pygame.mixer.music.get_pos() / 1000
        
        # Convert to time format
        mins, secs = divmod(current_time, 60)
        mins = round(mins)
        secs = round(secs)
        
        # Format time
        timeformat = f"{mins:02d}:{secs:02d}"
        
        # Get total time
        total_mins, total_secs = divmod(total_length, 60)
        total_mins = round(total_mins)
        total_secs = round(total_secs)
        
        # Update progress label
        self.progress_label.config(text=f"{timeformat} / {total_mins:02d}:{total_secs:02d}")
        
        # Update progress bar
        if total_length > 0:
            self.progress_bar["value"] = (current_time / total_length) * 100
        
        # Check if song has ended
        if not pygame.mixer.music.get_busy() and not self.paused:
            self.play_next()
        else:
            # Schedule next update
            self.root.after(1000, lambda: self.update_progress(total_length))
    
    def on_closing(self):
        # Stop music and close application
        pygame.mixer.music.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

