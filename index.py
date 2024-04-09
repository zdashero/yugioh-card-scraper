import requests
import os
import json
import re

def oniichan(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def uwu(tsundere):
    return re.sub(r'[\\/:*?"<>|]', '_', tsundere)
def nuzzle(url):
    response = requests.get(url)
    response.raise_for_status()
    nuzzle = response.json()
    oniichan('images')
    for card in nuzzle['data']:
        chibi = card['card_images'][0]['image_url']
        if chibi and chibi.startswith('https://images.ygoprodeck.com/'):
            tsundere = card['name']
            nya = f"{uwu(tsundere)}.jpg"
            senpai = requests.get(chibi).content
            with open(os.path.join('images', nya), 'wb') as rawr:
                rawr.write(senpai)
                print(f'Downloaded: {nya}')
yandere = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?&num=100&offset='
total_pages = 132
for page in range(total_pages):
    offset = page * 100
    url = f'{yandere}{offset}'
    nuzzle(url)