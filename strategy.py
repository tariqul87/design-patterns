# Say we have have multiple duck types, where every duck quacks differently,
# fly differently, but they do belong to duck famility. We can say the an activity (quack, flying, e.t.c.)
# follows different strategy. This is where the strategy pattern comes in. We define abstruct class for Duck
# and also other "activity" strategies. Then, when defining a specific duck, we can initialize that class with
# different statrgy

import abc


class QuackStrategyAbstract():
    """
    Our abstruck strategy for quacking
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def quack(self):
        """
        implement quack strategy!
        """


class FlyStrategyAbstract():
    """
    Flying strategy for a duck
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def fly(self):
        """
        flying method
        """


class VisibilityStrategyAbstract():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def visibility(self):
        """
        implement visibility strategy
        exmaple: if can hide into bushes
        """


class LoudQuack(QuackStrategyAbstract):
    def quack(self):
        print("QUACK QUACK!!!")


class SmallQuack(QuackStrategyAbstract):
    def quack(self):
        print("quack")


class Duck(object):
    def __init__(self, quack_strategy):
        self._quack_strategy = quack_strategy

    def quack(self):
        self._quack_strategy.quack()


small_quack = SmallQuack()
loud_quack = LoudQuack()


class VillageDuck(Duck):
    def __init__(self):
        super(VillageDuck, self).__init__(small_quack)


class MountainDuck(Duck):
    def __init__(self):
        super(MountainDuck, self).__init__(loud_quack)


village_duck = VillageDuck()
mountain_duck = MountainDuck()

print("village duck says: ")
village_duck.quack()

print("mountain duck says: ")
mountain_duck.quack()