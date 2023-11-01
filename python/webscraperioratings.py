import requests, re
from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r, "lxml")
tags = soup.findAll("div", {"class":re.compile('(ratings)')})
for p in tags:
    a = p.findAll("p",{"class":"pull-right"})
    print(a[0].string)


##This will create a space
##print(" ")

##print(" beggining of second tags")
## The second tag is searching for reviews on the page
## it will search through the div tags and searches for the class attribute that contain the regex characters "ratings"

##tagstwo = soup.findAll("div", {"class":re.compile('(ratings)')})

##for p in tagstwo:
    ##within each div tag it will search for every "p" tag that contains the class called "pulled-right"
  ##  x = p.findAll("p",{"class":"pull-right"})
    ##This will only grab one value which is the first value from the string and print it as a string
   ## print(x[0].string)
 
