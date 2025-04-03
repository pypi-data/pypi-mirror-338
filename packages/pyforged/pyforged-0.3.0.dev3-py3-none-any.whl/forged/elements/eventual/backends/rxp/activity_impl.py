from loguru import logger
from rx3.subject import Subject
from rx3 import operators as ops

class RxActivity:
    def __init__(self):
        self.subject = Subject()

    def push(self, value):
        logger.debug(f"Pushing value to subject: {value}")
        self.subject.on_next(value)

    def pipe(self, *operators):
        if operators:
            return self.subject.pipe(*operators)
        return self.subject

    def subscribe(self, callback):
        logger.debug(f"Subscribing callback: {callback}")
        return self.subject.subscribe(callback)