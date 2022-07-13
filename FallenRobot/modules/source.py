from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


ANON = "https://telegra.ph/file/336e96deae67b251c2a78.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [lucy ʙᴏᴛ-🇮🇩](t.me/LUCY_MANAGEMENT_BOT)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [lucy](tg://user?id=5110793115)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**Lucy ʙᴏᴛ sᴏᴜʀᴄᴇ ɪs  not available**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url="tg://user?id=5484516982"), 
                    InlineKeyboardButton(
                        "• rishabh •", url="https://t.me/thanosuser")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
