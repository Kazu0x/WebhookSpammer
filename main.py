import requests
import concurrent.futures
from colorama import init
init()
from termcolor import colored
import os

os.system("cls")
print(colored(""" 




                 ░▒█░░▒█░▒█▀▀▀░▒█▀▀▄░▒█░▒█░▒█▀▀▀█░▒█▀▀▀█░▒█░▄▀░░░▒█▀▀▀█░▒█▀▀█░█▀▀▄░▒█▀▄▀█░▒█▀▄▀█░▒█▀▀▀░▒█▀▀▄
                 ░▒█▒█▒█░▒█▀▀▀░▒█▀▀▄░▒█▀▀█░▒█░░▒█░▒█░░▒█░▒█▀▄░░░░░▀▀▀▄▄░▒█▄▄█▒█▄▄█░▒█▒█▒█░▒█▒█▒█░▒█▀▀▀░▒█▄▄▀
                 ░▒▀▄▀▄▀░▒█▄▄▄░▒█▄▄█░▒█░▒█░▒█▄▄▄█░▒█▄▄▄█░▒█░▒█░░░▒█▄▄▄█░▒█░░░▒█░▒█░▒█░░▒█░▒█░░▒█░▒█▄▄▄░▒█░▒█



""", 'green'))

print(colored("		                                  by Kazu   <3", 'red'))
webhook_url = input(colored("[+] Enter your webhook: ", 'blue'))
message = input(colored("[/] Enter your message: ", 'blue'))
nombre_de_messages = int(input(colored("[+] Enter number of your message: ", 'blue')))

try:
    executor = concurrent.futures.ThreadPoolExecutor()
    futures = [executor.submit(requests.post, webhook_url, json={"content": message}) for i in range(nombre_de_messages)]
    concurrent.futures.wait(futures)
    executor.shutdown(wait=True)
except requests.exceptions.RequestException as e:
    print(colored("Webhook Invalide !", 'red'))