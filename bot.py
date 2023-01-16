import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5673664225:AAGmOmvihju1n4tqK5Yq6IRI0GaHZdZ_WQY")

API_ID = int(os.environ.get("API_ID", "12635510"))

API_HASH = os.environ.get("API_HASH", "da59e4e56ec4fe35af603bd30208ecc5")

STRING = os.environ.get("STRING", "BQCFpqf3uF8UQSCZTF_Wf-anrTxQsog8DCPwIIkWQJhoyqMBUTcYq6cmGnwt5SDSwvkxcc10vU3m8OFAe684XfbN7cAtHyizB4_dtRz8Kjc_EHJKxb-uWSTL0zY-FJr3BMMfK5KM-jq_Tt8r5r04N8A0a6et9gH2aos6xtF89BTtjIx3ppjGViMFtYbOmn2_JFMCq-qfqg7aOmMspG4UXr1LfFW8C6jHxCznqdu_YQ9-M8Kdq5bRHAf7emvi3uXrJFGMSUq_J-q5CWA6zPgmIED3OjHLAevJOEnTSbpj1bb45cvTrdM-m2NZXoCaFSXA5is_Hq_4zhYyA0MJDBFeAqAAAAAENduS4A")



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
