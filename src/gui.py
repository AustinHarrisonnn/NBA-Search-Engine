import tkinter as tk
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
root.title("NBA Player Stats Search")

player_name_label = tk.Label(root, text="Enter Player's Name:")
player_name_label.pack()

player_name_entry = tk.Entry(root)
player_name_entry.pack()

search_button = tk.Button(root, text="Search", command=search_player_stats)
search_button.pack()

result_label = tk.Label(root, text="Player stats will be displayed here.")
result_label.pack()

root.mainloop()