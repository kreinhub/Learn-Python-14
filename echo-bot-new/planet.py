import ephem
import datetime
import logging


def get_planet_constelation(bot, update):
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



# planet_name = input("Enter planet: ").lower().capitalize()
# short_date = datetime.datetime.now().strftime("%x")

# planet_object = getattr(ephem, planet_name)(short_date)
# print(planet_object)

# const = ephem.constellation(planet_object)
# print(const)


