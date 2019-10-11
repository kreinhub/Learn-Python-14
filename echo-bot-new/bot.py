import logging
import datetime

import ephem
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from planet import get_planet_constelation
from wordcount import get_wordcount
from talk import talk_to_me
from greet import greet_user
from next_full_moon import get_next_full_moon
from cities import get_city

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', 
                    level=logging.INFO, 
                    filename='bot.log'
                    )


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Bot starting')

    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet_constelation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("wordcount", get_wordcount))
    dp.add_handler(CommandHandler("next_full_moon", get_next_full_moon))
    dp.add_handler(CommandHandler("cities", get_city))



    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()

