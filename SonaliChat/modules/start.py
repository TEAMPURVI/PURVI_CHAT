# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatType

from config import STICKER, FSUB, IMG, LOGGER_GROUP_ID, OWNER_ID, SUPPORT_GROUP, UPDATES_CHANNEL
from SonaliChat import app
from SonaliChat.database import add_user, add_chat, get_fsub, chatsdb


def get_stbutton():
    return [
      [
           InlineKeyboardButton(
        text="✙ ʌᴅᴅ ϻє ʙᴧʙʏ ✙",
        url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            ),
      ],
      [
        InlineKeyboardButton(
          text="⌯ ❍ᴡɴᴇʀ ⌯",
          user_id=OWNER_ID,
        ),
          InlineKeyboardButton(
          text="⌯ ᴧʙσᴜᴛ ⌯",
          callback_data="ABOUT",
        ),
      ],
        [
            InlineKeyboardButton(text="⌯ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅs ⌯", callback_data="help"),
        ],
    ]

ABOUT_BUTTON = [
    [
        InlineKeyboardButton("⌯ 𝛅ᴜᴘᴘσʀᴛ ⌯", url=f"https://t.me/{SUPPORT_GROUP}"),
        InlineKeyboardButton("⌯ ᴜᴘᴅᴧᴛє ⌯", url=f"https://t.me/{UPDATES_CHANNEL}")
    ],
    [
        InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"HELP_BACK")
    ]
]

