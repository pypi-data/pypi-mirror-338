"""
Telegram @Itz_Your_4Bhi
Copyright ©️ 2025
"""


from pyrogram import Client
from pytgcalls import PyTgCalls

import Config
from ..Logging import LOGGER

api_id: int = Config.API_ID
api_hash: str = Config.API_HASH
session_string: str = Config.SESSION_STRING

MusicBot = Client(
    name="Abhi", api_id=api_id, api_hash=api_hash, session_string=session_string
)

MusicUser = PyTgCalls(MusicBot)
