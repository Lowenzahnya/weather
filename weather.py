from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError


def check_weather():
    while True:
        try:
            place = input('В каком городе?: ')
            config_dict = get_default_config()
            config_dict['language'] = 'ru'

            owm = OWM('267f53ba6ee5620175b02e58315c4a56', config_dict)
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(place)
            w = observation.weather
            print(f'В городе {place} температура сейчас {w.temperature("celsius")["temp"]}°\n'
                  f'Погода: {w.detailed_status}, влажность {w.humidity}%, скорость ветра {w.wind()["speed"]}м/c')
            break
        except NotFoundError:
            print("Город не найден")


check_weather()
