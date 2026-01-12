#!/usr/bin/env python3

import sys
import os
sys.path.append('app')

from app.controllers import scrape, scrape_hacked_camera, markers_list
from app.config import country_list
from threading import Thread
import json

def scrape_all():
    try:
        os.remove('public/markers_loading.json')
    except FileNotFoundError:
        pass

    with open('public/markers_loading.json', 'w') as f:
        pass  # touch equivalent

    threads = []
    for y in range(0, len(country_list)):
        threads.append(Thread(target=scrape, args=(country_list[y], )))

    # Add thread for hacked.camera scraping
    threads.append(Thread(target=scrape_hacked_camera))

    for x in threads:
        x.start()

    for x in threads:
        x.join()

    with open('public/markers_loading.json', 'w', encoding='utf8') as markers_file:
        json.dump(markers_list, markers_file)

    try:
        os.remove('public/markers.json')
    except FileNotFoundError:
        pass
    os.rename('public/markers_loading.json', 'public/markers.json')

if __name__ == '__main__':
    scrape_all()
    print("Scraping completed. markers.json generated in public/")