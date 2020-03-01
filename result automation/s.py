from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

from rea_automation import getRes_a

rollno = '163G1A0505'
browser = webdriver.Chrome()
# browser = webdriver.PhantomJS()
url ='https://jntuaresults.ac.in/view-results-56736241.html'
browser.get(url)
field = browser.find_element_by_xpath('/html/body/div/div[1]/div/div/center/table/tbody/tr/th/center/input[1]')
btn = browser.find_element_by_xpath('/html/body/div/div[1]/div/div/center/table/tbody/tr/th/center/input[2]')
field.send_keys(rollno)
btn.click()
print('btn clicked')
# pr_btn = browser.find_element_by_xpath('/html/body/div/div[1]/div/div/center/div[1]/table/tbody/tr[5]/th/input')
# pr_btn.click()
print(browser.title)
