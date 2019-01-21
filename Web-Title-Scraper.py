import requests
import bs4

URL = input("Enter the URL here: ")

res = requests.get(URL.strip())
soup = bs4.BeautifulSoup(res.text, 'lxml')
title = soup.select('title')
print(title)