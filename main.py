from tkinter import *
from turtle import forward
import pygame
from tkinter import filedialog

# Create the Window
root = Tk()
root.title('TuneIn')
root.geometry("500x300")

# Initialize Pygame Mixer
pygame.mixer.init()


# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    
    # Strip out the directory info and file extention
    song = song.replace("C:/Users/tshow/OneDrive/Documents/GitHub/TuneIn/audio/","")
    song = song.replace(".mp3","")
    
    # Add song to list box
    song_box.insert(END, song)
    
# Add Many Songs
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    
    # loop through song list and strip out info and extention
    for song in songs:
        song = song.replace("C:/Users/tshow/OneDrive/Documents/GitHub/TuneIn/audio/","")
        song = song.replace(".mp3","")
        # Insert into playlist
        song_box.insert(END, song)
    
# Play Selected Song
def play():
    song = song_box.get(ACTIVE)
    song = f'C:/Users/tshow/OneDrive/Documents/GitHub/TuneIn/audio/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
# Stop Selected Song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    
# Play the next song
def next_song():
    # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one to the current song
    next_one = next_one[0]+1
    # Grab song title from playlist
    song = song_box.get(next_one)
    # Add filename and extention to song title
    song = f'C:/Users/tshow/OneDrive/Documents/GitHub/TuneIn/audio/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Clear and Move active bar in playlist
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)
    
# Play Previous Song in playlist
def previous_song():
    # Get the current song tuple number
    next_one = song_box.curselection()
    # Add one to the current song
    next_one = next_one[0]-1
    # Grab song title from playlist
    song = song_box.get(next_one)
    # Add filename and extention to song title
    song = f'C:/Users/tshow/OneDrive/Documents/GitHub/TuneIn/audio/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # Clear and Move active bar in playlist
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)
   
# Create global pause variable
global paused
paused = False
 
# Pause and Unpause Song
def pause(is_paused):
    global paused
    paused = is_paused
    
    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True
 
# delete a song        
def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

# delete all songs    
def delete_all_songs():
    song_box.delete(0, END)
    pygame.mixer.music.stop()
   

# Create Playlist Box
song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray",selectforeground="black")
song_box.pack(pady=20)

# Define Player Control Button Images
back_img = PhotoImage(file='images/prevbutton.png')
forward_img = PhotoImage(file='images/nextbutton.png')
play_img = PhotoImage(file='images/playbutton.png')
pause_img = PhotoImage(file='images/pausebutton.png')
stop_img = PhotoImage(file='images/stopbutton.png')

# Create Player Control Frames
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
# Add Many Songs to Playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# Create Delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song", command=delete_song)
remove_song_menu.add_command(label="Delete All Song", command=delete_all_songs)
root.mainloop()