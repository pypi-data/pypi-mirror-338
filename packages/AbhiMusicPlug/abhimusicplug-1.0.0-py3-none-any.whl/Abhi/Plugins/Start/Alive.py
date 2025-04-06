"""
Telegram @Itz_Your_4Bhi
Copyright ©️ 2025
"""


from pyrogram import filters
from Abhi import app
from Abhi.Misc import _boot_
from Abhi.Utils.Formaters import get_readable_time
import Config
import time

PING_COMMAND = ["alive", "ping"]
PREFIX = Config.PREFIX


@app.on_message(filters.command(PING_COMMAND, PREFIX))
async def _ping(_, message):
    uptime = get_readable_time(int(time.time() - _boot_))
    await message.reply_text(f"Jinda hu saale...since {uptime}")
