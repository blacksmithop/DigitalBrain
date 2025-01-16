from langchain_community.document_loaders import AsyncChromiumLoader
from bs4 import BeautifulSoup
# from utils import token_splitter
from os import environ
import re

# Playright
environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
)
# Regex
HTML_CLEANER = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(HTML_CLEANER, '', raw_html)
  return cleantext


def scrape_with_playwright(url):
    loader = AsyncChromiumLoader(urls=[url])
    docs = loader.load()
    doc = docs[0]

    soup = BeautifulSoup(doc.page_content, "html.parser")
    target_div = soup.find("div", class_="main-content mt-8")

    if not target_div:
        return

    article_content = target_div.get_text(strip=True)

    splits = token_splitter.split_text(article_content)

    cleaned_content = [cleanhtml(content) for content in splits]
    article_content = " ".join(cleaned_content)
    return article_content


if __name__ == "__main__":
    url = "https://freedium.cfd/https://medium.com/p/6ed96005c81f"
    extracted_content = scrape_with_playwright(url)
    print(extracted_content)