# suppose we have a weather station which emmits the current disaster signal,
# and we have some devices (phone display, radio display, home display) which
# warns people about the weather in differnt way. So, every "emit" mush be caught
# by all displays, meaning displays "obseres" the weacher. this pattern is called
# the observer pattern
import abc
import time
import random


class ObservableInterface():
    """
    Interface for weather station
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add(self, observer):
        """
        Add overserver
        """
        pass

    @abc.abstractmethod
    def remove(self, observer):
        """
        Remove observer
        """
        pass

    @abc.abstractmethod
    def notify(self, disaster_signal):
        pass


class ObserverInterface():
    """
    Interfaces for displays
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, disaster_signal):
        pass


class WeatherStation(ObservableInterface):
    """
    Our weather station
    """

    _observer_list = []

    def add(self, observer):
        self._observer_list.append(observer)

    def remove(self, observer):
        index = self._observer_list.index(observer)
        del self._observer_list[index]

    def notify(self, disaster_signal):
        for observer in self._observer_list:
            observer.update(disaster_signal)


class PhoneDisplay(ObserverInterface):
    """
    Phone display
    """
    def update(self, disaster_signal):
        if disaster_signal > 5:
            print("Phone says: Go home")
            return

        print("Phone says: Have a good day")

class HomeDisplay(ObserverInterface):
    """
    Home Display
    """
    def update(self, disaster_signal):
        if disaster_signal > 5:
            print("Home says: Please stay inside!")
            return

        print("It's a beautiful day! Go outside and enjoy!")

def generate_random_weather_data(count):
    for i in range(0, count):
        temperature = random.randint(0, 10)
        print("Temperature: %s" % (temperature))
        weather_station.notify(temperature)
        time.sleep(5)

weather_station = WeatherStation()
phone_display = PhoneDisplay()
home_display = HomeDisplay()

weather_station.add(phone_display)
weather_station.add(home_display)

generate_random_weather_data(5)

weather_station.remove(phone_display)

generate_random_weather_data(5)