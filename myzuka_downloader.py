import requests
from bs4 import BeautifulSoup


url = input('Insert url:')


def get_url(url):
    response = requests.get(url)
    if response == '200':
        soup = BeautifulSoup(response.text, 'lxml')
        links = soup.find_all('div', class_='player-inline')
        for link in links:
            song_url = 'https://myzuka.club' + link.find('div', class_='top').find('a').get('href')
            resp = requests.get(song_url)
            soup = BeautifulSoup(resp.text, 'lxml')
            name = soup.find('div', itemprop='tracks').find('h1').text
            mp3_url = 'https://myzuka.club' + soup.find('a', itemprop='audio').get('href')
            download(mp3_url, name)


def download(link, track):
    response = requests.get(link, stream=True)
    with open(track + '.mp3', 'wb') as mp3:
        for flow in response.iter_content(1024*1024):
            mp3.write(flow)
        print(f'File {track} has been downloaded!')


get_url(url)

