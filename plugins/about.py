import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','5673664225:AAGmOmvihju1n4tqK5Yq6IRI0GaHZdZ_WQY')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Origional BOT :- <a href='https://t.me/KingRenamer_bot'>King</a>\nCreater :- <a href='https://t.me/KingofFondness'>FondnessDeveloper</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- COLAB\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you **<a href='https://t.me/KingofFondness'>FondnessDeveloper</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/KingofFondness'>**Developer**</a> ❤️",quote=True)
