#pip install "unstructured[all-docs]"


from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

# Import for vector database and creating embeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma




local_path = "./story.pdf"

# Load the PDF document from a local file
if local_path:
    pdf_loader = UnstructuredPDFLoader(local_path)
    data = pdf_loader.load()
else:
    print("Please provide a valid path to a local PDF file.")

# print(data[0].page_content)

# Split and chunk the text into smaller pieces
splitter = RecursiveCharacterTextSplitter(chunk_size=7500, overlap_size=500)
chunks = splitter.split_documents(data)

# Add to the vector database
vector_db = Chroma.from_documents(
    documents=chunks,
    embeddings=OllamaEmbeddings(model="nomic-embed-text", show_progress=True),
    collection_name="local-rag"
)


   

