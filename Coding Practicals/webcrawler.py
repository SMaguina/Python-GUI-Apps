from bs4 import BeautifulSoup

import urllib2

webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")

# converts "urlopen" object into BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")
# finds the first instance of a div that has the id "container"
divContainer = soup.find("div", {"id":"container"})
# finds all instances of "div" with the id "container"
divBlock = divContainer.findAll("div", {"class":"block"})
divSep = divBlock[3].findAll("div", {"class":"separator"})
members = divSep[3].findAll("a")

def extractMData(webpage):
        soup = BeautifulSoup(webpage, "html.parser")
        divBlock = divContainer.findAll("div", {"class":"block"})
        info = divBlock[3]
        getLeft = info.findAll("div", {"class":"info_left"})
        getRight = info.findAll("div", {"class":"info_right"})
        for i in range(0,len(getLeft)):
            # get_text returns the string of text between HTML tags
            textLeft = getLeft[i].get_text()
            textRight = getRight[i].get_text()
            print textLeft + ": " + textRight
            print ""

for member in members:
    # strip <a> tags
    href = member.get("href")
    # create url to open
    url = "http://inadaybooks.com/justiceleague/"+href
    # open url
    mPage = urllib2.urlopen(url)
    extractMData(mPage)
