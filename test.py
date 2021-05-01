import requests
import PyPDF2
URL = "https://api.meaningcloud.com/summarization-1.0"

pdfFileObj = open('Resume.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
x=pageObj.extractText()
txt=x
key="73753b7cbc31fb6c4969cdd4f428d58d"
sentences=6
PARAMS = {"key":key,"txt":txt, "sentences":sentences}
r = requests.get(url = URL, params = PARAMS)
data = r.json()
print(data['summary'])