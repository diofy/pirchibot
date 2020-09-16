import logging
from logging import error
import random

import sqlite3
from telegram.error import BadRequest



from telegram.ext import Updater, CommandHandler
from telegram.ext import dispatcher

conn = sqlite3.connect('users.db')


users_id = [928026036, 923626248, 460729305, 405196888, 375832364, 368778663, 346956156, 228829286]

updater = Updater("923626248:AAHT1GVNcdDvdUjW6zDYrQ04biRJk4CRfhY", use_context=True)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )

def hello(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Que te pasa puta? queres que te la ponga?'
    )

def russian_roulette(update, context):
    chat_id = update.effective_chat.id
    user_id = update.message.from_user.id
    user_id = random.choice([user_id, False, False, False, False, False])
    if user_id:
        try:
            context.bot.kick_chat_member(chat_id=chat_id, user_id=user_id)
        except BadRequest as error:
            context.bot.send_message(chat_id=chat_id, text=str(error.message))    
    else:
        context.bot.send_message(chat_id=chat_id, text="Safaste Wachin")


dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('russian_roulette', russian_roulette))

updater.start_polling()
updater.idle()