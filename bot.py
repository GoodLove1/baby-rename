import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5673664225:AAGmOmvihju1n4tqK5Yq6IRI0GaHZdZ_WQY")

API_ID = int(os.environ.get("API_ID", "12635510"))

API_HASH = os.environ.get("API_HASH", "da59e4e56ec4fe35af603bd30208ecc5")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
