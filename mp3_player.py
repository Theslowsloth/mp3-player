import os
import pygame
import time
from pathlib import Path

folder_maker = Path("C:\\Users\\Public\\Documents\\mp3_songs").mkdir(exist_ok=True)

# folder path
folder_path = Path("C:\\Users\\Public\\Documents\\mp3_songs")
print("all music playlists you want to listen too should be put into the documents folder path is C:\\Users\\Public\\Documents")
# list only directories
subfolders = [f.name for f in folder_path.iterdir() if f.is_dir()]

print("playlists", subfolders)

folderinput = input("what playlist:")

# mp3 folder
folder_files_path = ("C:\\Users\\Public\\Documents\\mp3_songs" + "\\" + folderinput)

# start pygame
pygame.mixer.init()
pygame.init()

# Get mp3 files
mp3_files = [f for f in os.listdir(folder_files_path) if f.endswith(".mp3")]

# Play files
for file in mp3_files:
    file_path = os.path.join(folder_files_path, file)

    print(f"Now playing: {file}")

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print("Controls: 'p' = Pause | 's' = Unpause | 'e' = Skip")

    while True:
        # This waits for you to type and hit Enter
        choice = input("Enter command: ").lower()

        if choice == 'p':
            pygame.mixer.music.pause()
            print("Music paused.")
        elif choice == 's':
            pygame.mixer.music.unpause()
            print("Music playing.")
        elif choice == 'e':
            pygame.mixer.music.stop()
            break
        else:
            print("Invalid input, try again.")
# end
print("Done playing all songs please get more songs")