from datetime import datetime, timedelta

from pregnancy_counter import PregnancyCounter
from ways_of_counting import WayOfCounting

users = []

def add_or_get_user(username: str) -> PregnancyCounter:
    user = get_user_or_none(username)
    if user is not None:
        return user
    new_user = PregnancyCounter(username=username)
    users.append(new_user)
    return new_user

def get_user_or_none(username: str) -> PregnancyCounter:
    for i in range(len(users)):
        if users[i].username == username:
            return users[i]
    return None

def update_date(user: PregnancyCounter, date: datetime):
    if user.wayOfCounting == WayOfCounting.BY_MENSTRUATION:
        user.firstDayLastMenstruation = date
    if user.wayOfCounting == WayOfCounting.BY_WC:
        user.dateOfWC = date
    if user.wayOfCounting == WayOfCounting.BY_OVULATION:
        user.ovulationDate = date
    if user.wayOfCounting == WayOfCounting.BY_ULTRASOUND:
        user.dateOfUltrasound = date

def update_timedelta(user: PregnancyCounter, duration: timedelta):
    if user.wayOfCounting == WayOfCounting.BY_MENSTRUATION:
        user.cycleLength = duration
    if user.wayOfCounting == WayOfCounting.BY_WC:
        user.durationAtWC = duration
    if user.wayOfCounting == WayOfCounting.BY_ULTRASOUND:
        user.durationAtUltrasound = duration

def count(user: PregnancyCounter):
    if user.wayOfCounting == WayOfCounting.BY_MENSTRUATION:
        user.count_birth_date_by_menstruation()
    if user.wayOfCounting == WayOfCounting.BY_WC:
        user.count_birth_date_by_wc()
    if user.wayOfCounting == WayOfCounting.BY_OVULATION:
        user.count_birth_date_by_ovulation_date()
    if user.wayOfCounting == WayOfCounting.BY_ULTRASOUND:
        user.count_birth_date_by_ultrasound()
    user.count_pregnancy_duration()



