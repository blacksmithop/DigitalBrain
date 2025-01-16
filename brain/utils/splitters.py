from langchain_text_splitters import RecursiveCharacterTextSplitter

token_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=0
)
