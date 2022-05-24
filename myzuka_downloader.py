import threading
import webbrowser
import requests
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter.ttk import Progressbar
import time


def open_site_myzuka():
    webbrowser.open(r'http://myzuka.club', new=2)


class Music_downloader_app:
    root = tk.Tk()
    root.title('Myzuka.club downloader')
    root.geometry('800x600+500+10')

    def __init__(self):
        self.label1 = tk.Label(self.root, text='Insert url from "myzuka.club":').grid(row=1, column=0)
        self.entry = tk.Entry(self.root, width=50)
        self.entry.grid(row=1, column=1)
        self.btn = tk.Button(self.root, text='Start downloading', command=threading.Thread(target=self.get_url).start)
        self.btn.grid(row=1, column=3)
        self.btn_site = tk.Button(self.root, text='Open myzuka.club in browser', command=open_site_myzuka)
        self.btn_site.grid(row=0, column=1)
        self.label_message = tk.Label(self.root, text='download progress >>>>').grid(row=2, column=0)
        self.bar = Progressbar(self.root, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.bar.grid(row=2, column=1)

    def get_url(self):
        url = self.entry.get()
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            links = soup.find_all('div', class_='player-inline')
            for link in links:
                song_url = 'https://myzuka.club' + link.find('div', class_='top').find('a').get('href')
                resp = requests.get(song_url)
                soup = BeautifulSoup(resp.text, 'lxml')
                name = soup.find('div', itemprop='tracks').find('h1').text
                mp3_url = 'https://myzuka.club' + soup.find('a', itemprop='audio').get('href')
                self.download(mp3_url, name)

    def download(self, link, track):
        response = requests.get(link, stream=True)
        folder = track.split(' - ')[0]
        if not os.path.exists(folder):
            os.mkdir(folder)
        with open(f'{os.getcwd()}/{folder}/{track}.mp3', 'wb') as mp3:
            for flow in response.iter_content(1024 * 1024):
                self.bar.start()
                mp3.write(flow)
            self.bar.stop()
            message = f'File {track} has been downloaded!'
            # app.show_message(message)
            print(message)

    def show_message(self, text):
        self.label_message['text'] = text

    def start_app(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = Music_downloader_app()
    app.start_app()
