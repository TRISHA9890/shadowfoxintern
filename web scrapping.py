"""WEB SCRAPPING """
import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.codechef.com/practice#beginner-dsa")

"""it used as beautifulSoup libraies"""
web=BeautifulSoup(r.content,"html.parser") 

"""it will show the tittle of web"""
req=web.title
"""displaying the prettify function"""
print(req.prettify)