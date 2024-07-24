#pip install "unstructured[all-docs]"


from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

# Import for vector database and creating embeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Import for retrieving the text and matching the text
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever




local_path = "./story.pdf"

# Load the PDF document from a local file
if local_path:
    pdf_loader = UnstructuredPDFLoader(local_path)
    data = pdf_loader.load()
else:
    print("Please provide a valid path to a local PDF file.")

# print(data[0].page_content)

# Split and chunk the text into smaller pieces
splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=500)
chunks = splitter.split_documents(data)

# Add to the vector database
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text", show_progress=True),
    collection_name="local-rag"
)


# initialize the chat model
model = "mistral"
llm = ChatOllama(model=model)
query_prompt = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant. Your task is to generate five different versions of the given
    user question to retrieve relevant documents from a vector databse. By generating multiple perspectives on the 
    user question, your goal is to help the user overcome some of the limitations of the distance-based similarity search.
    Provide these alternative questions seperated by newlines. Original question: {question}
    """ 
)

# Retriever
retriever_from_llm = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(),
    llm, 
    prompt=query_prompt,
)

# RAG prompt
template = """Answer the question based only on the following context. If you're unsure, just say that you don't know.{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {'context': retriever_from_llm, "question": RunnablePassthrough()}
    |prompt
    |llm
    |StrOutputParser()
)

# Execute the chain and print the result
def execute_chain_and_print(question):
    result = chain.invoke(question)
    print("Answer:", result)

# Example question
question = input("Enter your question: ")
execute_chain_and_print(question)
   

