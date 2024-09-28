import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def scrape_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title
    title = soup.title.string if soup.title else "No title found"

    # Extract meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc['content'] if meta_desc else "No description found"

    # Extract all text content
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text(separator=' ', strip=True)

    # Extract links
    links = []
    for link in soup.find_all('a', href=True):
        links.append(urljoin(url, link['href']))

    # Extract images
    images = []
    for img in soup.find_all('img', src=True):
        images.append(urljoin(url, img['src']))

    # Clean the scraped text data
    cleaned_text = clean_scrap_data(text)

    return {
        'url': url,
        'title': title,
        'description': description,
        'text': cleaned_text,
        'links': links,
        'images': images
    }

def clean_scrap_data(scrapped_data):
    scrapped_data = re.sub(r'\s+', ' ', scrapped_data).strip()

    scrapped_data = re.sub(r'<[^>]+>', '', scrapped_data)

    scrapped_data = re.sub(r'[^\w\s.,!?-]', '', scrapped_data)

    return scrapped_data