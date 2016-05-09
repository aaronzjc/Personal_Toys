# -*- Coding: UTF-8 -*-

import codecs
import requests
import json
from bs4 import BeautifulSoup
from notify import notify

# track url
page_url = "http://cn163.net/archives/7698/"
# output file location
file = "/Users/memosa/Desktop/process.json"

process = open('process.json', 'r', encoding = 'utf-8')
series = json.load(process)
process.close()
# get page
page = requests.get(page_url).content.decode('utf-8')
index = BeautifulSoup(page, "html.parser")

for x in series:
    # if not tracked
    if 'chinese' not in series[x]:
        link = index.find("a", text=series[x]['name'])
        if link and link['href']:
            series[x]['chinese'] = link['href']
            notify(
                title = 'NOTICE',
                subtitle = '',
                message = "%s 更新了!" %(series[x]['name'])
            )

process = codecs.open(file, 'w+', 'utf-8')
process.write(json.dumps(series, ensure_ascii=False, sort_keys=True, indent=4))
process.close()