import re
from bs4 import BeautifulSoup
import requests
import json
import httplib2
import urllib.request


url='https://jntuaresults.ac.in/'

try:
    src = requests.get('https://jntuaresults.ac.in/').text
except:
    print('no internet')
    exit()
    
soup = BeautifulSoup(src, 'lxml')

table = soup.find('table', {'class': 'ui table segment'})


def listOfResultTitles():
    rows = list()
    for row in table.findAll("a"):
        rows.append(row.text)
    return rows

def listOfBtechResultTitles():
    rows = list()
    pattern = '^B.Tech.*'
    for row in table.findAll("a"):
        if re.match(pattern, row.text):
            rows.append(row.text)
    return rows

def lastResult():
    aa = table.find("a").text
    return aa


def isResult():
    pattern = '^B.Tech.*'
    test_string = lastResult()
    result = re.match(pattern, test_string)
    print(lastResult())
    if result:
        return True
    else:
        return False

def listOfBtechResultTitlesInJsonFormat():

    rows = {}
    pattern = '^B.Tech.*'
    c = 1
    for row in table.findAll("a"):
        if re.match(pattern, row.text):
            rows.update({c : row.text})
            # rows.append(row.text)
    return rows


def getRes_a():
    geturl=""
    for row in soup.findAll("a",href=True):
        if "B.Tech II Year I Semester (R15) Regular & Supplementary Examinations, Nov/Dec 2019" in row.text:
            geturl=url+row['href']


    return geturl


# B.Tech III Year I Semester (R15) Regular & Supplementary Examinations, Nov/Dec 2019


# lastResult()

# print(isResult())

# print(listOfBtechResultTitles())

# print(listOfBtechResultTitlesInJsonFormat())

