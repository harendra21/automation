# pip3 install requests-random-user-agent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import random
from datetime import datetime
import json
from selenium.webdriver.common.by import By
import http.client as httplib
from pyvirtualdisplay import Display
import urllib.request as urllib2
import requests
import requests_random_user_agent

# time.sleep(random.randint(0,10))

vDisplay = False
vDisplayVisible = False


postsData = open('./posts.json')
posts = json.load(postsData)['posts']
# data = open('./userAgents.json')
# agents = json.load(data)['agents']

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
    elem = driver.find_element(by, selector)
    driver.execute_script("arguments[0].click();", elem)

def readStory(story, driver, count):
    start = datetime.now()
    if count > 1:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[count -1])

    driver.get(story)
    
    if count == 1:
        closeExtraTabs(driver)
    print(driver.title)
    y = 0
    height = driver.execute_script("return document.body.scrollHeight")
    while height > y:
        y = int(y) + random.randint(160,200)
        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        time.sleep(2)

    time.sleep(random.randint(20,30))
    print("Time Taken: "+str(datetime.now() - start))



try:
    while True:
        if vDisplay:
            display = Display(visible=vDisplayVisible, size=(random.randint(320, 1920), random.randint(700, 750)))
            display.start()

        today = datetime.today()
        today = today.strftime("%d%m%Y")
        email = "harendra"+today+"@gmail.com"
        password = today

        try:
            options = Options()
            sess = requests.Session()
            ua = sess.headers['User-Agent']
            options.add_argument(f'user-agent={ua}')
            options.add_extension('./veepn.crx')
            options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("--autoplay-policy=no-user-gesture-required")
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(options=options)
            driver.set_page_load_timeout(90)
            driver.get('chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html')
            if random.randint(1,2) == 1:
                driver.set_window_size(random.randint(425, 1366), random.randint(700, 800))
                driver.set_window_position(random.randint(0, 800), 0, windowHandle='current')
            
            time.sleep(6)
            closeExtraTabs(driver)
            time.sleep(1)


            clickElem(By.CSS_SELECTOR, "#screen-tooltips-template > div.navigation > div > div:nth-child(3) > div > div > button", driver)
            time.sleep(0.5)

            clickElem(By.CSS_SELECTOR, "#screen-tooltips-template > div.navigation > div > div:nth-child(3) > div > div > button",driver)
            time.sleep(1)

            # Login

            clickElem(By.CSS_SELECTOR, "#hamburger",driver)
            
            time.sleep(1)
            clickElem(By.CSS_SELECTOR, "#menuContainer > div.container > div.menu-content-wrapper > button",driver)
            
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "#menuContainer > div.fullScreen.menuLogin > form > div:nth-child(3) > div > div > input[type=text]").send_keys(email)
            driver.find_element(By.CSS_SELECTOR, "#menuContainer > div.fullScreen.menuLogin > form > div:nth-child(4) > div > div > input[type=password]").send_keys(password)

            clickElem(By.CSS_SELECTOR, "#submit-form-button",driver)
            
            time.sleep(5)
            # select region
            clickElem(By.CSS_SELECTOR, "#content > div.current-region > div > div.current-region-upper-block",driver)
            time.sleep(2)
            collapse = [2, 8, 18, 20, 23, 27, 28, 41, 43, 47, 53, 55, 56]

            # randomRegion = random.randint(1, 56) # for all regions
            # randomRegion = random.choice([2, 3, 5, 8, 14, 16, 17, 43, 53, 55])
            
            randomRegion = random.choice([2, 8, 55, 53, 18, 49, 34])
            if randomRegion in collapse:
                
                clickElem(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div['+str(randomRegion)+']',driver)
                time.sleep(1)
                sub = {2: 5, 8: 3, 18: 3, 20: 5, 23: 3, 27: 3, 28: 3, 41: 7, 43: 3, 47: 2, 53: 3, 55: 12, 56: 2}
                subregion = str(random.randint(1,sub.get(randomRegion)))
                clickElem(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div['+str(randomRegion)+']/div[2]/div/div['+subregion+']',driver)
            else:
               clickElem(By.XPATH, '//*[@id="region-list"]/div['+str(randomRegion)+']',driver)
        
            time.sleep(1)
            clickElem(By.CSS_SELECTOR, "#mainBtn > span",driver)
            time.sleep(6)
            retry = 0
            isConnected = False
            while isConnected == False:
                if retry > 10:
                    print("VPN is not connecting")
                    driver.quit()
                    os.system("python3 veepn.py")
                else:    
                    element = driver.find_element( By.CSS_SELECTOR, "#mainBtn > div")
                    text = element.get_attribute('innerText')
                    # print(text)
                    if text == 'VPN is ON':
                        isConnected = True
                    if text == 'VPN is OFF':
                        driver.quit()
                    time.sleep(2)
                    retry = retry + 1
            ele = driver.find_element(By.CSS_SELECTOR, "#content > div.current-region > div > div.current-region-upper-block > div > div.current-region-name-wrapper")
            location = ele.get_attribute('innerText')
            print('Location: ' + location)
            
            readStory(random.choice(posts), driver,1)
            readStory(random.choice(posts), driver,2)
            if random.randint(1,2) == 1:
                readStory(random.choice(posts), driver,3)
            print("=======================================")
            driver.quit()
            if vDisplay:
                display.stop()
        except:
            print("Something went wrong!. Trying again......")
            driver.quit()
            if vDisplay:
                display.stop()
            os.system("python3 veepn.py")
except:
    print("Oops!  Something went wrong!. Trying again.")
    os.system("python3 veepn.py")
