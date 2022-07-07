class SimpleElevator:
    def __init__(self, storeys, out_device):
        if storeys > 0:
            self._storeys = storeys
            self._currentStorey = 1
            self._out_device = out_device
        else:
            raise ValueError('Некорректные данные')

    def _Up(self):
        self._currentStorey += 1

    def _Down(self):
        self._currentStorey -= 1

    @property
    def storeys(self):
        return self._storeys

    @property
    def currentStorey(self):
        return self._currentStorey

