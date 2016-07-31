import os

from bot.web import app


if __name__ == '__main__':
    PORT = os.environ.get('PORT', 8000)
    app.run(port=PORT)
