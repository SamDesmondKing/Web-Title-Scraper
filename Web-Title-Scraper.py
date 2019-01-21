import requests
import bs4

res = requests.get('https://eddb.io/')

soup = bs4.BeautifulSoup(res.text, 'lxml')

title = soup.select('title')

print(title)