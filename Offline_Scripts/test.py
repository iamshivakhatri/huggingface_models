import PyPDF2

# def extract_text_from_pdf(pdf_path, txt_path):
#     # Open the PDF file
    
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         # Create a text file to save the extracted text
#         with open(txt_path, 'w', encoding='utf-8') as text_file:
#             # Iterate over each page
#             for page_num in range(len(reader.pages)):
#                 print(f"Total number of pages: {len(reader.pages)}")
#                 print(f"Extracting text from page {page_num + 1}...")
#                 # Get the page
#                 page = reader.pages[page_num]
#                 # Extract text from the page
#                 text = page.extract_text()
#                 print(f"Extracted text: {text}")
#                 if text:  # Ensure the extracted text is not None
#                     # Write the text to the text file
#                     text_file.write(text)
#                     text_file.write('\n')  # Add a newline for readability
#     print(f"Opening PDF file: {pdf_path}")

def extract_text_from_pdf(pdf_path, txt_path):
    print(f"Opening PDF file: {pdf_path}")
    
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            print(f"Total number of pages: {len(reader.pages)}")
            
            # Create a text file to save the extracted text
            with open(txt_path, 'w', encoding='utf-8') as text_file:
                # Iterate over each page
                for page_num in range(len(reader.pages)):
                    print(f"Extracting text from page {page_num + 1}...")
                    # Get the page
                    page = reader.pages[page_num]
                    # Extract text from the page
                    text = page.extract_text()
                    print(f"Extracted text: {text}")
                    if text:  # Ensure the extracted text is not None
                        # Write the text to the text file
                        text_file.write(text)
                        text_file.write('\n')  # Add a newline for readability
                    else:
                        print(f"No text found on page {page_num + 1}")
    except Exception as e:
        print(f"Error opening or reading PDF file: {e}")

if __name__ == "__main__":
    # pdf_path = "Offline_Scripts/The_Intelligent_Investor.pdf"  # Replace with your PDF file path
    pdf_path = "Offline_Scripts/story.pdf"
    txt_path = "output_text_file.txt"  # Replace with the desired output text file path
    extract_text_from_pdf(pdf_path, txt_path)
    print(f"Text extracted and saved to {txt_path}")
