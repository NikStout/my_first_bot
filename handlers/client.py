from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboard import key_client
from data_base import data_base


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите интересующий вас курс', reply_markup=key_client)


async def get_youtube(message: types.Message):
    await data_base.sql_read(message)


async def get_vk(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали курс по ВК')


async def get_tg(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали курс по Телеграм')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(get_youtube, commands=['Ютуб'])
    dp.register_message_handler(get_vk, commands=['ВК'])
    dp.register_message_handler(get_tg, commands=['ТГ'])
