from langchain_ollama.chat_models import ChatOllama
from langchain_community.embeddings import Model2vecEmbeddings

llm = ChatOllama(model="phi3:mini")
embeddings = Model2vecEmbeddings("minishlab/potion-base-8M")