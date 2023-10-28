import requests, re

from bs4 import BeautifulSoup


##using get request to retrieve the nike website
r = requests.get("https://www.nike.com/t/luka-2-basketball-shoes-vcXFrk/DX8733-006").content

##Used buatifulSoup in order to work with the data
soup = BeautifulSoup( r , "lxml")

## This will search for specific text within the website through by specifying tags and classes
span = soup.find("h1", {"class":"headline-2"})
title = span.text

span2 = soup.find("div", {"class":"product-price"})
price = span2.text


##Printed out extracted content
print("On the Nike website the %s cost %s" % (title, price))

