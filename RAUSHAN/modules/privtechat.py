from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.enums import ChatAction
from pymongo import MongoClient
import random
from RAUSHAN import AMBOT
import os
import time
from datetime import datetime
import requests
import config

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")
# MongoDB connection
client = MongoClient(MONGO_URL, connectTimeoutMS=30000, serverSelectionTimeoutMS=30000)
db = client["Word"]
chatai = db["WordDb"]

AMBOT = Client(
    "chat-gpt",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Non-private chats handler (both text and stickers)
@AMBOT.on_message((filters.text | filters.sticker) & ~filters.private & ~filters.bot)
async def vickai(client: Client, message: Message):
    if not message.reply_to_message:
        vick = db["VickDb"]["Vick"]
        is_vick = vick.find_one({"chat_id": message.chat.id})

        if not is_vick:
            await Client.send_chat_action(message.chat.id, ChatAction.TYPING)

            results = chatai.find({"word": message.text})
            results_list = [result for result in results]

            if results_list:
                result = random.choice(results_list)
                if result.get('check') == "sticker":
                    await message.reply_sticker(result['text'])
                else:
                    await message.reply_text(result['text'])

# Private chats handler (both text and stickers)
@AMBOT.on_message((filters.text | filters.sticker) & filters.private & ~filters.bot)
async def vickprivate(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            await Client.send_chat_action(message.chat.id, ChatAction.TYPING)

            results = chatai.find({"word": message.text})
            results_list = [result for result in results]

            if results_list:
                result = random.choice(results_list)
                if result.get('check') == "sticker":
                    await message.reply_sticker(result['text'])
                else:
                    await message.reply_text(result['text'])
    except Exception as e:
        print(f"Error: {e}")
