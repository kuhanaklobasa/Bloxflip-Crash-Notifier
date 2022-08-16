from colorama import Fore, Style
import colorama as c
from discord_webhook import DiscordWebhook
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from playsound import playsound

#Set your user agent
USER_AGENT = ""







if USER_AGENT == "":
    print(f"{c.Back.RED}Set your user agent on line 14!{Style.RESET_ALL}")
    exit()

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('user-agent=' + USER_AGENT)
driver = webdriver.Chrome('./chromedriver',options=option)

def main():
    list_multi = []
    driver.get("https://bloxflip.com/crash")
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'gameLatestItem')))
    history_list = driver.find_elements_by_class_name("gameLatestItem")
    for child in history_list:
        list_multi.append(float(child.text))
    return list_multi

print(f"{c.Back.GREEN}Shreks Bloxflip crash notifier{Style.RESET_ALL}\n\n")
min_mult = float(input(f"{Fore.YELLOW}[{Style.RESET_ALL}?{Fore.YELLOW}]{Style.RESET_ALL} Enter the min. multiplier in number. Ex 3 > "))
mult_times = int(input(f"{Fore.YELLOW}[{Style.RESET_ALL}?{Fore.YELLOW}]{Style.RESET_ALL} How many times in a row should the multiplier appear Max. 7? > "))
interval = int(input(f"{Fore.YELLOW}[{Style.RESET_ALL}?{Fore.YELLOW}]{Style.RESET_ALL} Enter check interval in seconds Ex. 10 > "))
use_webhook = input(f"{Fore.YELLOW}[{Style.RESET_ALL}?{Fore.YELLOW}]{Style.RESET_ALL} Want to be notified via discord webhook? y/n > ")
if use_webhook == "y":
    webhook_url = input(f"{Fore.YELLOW}[{Style.RESET_ALL}?{Fore.YELLOW}]{Style.RESET_ALL} Enter webhook url > ")
    webhook_content = input(f"{Fore.YELLOW}[{Style.RESET_ALL}?{Fore.YELLOW}]{Style.RESET_ALL} Enter webhook content > ")
    webhook = DiscordWebhook(webhook_url, content=f"""{webhook_content}\n https://bloxflip.com/crash""")
notify_sound = input(f"{Fore.YELLOW}[{Style.RESET_ALL}?{Fore.YELLOW}]{Style.RESET_ALL} Want to be notified with a sound notification? y/n > ")
notify_sound = True if notify_sound == "y" else False

stop_on_notify = input(f"{Fore.YELLOW}[{Style.RESET_ALL}?{Fore.YELLOW}]{Style.RESET_ALL} Stop on notify? y/n > ")
stop_on_notify = True if stop_on_notify == "y" else False
print("\n\n")

class Checker():
    stop_checker = True

    while stop_checker:
        number_of_multi = 0
        list_multi = main()
        print(f"{Fore.YELLOW}[{Style.RESET_ALL}?{Fore.YELLOW}]{Style.RESET_ALL} Fetched multis. Current multis: {list_multi}")
        time.sleep(0.2)
        for item in list_multi:
            if item > min_mult:
                number_of_multi = number_of_multi+1
            else:
                number_of_multi = 0
            if number_of_multi >= mult_times:
                time.sleep(0.2)
                print(f"{Fore.GREEN}[{Style.RESET_ALL}!{Fore.GREEN}]{Style.RESET_ALL} Found {mult_times}x {min_mult}+ multipliers")
                if notify_sound:
                    playsound("notification.wav")
                if use_webhook == "y":
                    response = webhook.execute()
                    if response.status_code != 200:
                        print(f"{Fore.RED}[{Style.RESET_ALL}!{Fore.RED}]{Style.RESET_ALL} Something went wrong when sending the webhook. Message: {response.text}")
                if stop_on_notify:
                    stop_checker = False
                    break
                break

        if stop_checker:
            time.sleep(interval)
    
    print(f"{Fore.RED}[{Style.RESET_ALL}!{Fore.RED}]{Style.RESET_ALL} Stopped checker!")
    input()
Checker()