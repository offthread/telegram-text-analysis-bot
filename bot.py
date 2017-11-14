import logging
import sys

from telegram.ext import Updater, MessageHandler, Filters
from services import ElasticSearchFacade


class Bot(object):

    def __init__(self, token):
        self.updater = Updater(
            token=token)
        self.dispatcher = self.updater.dispatcher

        message_handler = MessageHandler(Filters.chat, self.handle_message)
        self.dispatcher.add_handler(message_handler)

        self.es_connector = ElasticSearchFacade()

    def handle_message(self, bot, update):
        self.es_connector.insert_update(update)
        # bot.send_message(chat_id=update.message.chat_id,
        #                  text="I'm a bot, please talk to me!")


if __name__ == '__main__':
    bot = Bot(sys.argv[1])
    bot.updater.start_polling(timeout=10)
    bot.updater.idle()
