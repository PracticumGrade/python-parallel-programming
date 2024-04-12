# import logging
# import threading
# import subprocess
# import multiprocessing


from external.client import YandexWeatherAPI
from tasks import (
    DataFetchingTask,
    DataCalculationTask,
    DataAggregationTask,
    DataAnalyzingTask,
)
from utils import CITIES, get_url_by_city_name


def forecast_weather():
    """
    Анализ погодных условий по городам
    """
    # TODO Воспользуйтесь реализованными вами классами для решения
    pass


if __name__ == "__main__":
    forecast_weather()
