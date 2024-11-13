import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from nba_scraper import get_player_stats

def search_player_stats():
    player_name = player_name_entry.get()
    if player_name:
        ppg, rpg, apg = get_player_stats(player_name)
        if ppg:
            result_label.config(text=f"{player_name} - PPG: {ppg}, RPG: {rpg}, APG: {apg}")
        else:
            result_label.config(text="Player not found or stats not available.")
    else:
        result_label.config(text="Please enter a player's name.")


root = tk.Tk()
root.geometry('600x400')
root.title("NBA Player Stats Search")

image = Image.open(r'C:\Users\ausgood\Desktop\NBATrack\src\assets\basketballIMG.png')
image = image.resize((130, 100), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=image)
image_label.image = image  # Prevent garbage collection
image_label.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

player_name_label = tk.Label(root, text="Enter Player's Name:")
player_name_label.grid(row=0, column=1, sticky='w')

player_name_entry = tk.Entry(root)
player_name_entry.grid(row=0, column=2, padx=5, pady=5, sticky='ew')

search_button = tk.Button(root, text="Search", command=search_player_stats)
search_button.grid(row=0, column=3, padx=10, pady=5, sticky='e')

root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

result_label = tk.Label(root, text="Player stats will be displayed here.")
result_label.grid(row=1, column=0, columnspan=4, pady=30)

root.mainloop()