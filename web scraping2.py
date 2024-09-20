import requests
from bs4 import BeautifulSoup

url=requests.get("https://timesofindia.indiatimes.com/")
print(url.content)
website=requests.get(url.content,"html.parser")

""" displaying prettify function"""
print(website.prettify)  

""" displaying tittle name"""      
print(website.tittle.name)

print(website.tittle.string)
print(website.a)
print(website.h1)
print(website.p)

"""Finding the anchor tag"""
print(website.find("a"))

print(website.find_all("h1"))
print(website.find(id="nav-bar"))