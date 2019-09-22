import logging


def greet_user(bot, update):
    text = "/start is called"
    logging.info(text)
    update.message.reply_text("I'm echoBot by KREIN. Send me something")