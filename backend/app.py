from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import tldextract


app = Flask(__name__)
CORS(app) 

DOMAIN = ''
CRAWL_DEPTH = 0
DOMAIN_NAME = ''

def get_soup(url):
    try:
        if not url.startswith('http'):
            url = DOMAIN + url
        request_object = requests.get(url)
        soup = BeautifulSoup(request_object.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}")
        print(e)
        return None

def get_raw_links(soup):
    return [a.get('href') for a in soup.find_all('a', href=True)]

def clean_links(raw_links):
    filtered_links = []
    for link in raw_links:
        if link.startswith('http') and DOMAIN_NAME in link:
            filtered_links.append(link)
        elif link.startswith('/') or link.startswith('#'):
            filtered_links.append(DOMAIN + link)

    return list(set(filtered_links))

def crawl_page(url):
    soup = get_soup(url)
    if soup:
        raw_links = get_raw_links(soup)
        links = clean_links(raw_links)
        return links
    else:
        return []

def crawl_recursive(url, depth, visited_urls, sitemap):
    if depth <= 0:
        return

    links = crawl_page(url)
    for link in links:
        if link not in visited_urls:
            visited_urls.add(link)
            sitemap[link] = {}
            crawl_recursive(link, depth - 1, visited_urls, sitemap[link])

@app.route('/crawl', methods=['POST'])
def crawl():
    global DOMAIN, DOMAIN_NAME
    data = request.json
    if 'url' not in data or 'depth' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    DOMAIN = data['url']
    CRAWL_DEPTH = int(data['depth'])
    DOMAIN_NAME = tldextract.extract(DOMAIN).domain

    visited_urls = set()
    sitemap = {}

    crawl_recursive(DOMAIN, CRAWL_DEPTH, visited_urls, sitemap)

    response_data = {'domain': DOMAIN, 'crawl_depth': CRAWL_DEPTH, 'sitemap': sitemap}

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
