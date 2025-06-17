from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pygame
import datetime

pygame.mixer.init()
pygame.mixer.music.load("notification_sound.mp3")

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)

pokemon_calendar = "https://www.target.com/p/2025-pok-233-mon-trading-card-game-holiday-calendar/-/A-94636863?afid=Mavely&cpng=&lnm=81938&ref=tgt_adv_xasd0002&clkid=8985bc2eN40d511f0a9549f724edc96ad"
pokemon_calendar_xpath = '//*[@id="above-the-fold-information"]/div[7]/div/div[1]/div/div/div/div'

alertMsg = "IN STOCK"

driver.get(pokemon_calendar)
time.sleep(5)

def find_element(xpath):
    out_of_stock_page = driver.find_element(By.XPATH, xpath)
    return (out_of_stock_page.text)

previous_content = find_element(pokemon_calendar_xpath)

while True:
    driver.refresh()
    time.sleep(0.01)
    current_content = find_element(pokemon_calendar_xpath)
    if current_content != previous_content:
        pygame.mixer.music.play()
        print(f"{datetime.now()}: {alertMsg} --{current_content}")
        last_content = current_content
    else:
        continue

time.sleep(5)

driver.quit()