from bottle import (
    route, run, template, request, redirect
)

from scraputils import get_news
from db import News, session
from bayes import NaiveBayesClassifier
import string


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
    news_lst = get_news('https://news.ycombinator.com/newest', 5)
    s = session()
    for i in range(len(news_lst)):
        if len(s.query(News).filter(News.title == news_lst[i]['title']).filter(News.author == news_lst[i]['author']).all()) == 0:
            new_news = News(title=news_lst[i]['title'],
                            author=news_lst[i]['author'],
                            points=news_lst[i]['points'],
                            comments=news_lst[i]['comments'],
                            url=news_lst[i]['url'])
            s.add(new_news)
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    X, y, info = [], [], []
    s = session()
    for i in range(1001):
        for item in s.query(News).filter(News.id == i).all():
            X.append(item.title)
            y.append(item.label)
    X_test = []
    for i in range(1001, len(s.query(News).all()) + 1):
        for item in s.query(News).filter(News.id == i).all():
            X_test.append(item.title)
            info.append(News(author=item.author,
                             points=item.points,
                             comments=item.comments,
                             url=item.url))
    X = [x.translate(str.maketrans("", "", string.punctuation)).lower() for x in X]
    X_cleared = [x.translate(str.maketrans("", "", string.punctuation)).lower() for x in X_test]
    model = NaiveBayesClassifier(alpha=0.01)
    model.fit(X, y)
    predicted_news = model.predict(X_cleared)
    classified_news = []
    for i in range(len(predicted_news)):
        classified_news.append([y[i], X_test[i], info[i]])
    classified_news = sorted(classified_news, key=lambda item: item[0])
    return template('homework06/news_recommendations', rows=classified_news)


if __name__ == "__main__":
    run(host="localhost", port=8080)
