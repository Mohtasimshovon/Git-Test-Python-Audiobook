import pyttsx3
import  PyPDF2
book= open('oop.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
shovon= pyttsx3.init()
for num in range(4,pages):
    page=pdfReader.getPage(7)
    text=page.extractText()
    shovon.say('sabbir likes Barovatari, he is a foolfuck at 6th grade')
    shovon.runAndWait()