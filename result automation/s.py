from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from rea_automation import getRes_a


print(getRes_a())

# driver = webdriver.PhantomJS()
driver = webdriver.Chrome('chromedriver')
print(driver)
