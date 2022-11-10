import telebot
from telebot import types
from course import course
from weather import weather


TOKEN = '5627322030:AAEd2cPnnyHlUz2mbbjTkqslcRczIesNXKo'
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    return bot.send_message(message.chat.id, f'Привет, {user_name}.\n{course()}\n'
    f'{weather()}\nУзнать подробнее жми /help'
    )


@bot.message_handler(commands=['course'])
def course_(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Курс доллара',url='https://yandex.ru/search/?text=USD+ЦБ&lr=119544&redircnt=1667885806.1'))
    bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)


@bot.message_handler(commands=['weather'])
def weather_(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Погода', url='https://www.gismeteo.ru/weather-moscow-4368/now/'))    
    bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)   
  

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    course = types.KeyboardButton('/course')
    weather = types.KeyboardButton('/weather')
    markup.add(course, weather)
    bot.send_message(message.chat.id, 'Нажмите нужную кнопку', reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)

