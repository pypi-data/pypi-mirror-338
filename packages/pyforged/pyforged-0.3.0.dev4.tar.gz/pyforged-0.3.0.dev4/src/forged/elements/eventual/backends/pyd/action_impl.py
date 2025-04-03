from pydispatch import dispatcher
from loguru import logger

class PyDispatcherAction:
    def __init__(self, name):
        self.name = name

    def emit(self, *args, **kwargs):
        logger.debug(f"Emitting event {self.name} with args {args} and kwargs {kwargs}")
        dispatcher.send(signal=self.name, sender=self, **kwargs)

    def connect(self, handler):
        logger.debug(f"Connecting handler {handler} to signal {self.name}")
        dispatcher.connect(handler, signal=self.name, sender=dispatcher.Any)

    def disconnect(self, handler):
        logger.debug(f"Disconnecting handler {handler} from signal {self.name}")
        dispatcher.disconnect(handler, signal=self.name)