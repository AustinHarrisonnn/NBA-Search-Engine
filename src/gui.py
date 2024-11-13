import tkinter as tk
from tkinter import messagebox
from nba_scraper import get_player_stats

def on_search_clicked():
    player_name = entry.get()
    if player_name:
        ppg, rpg, apg = get_player_stats(player_name)
        if ppg is None:
            messagebox.showerror("Error", "Could not fetch stats.")
        else:
            stats_label.config(text=f"PPG: {ppg}\nRebounds: {rebounds}\nAssists: {assists}")
    else:
        messagebox.showwarning("Input Error", "Please enter a player's name.")

root = tk.Tk()
root.title("NBA Player Stats")

entry_label = tk.Label(root, text="Enter Player Name:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="Search", command=on_search_button_click)
search_button.pack()

stats_label = tk.Label(root, text="Player stats will appear here")
stats_label.pack()

root.mainloop()