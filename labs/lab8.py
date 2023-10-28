import requests, re

from bs4 import BeautifulSoup

r = requests.get("https://www.nike.com/t/luka-2-basketball-shoes-vcXFrk/DX8733-006").content

soup = BeautifulSoup( r , "lxml")

## This will search for specific text within the website
## The first tag will find all "a" tags, then within those "a" tags it will find all "href" attributes that contains "allinone" in the url
## The second part of the tag is to query the "href" attributes is using re.complile or  regex complie"
## its telling findall to the use the following regular expresssion within the () on the "href" attribute


span = soup.find("h1", {"class":"headline-2"})
title = span.text

span2 = soup.find("div", {"class":"product-price"})
price = span2.text


print("On the Nike website the %s cost %s" % (title, price))

