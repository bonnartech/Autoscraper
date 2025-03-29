from django.shortcuts import render, redirect
from .models import ScrapedData
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
from azure.storage.blob import BlobServiceClient
from django.http import HttpResponseRedirect
from django.urls import reverse
import os

def dashboard(request):
    data = ScrapedData.objects.all()
    return render(request, 'dashboard.html', {'data': data})

def run_scrape(request):
    # legacy DataSource scraping 
    return HttpResponseRedirect(reverse('dashboard'))

def export_csv(request):
    df = pd.DataFrame(ScrapedData.objects.all().values())
    df.to_csv('scraped_data.csv', index=False)
    print("CSV Exported: scraped_data.csv")
    return HttpResponseRedirect(reverse('dashboard'))

def upload_azure(request):
    try:
        # Read connection string from environment variable (for Azurite or Azure)
        connection_string = os.getenv('AZURE_CONNECTION_STRING')

        if not connection_string:
            print("AZURE_CONNECTION_STRING environment variable is not set.")
            return HttpResponseRedirect(reverse('dashboard'))

        # Connect to Azurite or Azure Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_name = "test-container"

        # Create container if it doesn't exist
        container_client = blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()
            print(f" Container '{container_name}' created")

        # Upload the CSV file
        blob_client = container_client.get_blob_client("scraped_data.csv")
        with open('scraped_data.csv', 'rb') as data:
            blob_client.upload_blob(data, overwrite=True)

        print("Upload Successful to Azure/Azurite Blob Storage")

    except Exception as e:
        print("Upload Failed:", e)

    return HttpResponseRedirect(reverse('dashboard'))

def dynamic_scrape(request):
    url = request.GET.get('url')
    scraped_results = []
    if url:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Auto scrape common tags
            for tag in ['p', 'span', 'div', 'li', 'blockquote']:
                for el in soup.find_all(tag):
                    text = el.get_text(strip=True)
                    if text:
                        sentiment = 'Positive' if TextBlob(text).sentiment.polarity > 0 else 'Negative' if TextBlob(text).sentiment.polarity < 0 else 'Neutral'
                        scraped_results.append({'tag': tag, 'content': text, 'sentiment': sentiment})
            print(f"Scraping Completed for {url}")
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            scraped_results.append({'tag': 'Error', 'content': str(e), 'sentiment': 'N/A'})

    # Auto-export to CSV for Power BI
    if scraped_results:
        df = pd.DataFrame(scraped_results)
        df.to_csv('scraped_data.csv', index=False)
        print(" Dynamic CSV Exported: scraped_data.csv")

    return render(request, 'dynamic_result.html', {'results': scraped_results, 'url': url})
