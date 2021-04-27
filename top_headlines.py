from flask import Flask, render_template
app = Flask(__name__)

import secrets
import requests
import json

key = secrets.KEY

# baseurl = "https://api.nytimes.com/svc/topstories/v2/technology.json"
# params = {'api-key': key}
# response = requests.get(baseurl, params).json()
# results = response['results'][0:5]
# # print(results)
# headlines = []
# for headline in results:
#     headlines.append(headline['title'])
# print(headlines)

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/name/<name>')
def hello_name(name):
    # name = "Eva"
    return render_template('name.html',
        name=name)

@app.route('/headlines/<name>')
def display_headlines(name):
    baseurl = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    params = {'api-key': key}
    response = requests.get(baseurl, params).json()
    results = response['results']
    headlines = []
    for headline in results:
        headlines.append(headline['title'])
    # print(headlines)
    return render_template('headlines.html', name=name, headlines=headlines)

if __name__ == '__main__':  
    app.run(debug=True)