import tkinter as tk
from myzuka_downloader import download, get_url
import webbrowser


def open_site_myzuka():
    webbrowser.open(r'http://myzuka.club', new=2)


class Main_window:
    root = tk.Tk()
    root.title('Myzuka.club downloader')

    def __init__(self):
        tk.Label(self.root, text='Insert url from "myzuka.club":').grid(row=1, column=0)
        self.entry = tk.Entry(width=50)
        self.entry.grid(row=1, column=1)
        btn = tk.Button(self.root, text='Start downloading', command=self.download_mp3)
        btn.grid(row=1, column=3)
        btn_site = tk.Button(self.root, text='Open myzuka.club in browser', command=open_site_myzuka)
        btn_site.grid(row=0, column=1)

    def download_mp3(self):
        url = self.entry.get()
        get_url(url)

    def start_app(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = Main_window()
    app.start_app()
