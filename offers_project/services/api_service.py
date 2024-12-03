import os
import requests
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'offers_project.settings')

def fetch_products_from_api():
    url = "https://api.unsplash.com/photos/"
    headers = {"Authorization": f"Client-ID {settings.UNSPLASH_ACCESS_KEY}"}
    print(headers)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    return []