from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import re
from bs4 import BeautifulSoup
import requests
import json
import httplib2
import urllib.request

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"\\chromedriver.exe"
# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("https://www.google.com")
url ='https://jntuaresults.ac.in/view-results-56736241.html'
rollno = '163G1A0505'
driver.get(url)
field = driver.find_element_by_xpath('/html/body/div/div[1]/div/div/center/table/tbody/tr/th/center/input[1]')
btn = driver.find_element_by_xpath('/html/body/div/div[1]/div/div/center/table/tbody/tr/th/center/input[2]')
field.send_keys(rollno)
btn.click()
print('btn clicked')
# pr_btn = browser.find_element_by_xpath('/html/body/div/div[1]/div/div/center/div[1]/table/tbody/tr[5]/th/input')
# pr_btn.click()
print(driver.current_url)
driver.get_screenshot_as_file("capture.png")
driver.close()
src=requests.get(driver.current_url)
# print(src.text())
# soup = BeautifulSoup(src, 'lxml')
# print(soup.name())

# table = soup.find('table', {'class': 'ui table segment'})
# capture the screen