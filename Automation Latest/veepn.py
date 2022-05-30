# 873a1cb1e1fd6b2cbe4008440ba71eb6
# pip3 install requests-random-user-agent logdna
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import random
from datetime import datetime
from selenium.webdriver.common.by import By
from sys import platform
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import socket

def saveVisit(formdata):
    url = 'http://129.154.237.40/'
    website = requests.post(url, data=formdata)
    output = website.text
    return output

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
agents = getUserAgents()

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

def readStory(story, driver, location = ' - '):
    start = datetime.now()
    driver.get(story)
    closeExtraTabs(driver)
    title = driver.title
    print(title)
    time.sleep(random.randint(30,40))
    y = 0
    height = driver.execute_script("return document.body.scrollHeight")
    while height > y:
        y = int(y) + random.randint(160,200)
        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        time.sleep(3)

    time.sleep(random.randint(20,30))
    links = getAllLinks(driver)
    link = random.choice(links)
    driver.execute_script("arguments[0].click();", link)
    time.sleep(random.randint(20,30))
    time_taken = str(datetime.now() - start)
    print("Time Taken: "+time_taken)
    location = location.split(" - ")[1]
    system = socket.gethostname()
    formdata = {
        "system_name":system,
        "url":story,
        "title":title,
        "time": time_taken,
        "location" : location,
        "vpn_name" : "Veepn",
        "meta_data" : ""
    }
    print(formdata)
    saveVisit(formdata)
    time.sleep(10)

while True:
    today = datetime.today()
    today = today.strftime("%d%m%Y")
    email_no = random.choice([1,2,3,4,5])
    email = "harendra"+today+str(email_no)+"@gmail.com"
    password = "harendra21@HK"


    try:
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
        driver.switch_to.default_content()
        driver.get('chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html')

        
        if random.randint(1,2) == 1:
            driver.set_window_size(random.randint(425, 1366), random.randint(700, 800))
            driver.set_window_position(random.randint(0, 800), 0, windowHandle='current')
        
        time.sleep(6)
        closeExtraTabs(driver)
        time.sleep(2)

        clickElem(By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]/div/div/button", driver)
        time.sleep(0.5)

        clickElem(By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]/div/div/button",driver)
        time.sleep(0.5)

        # Login

        clickElem(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/button",driver)
        time.sleep(0.5)

        clickElem(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/button",driver)
        time.sleep(0.5)

        driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[3]/form/div[3]/div/div/input").send_keys(email)
        time.sleep(0.5)

        driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[3]/form/div[4]/div/div/input").send_keys(password)
        time.sleep(1)

        clickElem(By.XPATH, "/html/body/div/div/div/div[2]/div[3]/form/button",driver)
        time.sleep(5)

        # select region
        clickElem(By.XPATH, "/html/body/div/div/div/div[3]/div[3]/div/div[1]",driver)
        time.sleep(2)

        collapse = [2, 8, 18, 20, 23, 27, 28, 41, 43, 47, 53, 55, 56]

        # randomRegion = random.randint(1, 56) # for all regions
        # randomRegion = random.choice([2, 3, 5, 8, 14, 16, 17, 43, 53, 55])
        
        randomRegion = random.choice([2, 8, 55, 53, 18, 49, 34])
        # randomRegion = random.choice([53])

        if randomRegion in collapse:
            
            clickElem(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div['+str(randomRegion)+']',driver)
            time.sleep(1)
            sub = {2: 5, 8: 3, 18: 3, 20: 5, 23: 3, 27: 3, 28: 3, 41: 7, 43: 3, 47: 2, 53: 3, 55: 12, 56: 2}
            subregion = str(random.randint(1,sub.get(randomRegion)))
            clickElem(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div['+str(randomRegion)+']/div[2]/div/div['+subregion+']',driver)
        else:
            clickElem(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div['+str(randomRegion)+']',driver)
    
        
        clickElem(By.XPATH, "/html/body/div/div/div/div[3]/div[1]/div/div/span",driver)
        time.sleep(8)
        
        retry = 0
        isConnected = False
        while isConnected == False:
            if retry > 10:
                # print("VPN is not connecting")
                print("VPN is not connecting")
                driver.quit()
                time.sleep(4)
                os.system("python3 veepn.py")
            else:    
                element = driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div[1]/div/div/div")
                text = element.get_attribute('innerText')
                # print(text)
                if text == 'VPN is ON':
                    isConnected = True
                if text == 'VPN is OFF':
                    print("VPN is OFF")
                    driver.quit()
                    time.sleep(4)
                    os.system("python3 veepn.py")
                time.sleep(2)
                retry = retry + 1
        
        time.sleep(2)
        ele = driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div[3]/div/div[1]/div/div[2]")
        location = ele.get_attribute('innerText')
        location = location.replace('\n', ' - ')
        
        print('Location: ' + location)
        
        readStory(random.choice(posts), driver,location)
        readStory(random.choice(posts), driver,location)
        if random.randint(1,2) == 1:
            readStory(random.choice(posts), driver,location)
        print("=======================================")
        driver.quit()
    except Exception as e:
        print(str(e))
        driver.quit()
        time.sleep(4)
        if platform == "linux" or platform == "linux2":
            os.system('python3 veepn.py')
        else:
            os.system('python veepn.py')
