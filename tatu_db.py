import sqlite3


conn = sqlite3.connect('bot_db.db', check_same_thread=False)
cursor = conn.cursor()


def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT exists Masters(     
    id SERIAL PRIMARY KEY, 
    name VARCHAR (60) not null, 
    number_ VARCHAR (60) 
    );
    """)

    # cursor.execute("""
    #     CREATE TABLE IF NOT exists Masters(
    #     id SERIAL PRIMARY KEY,
    #     name VARCHAR (60) not null,
    #     number_ VARCHAR (60)
    #     );
    #     """)

