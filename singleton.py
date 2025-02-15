import logging

class singleton_logger:
    _initialized = None ;
    _logger = None

    def __new__(cls, *args, **kwargs):
        print("IN NEW")
        if cls._logger is None:
            cls._logger = super(singleton_logger , cls).__new__(cls)
        return  cls._logger

    def __init__(self,  name = "Singleton_logger" , file_name = "Singleton_logger.log"):
        print("IN INIT")
        if not hasattr(self , "_initialized"):
            self._log = logging.getLogger(name)
            self._log.setLevel(level=logging.DEBUG)

            handler = logging.FileHandler(file_name)
            handler.setLevel(level=logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

            self._log.addHandler(handler)

            self._initialized = True


logger1 = singleton_logger()
logger2 = singleton_logger("1" , "2.log")

print(logger1)
print(logger2)

if logger1 is logger2:
    print("Both are same")
else:
    print("Both are NOT same")

