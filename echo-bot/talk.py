import logging

def talk_to_me(bot, update):
    name = update.message.chat.first_name
    text = update.message.text
    user_text = f"Hello {name}! You wrote: '{text}'"

    username = update.message.chat.username
    chat_id = update.message.chat.id
    logging.info(f"User: {username}, Chat id: {chat_id}, Message: {text}")
    update.message.reply_text(user_text)