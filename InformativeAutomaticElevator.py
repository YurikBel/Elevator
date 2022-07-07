from elevators.AutomaticElevator import *


class InformativeAutomaticElevator(AutomaticElevator):

    def _Up(self):
        super()._Up()
        self._out_device.write(f'Текущий этаж = {self._currentStorey}')

    def _Down(self):
        super()._Down()
        self._out_device.write(f'Текущий этаж = {self._currentStorey}')
