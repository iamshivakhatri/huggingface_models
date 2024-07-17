#pip install "unstructured[all-docs]"


from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader


local_path = "./story.pdf"

# Load the PDF document from a local file
if local_path:
    pdf_loader = UnstructuredPDFLoader(local_path)
    data = pdf_loader.load()
else:
    print("Please provide a valid path to a local PDF file.")

print(data[0].page_content)


