import telebot
from telebot import types
from sqlite_db import select_Name, update_person, select_Name1, insert_master, delete, select_master
from month import *


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
get_admin_question = ''
get_admin_user = ''
get_admin_number = ''

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
    bot.send_message(message.chat.id, f'Привет,{user_name}!\nЯ бот-помощник тату-студии "Hokage Tattoo". Хочешь записаться на сеанс, жми "Клиентам". Если ты мастер и хочешь у нас поработать, то жми "Мастерам"', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    id = message.from_user.id
    if message.chat.type == 'private':
        if message.text == 'Мастерам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Студия')
            board2 = types.KeyboardButton('Аренда')
            board3 = types.KeyboardButton('Обучение')
            board4 = types.KeyboardButton('Связаться с администратором')
            board5 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5)
            bot.send_message(message.chat.id, 'Был у нас? Если нет, то жми кнопку "Студия". Там у нас пару фотографий твоего будущего рабочего пространства. Был? Тогда ещё лучше, сразу жми кнопку "Аренда". Ну а если ты, замечательный человек, хочешь обучиться искусству татуировки, то жмякай кнопку "Обучение"', reply_markup=markup)

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
            bot.send_message(message.chat.id, f'Привет,{user_name}!\nЯ бот-помощник тату-студии "Hokage Tattoo". Хочешь записаться на сеанс, жми "Клиентам". Если ты мастер и хочешь у нас поработать, то жми "Мастерам"', reply_markup=markup)
        elif message.text == 'Студия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            list_foto = ['Фото студии/IMG_6194.JPG', 'Фото студии/IMG_6295.JPG', 'Фото студии/IMG_6194.JPG']
            bot.send_message(message.chat.id, 'Посмотрим фоточки')
            for foto in list_foto:
                p = open(foto, "rb")
                bot.send_photo(message.chat.id, p)
            board4 = types.KeyboardButton('Связаться с администратором')    
            board1 = types.KeyboardButton('На главную')
            markup.add(board1, board4)
            bot.send_message(message.chat.id, 'Вернуться назад', reply_markup=markup)

        elif message.text == 'Аренда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board5 = types.KeyboardButton('На день(гостевой)')
            board6 = types.KeyboardButton('Помесячно')
            board4 = types.KeyboardButton('Связаться с администратором')
            board7 = types.KeyboardButton('На главную')
            markup.add(board5, board6, board7, board4)
            bot.send_message(message.chat.id, 'Думаешь к нам на постоянку или на гостевое место?', reply_markup=markup)

        elif message.text == 'Обучение':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board4 = types.KeyboardButton('Связаться с администратором')
            board1 = types.KeyboardButton('На главную')
            markup.add(board1, board4)
            bot.send_message(message.chat.id, 'Скоро будет')

        elif message.text == 'На день(гостевой)':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                board8 = types.KeyboardButton('Проверить свободные места')
                board4 = types.KeyboardButton('Связаться с администратором')
                board9 = types.KeyboardButton('На главную')
                markup.add(board8, board9, board4)
                bot.send_message(message.chat.id, f'Такс, день у нас стоит 3,500₽. Мы даем всю расходку, кроме игл, краски и машинки. Заживляющую пленку и наборы твой клиент может купить на студии.',
                                 reply_markup=markup)

        elif message.text == 'Проверить свободные места':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board4 = types.KeyboardButton('Связаться с администратором')
            board1 = types.KeyboardButton('На главную')
            markup.add(board1, board4)
            bot.send_message(message.chat.id, 'Скоро будет')

        elif message.text == 'Помесячно':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board8 = types.KeyboardButton('Проверить свободные места')
            board4 = types.KeyboardButton('Связаться с администратором')
            board9 = types.KeyboardButton('На главную')
            markup.add(board8, board9, board4)
            bot.send_message(message.chat.id, f'Цены у нас варьируются от 25,000₽ до 35,000₽. Все зависит от того, что включено в стоймость аренды. Ещё у нас есть возможность сидеть на проценте. Обо всем этом тебе расскажет наш администратор.',
                             reply_markup=markup)

        elif message.text == 'Клиентам':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Ознакомиться')
            board2 = types.KeyboardButton('Записаться')
            board4 = types.KeyboardButton('Связаться с администратором')
            board3 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4)
            bot.send_message(message.chat.id, 'Знаком с нашими мастерами? Если нет, то кликай "Ознакомиться". Если у нас не в первый раз, то кликай "Записаться"', reply_markup=markup)

        elif message.text == 'Ознакомиться':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Мастера')
            board2 = types.KeyboardButton('Внешний вид студии')
            board4 = types.KeyboardButton('Связаться с администратором')
            board3 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4)
            bot.send_message(message.chat.id, 'Тут у нас собрано портфолио наших мастеров, а также фотографии студии. Что хочешь посмотреть?', reply_markup=markup)

        elif message.text == 'Внешний вид студии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Фото студии')
            board2 = types.KeyboardButton('Удобства')
            board3 = types.KeyboardButton('Сдание снаружи')
            board4 = types.KeyboardButton('Адрес + как добраться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board5 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5, board44)
            bot.send_message(message.chat.id, 'кнопка "Студия"', reply_markup=markup)

        elif message.text == 'На главную':
            user_name = message.from_user.first_name
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            client = types.KeyboardButton('Клиентам')
            master = types.KeyboardButton('Мастерам')
            markup.add(client, master)
            bot.send_message(message.chat.id, f'Привет,{user_name}!\nЯ бот-помощник тату-студии "Hokage Tattoo". Хочешь записаться на сеанс, жми "Клиентам". Если ты мастер и хочешь у нас поработать, то жми "Мастерам"', reply_markup=markup)

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
            board44 = types.KeyboardButton('Связаться с администратором')
            markup.add(board1, board2, board3, board4, board5, board6, board7, board8, board9, board10, board44)
            bot.send_message(message.chat.id, 'Выбери мастера', reply_markup=markup)
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
            board44 = types.KeyboardButton('Связаться с администратором')
            board5 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5, board44)
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
            board44 = types.KeyboardButton('Связаться с администратором')
            board5 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5, board44)
            bot.send_message(message.chat.id, 'На что еще посмотрим или запишемся)', reply_markup=markup)

        elif message.text == 'Сдание снаружи':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            p1 = open("Как добраться/E7BF2779-3D55-49FD-823D-F4ACE89D07C1.JPG", "rb")
            bot.send_photo(message.chat.id, p1)
            board1 = types.KeyboardButton('Удобства')
            board2 = types.KeyboardButton('Адрес + как добраться')
            board3 = types.KeyboardButton('Фото студии')
            board4 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board5 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5, board44)
            bot.send_message(message.chat.id, 'На что еще посмотрим или запишемся)', reply_markup=markup)

        elif message.text == 'Удобства':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            board1 = types.KeyboardButton('Сдание снаружи')
            board2 = types.KeyboardButton('Адрес + как добраться')
            board3 = types.KeyboardButton('Фото студии')
            board4 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board5 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5, board44)
            bot.send_message(message.chat.id, 'На что еще посмотрим или запишемся)', reply_markup=markup)

        elif message.text == 'Мастера':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            board1 = types.KeyboardButton('мастер Анастасия')
            board2 = types.KeyboardButton('мастер Антон')
            board3 = types.KeyboardButton('мастер Артур')
            board4 = types.KeyboardButton('мастер Валерия')
            board5 = types.KeyboardButton('мастер Виктория Пахина')
            board6 = types.KeyboardButton('мастер Димон')
            board7 = types.KeyboardButton('мастер Ирина')
            board8 = types.KeyboardButton('мастер Кеша')
            board9 = types.KeyboardButton('мастер Килди')
            board10 = types.KeyboardButton('мастер Роман')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5, board6, board7, board8, board9, board10, board11, board12, board44)
            bot.send_message(message.chat.id, 'Выбери интересующего мастера. Потыкай всех, нас много', reply_markup=markup)

        elif message.text == 'мастер Анастасия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Anastas = ['Анастасия (мастер)/Работа1.jpg', 'Анастасия (мастер)/Работа2.jpg', 'Анастасия (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Анастасия')
            p1 = open("Анастасия (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p1)
            for photo_An in list_Anastas:
                p = open(photo_An, "rb")
                bot.send_photo(message.chat.id, p)
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)

        elif message.text == 'мастер Антон':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Anton = ['Антон Карибский (мастер)/Работа1.jpg', 'Антон Карибский (мастер)/Работа2.jpg',
                            'Антон Карибский (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Антон')
            p2 = open("Антон Карибский (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p2)
            for photo_Ant in list_Anton:
                p3 = open(photo_Ant, "rb")
                bot.send_photo(message.chat.id, p3)
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)

        elif message.text == 'мастер Артур':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            bot.send_message(message.chat.id, 'Артур')
            p3 = open("Артур (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p3)
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)

        elif message.text == 'мастер Валерия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Valeria = ['Валерия (мастер)/Работа1.jpg', 'Валерия (мастер)/Работа2.jpg',
                          'Валерия (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Валерия')
            p4 = open("Валерия (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p4)
            for photo_Val in list_Valeria:
                p5 = open(photo_Val, "rb")
                bot.send_photo(message.chat.id, p5)
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)

        elif message.text == 'мастер Виктория Пахина':
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
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)

        elif message.text == 'мастер Димон':
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
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)

        elif message.text == 'мастер Ирина':
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
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)

        elif message.text == 'мастер Кеша':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Kecha = ['Кеша (мастер)/Работа1.jpg', 'Кеша (мастер)/Работа2.jpg',
                            'Кеша (мастер)/Работа3.jpg']
            bot.send_message(message.chat.id, 'Кеша')
            p11 = open("Кеша (мастер)/Лицо.jpg", "rb")
            bot.send_photo(message.chat.id, p11)
            for photo_Kech in list_Kecha:
                p12 = open(photo_Kech, "rb")
                bot.send_photo(message.chat.id, p12)
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)

        elif message.text == 'мастер Килди':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Kildi = ['Килди (мастер)/Работа1.JPG', 'Килди (мастер)/Работа2.JPG',
                          'Килди (мастер)/Работа4.JPG', 'Килди (мастер)/Работа5.JPG']
            bot.send_message(message.chat.id, 'Килди')
            for photo_Kild in list_Kildi:
                p13 = open(photo_Kild, "rb")
                bot.send_photo(message.chat.id, p13)
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)

        elif message.text == 'мастер Роман':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            list_Roman = ['Роман (мастер)/IMG_3731.jpg', 'Роман (мастер)/IMG_5140.jpg',
                            'Роман (мастер)/IMG_5475.JPG']
            bot.send_message(message.chat.id, 'Роман')
            p14 = open("Роман (мастер)/IMG_7088.jpg", "rb")
            bot.send_photo(message.chat.id, p14)
            for photo_Rom in list_Roman:
                p15 = open(photo_Rom, "rb")
                bot.send_photo(message.chat.id, p15)
            board10 = types.KeyboardButton('Посмотреть еще')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board10, board11,board12, board44)
            bot.send_message(message.chat.id, 'Посмотришь еще или сразу записать тебя на сеанс?', reply_markup=markup)
            
        elif message.text == 'Посмотреть еще':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            board1 = types.KeyboardButton('мастер Анастасия')
            board2 = types.KeyboardButton('мастер Антон')
            board3 = types.KeyboardButton('мастер Артур')
            board4 = types.KeyboardButton('мастер Валерия')
            board5 = types.KeyboardButton('мастер Виктория Пахина')
            board6 = types.KeyboardButton('мастер Димон')
            board7 = types.KeyboardButton('мастер Ирина')
            board8 = types.KeyboardButton('мастер Кеша')
            board9 = types.KeyboardButton('мастер Килди')
            board10 = types.KeyboardButton('мастер Роман')
            board11 = types.KeyboardButton('Записаться')
            board44 = types.KeyboardButton('Связаться с администратором')
            board12 = types.KeyboardButton('На главную')
            markup.add(board1, board2, board3, board4, board5, board6, board7, board8, board9, board10, board11, board12, board44)
            bot.send_message(message.chat.id, 'Кого еще посмотришь?', reply_markup=markup)

        elif message.text == 'Посмотреть запись':
            bot.send_message(message.chat.id, 'Введите мастера')
            bot.register_next_step_handler(message, master_select2)
            
        elif message.text == 'Связаться с администратором':
            bot.send_message(message.chat.id, 'Напиши свой вопрос')
            bot.register_next_step_handler(message, get_admin)
            
        elif 'Мастера':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('На главную')
            markup.add(board1)
            bot.send_message(message.chat.id, 'Вы ввели не верную команду', reply_markup=markup)


