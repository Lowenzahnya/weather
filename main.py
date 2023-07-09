import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import APIRequestError
from pyowm.commons.exceptions import NotFoundError
from random import choice


class WeatherCheck(QtWidgets.QMainWindow):
    def __init__(self):
        super(WeatherCheck, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Weather')

        cities = ['Москва, Россия', "Белград, Сербия", "Нью-Йорк, США", "Рим, Италия", "Пекин, Китай"]
        self.ui.lineEdit.setPlaceholderText(choice(cities))
        self.ui.pushButton.clicked.connect(self.weather_check)

    def weather_check(self):
        try:
            config_dict = get_default_config()
            config_dict['language'] = 'ru'
            owm = OWM('267f53ba6ee5620175b02e58315c4a56', config_dict)
            mgr = owm.weather_manager()

            input_string = self.ui.lineEdit.text()
            observation = mgr.weather_at_place(input_string)
            w = observation.weather
            self.ui.textEdit.setText(f'Температура сейчас {w.temperature("celsius")["temp"]}° \n'
                                     f'Погода: {w.detailed_status.capitalize()} \n'
                                     f'Влажность: {w.humidity}% \n'
                                     f'Скорость ветра: {w.wind()["speed"]} м/с ')
        except APIRequestError:
            self.ui.textEdit.setText('Город не найден')
        except NotFoundError:
            self.ui.textEdit.setText('Город не найден')


app = QtWidgets.QApplication(sys.argv)
window = WeatherCheck()
window.show()

sys.exit(app.exec())
