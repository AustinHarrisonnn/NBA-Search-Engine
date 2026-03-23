# NBA Search Engine
![app image](https://github.com/AustinHarrisonnn/NBA-Search-Engine/blob/main/pic.PNG?raw=true)
## Overview
This project uses selenium and python to scrape the NBA's official website for players live stats, specifically points, rebounds, and assists. 

---

## What it does
Type in a current NBA player's name, hit search, and the application scrapes NBA.com to retrieve real time player statistics of their current averages.
- **PPG** – Points per game
- **RPG** – Rebounds per game
- **APG** – Assists per game

---

## How it works
The app is built in Python using 3 components
- **`gui.py`** – The desktop interface built with Tkinter. Handles user input, displays results, and runs the scraper in a background thread so the UI stays responsive.
- **`nba_scraper.py`** – Uses Selenium to launch a headless Chrome browser, navigate to NBA.com, search for the player, and extract their stats.
- **`main.py`** – Entry point that launches the GUI.

---
 
## Requirements
 
- Python 3.x
- Google Chrome installed
- The following Python packages:
 
```bash
pip install selenium pillow webdriver-manager
```
 
---
 
## How to Run
 
```bash
python main.py
```
 
Then type a player's name in the search box and click **Search**.
 
---
