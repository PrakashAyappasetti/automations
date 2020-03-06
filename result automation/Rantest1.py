import re
from bs4 import BeautifulSoup
import requests
import json
import httplib2
import urllib.request
from selenium import webdriver

url = 'https://jntuaresults.ac.in/'

try:
    src = requests.get('https://jntuaresults.ac.in/').text
except:
    print('no internet')
    exit()

soup = BeautifulSoup(src, 'lxml')

table = soup.find('table', {'class': 'ui table segment'})


l = ""
def getRes_a(value1, value2):
    # geturl = ""
    for row in soup.findAll("a", href=True):
        if value1 in row.text:
            # print(row.text)
            h = row['href']
            geturl = f'{url}{h}'
            print(f'{row.text} : {geturl}')
            if value2 in row.text:
                return geturl
        else :
            return "result not found or has been deleted by Admin"




l=getRes_a("B.Tech III Year I Semester (R15) ", "June/July 2019")
print(l)

rollno = '163G1A0505'
browser = webdriver.Chrome()
# browser = webdriver.PhantomJS()
print(l)
browser.get(l)
field = browser.find_element_by_xpath(
        '/html/body/div/div[1]/div/div/center/table/tbody/tr/th/center/input[1]')
btn = browser.find_element_by_xpath(
        '/html/body/div/div[1]/div/div/center/table/tbody/tr/th/center/input[2]')
field.send_keys(rollno)
btn.click()
print('btn clicked')
    # pr_btn = browser.find_element_by_xpath('/html/body/div/div[1]/div/div/center/div[1]/table/tbody/tr[5]/th/input')
    # pr_btn.click()
    # print(browser.title)
    # browser.stop_client()