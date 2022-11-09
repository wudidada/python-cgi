#! /usr/bin/env python3

import cgitb
import re

import requests

cgitb.enable()

header = "Content-type: text/xml\n"

url = 'https://www.south-plus.net/rss.php?fid=9'

r = requests.get(url)
if r.ok:
    print(header)
    text = re.sub(r'CDATA\[//[^/]+/read.php', 'CDATA[//south-plus.net/read.php', r.text)
    print(text)
