from datetime import *
import resources.messages as msgs

import config


def parse_date(text: str) -> (datetime, str):
    month = get_month_number_from_text(text)
    numbers = get_all_numbers_from_string(text)
    if len(numbers) == 0:
        return None, msgs.DATE_CANNOT_FIND_DIGITS
    now = datetime.now()
    try:
        if month == -1:
            if len(numbers) == 1:
                return datetime(now.year, now.month, numbers[0]), ''
            if len(numbers) == 2:
                return datetime(now.year, numbers[1], numbers[0]), ''
            if len(numbers) == 3:
                if numbers[0] > 999:
                    return datetime(numbers[0], numbers[2], numbers[1]), ''
                if numbers[1] > 999:
                    return datetime(numbers[1], numbers[2], numbers[0]), ''
                if numbers[2] > 999:
                    return datetime(numbers[2], numbers[1], numbers[0]), ''
                return datetime(2000 + numbers[2], numbers[1], numbers[0]), ''

        if len(numbers) == 1:
            return datetime(now.year, month, numbers[0]), ''
        if len(numbers) == 2:
            if numbers[0] > 999:
                return datetime(numbers[0], month, numbers[1]), ''
            if numbers[1] > 999:
                return datetime(numbers[1], month, numbers[0]), ''
            return datetime(2000 + numbers[1], month, numbers[0]), ''
    except:
        return None, msgs.DATE_CANNOT_PARSE

    return None, msgs.DATE_CANNOT_PARSE

def parse_timedelta(text: str) -> (timedelta, str):
    numbers = get_all_numbers_from_string(text)
    try:
        if len(numbers) == 2:
            return timedelta(weeks=numbers[0], days=numbers[1]), ''
        if len(numbers) == 1:
            if 'нед' in text:
                return timedelta(weeks=numbers[0]), ''
            return timedelta(days=numbers[0]), ''
    except:
        return None, msgs.TIMEDELTA_CANNOT_PARSE
    return None, msgs.TIMEDELTA_CANNOT_PARSE


def get_all_numbers_from_string(text: str) -> list:
    numbers = []
    i = 0
    while i < len(text):
        number = ''
        while i < len(text) and not text[i].isdigit():
            i += 1

        while i < len(text) and text[i].isdigit():
            number += text[i]
            i += 1
        if len(number) > 0:
            numbers.append(int(number))
    return numbers

def get_month_number_from_text(text: str) -> int:
    months = ['январ', 'феврал', 'март', 'апрел', 'ма', 'июн', 'июл', 'август', 'сентябр', 'октябр', 'ноябр', 'декабр']
    text = text.lower()
    for i in range(len(months)):
        if months[i] in text:
            return i+1
    return -1

def timedelta_as_weeks_and_days(duration: timedelta) -> str:
    text = ''
    weeks = str(duration.days // 7)
    days = str(duration.days % 7)
    if weeks != '0' and days != '0':
        text = weeks + ' нед, ' + days + ' дн'
    elif weeks != '0' and days == '0':
        text = weeks + ' нед'
    else:
        text = days + ' дн'
    return text

