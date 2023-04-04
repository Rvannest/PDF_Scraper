
import PyPDF2
import re

# Replace with your PDF file path
path = 'C:\\Users\\R\\Downloads\\budget-2023-en.pdf'

pdf_file = open(path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
page_text = ''

# Extract text
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    page_text += page.extract_text()

# Search for the keyword (in this case its "provide $") and extract the 30 words before and after it
keyword = r'provide \$\d+(?:\.\d+)?\s\w+\s\w+'
pattern = re.compile(r'((?:\S+\s+){0,30})(' + keyword + r')((?:\s+\S+){0,30})')
matches = pattern.findall(page_text)

# Print each sentence on a new line
for match in matches:
    sentence = ''.join(match).strip()
    sentence = re.sub(r'\s+', ' ', sentence)
    print(f"{sentence}\n")
