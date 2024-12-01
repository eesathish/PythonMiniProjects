import PyPDF2
import os

# Check if "temp" directory exists, if not, create it
if not os.path.isdir("temp"):
    os.mkdir("temp")

txtpath = ""
pdfpath = ""

# Get the PDF file path and text file output path from the user
pdfpath = input("Enter the name of your pdf file - please use backslash when typing in directory path: ")  # Provide the path for your pdf here
txtpath = input("Enter the name of your txt file - please use backslash when typing in directory path: ")  # Provide the path for the output text file

# Define base directory for storing text files if none is specified
BASEDIR = os.path.realpath("temp")
print(BASEDIR)

# If no text path is provided, use default directory with the PDF file name
if len(txtpath) == 0:
    txtpath = os.path.join(BASEDIR, os.path.basename(os.path.normpath(pdfpath)).replace(".pdf", "") + ".txt")

# Open the PDF file in read-binary mode
with open(pdfpath, 'rb') as pdfobj:
    # Use PdfReader instead of PdfFileReader
    pdfread = PyPDF2.PdfReader(pdfobj)

    # Get the number of pages in the PDF
    x = len(pdfread.pages)

    # Loop through all pages in the PDF
    for i in range(x):
        pageObj = pdfread.pages[i]
        # Open the text file in append mode and write extracted text
        with open(txtpath, 'a+') as f:
            text = pageObj.extract_text()
            f.write(text)
            print(text)  # This just provides the overview of what is being added to your output, you can remove it if you want
