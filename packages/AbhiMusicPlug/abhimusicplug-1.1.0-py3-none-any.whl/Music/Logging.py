"""
Telegram @Itz_Your_4Bhi
Copyright ©️ 2025
"""


import logging
from logging.handlers import RotatingFileHandler
from Config import LOG_FILE_NAME

logging.basicConfig(
    level=logging.ERROR,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=5000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
