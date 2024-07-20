import requests
import os
import re
import concurrent.futures

def oniichan(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def uwu(tsundere):
    return re.sub(r'[\\/:*?"<>|]', '_', tsundere)

def download_image(session, chibi, file_path, tsundere):
    if not os.path.exists(file_path):
        try:
            response = session.get(chibi)
            response.raise_for_status()
            with open(file_path, 'wb') as rawr:
                rawr.write(response.content)
                print(f'Downloaded: {tsundere}')
        except requests.RequestException as e:
            print(f"Failed to download {tsundere}: {e}")
    else:
        print(f'Skipped: {tsundere} (already exists)')

def nuzzle(session, url):
    response = session.get(url)
    response.raise_for_status()
    nuzzle = response.json()
    oniichan('images')
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for card in nuzzle['data']:
            chibi = card['card_images'][0]['image_url']
            if chibi and chibi.startswith('https://images.ygoprodeck.com/'):
                tsundere = card['name']
                nya = f"{uwu(tsundere)}.jpg"
                file_path = os.path.join('images', nya)
                futures.append(executor.submit(download_image, session, chibi, file_path, tsundere))
        concurrent.futures.wait(futures)

def main():
    yandere = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?&num=100&offset='
    total_pages = 134
    with requests.Session() as session:
        for page in range(total_pages):
            offset = page * 100
            url = f'{yandere}{offset}'
            nuzzle(session, url)

if __name__ == "__main__":
    main()
