
from flask import Flask, redirect, url_for, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    news_api_key = 'YOUR_API_KEY'
    news_url = f'https://newsapi.org/v2/everything?q=tesla&from=2023-03-08&to=2023-03-08&sortBy=popularity&apiKey={news_api_key}'
    response = requests.get(news_url).json()
    articles = response['articles']
    return render_template('index.html', articles=articles)

@app.route('/full-article/<article_id>')
def full_article(article_id):
    return redirect(articles[int(article_id)]['url'])

if __name__ == '__main__':
    app.run()
