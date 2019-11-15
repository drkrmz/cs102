import requests
import config
import telebot
from bs4 import BeautifulSoup
from typing import List, Tuple
import datetime

telebot.apihelper.proxy = {'https': 'https://45.71.113.187:3128'}
bot = telebot.TeleBot(config.access_token)


def get_page(group, week):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain,
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page

def schedule(soup, day):
    schedule_table = soup.find("table", attrs={"id": day})
    if schedule_table is None:
        return None, None, None
    else:
        times_list = schedule_table.find_all("td", attrs={"class": "time"})
        times_list = [time.span.text for time in times_list]

        locations_list = schedule_table.find_all("td", attrs={"class": "room"})
        locations_list = [room.span.text for room in locations_list]

        lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
        lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
        lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]
    return(times_list, locations_list, lessons_list)

@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """
    day, group, week = message.text.split()
    if day == '/monday' or day == '/sunday':
        day = '1day'
    elif day == '/tuesday':
        day = '2day'
    elif day == '/wednesday':
        day = '3day'
    elif day == '/thursday':
        day = '4day'
    elif day == '/friday':
        day = '5day'
    else:
        day = '6day'
    web_page = get_page(group, week)
    soup = BeautifulSoup(web_page, "html5lib")
    times_list, locations_list, lessons_list = schedule(soup, day)
    if times_list is None:
        resp = "\nВ этот день занятий нет\n"
    else:
        resp = ''
        for time, location, lession in zip(times_list, locations_list, lessons_list):
            resp += '<b>{}</b>, {}, {}\n'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    weekday = datetime.datetime.isoweekday(datetime.datetime.now())
    time = datetime.datetime.now().time()
    _, group, week = message.text.split()
    web_page = get_page(group, week)
    soup = BeautifulSoup(web_page, "html5lib")
    next_day = 0
    day = str(weekday)+'day'
    times_list, locations_list, lessons_list = schedule(soup, day)
    hours_lst = [[]]
    minutes_lst = [[]]
         

    


@bot.message_handler(commands=['tomorrow'])
def get_tomorrow(message):
    """ Получить расписание на следующий день """
    weekday = datetime.datetime.isoweekday(datetime.datetime.now())+1
    _, group, week = message.text.split()
    web_page = get_page(group, week)
    soup = BeautifulSoup(web_page, "html5lib")
    day = str(weekday)+'day'
    weekdays = {1:'Понедельник', 2:'Вторник', 3:'Среда', 4:'Четверг', 5:'Пятница', 6:'Суббота', 7:'Воскресенье'}
    resp = ''
    times_list, locations_list, lessons_list = schedule(soup, day)
    while times_list is None:
        resp += '\n<b>{}</b>\nВ этот день занятий нет\n'.format(weekdays[weekday])
        weekday += 1
        if weekday > 7:
            weekday = 1
        day = str(weekday)+'day'
        times_list, locations_list, lessons_list = schedule(soup, day)
    resp += '\n<b>{}</b>\n'.format(weekdays[weekday])
    for time, location, lession in zip(times_list, locations_list, lessons_list):
        resp += '\n<b>{}</b>, {}, {}'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    _, group, week = message.text.split()
    web_page = get_page(group, week)
    soup = BeautifulSoup(web_page, "html5lib")
    resp = ''
    weekdays = {1:'Понедельник', 2:'Вторник', 3:'Среда', 4:'Четверг', 5:'Пятница', 6:'Суббота'}
    for i in range(1, 7):
        day = str(i)+'day'
        resp += '\n<b>{}</b>\n'.format(weekdays[i])
        times_list, locations_list, lessons_list = schedule(soup, day)
        if times_list is None:
            resp += "\nВ этот день занятий нет\n"
        else:
            for time, location, lession in zip(times_list, locations_list, lessons_list):
                resp += '\n<b>{}</b>, {}, {}'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)