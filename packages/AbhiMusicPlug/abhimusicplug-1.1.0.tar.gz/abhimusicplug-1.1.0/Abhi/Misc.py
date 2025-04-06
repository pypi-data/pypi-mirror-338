"""
Telegram @Itz_Your_4Bhi
Copyright ©️ 2025
"""

import time
from pyrogram import filters

from .Logging import LOGGER
import Config


SUDOERS = filters.user()

_boot_ = time.time()


def sudo():
    global SUDOERS
    for user_id in Config.OWNER_ID:
        SUDOERS.add(user_id)
    LOGGER("Player").info("SUDO USERS LOADED")
