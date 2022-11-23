import os, sys
from flask import Flask, request, redirect, url_for
from flask.templating import render_template
#from werkzeug import secure_filename
import crawling
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crawl', methods=['GET', 'POST'])
def crawl():
    if request.method == 'POST':
        prompt = request.form['prompt']
        crawling.main(prompt)

    return redirect(url_for('result'))

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run()


'''
topics = [
    {'id':1, 'title': 'html', 'body': 'html is...'},
    {'id':2, 'title': 'css', 'body': 'css is...'},
    {'id':3, 'title': 'javascript', 'body': 'javascript is...'},
]

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f''' '''
    <!DOCTYPE html>
    <html>
    <body>
    <hl><a href="/">WEB</a></h1>
    <ol>
    {liTags}
    </ol>
    <h2>Welcome</h2>
    Hello, Web
    </body>
    </html>
    ''' '''

@app.route('/hello')
def hello():
    return 'Hello, world'

@app.route('/create')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    return 'Read' + id


app.run(debug=True)
'''