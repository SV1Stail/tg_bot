from telebot import *
from copilot import Copilot 
import requests
import sqlite3
bot_token ="5749977133:AAHfM6_CPcmfAGwTJ-pFCyiH5WQ9WhXnoMs"#дял телеграм
bot=telebot.TeleBot("5749977133:AAHfM6_CPcmfAGwTJ-pFCyiH5WQ9WhXnoMs")


@bot.message_handler(commands=['reg']) 
def reg_new_chat(message):
    bot.send_message(message.from_user.id, "enter chat id")
    bot.register_next_step_handler(message, get_id)
def get_id(message):
    try:
        if message.text.lower()!="отмена":
            if len(message.text)<9:
                bot.send_message(message.from_user.id,"id не может состоять меньше чем из 9 символов\nЧтобы отменить регистрацию напиши Отмена")
                bot.register_next_step_handler(message, get_id)
            elif len(message.text)>12 :
                bot.send_message(message.from_user.id,"id не может состоять больше чем из 12 символов\nЧтобы отменить регистрацию напиши Отмена")
                bot.register_next_step_handler(message, get_id)
            else:
                print(int(message.text))
        else:
            print("LOL")
    except ValueError:
        bot.send_message(message.from_user.id,"id состоит только из цифр\nЧтобы отменить регистрацию напиши Отмена")
        if message.text.lower()!="отмена":
            bot.register_next_step_handler(message, get_id)



if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)










