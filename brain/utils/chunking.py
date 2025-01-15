from chonkie import SemanticChunker

# Basic initialization with default parameters
chunker = SemanticChunker(
    embedding_model="minishlab/potion-base-8M",  # Default model
    threshold=0.5,                               # Similarity threshold (0-1) or (1-100) or "auto"
    chunk_size=512,                              # Maximum tokens per chunk
    min_sentences=1                              # Initial sentences per chunk
)
