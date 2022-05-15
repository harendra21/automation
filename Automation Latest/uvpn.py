from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import random
import json
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display

postsData = open('./posts.json')
posts = json.load(postsData)['posts']

print(len(posts))

data = open('./userAgents.json')
agents = json.load(data)['agents']

def closeExtraTabs(driver):
    tab_list = driver.window_handles
    if len(tab_list) > 1:
        tabs = len(tab_list)
        while tabs > 1:
            tabs = tabs - 1
            driver.switch_to.window(tab_list[tabs])
            driver.close()
            driver.switch_to.window(tab_list[tabs - 1])


def readStory(story, driver):
    driver.get(story)
    print(driver.title)
    scheight = .01
    time.sleep(random.randint(10,15))
    while scheight < 1:
        rand_sec = random.randint(0, 20)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
        scheight += .002 * rand_sec
        time.sleep(0.2 * rand_sec)
    time.sleep(random.randint(10,15))


def connectUVPN(driver):
    driver.get('chrome-extension://jaoafpkngncfpfggjefnekilbkcpjdgp/popup/popup.html')
    time.sleep(6)
    closeExtraTabs(driver)

    time.sleep(2)   
    element = driver.find_element(By.XPATH,"/html/body/div/div/main/div[2]/a")
    driver.execute_script("arguments[0].click();", element)
    
    time.sleep(5)
    element = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

    location = random.randint(1,2)


    if location == 1:
        element = driver.find_element(By.XPATH,"/html/body/div/div/div/main/div[1]/ul/li[1]")
    elif location == 2:
        element = driver.find_element(By.XPATH,"/html/body/div/div/div/main/div[1]/ul/li[2]")
    
    driver.execute_script("arguments[0].click();", element)            
    time.sleep(4)

def connectVPNPro(driver):
    driver.get('chrome-extension://foiopecknacmiihiocgdjgbjokkpkohc/lib/select/popup.html')
    if random.randint(1,3) == 1:
        driver.set_window_size(random.randint(425, 1366), random.randint(700, 800))
        driver.set_window_position(random.randint(0, 800), 0, windowHandle='current')
    time.sleep(2)
    
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(2)

    
    element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)
    location = str(random.randint(2,12))
    element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/div["+location+"]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(20)

def connectWindscribe(driver):
    driver.get('chrome-extension://hnmpcagpplmpfojmgmnngilcnanddlhb/popup.html')
    # if random.randint(1,3) == 1:
    #     driver.set_window_size(random.randint(425, 1366), random.randint(700, 800))
    #     driver.set_window_position(random.randint(0, 800), 0, windowHandle='current')
    time.sleep(1)
    element = driver.find_element(By.XPATH,"/html/body/div/div/button[2]")
    driver.execute_script("arguments[0].click();", element)

    time.sleep(0.5)
    driver.find_element(By.XPATH,"/html/body/div/div/div/form/div[1]/div[2]/input").send_keys('harendra21')
    time.sleep(0.5)
    driver.find_element(By.XPATH,"/html/body/div/div/div/form/div[2]/div[2]/input").send_keys('harendra21@HK')

    time.sleep(0.5)
    element = driver.find_element(By.XPATH,"/html/body/div/div/div/form/div[3]/button")
    driver.execute_script("arguments[0].click();", element)

    time.sleep(3)
    element = driver.find_element(By.XPATH,"/html/body/div/div/button[2]")
    driver.execute_script("arguments[0].click();", element)


    time.sleep(0.5)
    element = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[2]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(0.5)
    element = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div/div[1]/div[1]/div/div[2]/div")
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(0.5)

    driver.execute_script("location.reload();")

    time.sleep(2)

    
    element = driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[1]/div/div[1]/div/div[2]/button/div/div[1]")
    driver.execute_script("arguments[0].click();", element)

    time.sleep(2)
        
    element = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]")
    driver.execute_script("arguments[0].click();", element)


    element = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]")
    driver.execute_script("arguments[0].click();", element)

    # /html/body/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]
    # /html/body/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]
    time.sleep(5)
    


    time.sleep(5)



vpn = random.randint(1,2)
vpn = 1
try:
    while True:
        display = Display(visible=1, size=(random.randint(320, 1920), random.randint(600, 750)))
        display.start()
        options = Options()
        ua = random.choice(agents)
        options.add_argument(f'user-agent={ua}')
        if vpn == 1:
            options.add_extension('./uvpn.crx')
        elif vpn == 2:
            options.add_extension('./windscribe.crx')
        else:
            options.add_extension('./vpnpro.crx')
        options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(150)

        try:
            if vpn == 1:
                connectUVPN(driver)
            elif vpn == 2:
                time.sleep(5)
                connectWindscribe(driver)
            else:
                connectVPNPro(driver)
            
            readStory(random.choice(posts), driver)
            if random.randint(1,2) == 1:
                readStory(random.choice(posts), driver)
            driver.quit()
            time.sleep(300)
        except:
            print("Something went wrong!.  Trying again......")
            driver.quit()
            display.stop()
            time.sleep(random.randint(4,8))
            os.system("python3 uvpn.py")
except:
    print("Oops!  Something went wrong!.  Trying again.")
    time.sleep(random.randint(4,8))
    os.system("python3 uvpn.py")
