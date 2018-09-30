# Главный файлик в этом репозитории...!!!!

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
import os 
import time 
import datetime
import sqlite3
import findwords


logging

TOKEN = "658846717:AAFaeIMx5DhDvW28E8Ci6QtDE5AnzFkr-bQ"

REQUEST_KWARGS={
    'proxy_url': 'socks5://46.8.17.184:1051',
    'urllib3_proxy_kwargs': {
        'username': 'hGUQEoaC',
        'password': 'pbWhw8l3',
    }
  
}

try:
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)    
except :
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)    

dispatcher = updater.dispatcher

def func_00(bot, update, state):
    pass

def func_01(bot, update, state):
    """ функция реализует взаимодействие по ответу на запрос 
        списка слов, соответствующих числу
    """
    global f_words_obj

    msg = update.message.text

    if f_words_obj.test_dig.match(msg):    
        w = f_words_obj.get_words(int(update.message.text))
    else:
        if msg.lower() != 'отмена':
            bot.send_message(
            chat_id=update.message.chat_id, 
            text = 'неправильное какое то число, попробуй еще раз, или отправь слово отмена')
        else:
            set_user_state(update.message.chat_id, update.message.from_user.id, 0, 0)
            return 



    w = "\n".join(w)

    bot.send_message(
        chat_id=update.message.chat_id, 
        text = ("Я обрабатываю запрос на слово... скоро все будет)))\n"
                f""))
    
    bot.send_message(
        chat_id=update.message.chat_id, 
        text = w)
    set_user_state(update.message.chat_id, update.message.from_user.id, 0, 0)
    

def check_db():
    conn = sqlite3.connect("words_bot.db")
    curs = conn.cursor()
    try:
        curs.execute("""\
            SELECT
                *
            FROM 
                bot_users
        """)
    except:
        return None
    else:
        return curs
def get_user_state(chat_id, user_id):
    
    curs = check_db()

    query_str = """\
        SELECT 
            *
        FROM 
            bot_users
        WHERE 
            (chat_id = ?) and (user_id = ?)
    """
    try:
        rows = list(curs.execute(query_str, (chat_id, user_id)))
    except:
        return
    else:
        pass
    if len(rows) == 0:
        query_str = """\
        INSERT INTO
            bot_users             
        VALUES  
        (?, ?, ?, ?)                
        """
        params = (chat_id, user_id, 0, 0)
        curs.execute(query_str, params)
        curs.connection.commit()
        state = (0, 0)
    else:
        query_str = """\
            SELECT 
                active_task, active_stage
            FROM
                bot_users
            WHERE
                (chat_id = ?) and (user_id = ?)
        """
        try:
            rows = list(curs.execute(query_str, (chat_id, user_id)))
        except:
            state = (0, 0)
        else:
            state = rows[0]
    return state

def set_user_state(chat_id, user_id, task_id, stage_num):    

    curs = check_db()

    query_str = """\
        UPDATE 
            bot_users
        SET
            active_task = ?, 
            active_stage = ?
        WHERE
            (chat_id = ?) and (user_id = ?)    
    """
    param = (task_id, stage_num, chat_id, user_id)
    try:
        res = curs.execute(query_str, param)
        curs.connection.commit()
    except:
        return False
    else:
        pass
    print(curs)
    return True

def start(bot, update):    
    bot.send_message(
        chat_id=update.message.chat_id, 
        text = "Вот такие вот дела!!! Привет!!!!")

def find_001(bot, update):    
    bot.send_message(
        chat_id=update.message.chat_id, 
        text = "Я сейчас поищу ответ на вопрос... не отключайся")
    



def echo(bot, update):
    """
    Процедура обработки любого сообщения.
    Сообщение будет обработано только в том случае, если при проверке
    пользователя, будет обнаружено, что имеется активная задача.
    """


    state = get_user_state(update.message.chat_id, 
                            update.message.from_user.id)
    
    msg = (f"ID Чата {update.message.chat_id:}\n"
            f"ID Пользователя {update.message.from_user.id:}\n"
            f"Сообщение {update.message.text:}")
    
    bot.send_message(
        chat_id=update.message.chat_id, 
        text=msg)

    func[state[0]](bot, update, state)

    
    
    
def find_002 (bot, update):
    set_user_state(update.message.chat_id, update.message.from_user.id, 1, 0)
    bot.send_message(
        chat_id=update.message.chat_id, 
        text="Введи число, а я подберу подходящие слова...")


f_words_obj = findwords.words()   

start_handler = CommandHandler('start', start)
find_handler = CommandHandler('find', find_001)
f_word_handler = CommandHandler('fword', find_002)
echo_handler = MessageHandler(Filters.text|Filters.document, echo)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(find_handler)
dispatcher.add_handler(f_word_handler)
dispatcher.add_handler(echo_handler)

def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized as exc:
        print("Ошибка", exc)
        pass
        # remove update.message.chat_id from conversation list
    except BadRequest as exc:
        print("Ошибка", exc)
        pass
        # handle malformed requests - read more below!
    except TimedOut as exc:
        print("Ошибка", exc)
        pass
        # handle slow connection problems
    except NetworkError as exc:
        print("Ошибка", exc)
        pass
        # handle other connection problems
    except ChatMigrated as exc:
        print("Ошибка", exc)
        pass
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        # handle all other telegram related errors
        print("Ошибка", TelegramError)

# curs = check_db()

func = {
    0 : func_00,
    1 : func_01
}

dispatcher.add_error_handler(error_callback)
updater.start_polling()

