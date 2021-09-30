from aiogram import types
from loader import dp
import psycopg2
from data.data import *


@dp.message_handler()
async def test(message: types.Message):
    user_message = message.text
    user_id = message.chat['id']
    user_name = message.chat['first_name']
    user_nick = message.chat['username'] or message.chat['first_name']
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            create = """CREATE TABLE IF NOT EXISTS user_phrases (
                            id serial PRIMARY KEY, 
                            user_phrase varchar(1000) NOT NULL,
                            user_id int NOT NULL,
                            user_name varchar(100),
                            user_nick varchar (100),
                            date_time varchar (100));"""
            cursor.execute(create)
            print('Table created')

    except Exception as ex:
        print(f'[INFO] - {ex}')
    finally:
        if connection:
            print('Connection close')
            connection.close()