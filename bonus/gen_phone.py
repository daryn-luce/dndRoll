import random
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.areacodelocations.info/areacodelist.html')
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.table
td = [td.get_text() for td in table.find_all('td')]
area = [td[i] for i in range(0,len(td),4)]
state = [td[i] for i in range(1,len(td),4)]
timezone = [td[i] for i in range(3,len(td),4)]

logfile = []
def four_digit():
    num = str(random.randint(0,9999))
    while len(num) < 4:
        num = '0' + num
    return num

for i in range(10000):
    temp = random.randint(0,len(area)-1)
    logfile.append(f'{area[temp]}-{random.randint(100,999)}-{four_digit()}@{state[temp].rstrip()}={timezone[temp]}')


with open('phone.txt','w') as f:
    f.write('\n'.join(logfile))
