import phonenumbers
import os
from phonenumbers import geocoder, carrier, timezone

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
    
def phonenumber(number):
    try:
        parsed = phonenumbers.parse(number)
        region = geocoder.description_for_number(parsed, "en")
        print(f"{region}")
        carrier_name = carrier.name_for_number(parsed, "en")
        print(f"{carrier_name}")
        timezones = timezone.time_zones_for_number(parsed)
        print(f"{timezones}")
        print(f"{phonenumbers.is_valid_number(parsed)}")
        print(f"{phonenumbers.is_possible_number(parsed)}")
    except phonenumbers.NumberParseException as e:
        print(f"{e}")

def vaildcheck():
    banner()
    number = input("[+] +00           > ")
    phonenumber(number)
    input()
