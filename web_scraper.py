import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


class WebScrapper:
    def __init__(self):
        self.URL = os.getenv('URL')
        self.data = ''

    def get_data(self):
        # we use headers to appear human to the sight we are accessing
        response = requests.get(self.URL, headers={'Accept-Language': 'en-US',
                                                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
                                )
        self.data = response.text
        soup = BeautifulSoup(self.data, 'html.parser')
        return soup
