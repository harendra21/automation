from selenium import webdriver
import time
import random
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
import json


# time.sleep(random.randint(4,8))

postsData = open('./posts.json')
posts = json.load(postsData)['posts']
data = open('./userAgents.json')
user_agents = json.load(data)['agents']


def closeExtraTabs(driver):
    tab_list = driver.window_handles
    if len(tab_list) > 1:
        driver.switch_to.window(tab_list[1])
        driver.close()
        driver.switch_to.window(tab_list[0])

def visit():
    try:
        options = Options()
        

        options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--disable-gpu")
        options.add_argument('--start-maximized')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("disable-infobars")



        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": random.choice(user_agents)})
        driver.set_page_load_timeout(120)
        driver.set_window_size(random.randint(300, 1200), random.randint(500, 900))
        driver.set_window_position(random.randint(0, 800), 0, windowHandle='current')
        time.sleep(5)
        driver.execute_script("var images = document.getElementsByTagName('img');var l = images.length;for (var i = 0; i < l; i++) {images[0].parentNode.removeChild(images[0]);}")
        
        closeExtraTabs(driver)
        driver.get(random.choice(posts))
        closeExtraTabs(driver)
        print(driver.title)
        start = datetime.now()

        y = 0
        height = driver.execute_script("return document.body.scrollHeight")
        while height > y:
            y = int(y) + random.randint(160,200)
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            time.sleep(2)

        time.sleep(random.randint(5,10))
        driver.execute_script('window.location.href = "{}";'.format(random.choice(posts)))
        time.sleep(random.randint(5,10))
        print(driver.title)

        y = 0
        height = driver.execute_script("return document.body.scrollHeight")
        while height > y:
            y = int(y) + random.randint(160,200)
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            time.sleep(2)

        time.sleep(random.randint(10,25))

        print("Time Taken: "+str(datetime.now() - start))
        print("=========================================")
        driver.quit()
    except:
        driver.quit()
        print("Try Again....")
        os.system('python3 ultra.py')
while True:
    visit()
