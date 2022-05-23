from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from DestinyBot import pbot
from DestinyBot.utils.errors import capture_err
from DestinyBot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon to pollute the air`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading Carbon...`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://telegra.ph/file/8e4e0294c6e9bbbaaa144.jpg"

#@support_plus
@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f"""💕 **I'm at your laps darling** 

**Owner : [Hawks](https://t.me/TheShapEye)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`

**My repo is not mentioned below but I'm created using the repo of Emiko repo.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url="https://t.me/Anime_Alfa_X"), 
                    InlineKeyboardButton(
                        "Support", url="https://t.me/RiasGremorySupportGroup")
                ]
            ]
        )
    )
