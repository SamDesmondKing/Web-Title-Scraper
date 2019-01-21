import requests
import bs4
import re

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

URL = input("Enter the URL here: ")

res = requests.get(URL.strip())
soup = bs4.BeautifulSoup(res.text, 'lxml')
title_list = soup.select('title')

title = title_list[0]

print("The title of the web page at " + URL + "is: \"" + remove_html_tags(str(title)) + "\"")

