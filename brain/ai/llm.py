from langchain_ollama import OllamaLLM
# from langchain_ollama.chat_models import ChatOllama
from langchain_community.embeddings import Model2vecEmbeddings

phi3 = OllamaLLM(model="phi3:mini")
embeddings = Model2vecEmbeddings("minishlab/potion-base-8M")
