from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_player_stats(player_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        player_name_formatted = player_name.lower().replace(" ", "-")
        driver.get(f'https://www.nba.com/player-search?q={player_name.replace(" ", "+")}')
        
        wait = WebDriverWait(driver, 15)
        time.sleep(3)  

        try:
            player_xpath = f"//a[contains(@href, '{player_name_formatted}/')]"
            player_link = wait.until(EC.element_to_be_clickable((By.XPATH, player_xpath)))
            player_link.click()
        except:
            driver.get('https://www.nba.com/players')
            time.sleep(3)

            search_selectors = [
                'input[placeholder="Search Players"]',
                'input[type="search"]',
                'input[placeholder*="Search"]',
                'input[placeholder*="search"]',
                '.search-input input',
            ]
            
            search_box = None
            for selector in search_selectors:
                try:
                    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
                    break
                except:
                    continue
            
            if search_box:
                search_box.send_keys(player_name)
                time.sleep(2)
                player_link = wait.until(EC.element_to_be_clickable((By.XPATH, player_xpath)))
                player_link.click()
            else:
                print("Could not find search box.")
                return None, None, None

        time.sleep(3)
        stat_selectors = [
            "PlayerSummary_playerStatValue___EDg_",
            "PlayerSummary_playerStatValue__",
        ]

        stat_elements = []
        for selector in stat_selectors:
            stat_elements = driver.find_elements(By.CSS_SELECTOR, f"[class*='playerStatValue']")
            if stat_elements:
                break

        if len(stat_elements) >= 3:
            ppg = stat_elements[0].text
            rpg = stat_elements[1].text
            apg = stat_elements[2].text
            return ppg, rpg, apg
        else:
            print(f"Couldn't extract stats for {player_name}. Found {len(stat_elements)} stat elements.")
            return None, None, None

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None
    finally:
        driver.quit()