import datetime
from enum import Enum
from mealbot.config import MealBotConfig
import requests


DEFAULT_CONFIG_FILENAME = 'config/mealbot.conf'


class MealBot(object):
    def __init__(self, conf_file=DEFAULT_CONFIG_FILENAME):
        self.conf = MealBotConfig(conf_file)
        self.meal_time = MealTime.get_meal_time()

    def post(self):
        if self.meal_time != MealTime.OTHER:
            url = self.conf.dooray.hook_url
            data = self._make_data()
            header = {'Content-Type': 'application/json'}
            response = requests.post(url, json=data, headers=header)
            if response.status_code == 200:
                print(data)
                return 'OK'
        return 'Not yet meal time'

    def _make_data(self):
        return {
            'botName': self.conf.mealbot.get_name(self.meal_time.value),
            'botIconImage': self.conf.mealbot.face_url,
            'text': self._get_message()
        }

    def _get_message(self):
        message = self.conf.mealbot.get_message(self.meal_time.value) + '\n'
        if self.meal_time == MealTime.LUNCH:
            message += self.conf.mealbot.get_recommended_message() + '\n'
        message += self.conf.mealbot.get_random_pic()
        return message


class MealTime(Enum):
    BREAKFAST = 0
    LUNCH = 1
    DINNER = 2
    OTHER = 3

    @staticmethod
    def get_meal_time():
        now = datetime.datetime.now()
        if now.hour == 8:
            return MealTime.BREAKFAST
        elif now.hour == 11:
            return MealTime.LUNCH
        elif now.hour == 18:
            return MealTime.DINNER
        else:
            return MealTime.OTHER
