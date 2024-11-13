import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from threading import Thread
from nba_scraper import get_player_stats

def search_player_stats():
    progress_bar.start()  # Start the progress bar animation
    result_label.config(text="Loading...")

    def scrape_and_display():
        player_name = player_name_entry.get()
        if player_name:
            ppg, rpg, apg = get_player_stats(player_name)
            if ppg:
                result_label.config(text=f"{player_name} - PPG: {ppg}, RPG: {rpg}, APG: {apg}")
            else:
                result_label.config(text="Player not found or stats not available.")
        else:
            result_label.config(text="Please enter a player's name.")
        progress_bar.stop()  # Stop the progress bar animation

    # Run the scraping function in a separate thread to prevent UI freezing
    Thread(target=scrape_and_display).start()


root = tk.Tk()
root.geometry('600x400')
root.title("NBA Player Stats Search")
root.config(bg="#000B58")

row0_frame = tk.Frame(root, bg="#003161")  # Set the background color for row 0
row0_frame.grid(row=0, column=0, columnspan=5, padx=20, pady=10, sticky='ew')

image = Image.open(r'C:\Users\ausgood\Desktop\NBATrack\src\assets\basketballIMG.png')
image = image.resize((130, 100), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

image_label = tk.Label(row0_frame, image=image, bg="#003161")
image_label.image = image  # Prevent garbage collection
image_label.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

player_name_label = tk.Label(row0_frame, text="Enter Player's Name:", bg="#003161", fg="white", font=("Helvetica", 12, "bold"))
player_name_label.grid(row=0, column=1, pady=37, sticky='n')

player_name_entry = tk.Entry(row0_frame)
player_name_entry.grid(row=0, column=2, padx=5, pady=40, sticky='n')

search_button = tk.Button(row0_frame, text="Search", font=("Helvetica", 11), command=search_player_stats, bg="#FFF4B7")
search_button.grid(row=0, column=3, padx=10, pady=35, sticky='ne')

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

progress_bar = ttk.Progressbar(root, mode='indeterminate')
progress_bar.grid(row=2, column=0, columnspan=4, padx=100, pady=10, sticky="ew")

result_label = tk.Label(root, text="Player stats will be displayed here.", font=("Helvetica", 12, "bold"), bg="#000B58", fg="white")
result_label.grid(row=1, column=0, columnspan=4, pady=30)

root.mainloop()