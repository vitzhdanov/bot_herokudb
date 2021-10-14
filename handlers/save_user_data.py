from aiogram import types
from loader import dp
import psycopg2
from data.data import *


@dp.message_handler(commands=['start'])
async def test(message: types.Message):
    user_id = message.chat['id']
    user_name = message.chat['first_name']
    user_nick = message.chat['username'] or message.chat['first_name']
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
            create = """CREATE TABLE IF NOT EXISTS user_data (
                            id serial PRIMARY KEY, 
                            user_id int NOT NULL,
                            user_name varchar(100),
                            user_nick varchar (100));"""
            cursor.execute(create)
            print('Table created')

        with connection.cursor() as cursor:
            cursor.execute("""SELECT user_id FROM user_data;""")
            if str(user_id) not in str(cursor.fetchall()):
                insert_command = """INSERT INTO user_data (user_id, user_name, user_nick) VALUES (%s, %s, %s)"""
                insert_values = (user_id, user_name, user_nick,)
                cursor.execute(insert_command, insert_values)
                print('Insert success')
            else:
                print('Already inserted')

        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM user_data;""")
            print(cursor.fetchall())

    except Exception as ex:
        print(f'[INFO] - {ex}')
    finally:
        if connection:
            print('Connection close')
            connection.close()