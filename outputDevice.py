from abc import ABC, abstractmethod


class OutputDevice(ABC):
    @abstractmethod
    def write(self, s):
        pass

    @abstractmethod
    def close(self):
        pass


class ConsoleDevice(OutputDevice):
    def write(self, s):
        print(s)

    def close(self):
        pass


class FileDevice(OutputDevice):
    def __init__(self, filename):
        self.file = open(filename, 'w')

    def write(self, s):
        self.file.write(s + '\n')

    def close(self):
        self.file.close()
