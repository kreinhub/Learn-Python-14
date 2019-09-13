from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


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

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Bot starting')

    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()

    
Consolas, 'Courier New', monospace