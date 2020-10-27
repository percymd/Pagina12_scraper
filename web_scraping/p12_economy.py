import requests
from bs4 import BeautifulSoup

url = 'https://www.pagina12.com.ar/secciones/economia'

def getlinks(soup):
    news = soup.find_all('div', attrs={'class':'article-item__content'})
    links_n = [new.a.get('href') for new in news]
    print(links_n)

def main():
    p12 = requests.get(url)
    soup = BeautifulSoup(p12.text, 'lxml')
    getlinks(soup)

if __name__=='__main__':
    main()