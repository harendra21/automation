from pyvirtualdisplay import Display
from selenium import webdriver
import time
import random
from selenium.webdriver.chrome.options import Options
import os

time.sleep(random.randint(4,8))

vDisplay = False
vDisplayVisible = False

posts = [
    "https://hackeradda.com/blog/",
    "https://hackeradda.com/",
    "https://hackeradda.com/post/10-fantastic-developer-tools-you-probably-do-not-use/",
    "https://hackeradda.com/post/15-free-hosting-providers-for-web-developers/",
    "https://hackeradda.com/post/6-points-to-consider-when-choosing-a-web-host-for-your-business/",
    "https://hackeradda.com/post/consider-before-you-code/",
    "https://hackeradda.com/post/everything-you-need-to-know-about-cpanel/",
    "https://hackeradda.com/post/five-things-to-keep-in-mind-while-selecting-web-hosting-service/",
    "https://hackeradda.com/post/free-cicd-and-integration-with-web-hosting-githubpage-travisci/",
    "https://hackeradda.com/post/free-static-website-hosting-with-a-custom-domain-name/",
    "https://hackeradda.com/post/free-web-hosting-and-domain-name/",
    "https://hackeradda.com/post/how-to-choose-the-best-web-hosting-provider-the-ultimate-guide/",
    "https://hackeradda.com/post/how-to-setup-cron-jobs-in-cpanel/",
    "https://hackeradda.com/post/how-to-use-bluehost-to-create-your-own-wordpress-website/",
    "https://hackeradda.com/post/i-want-to-learn-programming-but-dont-know-where-to-begin/",
    "https://hackeradda.com/post/in-2022-the-best-web-hosting-and-domain-name-registration-services-to-use/",
    "https://hackeradda.com/post/is-it-worth-using-free-web-hosting/",
    "https://hackeradda.com/post/programming-fundamentals-compiler-and-interpreter/",
    "https://hackeradda.com/post/what-does-it-mean-to-host-a-website-anonymously/",
    "https://hackeradda.com/post/why-should-you-use-ssd-web-hosting/",
    "https://hackeradda.com/tags/best-hosting/",
    "https://hackeradda.com/tags/coding/",
    "https://hackeradda.com/tags/cpanel/",
    "https://hackeradda.com/tags/free/",
    "https://hackeradda.com/tags/free-web-hosting/",
    "https://hackeradda.com/tags/learn-to-code/",
    "https://hackeradda.com/tags/programming/",
    "https://hackeradda.com/tags/tools/",
    "https://hackeradda.com/tags/web-hosting/",
    "https://hackeradda.com/tags/website-hosting/",
    "https://codingblog.online/blog/",
    "https://codingblog.online/",
    "https://codingblog.online/post/10-strategies-to-increase-your-programming-logical-thinking-abilities/",
    "https://codingblog.online/post/50-useful-python-scripts-free-pdf-download/",
    "https://codingblog.online/post/6-algorithms-every-developer-should-be-aware-of/",
    "https://codingblog.online/post/8-google-courses-that-offer-free-certifications/",
    "https://codingblog.online/post/a-guide-to-create-pure-css-tooltips/",
    "https://codingblog.online/post/a-more-effective-method-of-coding/",
    "https://codingblog.online/post/create-an-rgb-color-picker-using-html-and-bootstrap/",
    "https://codingblog.online/post/create-elegant-javascript-code-using-shortcircuit-evaluation/",
    "https://codingblog.online/post/during-coding-interviews-there-are-three-javascript-queries-to-watch-out-for/",
    "https://codingblog.online/post/every-programmer-should-be-aware-of-these-10-javascript-hacks/",
    "https://codingblog.online/post/how-can-you-improve-your-coding-skills/",
    "https://codingblog.online/post/how-i-would-learn-to-code-if-i-could-start-over/",
    "https://codingblog.online/post/how-to-improve-your-programming-problem-solving-skills/",
    "https://codingblog.online/post/how-to-learn-programmming/",
    "https://codingblog.online/post/how-to-make-a-simple-html-5-webpage/",
    "https://codingblog.online/post/how-to-make-the-most-of-your-programming-workflow/",
    "https://codingblog.online/post/how-to-think-like-a-programmer/",
    "https://codingblog.online/post/how-to-write-functions-like-a-senior-developer-eight-tips/",
    "https://codingblog.online/post/i-wish-i-had-known-about-these-tools-when-i-first-started-coding/",
    "https://codingblog.online/post/programming-is-a-difficult-task-that-is-exactly-why-you-should-study-it/",
    "https://codingblog.online/post/the-all-in-one-programming-language/",
    "https://codingblog.online/post/these-5-frontend-development-tools-will-help-you-save-a-lot-of-time/",
    "https://codingblog.online/post/what-can-you-do-to-improve-your-logical-thinking/",
    "https://codingblog.online/post/what-to-do-if-youre-stuck-in-a-coding-tutorial/",
    "https://codingblog.online/tags/algorithms/",
    "https://codingblog.online/tags/chrome-extensions/",
    "https://codingblog.online/tags/coding/",
    "https://codingblog.online/tags/css/",
    "https://codingblog.online/tags/frontend/",
    "https://codingblog.online/tags/html/",
    "https://codingblog.online/tags/interview/",
    "https://codingblog.online/tags/javascript/",
    "https://codingblog.online/tags/learn/",
    "https://codingblog.online/tags/programming/",
    "https://codingblog.online/tags/python/",
    "https://codingblog.online/tags/tips/",
    "https://codingblog.online/tags/vscode-extensions/",
    "https://codingblog.online/tags/webdev/",
]

user_agents = [
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0",
    "Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",
    "Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",
    "Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",
    "Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3",
    "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
    "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
    "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/50.0.125 Chrome/44.0.2403.125 Safari/537.36",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4"
]

def closeExtraTabs(driver):
    tab_list = driver.window_handles
    if len(tab_list) > 1:
        driver.switch_to.window(tab_list[1])
        driver.close()
        driver.switch_to.window(tab_list[0])

def visit():
    try:
        if vDisplay:
            display = Display(visible=vDisplayVisible, size=(random.randint(320, 1920), random.randint(700, 750)))
            display.start()

        options = Options()
        options.add_extension('./ultra.crx')
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": random.choice(user_agents)})

        time.sleep(8)
        driver.get(random.choice(posts))
        closeExtraTabs(driver)
        print(driver.title)


        time.sleep(random.randint(20,40))
        y = 0
        for timer in range(0,random.randint(130,180)):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += random.randint(30,60)
            time.sleep(0.5)
        time.sleep(random.randint(10,30))

        driver.execute_script('window.location.href = "{}";'.format(random.choice(posts)))
        time.sleep(random.randint(5,15))
        print(driver.title)
        y = 0
        for timer in range(0,int(random.randint(130,180))):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += random.randint(30,60)
            time.sleep(0.5)
        time.sleep(random.randint(15,45))

        driver.quit()
        display.stop()
        if vDisplay:
                display.stop()
    except:
        driver.quit()
        display.stop()
        print("Try Again....")
        if vDisplay:
                display.stop()
        os.system('python3 ultra.py')
while True:
    visit()
