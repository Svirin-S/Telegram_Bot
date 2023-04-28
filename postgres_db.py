import psycopg2


conn = psycopg2.connect(database='postgres', user='user', password='1111')
cur = conn.cursor()

def create_table(cur):
    cur.execute("""
    CREATE TABLE IF NOT exists Masters(
    id SERIAL PRIMARY KEY,
    name VARCHAR (60) not null,
    number_ VARCHAR (60),
    data VARCHAR (60) not null,
    time VARCHAR (60) not null,
    name_person VARCHAR (100) DEFAULT 0
    );
    """)


def select_Name(name, data, name_person):
    cur.execute("""
    SELECT time FROM Masters
    WHERE name=%s and data=%s and name_person=%s
    """, (name, data, name_person,))
    list_ = []
    for i in cur.fetchall():
        for a in i:
            list_.append(a)
    return list_


# print(select_Name('Петр', '21.01.01', '0'))


def update_person(name, data, time, name_person):
    # cur.execute("""
    # UPDATE Masters SET name_person=%s WHERE name=%s and data=%s and time=%s;
    # """, (name, data, time, name_person))
    # conn.commit()
    # conn.close()
    sql_update_query = """UPDATE Masters SET name_person=%s WHERE name=%s and data=%s and time=%s"""
    cur.execute(sql_update_query, (name_person, name, data, time))
    conn.commit()

# update_person('Маркуля 5559', '21.01.01', '9:00', 'Сергей')


def insert(name, number_, data, time, name_person):
    cur.execute("""
        INSERT INTO Masters(name, number_, data, time, name_person)
        VALUES (%s,%s,%s,%s,%s)
        """, (name, number_, data, time, name_person))
    conn.commit()


def delete(name):
    cur.execute("""
    DELETE FROM Masters WHERE name=%s;
    """, (name,))
    conn.commit()







