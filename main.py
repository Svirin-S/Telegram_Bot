import telebot
from telebot import types
from postgres_db import create_table, select_Name, update_person, select_Name1

data1 = ''
time1 = ''
name_person1 = ''
master = ''


TOKEN = '6074203197:AAGh4YuAoXnH5iqTSLzGJHV9quOuvOFPQUc'
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    id = message.from_user.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if id == 995091801:
        client = types.KeyboardButton('Клиентам')
        master = types.KeyboardButton('Мастерам')
        create_table = types.KeyboardButton('Создать таблицу')
        insert = types.KeyboardButton('Добавить мастера')
        select = types.KeyboardButton('Записаться')
        markup.add(client, master, create_table, insert, select)
    else:
        client = types.KeyboardButton('Клиентам')
        master = types.KeyboardButton('Мастерам')
        markup.add(client, master)
    bot.send_message(message.chat.id, f'Привет,{user_name}!\nЯ чат-бот😇', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    id = message.from_user.id
    if message.chat.type == 'private':
        if message.text == 'Мастерам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Студия')
            board2 = types.KeyboardButton('Аренда')
            board3 = types.KeyboardButton('Обучение')
            board4 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3, board4)
            bot.send_message(message.chat.id, 'Выбирите нужный пункт', reply_markup=markup)

        elif message.text == 'Назад':
            user_name = message.from_user.first_name
            id = message.from_user.id
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            if id == 995091801:
                client = types.KeyboardButton('Клиентам')
                master = types.KeyboardButton('Мастерам')
                create_table = types.KeyboardButton('Создать таблицу')
                insert = types.KeyboardButton('Добавить мастера')
                select = types.KeyboardButton('Записаться')
                markup.add(client, master, create_table, insert, select)
            else:
                client = types.KeyboardButton('Клиентам')
                master = types.KeyboardButton('Мастерам')
                markup.add(client, master)
            bot.send_message(message.chat.id, f'Привет,{user_name}!\nЯ чат-бот😇', reply_markup=markup)

        elif message.text == 'Студия':
            bot.send_message(message.chat.id, 'Тут будет описание студии и все такое')

        elif message.text == 'Аренда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board5 = types.KeyboardButton('На день(гостевой)')
            board6 = types.KeyboardButton('Помесячно')
            board7 = types.KeyboardButton('Назад')
            markup.add(board5, board6, board7)
            bot.send_message(message.chat.id, 'Выбирите нужный пункт', reply_markup=markup)

        elif message.text == 'Обучение':
            bot.send_message(message.chat.id, 'Скоро будет')

        elif message.text == 'На день(гостевой)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board8 = types.KeyboardButton('Проверить свободные места')
            board9 = types.KeyboardButton('Назад')
            markup.add(board8, board9)
            bot.send_message(message.chat.id, f'Цена, ну сколько-то стоит\nВ стоимость входит примерно то, что входит',
                             reply_markup=markup)

        elif message.text == 'Помесячно':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board8 = types.KeyboardButton('Проверить свободные места')
            board9 = types.KeyboardButton('Назад')
            markup.add(board8, board9)
            bot.send_message(message.chat.id, f'Цена, ну сколько-то стоит\nВ стоимость входит примерно то, что входит',
                             reply_markup=markup)

        elif message.text == 'Клиентам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Ознакомиться')
            board2 = types.KeyboardButton('Записаться')
            board3 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3)
            bot.send_message(message.chat.id, 'Ознакомиться, или сразу на запись?', reply_markup=markup)

        elif message.text == 'Ознакомиться':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Мастера')
            board2 = types.KeyboardButton('Внешний вид студии')
            board3 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3)
            bot.send_message(message.chat.id, 'Просмотр мастеров и студии', reply_markup=markup)

        elif message.text == 'Внешний вид студии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Фото студии')
            board2 = types.KeyboardButton('Удобства')
            board3 = types.KeyboardButton('Сдание снаружи')
            board4 = types.KeyboardButton('Адрес + как добраться')
            board5 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3, board4, board5)
            bot.send_message(message.chat.id, 'На что посмотрим', reply_markup=markup)

        elif message.text == 'Назад':
            user_name = message.from_user.first_name
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            client = types.KeyboardButton('Клиентам')
            master = types.KeyboardButton('Мастерам')
            markup.add(client, master)
            bot.send_message(message.chat.id, f'Привет,{user_name}!\nЯ чат-бот😇', reply_markup=markup)

        # elif message.text == 'Создать таблицу':
        #     if id == 995091801:
        #         create_table()
        #         bot.send_message(message.chat.id, 'Таблицы созданы мой господин')

        elif message.text == 'Добавить мастера':
            if id == 995091801:
                pass

        elif message.text == 'Записаться':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            board1 = types.KeyboardButton('Анастасия')
            board2 = types.KeyboardButton('Антон')
            board3 = types.KeyboardButton('Артур')
            board4 = types.KeyboardButton('Валерия')
            board5 = types.KeyboardButton('Виктория Пахина')
            board6 = types.KeyboardButton('Димон')
            board7 = types.KeyboardButton('Ирина')
            board8 = types.KeyboardButton('Кеша')
            board9 = types.KeyboardButton('Килди')
            board10 = types.KeyboardButton('Роман')
            board10 = types.KeyboardButton('Маркуля 555')
            markup.add(board1, board2, board3, board4, board5, board6, board7, board8, board9, board10)
            bot.send_message(message.chat.id, 'Выбирите мастера', reply_markup=markup)
            bot.register_next_step_handler(message, name_master)

        elif message.text == 'Фото студии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_foto = ['Фото студии/IMG_6194.JPG', 'Фото студии/IMG_6295.JPG', 'Фото студии/IMG_6194.JPG']
            bot.send_message(message.chat.id, 'Посмотрим фоточки')
            for foto in list_foto:
                p = open(foto, "rb")
                bot.send_photo(message.chat.id, p)
            board1 = types.KeyboardButton('Удобства')
            board2 = types.KeyboardButton('Сдание снаружи')
            board3 = types.KeyboardButton('Адрес + как добраться')
            board4 = types.KeyboardButton('Записаться')
            board5 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3, board4, board5)
            bot.send_message(message.chat.id, 'На что еще посмотрим или запишемся)', reply_markup=markup)
        elif message.text == 'Адрес + как добраться':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            p1 = open("Как добраться/E7BF2779-3D55-49FD-823D-F4ACE89D07C1.JPG", "rb")
            p2 = open("Как добраться/IMG_7776.JPG", "rb")
            p3 = open("Как добраться/IMG_7775.JPG", "rb")
            bot.send_message(message.chat.id, 'Готэм-Сити, Халковая д1.')
            bot.send_photo(message.chat.id, p1)
            bot.send_photo(message.chat.id, p2)
            bot.send_photo(message.chat.id, p3)
            board1 = types.KeyboardButton('Удобства')
            board2 = types.KeyboardButton('Сдание снаружи')
            board3 = types.KeyboardButton('Фото студии')
            board4 = types.KeyboardButton('Записаться')
            board5 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3, board4, board5)
            bot.send_message(message.chat.id, 'На что еще посмотрим или запишемся)', reply_markup=markup)

        elif message.text == 'Сдание снаружи':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            p1 = open("Как добраться/E7BF2779-3D55-49FD-823D-F4ACE89D07C1.JPG", "rb")
            bot.send_photo(message.chat.id, p1)
            board1 = types.KeyboardButton('Удобства')
            board2 = types.KeyboardButton('Адрес + как добраться')
            board3 = types.KeyboardButton('Фото студии')
            board4 = types.KeyboardButton('Записаться')
            board5 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3, board4, board5)
            bot.send_message(message.chat.id, 'На что еще посмотрим запишемся)', reply_markup=markup)

        elif message.text == 'Удобства':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            board1 = types.KeyboardButton('Сдание снаружи')
            board2 = types.KeyboardButton('Адрес + как добраться')
            board3 = types.KeyboardButton('Фото студии')
            board4 = types.KeyboardButton('Записаться')
            board5 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3, board4, board5)
            bot.send_message(message.chat.id, 'На что еще посмотрим запишемся)', reply_markup=markup)

        elif 'Мастера':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Anastas = ['Анастасия (мастер)/Работа1.jpg', 'Анастасия (мастер)/Работа2.jpg', 'Анастасия (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Анастасия')
            p1 = open("Анастасия (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p1)
            for photo_An in list_Anastas:
                p = open(photo_An, "rb")
                bot.send_photo(message.chat.id, p)

            list_Anton = ['Антон Карибский (мастер)/Работа1.jpg', 'Антон Карибский (мастер)/Работа2.jpg',
                            'Антон Карибский (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Антон')
            p2 = open("Антон Карибский (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p2)
            for photo_Ant in list_Anton:
                p3 = open(photo_Ant, "rb")
                bot.send_photo(message.chat.id, p3)

            bot.send_message(message.chat.id, 'Артур')
            p3 = open("Артур (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p3)

            list_Valeria = ['Валерия (мастер)/Работа1.jpg', 'Валерия (мастер)/Работа2.jpg',
                          'Валерия (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Валерия')
            p4 = open("Валерия (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p4)
            for photo_Val in list_Valeria:
                p5 = open(photo_Val, "rb")
                bot.send_photo(message.chat.id, p5)

            list_Victoria = ['Виктория Пахина (мастер)/Работа1.jpg', 'Виктория Пахина (мастер)/Работа2.jpg',
                            'Виктория Пахина (мастер)/Работа3.jpg',
                             'Виктория Пахина (мастер)/Работа4.jpg', 'Виктория Пахина (мастер)/Работа5.jpg',
                             'Виктория Пахина (мастер)/Работа6.jpg']
            bot.send_message(message.chat.id, 'Виктория')
            p5 = open("Виктория Пахина (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p5)
            for photo_Vic in list_Victoria:
                p6 = open(photo_Vic, "rb")
                bot.send_photo(message.chat.id, p6)

            list_Dimon = ['Димон (мастер)/Работа1.jpg', 'Димон (мастер)/Работа2.jpg',
                             'Димон (мастер)/Работа3.jpg',
                             'Димон (мастер)/Работа4.jpg', 'Димон (мастер)/Работа5.jpg',
                             'Димон (мастер)/Работа6.jpg']
            bot.send_message(message.chat.id, 'Димон')
            p7 = open("Димон (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p7)
            for photo_Dim in list_Dimon:
                p8 = open(photo_Dim, "rb")
                bot.send_photo(message.chat.id, p8)

            list_Irina = ['Ирина (мастер)/Работа1.jpg', 'Ирина (мастер)/Работа2.jpg',
                          'Ирина (мастер)/Работа3.jpg',
                          'Ирина (мастер)/Работа4.jpg', 'Ирина (мастер)/Работа5.jpg',
                          'Ирина (мастер)/Работа6.jpg']
            bot.send_message(message.chat.id, 'Ирина')
            p9 = open("Ирина (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p9)
            for photo_Irin in list_Irina:
                p10 = open(photo_Irin, "rb")
                bot.send_photo(message.chat.id, p10)

            list_Kecha = ['Кеша (мастер)/Работа1.jpg', 'Кеша (мастер)/Работа2.jpg',
                            'Кеша (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Кеша')
            p11 = open("Кеша (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p11)
            for photo_Kech in list_Kecha:
                p12 = open(photo_Kech, "rb")
                bot.send_photo(message.chat.id, p12)

            list_Kildi = ['Килди (мастер)/Работа1.JPG', 'Килди (мастер)/Работа2.JPG',
                          'Килди (мастер)/Работа4.JPG', 'Килди (мастер)/Работа5.JPG']
            bot.send_message(message.chat.id, 'Килди')
            for photo_Kild in list_Kildi:
                p13 = open(photo_Kild, "rb")
                bot.send_photo(message.chat.id, p13)

            list_Roman = ['Роман (мастер)/IMG_3731.jpg', 'Роман (мастер)/IMG_5140.jpg',
                            'Роман (мастер)/IMG_5475.JPG']
            bot.send_message(message.chat.id, 'Роман')
            p14 = open("Роман (мастер)/IMG_7088.jpg", "rb")
            bot.send_photo(message.chat.id, p14)
            for photo_Rom in list_Roman:
                p15 = open(photo_Rom, "rb")
                bot.send_photo(message.chat.id, p15)

            board1 = types.KeyboardButton('Записаться')
            board2 = types.KeyboardButton('Назад')
            markup.add(board1, board2)
            bot.send_message(message.chat.id, 'Ну что, запишемся😜)', reply_markup=markup)


def name_master(message):
    global master
    master = message.text
    bot.send_message(message.chat.id, 'Выбирите и напишите дату например 21.01.01')
    bot.register_next_step_handler(message, get_data1)


def get_data1(message):
    global master
    global data1
    data1 = message.text
    result = select_Name(master, data1, '0')
    if result == []:
        bot.send_message(message.chat.id, f'На выбранную дату нет свободного времени')
        bot.send_message(message.chat.id, f'Посмотрите ближайшие свободные дыты')
        a = select_Name1(master, '0', data1)
        for b in a:
            bot.send_message(message.chat.id, b)

        bot.register_next_step_handler(message, get_data2)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        board1 = types.KeyboardButton('Назад')
        markup.add(board1)
        bot.send_message(message.chat.id, 'Выбирите дату из списка)', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Выбирите и напишите время')
        for i in result:
            bot.send_message(message.chat.id, f'{i}')
        bot.register_next_step_handler(message, get_updata1)


def get_data2(message):
    global master
    global data1
    data1 = message.text
    result = select_Name(master, data1, '0')
    if result == []:
        bot.send_message(message.chat.id, f'Вы снова ввели неверную дату')
    else:
        bot.send_message(message.chat.id, f'Выбирите и напишите время')
        for i in result:
            bot.send_message(message.chat.id, f'{i}')
        bot.register_next_step_handler(message, get_updata1)


def get_updata1(message):
    global time1
    time1 = message.text
    bot.send_message(message.chat.id, f'Введите свое имя')
    bot.register_next_step_handler(message, get_name_person1)


def get_name_person1(message):
    global name_person1
    global data1
    global time1
    global master
    name_person1 = message.text
    update_person(master, data1, time1, name_person1)
    bot.send_message(
        message.chat.id, f'Ваша запись к мастеру {master}, {data1} в {time1} успешно произведена, хорошего вам дня!'
    )


if __name__ == "__main__":
    bot.polling(none_stop=True)