HELP_BACK = [

    [
        InlineKeyboardButton(text="𝛅ᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
        InlineKeyboardButton(text="вᴧᴄᴋ", callback_data="HELP_BACK"),
    ],
]


def get_start_text():
    return f"""
**╭────────────────────⦿
│❖ ʜєʏ ɪ'ϻ {app.me.mention} 🥳
├────────────────────⦿
│✦ ɪ ᴧϻ ϻɪηɪ ᴄʜᴧᴛ ʙσᴛ. 🙌
│✦ ᴧɪ ʙᴧsєᴅ & sσϻє ғєᴧᴛᴜʀєs. 😆
├────────────────────⦿
│✦ ʀєᴘʟʏ ɪη ɢʀσᴜᴘs & ᴘʀɪᴠᴧᴛє.🥀
│✦ ηᴏ ᴧʙᴜsɪηɢ & zєʀσ ᴅσᴡηᴛɪϻє.🍫
│✦ ᴄʟɪᴄᴋ ʜєʟᴘ ʙᴜᴛᴛση ғσʀ ʜєʟᴘs.❤️‍🔥
├────────────────────⦿
│❖ ϻᴧᴅє ʙʏ...[˹ ᴘᴜʀᴠɪ-ᴍᴜ𝛅𝛊ᴄ™ ˼](t.me/{SUPPORT_GROUP})♡
╰────────────────────⦿**
"""


HELP_ABOUT =f"""
**─────────────────────────
❖ ᴧ ϻɪηɪ ᴄʜᴧᴛ ʙσᴛ ғσʀ ᴛєʟєɢʀᴧϻ ɢʀσᴜᴘs & ᴘʀɪᴠᴧᴛє
─────────────────────────
● ᴡʀɪᴛᴛєη ɪη ➥ [ᴩʏᴛʜση](https://www.python.org/)
● ᴅᴧᴛᴧʙᴧsє ➥ [ϻᴏηɢᴏ-ᴅʙ](https://www.mongodb.com/)
● ʀєsᴘσηᴄє [ᴄʜᴀᴛ-ɢᴘᴛ](https://openai.com/)
─────────────────────────
● ᴧη ᴧɪ ʙᴀsєᴅ ᴄʜᴀᴛ ʙσᴛ.
● ᴋєєᴘ ʏσᴜʀ ᴧᴄᴛɪᴠє ɢʀσᴜᴘ.
● ᴧᴅᴅ ϻє ηᴏᴡ ʙᴧʙʏ ɪɴ ʏᴏᴜʀ ɢʀσᴜᴘs.
─────────────────────────
❖ υᴘᴅᴧᴛєs ᴄʜᴧηηєʟ ➥ [ᴘᴜʀᴠɪ-ʙᴏᴛs](https://t.me/{UPDATES_CHANNEL})
❖ sυᴘᴘσʀᴛ ᴄʜᴧᴛ ➥ [ᴘᴜʀᴠɪ-ᴜᴘᴅᴀᴛᴇs](https://t.me/{SUPPORT_GROUP})
❖ ʙᴏᴛ σᴡηєʀ ➥ [⎯᪵፝֟፝֟⎯꯭𓆩꯭ 𝐀 ꯭ʟ ꯭ᴘ ꯭ʜ꯭ ᴧ꯭⎯꯭꯭‌꯭🥂꯭༎꯭ 𓆪](https://t.me/TheSigmaCoder)
❖ ʀєᴘσ ʟɪηᴋ ➥ [ᴄʟɪᴄᴋ-ʜєʀє](github.com/TEAMPURVI/PURVI_CHAT)
─────────────────────────**
"""

HELP_READ =f"""
**<u>⊚ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs  :</u>

<u>⊚ ᴀʟʟ ᴜsᴇʀs :</u>

/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.
/ping - ᴄʜᴇᴀᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ.
/help - sᴇᴇ ʜᴇʟᴘ ᴘᴀɴɴᴇʟ.
/stats - ᴄʜᴇᴀᴋ ʙᴏᴛ sᴛᴀᴛs.
/id - ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ 

<u>⊚ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ :</u>

/chabot - ᴇɴᴀʙʟᴇ / ᴅɪsᴀʙʟᴇ ʜᴀɴᴅʟɪɴɢ

➻ ɴᴏᴛᴇ : ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs

<u>⊚ ᴏɴʟʏ ᴏᴡɴᴇʀ :</u>

/broadcast message - sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ɢʀᴏᴜᴘs & ᴜsᴇʀs.

✦ 𝐏ᴏᴡᴇʀᴇᴅ вʏ » [ᴀʟᴘʜᴀ-ʙᴀʙʏ](t.me/TheSigmaCoder)**
"""



@app.on_message(filters.command(["start"]) & ~filters.bot)
async def start(client, m: Message):
    if FSUB and not await get_fsub(client, m):
        return

    bot_name = app.name

    if m.chat.type == ChatType.PRIVATE:
        user_id = m.from_user.id
        await add_user(user_id, m.from_user.username or None)

        if STICKER and isinstance(STICKER, list):
            sticker_to_send = random.choice(STICKER)
            umm = await m.reply_sticker(sticker=sticker_to_send)
            await asyncio.sleep(1)
            await umm.delete()

        log_msg = f"**✦ ηєᴡ ᴜsєʀ sᴛᴧʀᴛєᴅ ᴛʜє ʙσᴛ**\n\n**➻ ᴜsєʀ :** [{m.from_user.first_name}](tg://user?id={user_id})\n**➻ ɪᴅ :** `{user_id}`"
        await client.send_message(LOGGER_GROUP_ID, log_msg)

        purvi = await m.reply_text(text="**ꜱᴛᴧʀᴛɪηɢ....🥀**")
        await asyncio.sleep(1)
        await purvi.edit("**ᴘɪηɢ ᴘσηɢ...🍫**")
        await asyncio.sleep(0.5)
        await purvi.edit("**ꜱᴛᴧʀᴛєᴅ.....😱**")
        await asyncio.sleep(0.5)
        await purvi.delete()

        await m.reply_photo(
        photo=random.choice(IMG),
        caption=get_start_text(),
        reply_markup=InlineKeyboardMarkup(get_stbutton()),
    )



@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        chat_id = message.chat.id
        chat_title = message.chat.title
        added_by = message.from_user.mention if message.from_user else "Unknown User"
        chatusername = f"@{message.chat.username}" if message.chat.username else "Private Chat"
        
        try:
            chat_info = await client.get_chat(chat_id)
            total_members = chat_info.members_count
        except:
            total_members = "Unknown"

        try:
            invite_link = await client.export_chat_invite_link(chat_id)
        except Exception:
            invite_link = f"https://t.me/{SUPPORT_GROUP}"

        await add_chat(chat_id, chat_title)

        await message.reply_photo(
            photo=random.choice(IMG),
            caption=get_start_text(),
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("ᴧᴅᴅ ϻє ʙᴧʙʏ", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"),
                    InlineKeyboardButton("sᴜᴘᴘσʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ])
        )

        log_msg = (
            f"<b>✦ ʙᴏᴛ #ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɢʀᴏᴜᴘ</b>\n\n"
            f"**⚘ ɢʀᴏᴜᴘ ɴᴀᴍᴇ :** {chat_title}\n"
            f"**⚘ ɢʀᴏᴜᴘ ɪᴅ :** {chat_id}\n"
            f"**⚘ ᴜsᴇʀɴᴀᴍᴇ :** {chatusername}\n"
            f"**⚘ ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs :** {total_members}\n"
            f"**⚘ ɢʀᴏᴜᴘ ʟɪɴᴋ : [ᴛᴀᴘ ʜᴇʀᴇ]({invite_link})**\n"
            f"**⚘ ᴀᴅᴅᴇᴅ ʙʏ :** {added_by}"
        )

        await app.send_photo(
            LOGGER_GROUP_ID,
            photo=random.choice(IMG),
            caption=log_msg,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ɢʀᴏᴜᴘ ʟɪɴᴋ", url=invite_link)]
            ])
        )
        
@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    if (await client.get_me()).id == message.left_chat_member.id:
        chat_id = message.chat.id
        chat_title = message.chat.title
        remove_by = message.from_user.mention if message.from_user else "Unknown User"
       
        await chatsdb.delete_one({"chat_id": chat_id})
        
        left_msg = (
            f"<b>✦ ʙᴏᴛ #ʟᴇғᴛ ᴀ ɢʀᴏᴜᴘ</b>\n\n"
            f"**⚘ ɢʀᴏᴜᴘ ɴᴀᴍᴇ :** {chat_title}\n"
            f"**⚘ ɢʀᴏᴜᴘ ɪᴅ :** {chat_id}\n"
            f"**⚘ ʀᴇᴍᴏᴠᴇᴅ ʙʏ :** {remove_by}"
        )
        
        await app.send_photo(
            LOGGER_GROUP_ID,
            photo=random.choice(IMG),
            caption=left_msg,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("sᴇᴇ ɢʀᴏᴜᴘ", url=f"https://t.me/{message.chat.username}" if message.chat.username else f"https://t.me/{SUPPORT_GROUP}")]
            ])
        )



