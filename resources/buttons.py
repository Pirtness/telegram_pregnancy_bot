from telebot import types

# main keyboard
GET_BIRTH_DATE_TEXT = 'Узнать дату рождения'
GET_BIRTH_DATE_CALLBACK = 'birth_date'
GET_BIRTH_DATE_BUTTON = types.InlineKeyboardButton(text=GET_BIRTH_DATE_TEXT,
                                                   callback_data=GET_BIRTH_DATE_CALLBACK)

GET_PREGNANCY_DURATION_TEXT = 'Узнать срок беременности'
GET_PREGNANCY_DURATION_CALLBACK = 'pregnancy_duration'
GET_PREGNANCY_DURATION_BUTTON = types.InlineKeyboardButton(text=GET_PREGNANCY_DURATION_TEXT,
                                                   callback_data=GET_PREGNANCY_DURATION_CALLBACK)

# birth date or pregnancy duration
COUNT_BY_MENSTRUATION_TEXT = 'По менструации'
COUNT_BY_MENSTRUATION_CALLBACK = 'by_menstruation'
COUNT_BY_MENSTRUATION_BUTTON = types.InlineKeyboardButton(text=COUNT_BY_MENSTRUATION_TEXT,
                                                   callback_data=COUNT_BY_MENSTRUATION_CALLBACK)

COUNT_BY_ULTRASOUND_TEXT = 'По узи'
COUNT_BY_ULTRASOUND_CALLBACK = 'by_ultrasound'
COUNT_BY_ULTRASOUND_BUTTON = types.InlineKeyboardButton(text=COUNT_BY_ULTRASOUND_TEXT,
                                                   callback_data=COUNT_BY_ULTRASOUND_CALLBACK)

COUNT_BY_OVULATION_TEXT = 'По овуляции/ЭКО'
COUNT_BY_OVULATION_CALLBACK = 'by_ovulation'
COUNT_BY_OVULATION_BUTTON = types.InlineKeyboardButton(text=COUNT_BY_OVULATION_TEXT,
                                                   callback_data=COUNT_BY_OVULATION_CALLBACK)

COUNT_BY_WC_TEXT = 'По явке в ж/к'
COUNT_BY_WC_CALLBACK = 'by_wc'
COUNT_BY_WC_BUTTON = types.InlineKeyboardButton(text=COUNT_BY_WC_TEXT,
                                                   callback_data=COUNT_BY_WC_CALLBACK)