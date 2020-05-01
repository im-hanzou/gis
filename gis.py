## Using Python3.x
## Usage : python3 gis.py / python gis.py
## IM.Hanzou <> Thanks for Con7ext

import urllib.request
import re
import sys

def scrap(args):
  args = args.split()
  url = 'https://www.google.co.id/search?ei=c_uHW87hBc_p9QO-6I7wBg&safe=strict&yv=3&tbm=isch&q=' + "+" .join(args)  +'&vet=1ahUKEwis6PO4p5PpAhXTeisKHWhzCQsQ4dUDCAY.c_uHW87hBc_p9QO-6I7wBg.i&ved=0ahUKEwis6PO4p5PpAhXTeisKHWhzCQsQ4dUDCAY&ijn=1&start=10000&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc'
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
  req = urllib.request.Request(url, headers = headers)
  resp = urllib.request.urlopen(req)
  respData = resp.read()
  paragraphs = re.findall(r'"ou":"(.*?)"',str(respData))
  sys.stdout = open('gis.txt','wt')
  for res in paragraphs:
    print(res)

print("./Hanzou > Google Images Search\n")
dorks = input("Your Dork : ")
print("result saved > gis.txt\n")

for dork in dorks:
  scrap(dorks)
