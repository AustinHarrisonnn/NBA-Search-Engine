from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def get_player_stats(player_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_driver_path = r"C:\Users\ausgood\Desktop\NBATrack\src\chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get('https://www.nba.com/players')
    wait = WebDriverWait(driver, 15)
    
    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search Players"]')))
    search_box.send_keys(player_name)
    search_box.send_keys(Keys.RETURN)

    try:
        player_name_formatted = player_name.lower().replace(" ", "-")
        player_xpath = f"//a[contains(@href, '{player_name_formatted}/')]"
        
        player_link = wait.until(EC.element_to_be_clickable((By.XPATH, player_xpath)))
        player_link.click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "PlayerSummary_playerStatValue___EDg_")))
        stat_elements = driver.find_elements(By.CLASS_NAME, "PlayerSummary_playerStatValue___EDg_")
        
        if len(stat_elements) >= 3:
            ppg = stat_elements[0].text  
            rpg = stat_elements[1].text  
            apg = stat_elements[2].text 

            return ppg, rpg, apg
        else:
            print(f"Couldn't extract stats for {player_name}. The page structure might have changed.")
            return None, None, None

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None
    finally:
        driver.quit()