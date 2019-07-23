
import urllib.request
import bs4

import xlwt
'''
url = 'https://www.saemes.fr/en/list-car-parks-paris-and-ile-de-france-region'

page_data = urllib.request.urlopen(url)

page_soup = bs4.BeautifulSoup(page_data,'html.parser')

a = page_soup.find('div',attrs={'class':'intro-content clearfix'})
a = a.find('div',attrs={'class':'field-body'})
a=a.find('div',attrs={'property':'schema:text'})
a = a.find('table')
all_ones = a.find('tbody')
i=0

class park:

  def __init__(self,name,address,kind,url,count,hours,days,country='France'):
    self.name = name
    self.address = address
    self.kind = kind
    self.count = count
    self.hours = hours
    self.url = url

class_arr = []
i = 1
for item in all_ones:

  kind = item['class'][0]

  name,address = item.find_all('td')
  name = name.find('p')
  name = name.find('a')

  final_name = name.get_text()
  link = 'https://www.saemes.fr'+name['href']

  try:
    adrp = address.find('p')
    addr = adrp.get_text()
  except:
    addr = 'Null'

  html = urllib.request.urlopen(link)

  parser2 = bs4.BeautifulSoup(html,'html.parser')

  time_bit = parser2.find('div',attrs={'class':'icon-clock display-flex valign-center'})
  time_bit = time_bit.find('div')
  final_time,dates = time_bit.find('div').get_text().split(',')
  

  places_div = parser2.find('div',attrs={'class':'nb-places-libres'})
  amount = places_div.get_text().replace(' ','').replace('/','').replace('\n','')

  class_arr.append(park(final_name,addr,kind,link,amount,final_time,dates))

  print('Carpark '+str(i))
  i+=1
'''

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

title_arr = ['No.','Site Name','Country','Address','Type','Operating Hours','Operating days','Bay Count']
for i in range(0,len(title_arr)):
  sheet1.write(0,0+i,title_arr[i])



book.save("main.xls")
