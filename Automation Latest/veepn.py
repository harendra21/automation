# 873a1cb1e1fd6b2cbe4008440ba71eb6
# pip3 install requests-random-user-agent logdna
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import random
from datetime import datetime
import json
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import requests
import requests_random_user_agent
import logging
import sys
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import socket
from sentry_sdk import set_tag
from sys import platform
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sentry_sdk.init(
    # "https://d096b23f59334172b63d968435501637@o514513.ingest.sentry.io/5617820",
    # traces_sample_rate=1.0
)

sys.tracebacklimit=0
# time.sleep(random.randint(0,10))

vDisplay = False
vDisplayVisible = False

def getPosts():
    with open("./files/posts.txt") as file_in:
        posts = []
        for url in file_in:
            post = url.replace('\n','')
            posts.append(post)
        return posts

def getUserAgents():
    with open("./files/userAgents.txt") as file_in:
        userAgents = []
        for name in file_in:
            agent = name.replace('\n','')
            userAgents.append(agent)
        return userAgents

posts = getPosts()

print(len(posts))

agents = getUserAgents()

def errorLog(err):
    err = err.replace('\n','')
    err = err.replace('\t','')
    err = err.replace('(Session info: chrome=101.0.4951.64)','')
    err = err.split("Stacktrace:",1)[0]
    set_tag("hostname", socket.gethostname())
    logging.error(err)

def closeExtraTabs(driver):
    tab_list = driver.window_handles
    if len(tab_list) > 1:
        tabs = len(tab_list)
        while tabs > 1:
            tabs = tabs - 1
            driver.switch_to.window(tab_list[tabs])
            driver.close()
            driver.switch_to.window(tab_list[tabs - 1])

def clickElem(by,selector,driver):
    elem = WebDriverWait(driver, 1).until(EC.presence_of_element_located((by, selector)))
    # elem = driver.find_element(by, selector)
    driver.execute_script("arguments[0].click();", elem)

def getAllLinks(driver):
    links = []
    elems = driver.find_elements(By.XPATH,"//a[@href]")
    for elem in elems:
        url = elem.get_attribute("href")
        host = url.split("//")[-1].split("/")[0].split('?')[0]
        if host == "hackeradda.com" or host == "codingblog.online":
            links.append(elem)
    return links

def readStory(story, driver, count):
    start = datetime.now()
    driver.get(story)
    closeExtraTabs(driver)
    print(driver.title)
    time.sleep(random.randint(5,6))
    
    time.sleep(random.randint(20,30))
    y = 0
    height = driver.execute_script("return document.body.scrollHeight")
    while height > y:
        y = int(y) + random.randint(160,200)
        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        time.sleep(2)

    time.sleep(random.randint(10,15))
    links = getAllLinks(driver)
    link = random.choice(links)
    driver.execute_script("arguments[0].click();", link)
    time.sleep(random.randint(10,15))
    print("Time Taken: "+str(datetime.now() - start))


