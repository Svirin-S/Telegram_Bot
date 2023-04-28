import psycopg2
from psycopg2 import Error


def update_table(name, data, time, name_person):
    try:
        # Подключиться к существующей базе данных
        conn = psycopg2.connect(database='postgres', user='user', password='1111')

        cursor = conn.cursor()
        print("Таблица до обновления записи")
        sql_select_query = """select * from Masters"""
        cursor.execute(sql_select_query)
        record = cursor.fetchone()
        print(record)

        # Обновление отдельной записи
        sql_update_query = """Update Masters set name_person = %s WHERE name=%s and data=%s and time=%s"""
        cursor.execute(sql_update_query, (name, data, time, name_person))
        conn.commit()
        count = cursor.rowcount
        print(count, "Запись успешно обновлена")

        print("Таблица после обновления записи")
        sql_select_query = """select * from Masters"""
        cursor.execute(sql_select_query)
        record = cursor.fetchone()
        print(record)
        cursor.close()
        conn.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


update_table('Петр', '21.01.01', '12:00', 'Алексей')