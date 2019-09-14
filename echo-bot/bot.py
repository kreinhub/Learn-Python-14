from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', 
                    level=logging.INFO, 
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = "/start is called"
    logging.info(text)
    update.message.reply_text("I'm echoBot by KREIN. Send me something")

def talk_to_me(bot, update):
    name = update.message.chat.first_name
    text = update.message.text
    user_text = f"Hello {name}! You wrote: '{text}'"

    username = update.message.chat.username
    chat_id = update.message.chat.id
    logging.info(f"User: {username}, Chat id: {chat_id}, Message: {text}")
    update.message.reply_text(user_text)

def planet(bot, update):
    list_text = update.message.text.split()
    planet_name = list_text[1].lower().capitalize()

    short_date = datetime.datetime.now().strftime("%x")
    try:
        planet_object = getattr(ephem, planet_name)(short_date)
        const = ephem.constellation(planet_object)
        bot_answer = f"{planet_name} is in {const[1]} constellation today"
    
        log_text = f"/planet is called with arg {planet_name}"
        logging.info(log_text)
        update.message.reply_text(bot_answer)
    except AttributeError:
        planets = "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune"
        bot_answer = f"There is no such planet in our galaxy. Try to enter following ones: {planets}"

        logging.info("[Attribute Error] /planet gets wrong planet name")
        update.message.reply_text(bot_answer)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Bot starting')

    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()

