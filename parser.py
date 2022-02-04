from bs4 import BeautifulSoup
import os
import sys

f = None

for file in os.listdir(os.getcwd()):
    if file.endswith(".html"):
        f = open(file, 'rb')
        break
if not f:
    print("Ошибка: Файл не найден")
    sys.exit()

s = ''
print("Анализируем файл...")
for i in f:
    s += i.decode('utf8')

soup = BeautifulSoup(s, 'lxml')
table = soup.find('table', {"class": "generaltable attwidth boxaligncenter allsessions"})


td_s = table.select('td.c4,tr.grouper')
for td in td_s:
    if td.text != '? / 5' and td.text != '0 / 5':
        print(td.text)

print("Готово!")
