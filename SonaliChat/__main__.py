# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import importlib

from pyrogram import idle

from SonaliChat import app
from SonaliChat.modules import ALL_MODULES

async def boot():
    await app.start()

    for module in ALL_MODULES:
        importlib.import_module(f"SonaliChat.modules.{module}")

    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run(boot())

# ======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/TEAMPURVI/PURVI_CHAT
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
