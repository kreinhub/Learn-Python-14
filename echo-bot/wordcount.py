import logging


def get_wordcount(bot, update):
    list_text = update.message.text.split()
    words_count = len(list_text[1:])
    if words_count > 1 or words_count == 0:
        bot_answer = f"You entered {words_count} words"
    else:
        bot_answer = f"You entered {words_count} word"

    log_text = f"/wordcount is called with arg: {' '.join(list_text)}"
    logging.info(log_text)
    update.message.reply_text(bot_answer)
