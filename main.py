import telebot
from telebot import types

bot = telebot.TeleBot('6256840600:AAHS9-YPNZrJ7SPfI9aVuE0Q6zv56ZuLNkI')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    memorize = types.KeyboardButton('Повторить слова')
    grammar = types.KeyboardButton('Правописание')
    createexcercise = types.KeyboardButton('Создать упражнения')
    markup.add(memorize, grammar, createexcercise)
    bot.send_message(message.chat.id, 'Чтобы узнать, какие сервисы помогут тебе в изучении английского, '
                                      'нажимай на кнопки!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def memorize(message):
    if message.text == 'Повторить слова':
        bot.send_message(message.chat.id, 'Вот несколько ресурсов для того, чтобы учить слова:')
        bot.send_message(message.chat.id, 'http://quizlet.com')
        bot.send_message(message.chat.id, 'https://www.dictionary.com')
        bot.send_message(message.chat.id, 'https://quizizz.com')
    elif message.text == 'Правописание':
        bot.send_message(message.chat.id, 'Хочешь повторить правописание? \nТогда лови ссылочки:')
        bot.send_message(message.chat.id, 'http://correctenglish.ru')
        bot.send_message(message.chat.id, 'thefreedictionary.com')
    elif message.text == 'Создать упражнения':
        bot.send_message(message.chat.id, 'Чтобы создать свои упражнения тыкай на эти ссылки:')
        bot.send_message(message.chat.id, 'onlinetestpad.com')
        bot.send_message(message.chat.id, 'https://quizizz.com')
        bot.send_message(message.chat.id, 'classtools.net')
        bot.send_message(message.chat.id, 'flippity.net')
    else:
        bot.send_message(message.chat.id, 'Не понимаю слов, нажимай на кнопки, тогда смогу помочь :]')


bot.polling(none_stop=True)
