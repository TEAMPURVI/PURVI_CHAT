import random
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.enums import ChatAction, ChatType
from pyrogram.types import *
from config import MONGO_URL
from RAUSHAN import AMBOT
from RAUSHAN.modules.helpers import CHATBOT_ON, is_admins


@AMBOT.on_message(filters.command("chatbot") & filters.group, group=6)
@is_admins
async def toggle_chatbot(_, message: Message):
    await message.reply_text(
        f"Chat ID: {message.chat.id}\n**Choose an option to enable/disable ChatBot.**",
        reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
    )


@AMBOT.on_message(
    (filters.text & filters.sticker & ~filters.bot), group=4
)
async def handle_chat_message(client: Client, message: Message):
    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]
    vickdb = chatdb["VickDb"]["Vick"]

    if message.chat.type == ChatType.PRIVATE:
        await respond_from_db(client, message, chatai)
        return

    if message.chat.type in ["ChatType.GROUP", "ChatType.SUPERGROUP"]:
        if not message.reply_to_message:
            is_vick = vickdb.find_one({"chat_id": message.chat.id})
            if not is_vick:
                return
            await respond_from_db(client, message, chatai)
        elif message.reply_to_message.from_user.is_self:
            await respond_from_db(client, message, chatai)
        else:
            await learn_response(message, chatai)


async def respond_from_db(client: Client, message: Message, chatai):
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    query_key = (
        message.text if message.text else message.sticker.file_unique_id
    )
    responses = chatai.find({"word": query_key})
    response_list = [x["text"] for x in responses]
    
    if response_list:
        reply = random.choice(response_list)
        response_data = chatai.find_one({"text": reply})
        if response_data["check"] == "sticker":
            await message.reply_sticker(reply)
        else:
            await message.reply_text(reply)


async def learn_response(message: Message, chatai):
    if message.text and message.reply_to_message.text:
        is_chat = chatai.find_one(
            {"word": message.reply_to_message.text, "text": message.text}
        )
        if not is_chat:
            chatai.insert_one(
                {
                    "word": message.reply_to_message.text,
                    "text": message.text,
                    "check": "text",
                }
            )
    elif message.sticker and message.reply_to_message.text:
        is_chat = chatai.find_one(
            {
                "word": message.reply_to_message.text,
                "text": message.sticker.file_id,
            }
        )
        if not is_chat:
            chatai.insert_one(
                {
                    "word": message.reply_to_message.text,
                    "text": message.sticker.file_id,
                    "check": "sticker",
                    "id": message.sticker.file_unique_id,
                }
            )

