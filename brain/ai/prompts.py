from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from llm import phi3


EXTRACTION_TEMPLATE = """Extract the article content from the given input.

Article:
{input}

Content:
"""

extraction_prompt = ChatPromptTemplate.from_template(EXTRACTION_TEMPLATE)

chain = extraction_prompt | phi3 | StrOutputParser()