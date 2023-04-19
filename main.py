import telebot
from telebot import types
from tatu_db import create_table


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
        markup.add(client, master, create_table)
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
            board2 = types.KeyboardButton('Запись')
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

        elif message.text == 'Запись':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Выбор мастера')
            board2 = types.KeyboardButton('Записаться на консультацию к администраторутору')
            board3 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3)
            bot.send_message(message.chat.id, 'Сложный выбор', reply_markup=markup)

        elif message.text == 'Мастера':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            board1 = types.KeyboardButton('Мастера')
            board2 = types.KeyboardButton('Работы')
            board3 = types.KeyboardButton('Назад')
            markup.add(board1, board2, board3)
            bot.send_message(message.chat.id, 'Посмотреть работы, или самих мастеров?', reply_markup=markup)

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

        elif message.text == 'Создать таблицу':
            if id == 995091801:
                create_table()
                bot.send_message(message.chat.id, 'Таблицы созданы мой господин')


if __name__ == "__main__":
    bot.polling(none_stop=True)

