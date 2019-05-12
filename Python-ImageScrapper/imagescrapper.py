from bs4 import BeautifulSoup
import urllib.request

# https://www.youtube.com/watch?v=m_agcM_ds1c

def make_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, 'html.parser')
    print(page)
    return soupdata

soup = make_soup("https://www.phd.co.id/en/pizza")

'''
for img in soup.findAll('img'):
    print(img)
    temp = img.get('src')
    # print(temp)
    
    if temp[:1] == "/":
        image = "https://www.phd.co.id/en/pizza" + temp
    else : 
        image = temp
    
    print (image)
    
'''
