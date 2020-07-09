from bs4 import BeautifulSoup as soup
import requests

url = requests.get('https://store.playstation.com/en-us/grid/STORE-MSF77008-NEWGAMESGRID/1').text

filename = 'newGames.csv'
f = open(filename,'w', encoding='utf-8')
headers = "title, price\n"
f.write(headers)

b_soup = soup(url, 'lxml')
titles = b_soup.findAll('div', {'class':'grid-cell__title'})
allPrices = b_soup.findAll('div', {'class':'__shared-presentation__price-display__900cc'})

for i in range(0, len(titles)):
    price = allPrices[i].h3.text
    gameTitle = titles[i].span.text
    print(gameTitle)
    print(price)
    f.write(gameTitle + ',' + price + '\n')
f.close()
#print(page_soup)
#print(b_soup.prettify())
#print(price)
