from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = r"C:\Users\ausgood\Desktop\NBATrack\src\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://www.nba.com/players')

player_name = input("Enter the player's name: ")

# Wait for the search box to appear and interact with it
wait = WebDriverWait(driver, 15)
search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search Players"]')))
search_box.send_keys(player_name)

# Optionally, hit 'Enter' to initiate search
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load and click the player's link
wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '{player_name.lower().replace(' ', '-')}/')]")))
player_link = driver.find_element(By.XPATH, f"//a[contains(@href, '{player_name.lower().replace(' ', '-')}/')]")
player_link.click()

# Wait for the player page to load
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "PlayerSummary_playerStatValue___EDg_")))

# Extract PPG, Rebounds, and Assists
stat_elements = driver.find_elements(By.CLASS_NAME, "PlayerSummary_playerStatValue___EDg_")

if len(stat_elements) >= 3:
    ppg = stat_elements[0].text  # Points per game (PPG)
    rebounds = stat_elements[1].text  # Rebounds
    assists = stat_elements[2].text  # Assists

    print(f"{player_name} PPG: {ppg}, Rebounds: {rebounds}, Assists: {assists}")
else:
    print("Couldn't extract the stats. The page structure might have changed.")

# Wait for a few seconds to see the result
time.sleep(3)

# Close the browser
driver.quit()

