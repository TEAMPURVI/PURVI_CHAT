# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from . import chatbot_settings_db, chatsdb


async def is_SonaliChat_enabled(chat_id: int) -> bool:
    chat = await chatbot_settings_db.find_one({"chat_id": chat_id})
    return chat is None

async def enable_SonaliChat(chat_id: int):
    await chatbot_settings_db.delete_one({"chat_id": chat_id})

async def disable_SonaliChat(chat_id: int):
    if not await chatbot_settings_db.find_one({"chat_id": chat_id}):
        await chatbot_settings_db.insert_one({"chat_id": chat_id})

async def get_enabled_chats() -> list:
    disabled = await chatbot_settings_db.find({}, {"chat_id": 1, "_id": 0}).to_list(length=None)
    disabled_ids = {d["chat_id"] for d in disabled}
    all_chats = await chatsdb.find({}, {"chat_id": 1, "_id": 0}).to_list(length=None)
    return [c["chat_id"] for c in all_chats if c["chat_id"] not in disabled_ids]

# ======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/TEAMPURVI/PURVI_CHAT
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
