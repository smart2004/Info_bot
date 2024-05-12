import json
import logging
import os
import requests
import datetime

from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='main.log',
)

pic = 'adv_whole.jpg'
messagef = 'Анкета обратной связи: \n https://forms.yandex.ru/u/6612f98f068ff0e9a4a17dbe/'

def proposal(update, context):
    pprint(update)
    username = update.message.chat.username
    chat = update.effective_chat
    image = open(pic, 'rb')
    context.bot.send_photo(chat.id, image)
    logging.info(username)

def form(update, context):
    pprint(update)
    username = update.message.chat.username
    chat = update.effective_chat
    context.bot.send_message(chat.id, text='{}'.format(messagef))
    logging.info(username)  # username

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    user = update.message.chat.username
    buttons = ReplyKeyboardMarkup(
        [['/start 👋', '/proposal 📝', '/form ✍']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Доброго времени, {}. Будем знакомы :)'.format(name),
        reply_markup=buttons
    )
    logging.info(name)
    logging.info(user)


def main():
    updater = Updater(token=secret_token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('proposal', proposal))
    updater.dispatcher.add_handler(CommandHandler('form', form))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
