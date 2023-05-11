import telebot
from telebot import types
from sqlite_db import select_Name, update_person, select_Name1, insert_master, delete, select_master

data1 = ''
time1 = ''
name_person1 = ''
master = ''
create_master2 = ''
month = ''
person_number = ''
brief_description = ''
master_del = ''
select_master_ = ''
select_master_data = ''


# TOKEN = '6225249184:AAEwLLi6VgiPCRCEZLWTwQN_vK66lrrO-eE' #Тест бот
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
        board1 = types.KeyboardButton('Посмотреть запись')
        insert = types.KeyboardButton('Добавить мастера')
        delete_master = types.KeyboardButton('Удалить мастера')
        select = types.KeyboardButton('Записаться')
        markup.add(client, master, insert, select, delete_master, board1)
    elif id == 209289541 or id == 490294996:
        client = types.KeyboardButton('Клиентам')
        master = types.KeyboardButton('Мастерам')
        board1 = types.KeyboardButton('Посмотреть запись')
        delete_master = types.KeyboardButton('Удалить мастера')
        markup.add(client, master, delete_master, board1)        
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

        elif message.text == 'Удалить мастера':
            if id == 995091801:
                bot.send_message(message.chat.id, 'Введите имя')
                bot.register_next_step_handler(message, delete_master1)
            else:
                bot.send_message(message.chat.id, 'Данная команда вам не доступна')

        elif message.text == 'На главную':
            user_name = message.from_user.first_name
            id = message.from_user.id
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            if id == 995091801:
                client = types.KeyboardButton('Клиентам')
                master = types.KeyboardButton('Мастерам')
                insert = types.KeyboardButton('Добавить мастера')
                board1 = types.KeyboardButton('Посмотреть запись')
                delete_master = types.KeyboardButton('Удалить мастера')
                select = types.KeyboardButton('Записаться')
                markup.add(client, master, insert, select, delete_master, board1)
            else:
                client = types.KeyboardButton('Клиентам')
                master = types.KeyboardButton('Мастерам')
                markup.add(client, master)
            bot.send_message(message.chat.id, f'Привет,{user_name}!\nЯ чат-бот😇', reply_markup=markup)

        elif message.text == 'Студия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            list_foto = ['Фото студии/IMG_6194.JPG', 'Фото студии/IMG_6295.JPG', 'Фото студии/IMG_6194.JPG']
            bot.send_message(message.chat.id, 'Посмотрим фоточки')
            for foto in list_foto:
                p = open(foto, "rb")
                bot.send_photo(message.chat.id, p)
            board1 = types.KeyboardButton('На главную')
            markup.add(board1)
            bot.send_message(message.chat.id, 'Вернуться назад', reply_markup=markup)

        elif message.text == 'Аренда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board5 = types.KeyboardButton('На день(гостевой)')
            board6 = types.KeyboardButton('Помесячно')
            board7 = types.KeyboardButton('На главную')
            markup.add(board5, board6, board7)
            bot.send_message(message.chat.id, 'Выбирите нужный пункт', reply_markup=markup)

        elif message.text == 'Обучение':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('На главную')
            markup.add(board1)
            bot.send_message(message.chat.id, 'Скоро будет')

        elif message.text == 'На день(гостевой)':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                board8 = types.KeyboardButton('Проверить свободные места')
                board9 = types.KeyboardButton('На главную')
                markup.add(board8, board9)
                bot.send_message(message.chat.id, f'Цена, ну сколько-то стоит\nВ стоимость входит примерно то, что входит',
                                 reply_markup=markup)

        elif message.text == 'Проверить свободные места':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('На главную')
            markup.add(board1)
            bot.send_message(message.chat.id, 'Скоро будет')

        elif message.text == 'Помесячно':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board8 = types.KeyboardButton('Проверить свободные места')
            board9 = types.KeyboardButton('На главную')
            markup.add(board8, board9)
            bot.send_message(message.chat.id, f'Цена, ну сколько-то стоит\nВ стоимость входит примерно то, что входит',
                             reply_markup=markup)

        elif message.text == 'Клиентам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Ознакомиться')
            board2 = types.KeyboardButton('Записаться')
            board3 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3)
            bot.send_message(message.chat.id, 'Ознакомиться, или сразу на запись?', reply_markup=markup)

        elif message.text == 'Ознакомиться':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Мастера')
            board2 = types.KeyboardButton('Внешний вид студии')
            board3 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3)
            bot.send_message(message.chat.id, 'Просмотр мастеров и студии', reply_markup=markup)

        elif message.text == 'Внешний вид студии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Фото студии')
            board2 = types.KeyboardButton('Удобства')
            board3 = types.KeyboardButton('Сдание снаружи')
            board4 = types.KeyboardButton('Адрес + как добраться')
            board5 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5)
            bot.send_message(message.chat.id, 'На что посмотрим', reply_markup=markup)

        elif message.text == 'На главную':
            user_name = message.from_user.first_name
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            client = types.KeyboardButton('Клиентам')
            master = types.KeyboardButton('Мастерам')
            markup.add(client, master)
            bot.send_message(message.chat.id, f'Привет,{user_name}!\nЯ чат-бот😇', reply_markup=markup)

        elif message.text == 'Добавить мастера':
            if id == 995091801:
                bot.send_message(message.chat.id, 'Введите имя мастера')
                bot.register_next_step_handler(message, create_master1)
            else:
                bot.send_message(message.chat.id, 'У вас нет доступа к данному разделу')

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
            board5 = types.KeyboardButton('На главную')
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
            board5 = types.KeyboardButton('На главную')
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
            board5 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5)
            bot.send_message(message.chat.id, 'На что еще посмотрим или запишемся)', reply_markup=markup)

        elif message.text == 'Удобства':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            board1 = types.KeyboardButton('Сдание снаружи')
            board2 = types.KeyboardButton('Адрес + как добраться')
            board3 = types.KeyboardButton('Фото студии')
            board4 = types.KeyboardButton('Записаться')
            board5 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5)
            bot.send_message(message.chat.id, 'На что еще посмотрим или запишемся)', reply_markup=markup)

        elif message.text == 'Мастера':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            board1 = types.KeyboardButton('Фото Анастасия')
            board2 = types.KeyboardButton('Фото Антон')
            board3 = types.KeyboardButton('Фото Артур')
            board4 = types.KeyboardButton('Фото Валерия')
            board5 = types.KeyboardButton('Фото Виктория Пахина')
            board6 = types.KeyboardButton('Фото Димон')
            board7 = types.KeyboardButton('Фото Ирина')
            board8 = types.KeyboardButton('Фото Кеша')
            board9 = types.KeyboardButton('Фото Килди')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5, board6, board7, board8, board9, board10, board11, board12)
            bot.send_message(message.chat.id, 'На кого посмотрим?', reply_markup=markup)

        elif message.text == 'Фото Анастасия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Anastas = ['Анастасия (мастер)/Работа1.jpg', 'Анастасия (мастер)/Работа2.jpg', 'Анастасия (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Анастасия')
            p1 = open("Анастасия (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p1)
            for photo_An in list_Anastas:
                p = open(photo_An, "rb")
                bot.send_photo(message.chat.id, p)
            board2 = types.KeyboardButton('Фото Антон')
            board3 = types.KeyboardButton('Фото Артур')
            board4 = types.KeyboardButton('Фото Валерия')
            board5 = types.KeyboardButton('Фото Виктория Пахина')
            board6 = types.KeyboardButton('Фото Димон')
            board7 = types.KeyboardButton('Фото Ирина')
            board8 = types.KeyboardButton('Фото Кеша')
            board9 = types.KeyboardButton('Фото Килди')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Фото Антон':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Anton = ['Антон Карибский (мастер)/Работа1.jpg', 'Антон Карибский (мастер)/Работа2.jpg',
                            'Антон Карибский (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Антон')
            p2 = open("Антон Карибский (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p2)
            for photo_Ant in list_Anton:
                p3 = open(photo_Ant, "rb")
                bot.send_photo(message.chat.id, p3)
            board2 = types.KeyboardButton('Фото Анастасия')
            board3 = types.KeyboardButton('Фото Артур')
            board4 = types.KeyboardButton('Фото Валерия')
            board5 = types.KeyboardButton('Фото Виктория Пахина')
            board6 = types.KeyboardButton('Фото Димон')
            board7 = types.KeyboardButton('Фото Ирина')
            board8 = types.KeyboardButton('Фото Кеша')
            board9 = types.KeyboardButton('Фото Килди')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Фото Артур':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            bot.send_message(message.chat.id, 'Артур')
            p3 = open("Артур (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p3)
            board2 = types.KeyboardButton('Фото Анастасия')
            board3 = types.KeyboardButton('Фото Антон')
            board4 = types.KeyboardButton('Фото Валерия')
            board5 = types.KeyboardButton('Фото Виктория Пахина')
            board6 = types.KeyboardButton('Фото Димон')
            board7 = types.KeyboardButton('Фото Ирина')
            board8 = types.KeyboardButton('Фото Кеша')
            board9 = types.KeyboardButton('Фото Килди')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Фото Валерия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Valeria = ['Валерия (мастер)/Работа1.jpg', 'Валерия (мастер)/Работа2.jpg',
                          'Валерия (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Валерия')
            p4 = open("Валерия (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p4)
            for photo_Val in list_Valeria:
                p5 = open(photo_Val, "rb")
                bot.send_photo(message.chat.id, p5)
            board2 = types.KeyboardButton('Фото Анастасия')
            board3 = types.KeyboardButton('Фото Антон')
            board4 = types.KeyboardButton('Фото Артур')
            board5 = types.KeyboardButton('Фото Виктория Пахина')
            board6 = types.KeyboardButton('Фото Димон')
            board7 = types.KeyboardButton('Фото Ирина')
            board8 = types.KeyboardButton('Фото Кеша')
            board9 = types.KeyboardButton('Фото Килди')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Фото Виктория Пахина':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
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
            board2 = types.KeyboardButton('Фото Анастасия')
            board3 = types.KeyboardButton('Фото Антон')
            board4 = types.KeyboardButton('Фото Артур')
            board5 = types.KeyboardButton('Фото Валерия')
            board6 = types.KeyboardButton('Фото Димон')
            board7 = types.KeyboardButton('Фото Ирина')
            board8 = types.KeyboardButton('Фото Кеша')
            board9 = types.KeyboardButton('Фото Килди')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Фото Димон':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
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
            board2 = types.KeyboardButton('Фото Анастасия')
            board3 = types.KeyboardButton('Фото Антон')
            board4 = types.KeyboardButton('Фото Артур')
            board5 = types.KeyboardButton('Фото Валерия')
            board6 = types.KeyboardButton('Фото Виктория Пахина')
            board7 = types.KeyboardButton('Фото Ирина')
            board8 = types.KeyboardButton('Фото Кеша')
            board9 = types.KeyboardButton('Фото Килди')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Фото Ирина':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
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
            board2 = types.KeyboardButton('Фото Анастасия')
            board3 = types.KeyboardButton('Фото Антон')
            board4 = types.KeyboardButton('Фото Артур')
            board5 = types.KeyboardButton('Фото Валерия')
            board6 = types.KeyboardButton('Фото Виктория Пахина')
            board7 = types.KeyboardButton('Фото Димон')
            board8 = types.KeyboardButton('Фото Кеша')
            board9 = types.KeyboardButton('Фото Килди')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Фото Кеша':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Kecha = ['Кеша (мастер)/Работа1.jpg', 'Кеша (мастер)/Работа2.jpg',
                            'Кеша (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Кеша')
            p11 = open("Кеша (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p11)
            for photo_Kech in list_Kecha:
                p12 = open(photo_Kech, "rb")
                bot.send_photo(message.chat.id, p12)
            board2 = types.KeyboardButton('Фото Анастасия')
            board3 = types.KeyboardButton('Фото Антон')
            board4 = types.KeyboardButton('Фото Артур')
            board5 = types.KeyboardButton('Фото Валерия')
            board6 = types.KeyboardButton('Фото Виктория Пахина')
            board7 = types.KeyboardButton('Фото Димон')
            board8 = types.KeyboardButton('Фото Ирина')
            board9 = types.KeyboardButton('Фото Килди')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Фото Килди':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Kildi = ['Килди (мастер)/Работа1.JPG', 'Килди (мастер)/Работа2.JPG',
                          'Килди (мастер)/Работа4.JPG', 'Килди (мастер)/Работа5.JPG']
            bot.send_message(message.chat.id, 'Килди')
            for photo_Kild in list_Kildi:
                p13 = open(photo_Kild, "rb")
                bot.send_photo(message.chat.id, p13)
            board2 = types.KeyboardButton('Фото Анастасия')
            board3 = types.KeyboardButton('Фото Антон')
            board4 = types.KeyboardButton('Фото Артур')
            board5 = types.KeyboardButton('Фото Валерия')
            board6 = types.KeyboardButton('Фото Виктория Пахина')
            board7 = types.KeyboardButton('Фото Димон')
            board8 = types.KeyboardButton('Фото Ирина')
            board9 = types.KeyboardButton('Фото Кеша')
            board10 = types.KeyboardButton('Фото Роман')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Фото Роман':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Roman = ['Роман (мастер)/IMG_3731.jpg', 'Роман (мастер)/IMG_5140.jpg',
                            'Роман (мастер)/IMG_5475.JPG']
            bot.send_message(message.chat.id, 'Роман')
            p14 = open("Роман (мастер)/IMG_7088.jpg", "rb")
            bot.send_photo(message.chat.id, p14)
            for photo_Rom in list_Roman:
                p15 = open(photo_Rom, "rb")
                bot.send_photo(message.chat.id, p15)
            board2 = types.KeyboardButton('Фото Анастасия')
            board3 = types.KeyboardButton('Фото Антон')
            board4 = types.KeyboardButton('Фото Артур')
            board5 = types.KeyboardButton('Фото Валерия')
            board6 = types.KeyboardButton('Фото Виктория Пахина')
            board7 = types.KeyboardButton('Фото Димон')
            board8 = types.KeyboardButton('Фото Ирина')
            board9 = types.KeyboardButton('Фото Кеша')
            board10 = types.KeyboardButton('Фото Килди')
            board11 = types.KeyboardButton('Записаться')
            board12 = types.KeyboardButton('На главную')
            markup.add(board2, board3, board4, board5, board6, board7, board8, board9, board10, board11,
                       board12)
            bot.send_message(message.chat.id, 'На кого еще посмотрим? Или запишемся?', reply_markup=markup)

        elif message.text == 'Посмотреть запись':
            bot.send_message(message.chat.id, 'Введите мастера')
            bot.register_next_step_handler(message, master_select2)

        elif 'Мастера':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('На главную')
            markup.add(board1)
            bot.send_message(message.chat.id, 'Вы ввели не верную команду', reply_markup=markup)


def name_master(message):
    global master
    master = message.text
    bot.send_message(message.chat.id, 'Выбирите и напишите дату например 01.01.01')
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
        board1 = types.KeyboardButton('На главную')
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
    bot.register_next_step_handler(message, get_name_person)


def get_name_person(message):
    global name_person1
    name_person1 = message.text
    bot.send_message(message.chat.id, f'Введите свой номер телефона')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global person_number
    person_number = message.text
    bot.send_message(message.chat.id, f'Введите краткое описание тату (размер, место, референсы)')
    bot.register_next_step_handler(message, get_brief_description)


def get_brief_description(message):
    global name_person1
    global data1
    global time1
    global master
    global person_number
    global brief_description
    brief_description = message.text
    update_person(master, data1, time1, name_person1, person_number, brief_description)
    bot.send_message(
        message.chat.id, f'С вами скоро свяжется администратор'
    )


def create_master1(message):
    global create_master2
    create_master2 = message.text
    bot.send_message(message.chat.id, f'Выбирите месяц')
    bot.register_next_step_handler(message, get_month)


def get_month(message):
    global create_master2
    global month
    month = message.text
    data_may = ['01.05.23', '02.05.23', '03.05.23', '04.05.23', '05.05.23', '06.05.23', '07.05.23', '08.05.23', '09.05.23',
            '10.05.23', '11.05.23', '12.05.23', '13.05.23', '14.05.23', '15.05.23', '16.05.23', '17.05.23', '18.05.23',
                '19.05.23', '20.05.23', '21.05.23', '22.05.23', '23.05.23', '24.05.23', '25.05.23', '26.05.23',
                '27.05.23', '28.05.23', '29.05.23', '30.05.23', '31.05.23']

    data_iyn = ['1.05.23', '2.05.23', '3.05.23', '4.05.23', '5.05.23', '6.05.23', '7.05.23', '8.05.23', '9.05.23',
                '10.05.23', '11.05.23', '12.05.23', '13.05.23', '14.05.23', '15.05.23', '16.05.23', '17', '18', '19',
                '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

    data_iyl = ['1.05.23', '2.05.23', '3.05.23', '4.05.23', '5.05.23', '6.05.23', '7.05.23', '8.05.23', '9.05.23',
                '10.05.23', '11.05.23', '12.05.23', '13.05.23', '14.05.23', '15.05.23', '16.05.23', '17', '18', '19',
                '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    time = ['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']

    if month == 'Май':
        for a in data_may:
            for b in time:
                insert_master(create_master2, a, b)
        bot.send_message(message.chat.id, f'Мастер добавлен')

    elif month == 'Июнь':
        for a in data_iyn:
            for b in time:
                insert_master(create_master2, a, b)
        bot.send_message(message.chat.id, f'Мастер добавлен')

    elif month == 'Июль':
        for a in data_iyl:
            for b in time:
                insert_master(create_master2, a, b)
        bot.send_message(message.chat.id, f'Мастер добавлен')
        
    else:
        bot.send_message(message.chat.id, f'Вы ввели не существующий месяц')


def delete_master1(message):
    global master_del
    master_del = message.text
    delete(master_del)
    bot.send_message(message.chat.id, f'мастер удален')


def master_select(message):
    bot.send_message(message.chat.id, f'введите мастера')
    bot.register_next_step_handler(message, master_select2)
    
    
def master_select2(message):
    global select_master_
    select_master_ = message.text
    bot.send_message(message.chat.id, f'введите дату')
    bot.register_next_step_handler(message, master_select3)
    
    
def master_select3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    global select_master_
    global select_master_data
    select_master_data = message.text
    d = select_master(select_master_, select_master_data, '0')
    for i in d:
        list_ = []
        for a in i:
            list_.append(a)
        bot.send_message(message.chat.id, f'{list_[0]} {list_[1]} {list_[2]} {list_[3]} {list_[4]}')    
    board1 = types.KeyboardButton('На главную')
    markup.add(board1)
    bot.send_message(message.chat.id, 'Выбирите команду', reply_markup=markup)        


if __name__ == "__main__":
    bot.polling(none_stop=True)

