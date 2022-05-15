from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime
from pyvirtualdisplay import Display

today = datetime.today()

today = today.strftime("%d%m%Y")

email = "harendra"+today+"@gmail.com"
password = today
print(email)
print(password)
def createAccount(): 
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_extension('./extension_1_6_0_0.crx')
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.get('https://hackeradda.com.com/testing')
    sleep(200)
    exit()
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/form/div[2]/input").send_keys(email)
    sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/form/div[3]/input").send_keys(password)
    sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/form/div[6]/button").click()
    sleep(30)
    driver.close()

with Display(visible=False, size=(1200, 1500)):
    createAccount()