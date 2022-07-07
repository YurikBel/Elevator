from elevators.InformativeAutomaticElevator import *


class VeryInformativeAutomaticElevator(InformativeAutomaticElevator):
    def _UpN(self, n):
        self._out_device.write(f'Лифт идет вверх на {n} этажей')
        super()._UpN(n)

    def _DownN(self, n):
        self._out_device.write(f'Лифт идет вниз на {n} этажей')
        super()._DownN(n)

