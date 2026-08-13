# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from . import usersdb, chatsdb

async def get_chats() -> dict:
    chats = []
    users = []

    async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
        chats.append(chat["chat_id"])
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users.append(user["user_id"])

    return {
        "chats": chats,
        "users": users,
    }

async def add_user(user_id, username=None):
    if not await usersdb.find_one({"user_id": user_id}):
        await usersdb.insert_one({"user_id": user_id, "username": username})

async def add_chat(chat_id, title=None):
    if not await chatsdb.find_one({"chat_id": chat_id}):
        await chatsdb.insert_one({"chat_id": chat_id, "title": title})

# ======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/TEAMPURVI/PURVI_CHAT
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
