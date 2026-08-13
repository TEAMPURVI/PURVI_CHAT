# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import random
import asyncio
from datetime import datetime

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import IMG, SUPPORT_GROUP, UPDATES_CHANNEL
from SonaliChat import app
from SonaliChat.database import get_chats

start_time = datetime.now()


def get_png_btn():
    return [
        [
            InlineKeyboardButton(
                text="ʌᴅᴅ ϻє", 
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"
            ),
            InlineKeyboardButton(
                text="⌯ 𝛅ᴜᴘᴘᴏʀᴛ ⌯", 
                url=f"https://t.me/{SUPPORT_GROUP}"
            ),
        ],
    ]

@app.on_message(filters.command("ping"))
async def ping(client, message: Message):
    start = datetime.now()
    t = "**ᴘɪηɢɪηɢ..😱**"
    txxt = await message.reply(t)
    await asyncio.sleep(0.25)
    await txxt.edit_text("**ᴘɪηɢɪηɢ...❤️‍🔥**")
    await asyncio.sleep(0.35)
    await txxt.delete()
    end = datetime.now()
    ms = (end-start).microseconds / 1000
    uptime = datetime.now() - start_time
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    await message.reply_photo(
        photo=random.choice(IMG),
        caption=f"**ʜєʏ ʙᴧʙʏ !!**\n**{client.me.mention} ɪꜱ ᴧʟɪᴠє 🥀 ᴧηᴅ ᴡσʀᴋɪηɢ ꜰɪηє ᴡɪᴛʜ**\n\n**➥ ᴘσηɢ :** `{ms}` ms\n**➥ ᴜᴘᴛɪϻє :** `{hours}`ʜ:`{minutes}`ᴍ:`{seconds}`s\n\n**✦ 𝐏σᴡєʀєᴅ вʏ » [ᴀʟᴘʜᴀ-ʙᴀʙʏ](t.me/TheSigmaCoder)**",
        reply_markup=InlineKeyboardMarkup(get_png_btn()),
    )


@app.on_message(filters.command("stats"))
async def stats(client: app, message: Message):
    data = await get_chats()
    total_users = len(data["users"])
    total_chats = len(data["chats"])

    await message.reply_text(
        f"""**✮ {(await client.get_me()).first_name}  ʙᴏᴛ sᴛᴀᴛs :**\n
**:⧽ ᴜsᴇʀs :** {total_users}
**:⧽ ɢʀᴏᴜᴘs :** {total_chats}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{client.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"),
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ]
            ]
        )
    )

# ======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/TEAMPURVI/PURVI_CHAT
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
