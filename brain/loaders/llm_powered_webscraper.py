from langchain_community.document_loaders import AsyncChromiumLoader
from langchain.chains.openai_functions import create_extraction_chain
from langchain_ollama import OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from bs4 import BeautifulSoup
from os import environ

environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

phi3 = OllamaLLM(model="phi3:mini")

splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=0
)

EXTRACTION_TEMPLATE = """Extract the article content from the given input.

Article:
{input}

Content:
""" 

extraction_prompt = ChatPromptTemplate.from_template(EXTRACTION_TEMPLATE)

chain = extraction_prompt | phi3 | StrOutputParser()


def extract(content: str):
    return chain.invoke({"input": content})

def scrape_with_playwright(url):
    loader = AsyncChromiumLoader(urls=[url])
    docs = loader.load()
    doc = docs[0]

    soup = BeautifulSoup(doc.page_content, 'html.parser')
    target_div = soup.find('div', class_='main-content mt-8')

    if not target_div:
        return
    
    article_content = target_div.get_text(strip=True)
    
    splits = splitter.split_text(article_content)
    print(len(splits))
    extracted_content = extract(content=splits[0])
    print(extracted_content)
    return extracted_content

if __name__ == "__main__":
    url = "https://freedium.cfd/https://medium.com/p/6ed96005c81f"
    extracted_content = scrape_with_playwright(url)


