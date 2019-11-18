import requests
import config
import telebot
from bs4 import BeautifulSoup
from typing import List, Tuple
import datetime

telebot.apihelper.proxy = {'https': 'https://149.56.106.104:3128'}
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
        return None, None, None, None
    else:
        times_list = schedule_table.find_all("td", attrs={"class": "time"})
        times_list = [time.span.text for time in times_list]

        locations_list = schedule_table.find_all("td", attrs={"class": "room"})
        locations_list = [room.span.text for room in locations_list]
        
        rooms_list = schedule_table.find_all("dd", attrs={"class": "rasp_aud_mobile"})
        rooms_list = [room.text + ',' if room.text != '' else room.text for room in rooms_list ]

        lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
        lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
        lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]

    return times_list, locations_list, rooms_list, lessons_list


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """
    day, group, week = message.text.split()
    week_number = {'0', '1', '2'}
    if week not in week_number:
        resp = '\nНеверный номер недели\n'
    else:
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
        if soup.find(class_='rasp_day') is None:
            resp = '\nНеверный номер группы\n'
        else:
            times_list, locations_list, rooms_list, lessons_list = schedule(soup, day)
            if times_list is None:
                resp = "\nВ этот день занятий нет\n"
            else:
                resp = ''
                for time, location, room, lession in zip(times_list, locations_list, rooms_list, lessons_list):
                    resp += '<b>{}</b>, {}, {} {}\n'.format(time, location, room, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    weekday = datetime.datetime.isoweekday(datetime.datetime.now())
    _, group, week = message.text.split()
    week_number = {'0', '1', '2'}
    if week not in week_number:
        resp = '\nНеверный номер недели\n'
    else:
        web_page = get_page(group, week)
        soup = BeautifulSoup(web_page, "html5lib")
        day = str(weekday)+'day'
        if soup.find(class_='rasp_day') is None:
            resp = '\nНеверный номер группы\n'
        else:
            times_list, locations_list, rooms_list, lessons_list = schedule(soup, day)
            if times_list is None:
                resp = '\nСегодня пар больше нет\n'
            else:
                time = datetime.datetime.now().time()
                hours = []
                minutes = []
                for i in range(len(times_list)):
                    hours.append(int(times_list[i][0]+times_list[i][1]))
                    minutes.append(int(times_list[i][3]+times_list[i][4]))
                if time.hour > hours[len(hours)-1] or time.hour == hours[len(hours)-1] and time.minute >= minutes[len(minutes)-1]:
                    resp = '\nСегодня пар больше нет\n'
                else:
                    i = 0
                    while i < len(hours):
                        if hours[i] > time.hour or hours[i] == time.hour and minutes[i] > time.minute:
                            x = i
                            i = len(hours)
                        else:
                            i += 1
                    resp = ''
                    zip(times_list, locations_list, rooms_list, lessons_list)
                    resp += '\n<b>{}</b>, {}, {} {}'.format(times_list[x], locations_list[x], rooms_list[x], lessons_list[x])
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['tomorrow'])
def get_tomorrow(message):
    """ Получить расписание на следующий день """
    weekday = datetime.datetime.isoweekday(datetime.datetime.now())+1
    _, group, week = message.text.split()
    week_number = {'0', '1', '2'}
    if week not in week_number:
        resp = '\nНеверный номер недели\n'
    else:
        web_page = get_page(group, week)
        soup = BeautifulSoup(web_page, "html5lib")
        if soup.find(class_='rasp_day') is None:
            resp = '\nНеверный номер группы\n'
        else:
            day = str(weekday)+'day'
            weekdays = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
            resp = ''
            times_list, locations_list, rooms_list, lessons_list = schedule(soup, day)
            while times_list is None:
                resp += '\n<b>{}</b>\nВ этот день занятий нет\n'.format(weekdays[weekday])
                weekday += 1
                if weekday > 7:
                    weekday = 1
                    if week == '1':
                        week = '2'
                    else:
                        week = '1'
                day = str(weekday)+'day'
                times_list, locations_list, rooms_list, lessons_list = schedule(soup, day)
            resp += '\n<b>{}</b>\n'.format(weekdays[weekday])
            for time, location, room, lession in zip(times_list, locations_list, rooms_list, lessons_list):
                resp += '\n<b>{}</b>, {}, {} {}'.format(time, location, room, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    _, group, week = message.text.split()
    week_number = {'0', '1', '2'}
    if week not in week_number:
        resp = '\nНеверный номер недели\n'
    else:
        web_page = get_page(group, week)
        soup = BeautifulSoup(web_page, "html5lib")
        if soup.find(class_='rasp_day') is None:
            resp = '\nНеверный номер группы\n'
        else:
            resp = ''
            weekdays = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота'}
            for i in range(1, 7):
                day = str(i)+'day'
                resp += '\n<b>{}</b>\n'.format(weekdays[i])
                times_list, locations_list, rooms_list, lessons_list = schedule(soup, day)
                if times_list is None:
                    resp += "\nВ этот день занятий нет\n"
                else:
                    for time, location, room, lession in zip(times_list, locations_list, rooms_list, lessons_list):
                        resp += '\n<b>{}</b>, {}, {} {}'.format(time, location, room, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)
