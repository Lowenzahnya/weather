from colorama import Fore, Back, Style
from colorama import init

from pyowm import OWM
from pyowm.utils.config import get_default_config

init()
print(Fore.BLACK)
print(Back.CYAN)
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('267f53ba6ee5620175b02e58315c4a56', config_dict)
mgr = owm.weather_manager()

place = input("В каком городе?: ")
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]
veter = w.wind()['speed']

print("В городе " + place + " температура сейчас " + str(temp) + "°.")
print("Погода: " + w.detailed_status + ", влажность: " + str(w.humidity) + "%, скорость ветра: " + str(veter) + " м/с.")
input()