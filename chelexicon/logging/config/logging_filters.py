import logging


class LevelFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


class NoPymongoTopologyFilter(logging.Filter):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def filter(self, record):
        return record.name != self.name