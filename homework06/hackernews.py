from bottle import (
    route, run, template, request, redirect
)

from scraputils import get_news
from db import News, session
from bayes import NaiveBayesClassifier


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('homework06/news_template', rows=rows)


@route("/add_label/")
def add_label():
    ids = request.query.get("id")
    labels = request.query.get("label")
    s = session()
    for item in s.query(News).filter(News.id == ids).all():
        item.label = labels
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    news_lst = get_news('https://news.ycombinator.com/newest', 2)
    s = session()
    for i in range(len(news_lst)):
        if len(s.query(News).filter(News.title == news_lst[i]['title'] and News.author == news_lst[i]['author']).all()) == 0:
            new_news = News(title = news_lst[i]['title'],
                            author = news_lst[i]['author'],
                            points = news_lst[i]['points'],
                            comments = news_lst[i]['comments'],
                            url = news_lst[i]['url'])
            s.add(new_news)
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    # PUT YOUR CODE HERE
    pass


if __name__ == "__main__":
    run(host="localhost", port=8888)

