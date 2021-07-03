from actions import Action
from bot import bot
import resources.messages as msgs
from message_parser import timedelta_as_weeks_and_days
from pregnancy_counter import PregnancyCounter
from wait_for_input import WaitForInput
from ways_of_counting import WayOfCounting


def ask_client_input(chat_id, user: PregnancyCounter):
    if user.waitForInput == WaitForInput.HAS_EVERYTHING:
        bot.send_message(chat_id, msgs.COUNTED_BIRTH_DATE + user.birthDate.strftime(msgs.DATE_OUTPUT_FORMAT))
        bot.send_message(chat_id, msgs.COUNTED_PREGNANCY_DURATION + timedelta_as_weeks_and_days(user.pregnancyDuration))
        return
    if user.wayOfCounting == WayOfCounting.BY_MENSTRUATION:
        ask_client_input_menstruation(chat_id, user)
    if user.wayOfCounting == WayOfCounting.BY_OVULATION:
        ask_client_input_ovulation(chat_id, user)
    if user.wayOfCounting == WayOfCounting.BY_ULTRASOUND:
        ask_client_input_ultrasound(chat_id, user)
    if user.wayOfCounting == WayOfCounting.BY_WC:
        ask_client_input_wc(chat_id, user)

def ask_client_input_menstruation(chat_id, user: PregnancyCounter):
    if user.waitForInput == WaitForInput.DATE:
        bot.send_message(chat_id, msgs.ASK_DATE_OF_MENSTRUATION)
        return
    if user.waitForInput == WaitForInput.TIMEDELTA:
        bot.send_message(chat_id, msgs.ASK_TIMEDELTA_OF_MENSTRUATION)
        return

def ask_client_input_ovulation(chat_id, user: PregnancyCounter):
    if user.waitForInput == WaitForInput.DATE:
        bot.send_message(chat_id, msgs.ASK_DATE_OF_OVULATION)
        return

def ask_client_input_ultrasound(chat_id, user: PregnancyCounter):
    if user.waitForInput == WaitForInput.DATE:
        bot.send_message(chat_id, msgs.ASK_DATE_OF_ULTRASOUND)
        return
    if user.waitForInput == WaitForInput.TIMEDELTA:
        bot.send_message(chat_id, msgs.ASK_TIMEDELTA_OF_ULTRASOUND)
        return

def ask_client_input_wc(chat_id, user: PregnancyCounter):
    if user.waitForInput == WaitForInput.DATE:
        bot.send_message(chat_id, msgs.ASK_DATE_OF_WC)
        return
    if user.waitForInput == WaitForInput.TIMEDELTA:
        bot.send_message(chat_id, msgs.ASK_TIMEDELTA_OF_WC)
        return

