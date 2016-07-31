import os
import sys
import logging

from bot.web import app


def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel('DEBUG')
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel('DEBUG')
    root_logger.addHandler(handler)


if __name__ == '__main__':
    setup_logging()
    PORT = os.environ.get('PORT', 8000)
    app.run(port=PORT, debug=True)