def name_master(message):
    global master
    master = message.text
    bot.send_message(message.chat.id, 'На какой день записать тебя? (пример 01.01.01)')
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
        bot.send_message(message.chat.id, f'Предпочтительное время?')
        for i in result:
            # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            # board1 = types.KeyboardButton(i)
            # markup.add(board1)
            # bot.send_message(message.chat.id, "время", reply_markup=markup)
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
        bot.send_message(message.chat.id, f'Предпочтительное время?')
        for i in result:
            
            bot.send_message(message.chat.id, f'{i}')
        bot.register_next_step_handler(message, get_updata1)


def get_updata1(message):
    global time1
    time1 = message.text
    bot.send_message(message.chat.id, f'Как тебя зовут?')
    bot.register_next_step_handler(message, get_name_person)


def get_name_person(message):
    global name_person1
    name_person1 = message.text
    bot.send_message(message.chat.id, f'Номерочек свой тоже, пожалуйста, укажи ниже')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global person_number
    person_number = message.text
    bot.send_message(message.chat.id, f'Опиши свою идеи в двух словах. Если знаешь примерные размеры, то тоже укажи их, мы будем рады')
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
        message.chat.id, f'Ну всё! Ты большой молодец, в ближайшее время с тобой свяжется живой человек и уточнит у тебя пару вопрос'
    )
    bot.send_message(209289541, f'Запись, клиент {name_person1} дата {data1} время {time1} номер {person_number}\nописание тату - {brief_description}')


def create_master1(message):
    global create_master2
    create_master2 = message.text
    bot.send_message(message.chat.id, f'Выбирите месяц')
    bot.register_next_step_handler(message, get_month)


def get_month(message):
    global create_master2
    global month
    month = message.text
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


def get_admin(message):
    global get_admin_question
    get_admin_question = message.text
    bot.send_message(message.chat.id, 'Напишите свое имя')
    bot.register_next_step_handler(message, get_admin1)
    
    
def get_admin1(message):
    global get_admin_user
    get_admin_user = message.text    
    bot.send_message(message.chat.id, 'Напишите свой номер телефона')
    bot.register_next_step_handler(message, get_admin2)
    
    
def get_admin2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    global get_admin_question
    global get_admin_user
    global get_admin_number
    get_admin_number = message.text
    board1 = types.KeyboardButton('На главную')
    markup.add(board1)   
    bot.send_message(message.chat.id, 'В ближайшее время с вами свяжется администратор')
    bot.send_message(209289541, f'Запись к администратору клиент {get_admin_user} номер {get_admin_number}\nвопрос : {get_admin_question}')


if __name__ == "__main__":
    bot.polling(none_stop=True)

