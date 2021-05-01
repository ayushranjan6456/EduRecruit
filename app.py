from flask import Flask,request, url_for, redirect, render_template
import PyPDF2
import requests
URL = "https://api.meaningcloud.com/summarization-1.0"
app = Flask(__name__)


@app.route('/summarise')
def summarise_form():
    return render_template("summarise.html")


@app.route('/summarise', methods = ['POST'])
def summrise():
    if request.method == 'POST':
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
        return render_template("summarise.html", name=data['summary'])


@app.route('/evaluate')
def upload():
    return render_template("evaluate.html")

@app.route('/evaluate', methods = ['POST'])
def evaluate():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        f.save(f.filename)
        pdfFileObj = open(f.filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        print(pdfReader.numPages)
        pageObj = pdfReader.getPage(0)
        x=pageObj.extractText().split(" ")
        for i in x:
            if('.org' in i or '.com' in i):
                print(i)
                break
        i=i[:-8]
        # closing the pdf file object
        pdfFileObj.close()
        return render_template("evaluate.html", name=i)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


