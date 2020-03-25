import asyncio
import time
from asyncio import wait
from userbot.utils import admin_cmd

@borg.on(admin_cmd("tspam"))
async def tmeme(e):
     tspam = str(e.text[7:])
     message = tspam.replace("fuck", "madarchod", "randi", "lode", "laude")
     for letter in message:
         await e.respond(letter)
     await e.delete()
