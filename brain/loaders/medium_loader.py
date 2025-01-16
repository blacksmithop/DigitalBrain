import requests
import xml.etree.ElementTree as ET

# URL of the RSS feed
RSS_FEED_URL = "https://medium.com/feed"

# Fetch the RSS feed
def fetch_rss_feed(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fetch RSS feed. Status code: {response.status_code}")

# Parse the RSS feed and extract data
def parse_rss_feed(feed_content):
    root = ET.fromstring(feed_content)

    items = []
    for item in root.findall(".//item"):
        title = item.find("title").text.strip()
        pub_date = item.find("pubDate").text.strip()
        guid = item.find("guid").text.strip()
        items.append({
            "title": title,
            "published_on": pub_date,
            "medium_perma_link": guid
        })

    return items

def get_medium_publication_list(username: str):
    # Fetch and parse the feed
    try:
        author_feed_url = f"{RSS_FEED_URL}/@{username}"
        feed_content = fetch_rss_feed(author_feed_url)
        parsed_items = parse_rss_feed(feed_content)

        # Display the extracted items
        for item in parsed_items:
            print(f"Title: {item['Title']}")
            print(f"Publication Date: {item['Publication Date']}")
            print(f"GUID: {item['GUID']}")
            print("-" * 50)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_medium_publication_list(username="angstycoder101")