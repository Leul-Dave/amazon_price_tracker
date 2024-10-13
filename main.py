from web_scraper import WebScrapper
from notification import Notification

notification = Notification()
web_scrapper = WebScrapper()
soup = web_scrapper.get_data()

price_of_product = float(soup.find(name='span', class_='aok-offscreen').getText().split('$')[1])
name_of_product = soup.find(name='span', class_='a-size-large product-title-word-break',
                            id='productTitle').getText()
body = f'{name_of_product} is now ${price_of_product}\n{web_scrapper.URL}'

if price_of_product < 100:
    send_email = notification.email(body)
