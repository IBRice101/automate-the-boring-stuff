# A program to get the cost of an amazon product and return it to the console
#TODO: fix the user agent string

import bs4
import requests

def getAmazonPrice(productURL):
    # add user agent string to trick amazon into thinking this is a broswer
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    } 
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#price')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.co.uk/Automate-Boring-Stuff-Python-2nd/dp/1593279922/')
print('That item costs: ' + price)
