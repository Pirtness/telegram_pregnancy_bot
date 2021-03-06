import resources.buttons as btns
from telebot import types

MAIN_KEYBOARD_WIDTH = 1
MAIN_KEYBOARD = types.InlineKeyboardMarkup(row_width=MAIN_KEYBOARD_WIDTH)
MAIN_KEYBOARD.add(btns.GET_BIRTH_DATE_BUTTON, btns.GET_PREGNANCY_DURATION_BUTTON)

WAY_OF_COUNTING_KEYBOARD_WIDTH = 1
WAY_OF_COUNTING_KEYBOARD = types.InlineKeyboardMarkup(row_width=MAIN_KEYBOARD_WIDTH)
WAY_OF_COUNTING_KEYBOARD.add(btns.COUNT_BY_MENSTRUATION_BUTTON, btns.COUNT_BY_ULTRASOUND_BUTTON,
                             btns.COUNT_BY_OVULATION_BUTTON, btns.COUNT_BY_WC_BUTTON)