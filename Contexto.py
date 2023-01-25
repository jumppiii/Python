import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

file = open("wordlistnew.txt", "r")
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}

error1 = str("This word doesn't count, it's too common")
error2 = str("I don't know this word")

for entry in file:
    num = ''

    urls = "https://api.contexto.me/machado/en/game/129/" + entry
    url = urls[:-1]

    response = requests.get(url, headers=user_agent, verify=False)
    reply = response.text
    
    if reply.__contains__(error1) or reply.__contains__(error2):
        continue

    left = ":"
    right = ","
    result = reply[reply.index(left)+len(left):reply.index(right)]

    if int(result) < 1000:
        print(result, ":: Word was", entry)

