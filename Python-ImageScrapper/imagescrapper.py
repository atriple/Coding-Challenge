from bs4 import BeautifulSoup
import urllib
import urllib.request

# https://www.youtube.com/watch?v=m_agcM_ds1c

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(   page, 'html.parser')
    return soupdata

soup = make_soup("https://www.phd.co.id/en/pizza")

for img in soup.findAll('img'):
    temp = img.get('src')
    print(temp)
    '''
    if temp[:1] == "/":
        image = "https://www.phd.co.id/en/pizza" + temp
    else : 
        image = temp
    
    print (image)
    '''

