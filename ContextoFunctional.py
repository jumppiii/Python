import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

file = open("./Text/wordlist.txt", "r")
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}

error1 = str("This word doesn't count, it's too common")
error2 = str("I don't know this word")

for entry in file:
    num = ''
    # checks in wordlist word has a number
    if any(map(str.isdigit, entry)):
        continue

    urls = "https://api.contexto.me/machado/en/game/129/" + entry
    url = urls[:-1]

    response = requests.get(url, headers=user_agent, verify=False)
    reply = response.text

    # if reply contains error messages, skip to next
    if reply.__contains__(error1) or reply.__contains__(error2):
        continue

    # if reply does not contain error messages, run this code
    else:
        print(reply)
