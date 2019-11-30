from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome(executable_path="/Users/alexpatapan/coding/Python/chromedriver")

while True:
    company = input('What company would you like to check the listing of? ')

    if (company == "quit"):
        browser.quit()
        exit()

    url = 'https://www.asx.com.au/asx/share-price-research/company/'+company

    browser.get(url)

    try: 
        price_element = browser.find_elements_by_xpath("//*[@id=\"information-column\"]/div[4]/div[1]/div[1]/company-summary/table/tbody/tr[1]/td[1]/span")
        name_element = browser.find_elements_by_xpath("//*[@id=\"company-name-title\"]")

        print(name_element[0].text, 'has current share price of $' + price_element[0].text)

        url = 'https://www.google.com/search?q=' + name_element[0].text.replace(" ","+")
        browser.get(url)

    #try:
        info = browser.find_elements_by_xpath("/html/body/div[7]/div[3]/div[10]/div[1]/div[3]/div/div[1]/div[1]/span/div/div/div[3]/div/div[1]/div/div/div/div/span[1]")

        print(info[0].text)
    except: 
     #   pass
        print("Sorry, there was an issue retrieving this info")
