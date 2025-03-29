
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from .models import DataSource, ScrapedData

def scrape_data():
    for source in DataSource.objects.all():
        res = requests.get(source.url)
        soup = BeautifulSoup(res.text, 'html.parser')
        for el in soup.find_all(source.data_tag):
            text = el.get_text()
            sentiment = 'Positive' if TextBlob(text).sentiment.polarity > 0 else 'Negative' if TextBlob(text).sentiment.polarity < 0 else 'Neutral'
            ScrapedData.objects.create(source=source, content=text, sentiment=sentiment)
