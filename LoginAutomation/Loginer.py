from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Edge(executable_path = 'E:\\edgedriver\\msedgedriver.exe')
def facebook():
    WebDriverWait(driver, 10)
    driver.get("https://facebook.com")
    driver.find_element_by_name("email").send_keys("moory.ranjith@gmail.com")
    driver.find_element_by_name("pass").send_keys("163g1a0548"+Keys.ENTER)
    return "facebook as loged in"

def twitter():
    WebDriverWait(driver, 10)
    driver.get("https://twitter.com/login")
    WebDriverWait(driver, 20)
    driver.find_element_by_name("session[username_or_email]").send_keys("moory.ranjith@gmail.com")
    driver.find_element_by_name("session[password]").send_keys("Ranjith1@"+Keys.ENTER)
    return "twitter as loged in"
twitter()