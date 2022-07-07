from elevators.AutomaticElevator import *

class RestrictiveAutomaticElevator(AutomaticElevator):
    def __init__(self, storeys, out_device):
        super().__init__(storeys, out_device)
        self.restrictedStoreys = []

    def RestrictStorey(self, storey):
        if storey < 0 or storey > self.storeys:
            raise ValueError('Недопустимое значение этажа')
        self.restrictedStoreys.append(storey)

    def move_to(self, storey):
        if storey not in self.restrictedStoreys:
            super().move_to(storey)
            print(f'Этаж: {self.currentStorey}')
        else:
            raise ValueError('Этот этаж заблокирован')

