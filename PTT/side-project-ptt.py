import csv
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將網頁資料GET下來
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
for s in sel:
    print(s["href"], s.text)

with open('tcode/side-project-ptt_titles.csv', 'w', encoding='UTF-8-Sig', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['網址', '標題'])
    for s in sel:
        net = s["href"]
        title = s.text
        csv_writer.writerow([net, title])

