# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated
from pyrogram.enums import ChatAction, ChatMemberStatus
from SonaliChat import app
from SonaliChat.database import (
    is_SonaliChat_enabled,
    enable_SonaliChat,
    disable_SonaliChat,
    SonaliChat_api,
    is_admins
)

async def text_filter(_, __, m: Message):
    return (
        bool(m.text)
        and len(m.text) <= 69
        and not m.text.startswith(("!", "/"))
        and (not m.reply_to_message or m.reply_to_message.from_user.id == m._client.me.id)
        and not (m.mentioned and (m.text.startswith("!") or m.text.startswith("/")))
    )

SonaliChat_filter = filters.create(text_filter)

@app.on_message(
    (
        filters.text & filters.group & SonaliChat_filter
        & ~filters.regex(r"^[/!]")
    )
    & ~filters.bot
    & ~filters.sticker
)
async def SonaliChat(_, message: Message):
    chat_id = message.chat.id

    if not await is_SonaliChat_enabled(chat_id):
        return

    await app.send_chat_action(chat_id, ChatAction.TYPING)
    reply = SonaliChat_api.ask_question(message.text)
    await message.reply_text(reply or "❖ ᴄʜᴀᴛʙᴏᴛ ᴇʀʀᴏʀ. ᴄᴏɴᴛᴀᴄᴛ @Purvi_Updates.")

@app.on_message(filters.private & filters.text & ~filters.bot & ~filters.regex(r"^[/!]"))
async def SonaliChat_pm(_, message: Message):
    await app.send_chat_action(message.chat.id, ChatAction.TYPING)
    reply = SonaliChat_api.ask_question(message.text)
    await message.reply_text(reply or "❖ ᴄʜᴀᴛʙᴏᴛ ᴇʀʀᴏʀ. ᴄᴏɴᴛᴀᴄᴛ @Purvi_Updates.")


@app.on_message(filters.command("chatbot") & filters.group & ~filters.bot)
@is_admins
async def SonaliChat_toggle(_, message: Message):
    chat_id = message.chat.id
    chat_title = message.chat.title

    status = await is_SonaliChat_enabled(chat_id)
    status_text = "ᴇɴᴀʙʟᴇᴅ" if status else "ᴅɪꜱᴀʙʟᴇᴅ"

    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("ᴇɴᴀʙʟᴇ", callback_data="SonaliChat_enable"),
            InlineKeyboardButton("ᴅɪꜱᴀʙʟᴇ", callback_data="SonaliChat_disable")
        ]]
    )

    await message.reply_text(
        f"❖ ᴄᴜʀʀᴇɴᴛʟʏ ᴄʜᴀᴛʙᴏᴛ ɪꜱ **{status_text}** ɪɴ **{chat_title}**.",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex("SonaliChat_"))
@is_admins
async def SonaliChat_button_toggle(_, query):
    chat_id = query.message.chat.id
    user = query.from_user

    if query.data == "SonaliChat_enable":
        if await is_SonaliChat_enabled(chat_id):
            await query.answer("ᴄʜᴀᴛʙᴏᴛ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.", show_alert=True)
            return
        await enable_SonaliChat(chat_id)
        await query.message.edit_text(
            f"❖ ᴄʜᴀᴛʙᴏᴛ ʜᴀꜱ ʙᴇᴇɴ **ᴇɴᴀʙʟᴇᴅ** ʙʏ {user.mention}."
        )
        await query.answer("ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ !!")

    elif query.data == "SonaliChat_disable":
        if not await is_SonaliChat_enabled(chat_id):
            await query.answer("ᴄʜᴀᴛʙᴏᴛ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴅɪꜱᴀʙʟᴇᴅ.", show_alert=True)
            return
        await disable_SonaliChat(chat_id)
        await query.message.edit_text(
            f"❖ ᴄʜᴀᴛʙᴏᴛ ʜᴀꜱ ʙᴇᴇɴ **ᴅɪꜱᴀʙʟᴇᴅ** ʙʏ {user.mention}."
        )
        await query.answer("ᴄʜᴀᴛʙᴏᴛ ᴅɪꜱᴀʙʟᴇᴅ !!")

# ======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/TEAMPURVI/PURVI_CHAT
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
