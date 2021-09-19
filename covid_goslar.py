import csv
import excel_email
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://www.corona-in-zahlen.de/landkreise/lk%20goslar/"
html_code = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_code, 'lxml')

file = open('covid19_goslar.csv', 'w')

writer = csv.writer(file)
writer.writerow(['Einwohner', 'Infektionen', 'Infektionsrate', 'Inzidenz', 'Todesfälle', 'Letalitätsrate'])

data = soup.find('div', attrs={'class':'row row-cols-1 row-cols-md-3'})
info = data.findAll('p', attrs={'class':'card-title'})

numbers =  [d.text for d in info]

pop = numbers[0]
infect = numbers[1]
rate = numbers[2]
seven_day = numbers[3]
death = numbers[4]
leth = numbers[5]

writer.writerow([pop, infect, rate, seven_day, death, leth])

file.close()

excel_email.email_excel()



