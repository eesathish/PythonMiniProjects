import PyPDF2
import pyttsx3

# Initialize the PDF reader and text-to-speech engine
pdfReader = PyPDF2.PdfReader(open('invoice.pdf', 'rb'))
speaker = pyttsx3.init()

# Accumulate all text from the PDF
full_text = ''
for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    full_text += text

# Read the full text out loud
speaker.say(full_text)
speaker.runAndWait()

# Save the speech to an audio file
speaker.save_to_file(full_text, 'audio.mp3')
speaker.runAndWait()
