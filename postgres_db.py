import psycopg2


conn = psycopg2.connect(database='postgres', user='user', password='1111')
cur = conn.cursor()


def create_table():
    cur.execute("""
    CREATE TABLE IF NOT exists Masters(
    id SERIAL PRIMARY KEY,
    name VARCHAR (60) not null,
    data VARCHAR (60) not null,
    time VARCHAR (60) not null,
    name_person VARCHAR (100) DEFAULT 0,
    person_number VARCHAR (60) DEFAULT 0,
    brief_description VARCHAR (1000) DEFAULT 0
    );
    """)
    conn.commit()


# create_table()


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


def update_person(name, data, time, name_person, person_number, brief_description):
    sql_update_query = """UPDATE Masters SET name_person=%s, person_number=%s, brief_description=%s WHERE name=%s and data=%s and time=%s"""
    cur.execute(sql_update_query, (name_person, person_number, brief_description, name, data, time,))
    conn.commit()


def delete(name):
    cur.execute("""
    DELETE FROM Masters WHERE name=%s;
    """, (name,))
    conn.commit()

# delete('Петр')


def select_Name1(name, name_person, data):
    cur.execute("""
    SELECT data FROM Masters
    WHERE name=%s and name_person=%s and data>%s
    """, (name, name_person, data,))
    list_ = []
    for i in cur.fetchall():
        for a in i:
            list_.append(a)
    return sorted(set(list_))


def insert_master(name, data, time):
    cur.execute("""
    INSERT INTO Masters(name, data, time) 
    VALUES (%s,%s,%s) 
    """, (name, data, time))
    conn.commit()

# insert_master('Петр', '21.01.01', '10:00')




