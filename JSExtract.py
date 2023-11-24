import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import time

def get_page_content(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error when making request HTTP: {e}")
        return None

def extract_js_files(soup, url):
    js_files = [urljoin(url, script['src']) for script in soup.find_all('script', src=True)]
    return js_files

def download_file(url, file_name):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(file_name, 'wb') as file:
            file.write(response.content)

        print(f"Download successful of the file {file_name}")
    except requests.RequestException as e:
        print(f"Error when making request HTTP: {e}")

def download_js_files(js_urls, destiny_directory):
    if not os.path.exists(destiny_directory):
        os.makedirs(destiny_directory)

    for url in js_urls:
        file_name = os.path.join(destiny_directory, os.path.basename(url))
        download_file(url, file_name)

    time.sleep(1)

def main():
    # Get URLs from txt file
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print("ERROR: The file with the URLs is necessary")
        print("Example --> python JSExtractFromFile urls.txt")
        return

    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    for url in urls:
        # Get content from the web
        html_content = get_page_content(url)

        if html_content:
            # Analyzing HTML using BeautifulSoup
            soup = BeautifulSoup(html_content, "html.parser")

            # Get files JavaScript and write in a file
            js_files = extract_js_files(soup, url)
            print(f"Total of files JavaScript found in {url}: {len(js_files)}")

            # Download files JavaScript in a folder
            destiny_directory = "javascript_files_downloaded"
            download_js_files(js_files, destiny_directory)

if __name__ == "__main__":
    main()
