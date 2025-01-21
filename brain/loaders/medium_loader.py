import requests
import xml.etree.ElementTree as ET
from brain.models import MediumArticle
from typing import List
from brain.utils import scrape_medium_url
from os import path, makedirs
from pydantic import TypeAdapter
from typing import TypeAlias
from json import dump
import logging


# URL of the RSS feed
RSS_FEED_URL = "https://medium.com/feed"

class MediumLoader:
    def __init__(self):
        pass

    # Fetch the RSS feed
    def fetch_rss_feed(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to fetch RSS feed. Status code: {response.status_code}")

    # Parse the RSS feed and extract data
    def get_medium_articles(self, feed_content):
        root = ET.fromstring(feed_content)

        medium_articles = []
        for item in root.findall(".//item"):
            title = item.find("title").text.strip()
            pub_date = item.find("pubDate").text.strip()
            guid = item.find("guid").text.strip()

            article = MediumArticle(
                title=title,
                publication_date=pub_date,
                perma_link=guid
            )
            medium_articles.append(article)

        return medium_articles
    
    def get_article_content(self, articles: List[MediumArticle]):
        for article in articles:
            perma_link = article.perma_link
            try:
                article_content = scrape_medium_url(medium_url=perma_link)
                article.content = article_content
                logging.info(type(article_content))
            except Exception as e:
                logging.info(e)
        return articles
    
    def save_medium_content(self, articles: List[MediumArticle], target_directory: str = "./hippocampus/medium"):
        if not path.exists(target_directory):
            makedirs(target_directory)
        UserList: TypeAlias = list[MediumArticle]
        UserListModel = TypeAdapter(UserList)
        json_content = UserListModel.dump_json(articles)

        file_path = path.join(target_directory, "medium_data.json")
        with open(file_path, "w") as f:
            dump(json_content, f)
            
    def initalize(self, username: str):
        # Fetch and parse the feed
        try:
            author_feed_url = f"{RSS_FEED_URL}/@{username}"
            feed_content = self.fetch_rss_feed(author_feed_url)
            # print(feed_content)
            articles = self.get_medium_articles(feed_content) # TODO: Leverage passing mutliple urls to AsyncChromiumLoader
            logging.info(f"Article: {articles[0]}")
            article_with_content = self.get_article_content(articles=articles)
            # self.save_medium_content(articles=article_with_content)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    med = MediumLoader()
    med.get_medium_articles(username="angstycoder101")