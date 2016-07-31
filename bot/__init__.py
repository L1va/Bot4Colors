import logging
import sys

from bot.web import app


def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel('DEBUG')
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel('DEBUG')
    root_logger.addHandler(handler)

setup_logging()
