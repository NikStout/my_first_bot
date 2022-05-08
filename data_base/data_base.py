import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('base_bot.db')
    cur = base.cursor()
    if base:
        print('Подключение прошло успешно')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for yt in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, yt[0], f'{yt[1]}\nОписание: {yt[2]}\nЦена: {yt[-1]}')