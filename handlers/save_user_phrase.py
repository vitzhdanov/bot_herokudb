from data.data import data

from aiogram import types
from loader import dp
import psycopg2
from aiogram.dispatcher import filters
from datetime import datetime

SAVE_WORD = ['бот', 'сохрани']


@dp.message_handler(filters.Text(contains=SAVE_WORD))
async def phrases(message: types.Message):
    user_phrase = message.text.replace('бот', '').replace('сохрани', '')
    user_id = message.chat['id']
    user_name = message.chat['first_name'] or message.chat['username']
    date_time = datetime.now().strftime('%d-%m-%Y')

    try:
        connection = psycopg2.connect(
            host=data['host'],
            user=data['user'],
            database=data['database'],
            port=data['port'],
            password=data['password'],
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            create = """CREATE TABLE IF NOT EXISTS user_phrases (
                            id serial PRIMARY KEY, 
                            user_phrase varchar(1000) NOT NULL,
                            user_id int NOT NULL,
                            user_name varchar(100),
                            date_time varchar (100));"""
            cursor.execute(create)
            print('Table created')

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT user_phrase FROM user_phrases;"""
            )
            phrases = str(cursor.fetchall()).replace('(', '').replace(')', '').replace(',', '').replace('[', '').replace(']', '').replace("'", "").lower()
            if user_phrase.lower() not in phrases:
                insert_command = """INSERT INTO user_phrases 
                                    (user_phrase, user_id, user_name, date_time)
                                    VALUES (%s,%s,%s,%s)"""
                insert_values = (user_phrase, user_id, user_name, date_time)
                cursor.execute(insert_command, insert_values)
                await message.answer('Сохранил')
                print('Save')
            else:
                cursor.execute("""SELECT DISTINCT(date_time), user_name FROM user_phrases WHERE user_phrase=%s""", (user_phrase,))
                data_user = str(cursor.fetchall()[0]).replace('(', '').replace(')', '').replace(',', '').replace("'", '').split()
                await message.answer(f'Фраза уже была добавлена {data_user[0]} юзером {data_user[1]}')

    except Exception as ex:
        print(f'[INFO] - {ex}')
    finally:
        if connection:
            print('Connection close')
            connection.close()