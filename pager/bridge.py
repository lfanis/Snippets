#!/usr/bin/env python

import logging
from uuid import uuid4
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.ext import Updater, CommandHandler, CallbackContext, ChatMemberHandler
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.utils.helpers import escape_markdown

from typing import Tuple, Optional
import paramiko

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def dinner(update, context):
    """ The command that get triggered based on a message """
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="SSHing to pi")
    logger.debug(update.message.text)
    sendrf_overssh("dinner")


def echo(update, context):
    """ Command that echo back only in private channel"""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)
    logger.debug(update.message.text)


def sendrf_overssh(requestmessage):
    hostname = '192.168.1.56'
    port = 22
    username = 'pi-start'
    password = 'mypassword'

    # This is for debugging purpose but if you had different messages to send over page you would do a lookup
    logger.info(requestmessage)
    # SSH Part
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    command = 'sudo wrapper.sh'
    (stdin, stdout, stderr) = s.exec_command(command)
    # XXX Ideally you check the output and message the channel back
    # for line in stdout.readlines():
    #    print(line)
    s.close()


if __name__ == "__main__":
    # Iniialize logger
    logger = logging.getLogger(__name__)

    # Initialize bot and dispatcher
	# XXX You should pull the API from the environment variable / .env file not hardcoded.
    updater = Updater(
        token='XXX PUT API KEY HERE', use_context=True)
    dispatcher = updater.dispatcher

    # When sent  /dinner call function start
    start_handler = CommandHandler('start', dinner)
    dispatcher.add_handler(start_handler)

    # Anything sent is reflected
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()
