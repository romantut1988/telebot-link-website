import telebot

from telebot import types

bot = telebot.TeleBot("")


@bot.message_handler(commands=["start", "helps"])
def main(message):
    keyboard = types.InlineKeyboardMarkup()

    url_btn = types.InlineKeyboardButton(text="Сайт-суши", url="https://www.google.com")

    keyboard.add(url_btn)

    bot.send_message(message.chat.id, "Привет", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
