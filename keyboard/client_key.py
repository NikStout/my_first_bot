from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

yt = KeyboardButton('/Ютуб')
vk = KeyboardButton('/ВК')
tg = KeyboardButton('/ТГ')

key_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

key_client.add(yt).add(vk).insert(tg) #еще есть row(yt, vk, tg)