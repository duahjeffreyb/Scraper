from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.youtube.com/results?search_query=destiny+2').text

soup = BeautifulSoup(url, 'lxml')
#contains the raw html for the div tag, if needed.
#page_soup = soup.find_all('div',{'class':'yt-lockup-content'})
for idea in soup.find_all('div',{'class':'yt-lockup-content'}):
    name = idea.h3.a.text
    time = idea.h3.span.text
    
    print(name)
    print(time)
    print()
#print(soup.prettify())