while True:
    if vDisplay:
        display = Display(visible=vDisplayVisible, size=(random.randint(320, 1920), random.randint(700, 750)))
        display.start()

    today = datetime.today()
    today = today.strftime("%d%m%Y")

    email_no = random.choice(['',1,2])
    email = "harendra"+today+str(email_no)+"@gmail.com"
    if email_no == 1 or email_no == 2:
        password = "harendra21@HK"
    else:
        password = today

    try:
        # sess = requests.Session()
        # ua = sess.headers['User-Agent']
        ua = random.choice(agents)
        options = Options()

        
        options.add_extension('./files/veepn.crx')
        options.add_argument(f'user-agent={ua}')
        options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--disable-gpu")
        options.add_argument('--start-maximized')
        # options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("disable-infobars")
        

        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"
        driver = webdriver.Chrome(desired_capabilities=caps, options=options)
        driver.set_page_load_timeout(150)
        driver.get('chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html')
        if random.randint(1,2) == 1:
            driver.set_window_size(random.randint(425, 1366), random.randint(700, 800))
            driver.set_window_position(random.randint(0, 800), 0, windowHandle='current')
        
        time.sleep(6)
        closeExtraTabs(driver)
        time.sleep(2)



        clickElem(By.CSS_SELECTOR, "#screen-tooltips-template > div.navigation > div > div:nth-child(3) > div > div > button", driver)
        time.sleep(1)

        clickElem(By.CSS_SELECTOR, "#screen-tooltips-template > div.navigation > div > div:nth-child(3) > div > div > button",driver)
        time.sleep(1)

        # Login

        clickElem(By.CSS_SELECTOR, "#hamburger",driver)
        
        time.sleep(1)
        clickElem(By.CSS_SELECTOR, "#menuContainer > div.container > div.menu-content-wrapper > button",driver)
        
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#menuContainer > div.fullScreen.menuLogin > form > div:nth-child(3) > div > div > input[type=text]").send_keys(email)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#menuContainer > div.fullScreen.menuLogin > form > div:nth-child(4) > div > div > input[type=password]").send_keys(password)
        time.sleep(3)
        clickElem(By.CSS_SELECTOR, "#submit-form-button",driver)
        
        time.sleep(5)
        # select region
        clickElem(By.CSS_SELECTOR, "#content > div.current-region > div > div.current-region-upper-block",driver)
        time.sleep(2)
        collapse = [2, 8, 18, 20, 23, 27, 28, 41, 43, 47, 53, 55, 56]

        # randomRegion = random.randint(1, 56) # for all regions
        # randomRegion = random.choice([2, 3, 5, 8, 14, 16, 17, 43, 53, 55])
        
        # randomRegion = random.choice([2, 8, 55, 53, 18, 49, 34])
        randomRegion = random.choice([2, 8, 53, 18, 49, 34])
        if randomRegion in collapse:
            
            clickElem(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div['+str(randomRegion)+']',driver)
            time.sleep(1)
            sub = {2: 5, 8: 3, 18: 3, 20: 5, 23: 3, 27: 3, 28: 3, 41: 7, 43: 3, 47: 2, 53: 3, 55: 12, 56: 2}
            subregion = str(random.randint(1,sub.get(randomRegion)))
            clickElem(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div['+str(randomRegion)+']/div[2]/div/div['+subregion+']',driver)
        else:
            clickElem(By.XPATH, '//*[@id="region-list"]/div['+str(randomRegion)+']',driver)
    
        time.sleep(2)
        clickElem(By.CSS_SELECTOR, "#mainBtn > span",driver)
        time.sleep(8)
        retry = 0
        isConnected = False
        while isConnected == False:
            if retry > 10:
                # print("VPN is not connecting")
                logging.info("VPN is not connecting")
                driver.quit()
                time.sleep(4)
                os.system("python3 veepn.py")
            else:    
                element = driver.find_element( By.CSS_SELECTOR, "#mainBtn > div")
                text = element.get_attribute('innerText')
                # print(text)
                if text == 'VPN is ON':
                    isConnected = True
                if text == 'VPN is OFF':
                    logging.info("VPN is OFF")
                    driver.quit()
                    time.sleep(4)
                    os.system("python3 veepn.py")
                time.sleep(2)
                retry = retry + 1
        
        time.sleep(2)
        ele = driver.find_element(By.CSS_SELECTOR, "#content > div.current-region > div > div.current-region-upper-block > div > div.current-region-name-wrapper")
        location = ele.get_attribute('innerText')
        
        print('Location: ' + location.replace('\n', ' - '))
        driver.switch_to.default_content()
        readStory(random.choice(posts), driver,1)
        readStory(random.choice(posts), driver,2)
        if random.randint(1,2) == 1:
            readStory(random.choice(posts), driver,3)
        print("=======================================")
        driver.quit()
        if vDisplay:
            display.stop()
    except Exception as e:
        errorLog(str(e))
        driver.quit()
        if vDisplay:
            display.stop()
        time.sleep(4)
        if platform == "linux" or platform == "linux2":
            os.system('python3 veepn.py')
        elif platform == "win32":
            os.system('python veepn.py')
