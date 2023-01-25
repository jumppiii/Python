import requests
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

file = open("./text/wordlist.txt", "r")
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}

error1 = str("This word")
error2 = str("I don't know this word")

os.system("cls")
score = input("Enter the max score a word can have: ")
print("\n")

for entry in file:
    num = ''
    left = ":"
    right = ","

    urls = "https://api.contexto.me/machado/en/game/128/" + entry
    url = urls[:-1]

    response = requests.get(url, headers=user_agent, verify=False)
    reply = response.text

    if reply.__contains__(error1) or reply.__contains__(error2):
        continue

    try:
        result = reply[reply.index(left) + len(left):reply.index(right)]

    except ValueError:
        print("ValueError caught in:", reply, "Continuing..")
        continue

    if int(result) < int(score):
        result = int(result) + 1
        print(entry[:-1], " == ", result)
