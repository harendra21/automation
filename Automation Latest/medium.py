from selenium import webdriver
import time
import random
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sys import platform
from selenium.webdriver.common.by import By
import requests
import socket

def saveVisit(formdata):
    url = 'http://129.154.237.40/'
    website = requests.post(url, data=formdata)
    output = website.text
    return output


# time.sleep(random.randint(4,8))

def getPosts():
    with open("./files/medium.txt") as file_in:
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

agents = getUserAgents()
posts = getPosts()

def clickElem(by,selector,driver):
    elem = driver.find_element(by, selector)
    driver.execute_script("arguments[0].click();", elem)

def closeExtraTabs(driver):
    tab_list = driver.window_handles
    if len(tab_list) > 1:
        driver.switch_to.window(tab_list[1])
        driver.close()
        driver.switch_to.window(tab_list[0])

def getAllLinks(driver):
    links = []
    elems = driver.find_elements(By.XPATH,"//a[@href]")
    for elem in elems:
        url = elem.get_attribute("href")
        host = url.split("//")[-1].split("/")[0].split('?')[0]
        if host == "hackeradda.com" or host == "codingblog.online":
            links.append(elem)
    return links


def visit():
    try:
        # ua = random.choice(agents)
        options = Options()
        options.add_extension('./files/ultra.crx')
        # options.add_argument(f'user-agent={ua}')
        options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--start-maximized')
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("--no-sandbox")
        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--disable-gpu")
        # options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("disable-infobars")

        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"
        driver = webdriver.Chrome(desired_capabilities=caps, options=options)
        driver.set_page_load_timeout(150)

        driver.set_window_size(random.randint(300, 1200), random.randint(500, 900))
        driver.set_window_position(random.randint(0, 800), 0, windowHandle='current')
        
        time.sleep(5)
        driver.execute_script("var images = document.getElementsByTagName('img');var l = images.length;for (var i = 0; i < l; i++) {images[0].parentNode.removeChild(images[0]);}")
        
        closeExtraTabs(driver)
        
        story = random.choice(posts)
        driver.get(story)
        closeExtraTabs(driver)
        title = driver.title
        print(title)
        y = 0

        if random.randint(1,4) == 1:
            height = random.randint(0,500)
        else:
            height = driver.execute_script("return document.body.scrollHeight")

        height = driver.execute_script("return document.body.scrollHeight")
        while height > y:
            y = int(y) + random.randint(60,200)
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            time.sleep(3)
        
        time.sleep(random.randint(50,100))


        print("=========================================")
        driver.quit()
    except Exception as e:
        driver.quit()
        print("Try Again....",str(e))

while True:
    visit()
    
