from datetime import datetime
import users
import wait_for_input
from message_parser import parse_date, parse_timedelta, timedelta_as_weeks_and_days
from message_send import ask_client_input
from pregnancy_counter import PregnancyCounter
from actions import Action
from wait_for_input import WaitForInput
from wait_for_input_controller import next_step
from ways_of_counting import WayOfCounting
from bot import bot
from telebot import types
import resources.keyboards as kbs
import resources.buttons as btns
import resources.messages as msgs
from users import *

@bot.message_handler(content_types=["text"])
def any_msg(message):
    user = get_user_or_none(message.from_user.username)
    if user is not None:
        accepted = False
        if user.waitForInput == WaitForInput.DATE:
            accepted, date = wait_for_date_handler(message)
            if accepted:
                update_date(user, date)
        if user.waitForInput == WaitForInput.TIMEDELTA:
            accepted, duration = wait_for_timedelta_handler(message)
            if accepted:
                update_timedelta(user, duration)

        if accepted:
            next_step(user)
            if user.waitForInput is not None:
                if user.waitForInput == WaitForInput.HAS_EVERYTHING:
                    count(user)
                ask_client_input(message.chat.id, user)
                return

    add_or_get_user(message.from_user.username)
    bot.send_message(message.chat.id, msgs.CHOOSE_ACTION, reply_markup=kbs.MAIN_KEYBOARD)

@bot.callback_query_handler(func=lambda call: call.data == btns.GET_BIRTH_DATE_CALLBACK or
                            call.data == btns.GET_PREGNANCY_DURATION_CALLBACK)
def callback_inline(call):
    pc = add_or_get_user(call.message.from_user.username)
    msg_text = None
    if call.data == btns.GET_BIRTH_DATE_CALLBACK:
        msg_text = msgs.CHOOSE_WAY_OF_COUNTING_BIRTH_DATE
        pc.action = Action.GET_BIRTH_DATE
    elif call.data == btns.GET_PREGNANCY_DURATION_CALLBACK:
        msg_text = msgs.CHOOSE_WAY_OF_COUNTING_PREGNANCY_DURATION
        pc.action = Action.GET_PREGNANCY_DURATION
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=msg_text, reply_markup=kbs.WAY_OF_COUNTING_KEYBOARD)

@bot.callback_query_handler(func=lambda call: call.data == btns.COUNT_BY_WC_CALLBACK or
                            call.data == btns.COUNT_BY_MENSTRUATION_CALLBACK or
                            call.data == btns.COUNT_BY_OVULATION_CALLBACK or
                            call.data == btns.COUNT_BY_ULTRASOUND_CALLBACK)
def callback_inline1(call):
    user = get_user_or_none(call.message.chat.username)
    if call.data == btns.COUNT_BY_WC_CALLBACK:
        user.waitForInput = WaitForInput.DATE
        user.wayOfCounting = WayOfCounting.BY_WC
    if call.data == btns.COUNT_BY_MENSTRUATION_CALLBACK:
        user.waitForInput = WaitForInput.DATE
        user.wayOfCounting = WayOfCounting.BY_MENSTRUATION
    if call.data == btns.COUNT_BY_OVULATION_CALLBACK:
        user.waitForInput = WaitForInput.DATE
        user.wayOfCounting = WayOfCounting.BY_OVULATION
    if call.data == btns.COUNT_BY_ULTRASOUND_CALLBACK:
        user.waitForInput = WaitForInput.DATE
        user.wayOfCounting = WayOfCounting.BY_ULTRASOUND
    ask_client_input(call.message.chat.id, user)

def wait_for_date_handler(message) -> (bool, datetime):
    date, answer = parse_date(message.text)
    if date is None:
        bot.send_message(message.chat.id, answer)
        return False, None
    else:
        bot.send_message(message.chat.id, msgs.DATE_ACCEPTED + date.strftime(msgs.DATE_OUTPUT_FORMAT))
        return True, date

def wait_for_timedelta_handler(message) -> (bool, timedelta):
    duration, answer = parse_timedelta(message.text)
    if duration is None:
        bot.send_message(message.chat.id, answer)
        return False, None
    else:
        text = timedelta_as_weeks_and_days(duration)
        bot.send_message(message.chat.id, msgs.DATE_ACCEPTED + text)
        return True, duration



