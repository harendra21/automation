from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import random
import json
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib.request , socket
from sys import platform

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')  
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print( "ERROR:", detail)
        return 1
    return 0

def getProxyList():
    with open("./files/http_proxies.txt") as file_in:
        lines = []
        for line in file_in:
            proxy = line.replace('\n','')
            lines.append(proxy)
        return lines

def get_free_proxies(driver):
    driver.get('https://sslproxies.org')

    table = driver.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            header = headers[i]
            header = header.replace(' ','_')
            proxy_data[header] = tds[i].text.strip()
        proxies.append(proxy_data)
    
    return proxies

def getPosts():
    with open("./files/posts.txt") as file_in:
        posts = []
        for url in file_in:
            post = url.replace('\n','')
            posts.append(post)
        return posts

def getUserAgents():
    data = open('./files/userAgents.json')
    return json.load(data)['agents']

def getWorkingProxy(proxies):
    return "151.22.181.213:8080"
    proxy = random.choice(proxies)
    print("Checking - ", proxy)
    if is_bad_proxy(proxy) == False:
        return proxy
    else:
        getWorkingProxy(proxies)

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
    print("Uvpn")
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
    print("Vpnpro")
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
    print("Windscribe")
    driver.get('chrome-extension://hnmpcagpplmpfojmgmnngilcnanddlhb/popup.html')
    # if random.randint(1,3) == 1:
    #     driver.set_window_size(random.randint(425, 1366), random.randint(700, 800))
    #     driver.set_window_position(random.randint(0, 800), 0, windowHandle='current')
    time.sleep(1)
    element = driver.find_element(By.XPATH,"/html/body/div/div/button[1]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(20)
    element = driver.find_element(By.XPATH,"/html/body/div/div/button[2]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)

    element = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[2]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)

    element = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div/div[1]/div[1]/div/div[2]/div/div")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

    element = driver.find_element(By.XPATH,"/html/body/div/div/div[1]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

    # time.sleep(1000)

    freeLocations = ['Atlanta,Mountain','Dallas,Ranch','Chicago,Cub','Miami,Vice','Miami,Snow','New York,Empire','Washington DC,Precedent','Los Angeles,Dogg','Seattle,Cobain','Montreal,Expo 67','Toronto,Comfort Zone','Toronto,The 6','Vancouver,Vansterdam','Vancouver,Granville','Paris,Jardin','Paris,Seine','Frankfurt,Castle','Frankfurt,Wiener','Amsterdam,Canal','Amsterdam,Red Light','Amsterdam,Tulip','Oslo,Fjord','Bucharest,No Vampires','Zurich,Alphorn','Zurich,Lindenhof','London,Custard','London,Crumpets','Istanbul,Ataturk','Hong Kong,Victoria']

    element = driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[1]/div/div[1]/div/div[2]/button")
    driver.execute_script("arguments[0].click();", element)

    time.sleep(2)

    locations = [2,3,4,6,7,18,19,30,32,35,39,40,52,57]

    # locations = [2,3,4]

    cols = {2:8,3:10,4:14,6:5,7:3,18:2,19:2,30:4,32:1,35:1,39:3,40:5,52:3,57:2}

    
    isOk = False
    while isOk == False:
        location = random.choice(locations)
        # print(location)
        # print(cols[location])
        time.sleep(2)
        elementDrop = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div["+str(location)+"]/div[1]")
        driver.execute_script("arguments[0].click();", elementDrop)

        time.sleep(1)
        xPath = "/html/body/div/div/div[2]/div/div/div["+str(location)+"]/div[2]/div["+str(random.randint(1, cols[location]))+"]/div/div[2]"
        element = driver.find_element(By.XPATH,xPath)
        time.sleep(1)

        locationName = element.text
        locationName = locationName.replace('\n',',')
        print(locationName)
        if locationName in freeLocations:
            element = driver.find_element(By.XPATH,xPath)
            isOk = True
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
        else:
            time.sleep(1)
            driver.execute_script("arguments[0].click();", elementDrop)
            print("Not a free location")
            time.sleep(1)
            

    time.sleep(10)

def connectZenmate(driver):
    print("Zenmate")
    driver.get('chrome-extension://fdcgdnkidjaadafnichfpabhfomcebme/index.html')
    time.sleep(6)
    closeExtraTabs(driver)
    time.sleep(1)

    element = driver.find_element(By.XPATH,"/html/body/app-root/main/app-onboarding/div/div[1]/div/img[1]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    
    element = driver.find_element(By.XPATH,"/html/body/app-root/main/app-home/div/div[2]/div[4]/div/a")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)

    element = driver.find_element(By.XPATH,"/html/body/app-root/main/app-servers/div/div[4]/mat-tab-group/div/mat-tab-body[1]/div/div/div[1]/app-servers-list/div["+str(random.randint(1, 4))+"]/p/span[1]")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)

def connectUltrasurf(driver):
    print("Ultrasurf")
    driver.execute_script("var images = document.getElementsByTagName('img');var l = images.length;for (var i = 0; i < l; i++) {images[0].parentNode.removeChild(images[0]);}")
    time.sleep(6)
    closeExtraTabs(driver)

socket.setdefaulttimeout(10)
vpn = random.choice([1,2,3,4,5])
posts = getPosts()
print(len(posts))
agents = getUserAgents()

while True:
    try:
        # display = Display(visible=1, size=(random.randint(320, 1920), random.randint(600, 750)))
        # display.start()
        options = Options()
        ua = random.choice(agents)
        options.add_argument(f'user-agent={ua}')
        
        if vpn == 1:
            options.add_extension('./files/uvpn.crx')
        elif vpn == 2:
            options.add_extension('./files/vpnpro.crx')
        elif vpn == 3:
            options.add_extension('./files/zenmate.crx')
        elif vpn == 4:
            options.add_extension('./files/ultra.crx')
        else:
            options.add_extension('./files/windscribe.crx')
            

        options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--disable-gpu")
        options.add_argument('--start-maximized')
        if vpn != 4:
            options.add_argument('--single-process')

        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("disable-infobars")

        # PROXY_STR = getWorkingProxy(getProxyList())
        # options.add_argument('--proxy-server=%s' % PROXY_STR)

        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"
        driver = webdriver.Chrome(desired_capabilities=caps, options=options)
        driver.set_page_load_timeout(150)

        driver.execute_script("var images = document.getElementsByTagName('img');var l = images.length;for (var i = 0; i < l; i++) {images[0].parentNode.removeChild(images[0]);}")
        
        if vpn == 1:
            connectUVPN(driver)
        elif vpn == 2:
            connectVPNPro(driver)
        elif vpn == 3:
            connectZenmate(driver)
        elif vpn == 4:
            connectUltrasurf(driver)
        else:
            time.sleep(5)
            connectWindscribe(driver)

        time.sleep(5)
        readStory(random.choice(posts), driver)
        readStory(random.choice(posts), driver)
        if random.randint(1,2) == 1:
            readStory(random.choice(posts), driver)
        driver.quit()
        time.sleep(10)
    except Exception as e:
        print("Something went wrong!.  Trying again......")
        print(str(e))
        driver.quit()
        # display.stop()
        time.sleep(random.randint(4,8))
        if platform == "linux" or platform == "linux2":
            os.system('python3 ultra.py')
        elif platform == "win32":
            os.system('python ultra.py')