"""
Telegram @Itz_Your_4Bhi
Copyright ©️ 2025
"""

import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import GroupCallParticipant

from .Core.Bot import MusicBot, MusicUser
from .Logging import LOGGER
from .Misc import sudo

sudo()

app = MusicBot
call = MusicUser


seek_chats = {}



def greet(name: str) -> str:
    return f"Hello, {name}! This is a plugin."
