import os
import logging


class Main:
    def __init__(self):
        logging.basicConfig()
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

    def logging_exception(self):
        try:
            raise Exception("exception message")
        except Exception as e:
            self._logger.error("logging.error(exc_info=True): %s", e, exc_info=True)  # Show stack trace
            self._logger.info("================================")

            self._logger.error("logging.error(exc_info=False): %s", e)
            self._logger.info("================================")

            self._logger.exception("logging.exception()")  # Show stack trace
