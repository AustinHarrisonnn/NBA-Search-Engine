from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_player_stats(player_name):
    chrome_driver_path = r"C:\Users\ausgood\Desktop\NBATrack\src\chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.nba.com/players')

    wait = WebDriverWait(driver, 15)
    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search Players"]')))
    search_box.send_keys(player_name)
    search_box.send_keys(Keys.RETURN)

    try:
        player_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, player_name)))
        player_link.click()

        time.sleep(3)

        ppg = driver.find_element(By.CLASS_NAME, "PlayerSummary_playerStatValue___EDg_").text
        rpg = driver.find_elements(By.CLASS_NAME, "PlayerSummary_playerStatValue___EDg_")[1].text
        apg = driver.find_elements(By.CLASS_NAME, "PlayerSummary_playerStatValue___EDg_")[2].text

        return ppg, rpg, apg
    except Exception as e:
        return None, None, None
    finally:
        driver.quit()
