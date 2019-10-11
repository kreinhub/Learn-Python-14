import logging
import ephem
from datetime import datetime


def get_next_full_moon(bot, update):
    short_date = datetime.now()
    next_full_moon = ephem.next_full_moon(short_date)

    bot_answer = f"Next full moon at {next_full_moon}"
    update.message.reply_text(bot_answer)

    log_text = f"/next_full_moon is called"
    logging.info(log_text)    


