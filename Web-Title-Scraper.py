import requests
import bs4
import re

#HTML tag removal function
def remove_html_tags(text):
  clean = re.compile('<.*?>')
  return re.sub(clean, '', text)

#Input taking and validation
res = None
while res is None:
  URL = input("Enter the URL here: ")
  try:
    res = requests.get(URL.strip())
  except:
    print("Error: Not a valid URL.")

#Passing requests object to Beautiful Soup, getting title as list
soup = bs4.BeautifulSoup(res.text, 'lxml')
title_list = soup.select('title')

#Pulling title from list
title = title_list[0]

#Print statement
print("The title of the web page at " + URL + "is: \"" + remove_html_tags(str(title)) + "\"")