@app.on_message(filters.command("help"))
async def help_command(client, message):
    hmm = await message.reply_photo(
        photo=random.choice(IMG),
        caption=HELP_READ,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{client.me.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"),
                InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}")
            ]
        ])
    )
    


@app.on_callback_query(filters.regex('help'))
async def help_button(client, callback_query):
    help_text=HELP_READ
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="back"),
            InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}")
        ]
    ])
    await callback_query.answer()
    await callback_query.message.edit_text(help_text, reply_markup=keyboard)


@app.on_callback_query(filters.regex('back'))
async def back_to_menu(client, callback_query):
    await callback_query.message.edit_text(
        text=get_start_text(),
        reply_markup=InlineKeyboardMarkup(get_stbutton()),
    )



@app.on_callback_query(filters.regex('ABOUT'))
async def about_section(client, callback_query):
    about_text = HELP_ABOUT
    
    keyboard = InlineKeyboardMarkup(ABOUT_BUTTON)
    
    await callback_query.answer()
    await callback_query.message.edit_text(about_text, reply_markup=keyboard)




@app.on_callback_query(filters.regex('HELP_BACK'))
async def help_back(client, callback_query):
    await callback_query.message.edit_text(
        text=get_start_text(),
        reply_markup=InlineKeyboardMarkup(get_stbutton())
    )



@app.on_callback_query(filters.regex('close'))
async def close_callback(client, callback_query):
    try:
        await callback_query.message.delete()
    except Exception:
        pass


# ======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/TEAMPURVI/PURVI_CHAT
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
