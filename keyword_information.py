import requests
import urllib3.request
import time
from bs4 import BeautifulSoup
import re
import string
import json

with open('nk_api.json', 'r') as openfile:
    json_read = json.load(openfile)

with open('nk_api_links_V002.json', 'r') as openfile_links:
    json_read_links = json.load(openfile_links)


def information(word):
    space = False
    for dict in json_read_links:
        try:
            ext = dict[word]
            pikachu_word = dict[word].split('#')
            pikachu_word = pikachu_word[1]

            url = 'https://learn.foundry.com/nuke/developers/70/pythonreference/{}'.format(ext)
            print url

            response = requests.get(url)
            # print response.text

            soup = BeautifulSoup(response.text, 'html.parser')

            results = soup.find_all('table', attrs={"class": "details","border":"1", "cellspacing":"0", "width":"100%", "bgcolor":"white"})

            ### for detailed instrruction modules/classes
            for pikachu in results:
                if pikachu.text.find(pikachu_word) != -1:
                    # print type(pikachu.text)
                    return pikachu.text.strip()
                else:
                    space = True


            ### for small values for keywords and parameters
            if space is True:
                results = soup.find_all('td', attrs={"class": "summary"})
                for pikachu in results:
                    if pikachu.text.find(pikachu_word) != -1:
                        # print type(pikachu.text)
                        return pikachu.text.strip()
        except:
            pass

# keyword_info = []
# for i in json_read:
#     information(i)
#     value = {i:information(i)}
#     keyword_info.append(value)
#
# json_list = json.dumps(keyword_info, indent=4)
# with open('nk_api_info.json','w') as f:
#     f.write(json_list)

for dict in json_read_links:
    try:
        ext = dict["XY_Knob (nuke)"]
        pikachu_word = ext.split('#')
        pikachu_word = pikachu_word[1]

    except:
        pass

url = 'https://learn.foundry.com/nuke/developers/70/pythonreference/{}'.format(ext)
print pikachu_word

print url

print information("XY_Knob (nuke)")

# print keyword_info