from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime
from pyvirtualdisplay import Display
import random
def createAccount(email,password): 
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_extension('./extension_1_6_0_0.crx')
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.get('https://veepn.com/registration/')
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/form/div[2]/input").send_keys(email)
    sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/form/div[3]/input").send_keys(password)
    sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/form/div[6]/button").click()
    sleep(10)
    driver.close()

with Display(visible=True, size=(1200, 1500)):

    today = datetime.today().strftime("%d%m%Y")
    password = "harendra21@HK"
    email = "harendra"+today+"1@gmail.com"

    for i in range(1,6):
        email = "harendra"+today+str(i)+"@gmail.com"
        createAccount(email,password)
        sleep(5)
