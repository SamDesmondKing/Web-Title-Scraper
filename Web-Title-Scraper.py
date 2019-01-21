import requests
import bs4
import re

#HTML tag removal function
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

#Taking URL as input
URL = input("Enter the URL here: ")

#Passing URL to requests, then BeautifulSoup, left with title as list.
res = requests.get(URL.strip())
soup = bs4.BeautifulSoup(res.text, 'lxml')
title_list = soup.select('title')

#Pulling title from list
title = title_list[0]

#Print statement
print("The title of the web page at " + URL + "is: \"" + remove_html_tags(str(title)) + "\"")

