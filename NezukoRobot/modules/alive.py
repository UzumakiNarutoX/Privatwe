import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from NezukoRobot.events import register
from NezukoRobot import telethn as borg
from NezukoRobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/2371af37367b3454e9cdf.jpg"
file2 = "https://telegra.ph/file/b3d283f1040d5a2ce8aac.jpg"
file3 = "https://telegra.ph/file/d9986b3e88fdadc021279.jpg"
file4 = "https://telegra.ph/file/262cf5bb9780cbb96afb7.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Miku = f"♡ **Hey [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'm Todou Akira ♡**\n\n"
    Miku += f"♡ **My Uptime** ~♪ `{uptime}`\n\n"
    Miku += f"♡ **Telethon Version** ~♪ `{version.__version__}`\n\n"
    Miku += f"♡ **Python Telegram Bot Version** ~♪ `{telegram.__version__}`\n\n"
    Miku += f"♡ **Pyrogram Version** ~♪ `{pyro}`\n\n"
    Miku += f"♡ **My Master** ~♪ [S L A D E ♡](https://t.me/simp_ly_naveen)\n\n"
    Miku += f"Thanks For Adding Me ♡"
    BUTTON = [[Button.url("Support Chat", "https://t.me/BoaHancock_Support"), Button.url("Updates Channel", "https://t.me/boa_updates")]]
    on = await borg.send_file(yes.chat_id, file=file2,caption=Miku, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file3, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file4, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4, buttons=BUTTON)

@register(pattern=("/repo"))
async def repo(event):
    Miku = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), Click The Button Below To Get My Yamato Repo**\n\n"
    BUTTON = [[Button.url("[► Support ◄]", "https://t.me/BoaHancock_Support"), Button.url("[► Repo ◄]", "https://github.com/Nchuuya/Yamato")]]
    await borg.send_file(event.chat_id, file="https://telegra.ph/file/262cf5bb9780cbb96afb7.jpg", caption=Miku, buttons=BUTTON)
