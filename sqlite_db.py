import sqlite3


conn = sqlite3.connect(database='bot.db', check_same_thread=False)
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
    WHERE name=? and data=? and name_person=?
    """, (name, data, name_person,))
    list_ = []
    for i in cur.fetchall():
        for a in i:
            list_.append(a)
    return list_


def update_person(name, data, time, name_person, person_number, brief_description):
    sql_update_query = """UPDATE Masters SET name_person=?, person_number=?, brief_description=? WHERE name=? and data=? and time=?"""
    cur.execute(sql_update_query, (name_person, person_number, brief_description, name, data, time,))
    conn.commit()

# update_person('Анастасия', '07.05.23', '9:00', 'tttt', '453453534', 'fdgdfdgf')

def delete(name):
    cur.execute("""
    DELETE FROM Masters WHERE name=?;
    """, (name,))
    conn.commit()

# delete('Петр')


def select_Name1(name, name_person, data):
    cur.execute("""
    SELECT data FROM Masters
    WHERE name=? and name_person=? and data>?
    """, (name, name_person, data,))
    list_ = []
    for i in cur.fetchall():
        for a in i:
            list_.append(a)
    return sorted(set(list_))


def insert_master(name, data, time):
    cur.execute("""
    INSERT INTO Masters(name, data, time) 
    VALUES (?,?,?) 
    """, (name, data, time))
    conn.commit()

# insert_master('Анастасия', '05.05.01', '10:00')


def select_master(name, data, name_person):
    cur.execute("""
    SELECT name, time, name_person, person_number, brief_description FROM Masters
    WHERE name=? and data=? and name_person!=?
    """, (name, data, name_person))
    list_ = []
    a = cur.fetchall()
    b = list_.append(a)
    return a

# for i in select_master('Анастасия', '05.05.23', '0'):
#     list_ = []
#     for a in i:
#         list_.append(a)
#     print(f'{list_[0]} {list_[1]} {list_[2]} {list_[3]} {list_[4]}')

# def select_master2(name, data, name_person):
#     cur.execute("""
#     SELECT name, data, time, name_person, person_number, brief_description FROM Masters
#     WHERE name=? and data>? and name_person!=?
#     """, (name, data, name_person))
#     list_ = []
#     a = cur.fetchall()
#     return a

# for a in select_master('Анастасия', '05.05.23', '0'):
#     print(a)
    
    
