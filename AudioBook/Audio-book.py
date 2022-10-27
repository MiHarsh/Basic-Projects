#Importing Google Text to Speech library
from gtts import gTTS
import PyPDF2
File = open('file.pdf', 'rb') 

#Create PDF Reader Object
pdf_R = PyPDF2.PdfFileReader(File)
# counts number of pages in pdf
pages = pdf_R.numPages 
textList = []

#Extracting text data from each page of the pdf file
for i in range(0,pages):
   try:
    page = pdf_R.getPage(i)    
    textList.append(page.extractText())
   except:
       pass

#Converting multiline text to single line text
textString = " ".join(textList)
language = 'en'
myAudio = gTTS(text=textString, lang=language, slow=False)

#Save as mp3 file
myAudio.save("Audio.mp3")
