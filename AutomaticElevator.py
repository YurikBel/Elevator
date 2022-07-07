from elevators.SimpleElevator import *


class AutomaticElevator(SimpleElevator):
    def _UpN(self, n):
        i = 0
        while i < n:
            self._Up()
            i += 1

    def _DownN(self, n):
        i = 0
        while i < n:
            self._Down()
            i += 1

    def move_to(self, storey):
        if 0 < storey <= self._storeys:
            if storey < self._currentStorey:
                self._DownN(self._currentStorey - storey)
            if storey > self._currentStorey:
                self._UpN(storey - self._currentStorey)
        else:
            raise ValueError('Некорректные данные')
