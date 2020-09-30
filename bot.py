#!/usr/bin/env python
# coding: utf-8

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import socket

TELEGRAM_BOT_TOKEN = "1287201929:AAFPRjNM90jzaQa3PL8TXM-eYgnmhjv9IFw"

updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello world! I will be your server manager")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()


def internal_ip():
    return socket.gethostbyname(socket.gethostbyname())


def ip(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=internal_ip())


ip_handler = CommandHandler('internalip', ip)
dispatcher.add_handler(ip_handler)

updater.start_polling()


def command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text);


command_handler = MessageHandler(Filters.text, command)
dispatcher.add_handler(command_handler)
