# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from SonaliChat import app
from SonaliChat.database import get_chats
from config import OWNER_ID

@app.on_message(filters.command("broadcast"))
async def broadcast_(_, message: Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("❌ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀ!")

    reply = message.reply_to_message
    text = message.text.split(None, 1)[1] if len(message.command) > 1 else None

    if not reply and not text:
        return await message.reply_text("⚠ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ / ʀᴇᴘʟʏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ.")

    progress_msg = await message.reply_text("✦ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")

    sent_groups, sent_users, failed = 0, 0, 0
    data = await get_chats()
    
    recipients = data["chats"] + data["users"]

    for chat_id in recipients:
        try:
            if reply and reply.forward_from:
                msg = await reply.forward(chat_id)
            elif reply:
                msg = await reply.copy(chat_id)
            else:
                msg = await app.send_message(chat_id, text=text)
            
            if chat_id < 0:
                sent_groups += 1
            else:
                sent_users += 1

            await asyncio.sleep(0.2)

        except FloodWait as fw:
            await asyncio.sleep(fw.value + 1)
        except:
            failed += 1  

    await progress_msg.edit_text(
        f"✮ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ :\n\n"
        f"⚘ ɢʀᴏᴜᴘs : {sent_groups}\n"
        f"⚘ ᴜsᴇʀs : {sent_users}\n"
        f"⚘ ғᴀɪʟᴇᴅ : {failed}"
    )

# ======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/TEAMPURVI/PURVI_CHAT
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
