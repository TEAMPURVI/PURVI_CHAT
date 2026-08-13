# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import AUTH_CHANNEL, IMG
import random

async def get_fsub(bot, message):
    target_channel_id = AUTH_CHANNEL  
    user_id = message.from_user.id
    try:
        await bot.get_chat_member(target_channel_id, user_id)
    except UserNotParticipant:
        channel_link = (await bot.get_chat(target_channel_id)).invite_link
        join_button = InlineKeyboardButton("ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=channel_link)

        keyboard = [[join_button]]
        await message.reply_photo(
            photo=random.choice(IMG),
            caption=f"**❖ ʜᴇʏ {message.from_user.mention} ᴡʜᴀᴛ ᴀʀᴇ ʏᴏᴜ ᴅᴏɪɴɢ? 🤔**\n\n"
                    f"**» ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ [ᴄʜᴀɴɴᴇʟ]({channel_link}) ᴛʜᴇɴ sᴇɴᴅ /start ᴀɢᴀɪɴ ғᴏʀ sᴇᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴜ 📋**",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return False
    else:
        return True

# ======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/TEAMPURVI/PURVI_CHAT
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
