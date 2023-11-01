import requests, re

from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content

soup = BeautifulSoup( r , "lxml")

## This will search for specific text within the website
## The first tag will find all "a" tags, then within those "a" tags it will find all "href" attributes that contains "allinone" in the url
## The second part of the tag is to query the "href" attributes is using re.complile or  regex complie"
## its telling findall to the use the following regular expresssion within the () on the "href" attribute

tags= soup.findAll("a", {"href":re.compile('(allinone)')})


##Since tags is an array that contains all of the occurence from soupfindall it will now loop and print out each occurence

for a in tags:
    print (a.get('href'))


