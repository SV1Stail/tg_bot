from telebot import *
from copilot import Copilot 
import requests
import sqlite3

bot=telebot.TeleBot("6295550611:AAF86rjJ_GyYTGCjS86gjF7rztWKw1erVdE")
bot_token=("6295550611:AAF86rjJ_GyYTGCjS86gjF7rztWKw1erVdE")

chat_id="-1001735449825"
left="left"

def exept_LookupError_for_user_name(res): #проверяет имеется ли юзернейм у человека
    try:
        user_name=res.json()["result"]["user"]["username"]
    except LookupError:
        user_name="NULL" 
    return user_name
def exept_LookupError_for_user_status(res):
    try:
        user_status=res.json()["result"]["status"]
    except LookupError:
        user_status="NULL" 
    return user_status


# @bot.message_handler(commands=['start']) 
# def start_message(message): 
#      bot.send_message(message.chat.id, "ВВЕДИ ID ЧАТА")

@bot.message_handler(commands=['id']) 
def id_message(message): 
    user_id=message.from_user.id
    conn = sqlite3.connect('users_info.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
   user_id INT PRIMARY KEY,
   user_name TEXT,
   chat_id_for_acess INT,
   user_status TEXT);
""")
    res=requests.get(f"https://api.telegram.org/bot{bot_token}/getChatMember?chat_id={chat_id}&user_id={user_id}") #получаю инфу о пользоватеел если он гнаходится в чате
    user_name=exept_LookupError_for_user_name(res)
    user_status=exept_LookupError_for_user_status(res)

    if ("error_code" not in res.json()) and (res.json()["result"]["status"]!=("left"or"kicked")): #если пользователь в чате? дальше спрошу есть ли он в базе
        if cur.execute("""SELECT * FROM users WHERE user_id = user_id""" ).fetchone() : #если есть в базе выполнить:
            bot.send_message(message.chat.id, 'Привет, ты находишься в группе и твой id равен: ' + str(message.from_user.id)) 
            print(cur.execute("""SELECT * FROM users WHERE user_id = user_id""" ).fetchone())

        elif cur.execute("""SELECT * FROM users WHERE user_id = user_id""" ).fetchone() ==0:  #если есть в чате но нет в базе      
            cur.execute("INSERT INTO users (user_id,user_name,chat_id_for_acess,user_status) VALUES (?,?,?,?)",(user_id,user_name,chat_id,user_status,))
            print("LOL")
            cur.execute("SELECT user_id,user_name,chat_id_for_acess  FROM users")
            conn.commit()
    elif ("error_code" not in res.json()) and (res.json()["result"]["status"]==("left"or"kicked")):
        bot.send_message(message.from_user.id, 'НЕТ ДОСТУПА' ) 

    elif "error_code" in res.json():#если пользователя нет в чате
        bot.send_message(message.from_user.id, 'НЕТ ДОСТУПА. ЧТобы его получить вы должны состоять в чате' ) 
    cur.close()


# проверить находится ли юзер в группе 


@bot.message_handler(content_types=["text"])


def get_text_messages(message):
    user_id=message.from_user.id
    conn = sqlite3.connect('users_info.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
   user_id INT PRIMARY KEY,
   user_name TEXT,
   chat_id_for_acess INT,
   user_status TEXT);
""")
    res=requests.get(f"https://api.telegram.org/bot{bot_token}/getChatMember?chat_id={chat_id}&user_id={user_id}") #получаю инфу о пользоватеел если он гнаходится в чате

    user_name=exept_LookupError_for_user_name(res)
    user_status=exept_LookupError_for_user_status(res)

    if ("error_code" not in res.json()) and (res.json()["result"]["status"]!=("left"or"kicked")): #если пользователь в чате? дальше спрошу есть ли он в базе
        if cur.execute("""SELECT * FROM users WHERE user_id = user_id""" ).fetchone() : #если есть в базе выполнить:
            bot.send_message(message.chat.id, Copilot().get_answer(message.text))

        elif cur.execute("""SELECT * FROM users WHERE user_id = user_id""" ).fetchone() ==0:  #если есть в чате но нет в базе      
            cur.execute("INSERT INTO users (user_id,user_name,chat_id_for_acess,user_status) VALUES (?,?,?,?)",(user_id,user_name,chat_id,user_status,))
            print("LOL")
            cur.execute("SELECT user_id,user_name,chat_id_for_acess  FROM users")
            conn.commit()
    elif ("error_code" not in res.json()) and (res.json()["result"]["status"]==("left"or"kicked")):
        bot.send_message(message.from_user.id, 'НЕТ ДОСТУПА' ) 

    elif "error_code" in res.json():#если пользователя нет в чате
        bot.send_message(message.from_user.id, 'НЕТ ДОСТУПА. ЧТобы его получить вы должны состоять в чате' ) 
    cur.close()







if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)

# else:
#     print("LOL")














