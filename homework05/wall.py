import pandas as pd
import requests
import config
import pymorphy2
import gensim
from gensim.models import LdaModel, LdaMulticore
from nltk.corpus import stopwords
import pyLDAvis.gensim


def get_wall(
    owner_id: str = '',
    domain: str = '',
    offset: int = 0,
    count: int = 150,
    filter: str = 'owner',
    extended: int = 0,
    fields: str = '',
    v: str = '5.103'
) -> pd.DataFrame:
    """
    Возвращает список записей со стены пользователя или сообщества.

    @see: https://vk.com/dev/wall.get

    :param owner_id: Идентификатор пользователя или сообщества, со стены которого необходимо получить записи.
    :param domain: Короткий адрес пользователя или сообщества.
    :param offset: Смещение, необходимое для выборки определенного подмножества записей.
    :param count: Количество записей, которое необходимо получить (0 - все записи).
    :param filter: Определяет, какие типы записей на стене необходимо получить.
    :param extended: 1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах.
    :param fields: Список дополнительных полей для профилей и сообществ, которые необходимо вернуть.
    :param v: Версия API.
    """
    v = config.VK_CONFIG['version']
    access_token = config.VK_CONFIG['access_token']
    code = """return API.wall.get({
        "owner_id": "%s",
        "domain": "%s",
        "offset": "%d",
        "count": "%d",
        "filter": "%s",
        "extended": "%d",
        "fields": "%s",
        "v": "%s"
    });""" % (owner_id, domain, offset, count, filter, extended, fields, v)
    response = requests.post(
        url="https://api.vk.com/method/execute",
            data={
                "code": code,
                "access_token": config.VK_CONFIG['access_token'],
                "v": config.VK_CONFIG['version']
            }
    )
    return pd.DataFrame(response.json()['response']['items'])


data = get_wall(owner_id='-81828545')
data_new = get_wall(owner_id='-64257238')
data = data.append(data_new, ignore_index=True)
data_new = get_wall(owner_id='-40390678')
data = data.append(data_new, ignore_index=True)
data_new = get_wall(owner_id='-32978078')
data = data.append(data_new, ignore_index=True)
data_new = get_wall(owner_id='-137331446')
data = data.append(data_new, ignore_index=True)
posts = []
morph = pymorphy2.MorphAnalyzer()
letters = set()
for i in range(ord("a"), ord("z") + 1):
    letters.update(chr(i))
for i in range(ord("а"), ord("я") + 1):
    letters.update(chr(i))
letters.update("ё")
stop_words = stopwords.words("russian")
symbols = {'.', ',', ';', ':', '-', '—', '–', '"', "'", "`", "?", "!"}
for i in range(len(data)):
    st = data['text'][i]
    st = str(st)
    temp = []
    for word in st.split():
        word = morph.parse(word)[0]
        if ('NOUN' in word.tag):
            word = word.normal_form
            if word not in stop_words:
                k = 0
                temp_word = ''
                for letter in word:
                    if letter in letters:
                        temp_word += letter
                    elif (letter not in letters) and (letter not in symbols):
                        k = 1
                if k == 0:
                    temp.append(temp_word)
            posts.append(temp)
dictionary = gensim.corpora.Dictionary(posts)
mycorpus = [dictionary.doc2bow(doc) for doc in posts]
lda_model = gensim.models.ldamodel.LdaModel(corpus=mycorpus,
                                           id2word=dictionary,
                                           num_topics=3,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)
vis = pyLDAvis.gensim.prepare(lda_model, mycorpus, dictionary)
pyLDAvis.show(vis)
