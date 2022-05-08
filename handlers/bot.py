from aiogram.utils import executor
from create_bot import dp
from data_base import data_base


async def on_startup(_):
    print('Бот онлайн')
    data_base.sql_start()


from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
