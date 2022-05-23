import datetime
from telegram import TelegramError
from DestinyBot import dispatcher, SUPPORT_CHAT_ID, LOGGER
from DestinyBot.modules.disable import DisableAbleCommandHandler
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode,
                      Update, Message)
from telegram.ext import CallbackContext, CallbackQueryHandler

def bug(update: Update, context: CallbackContext):
    message = update.effective_message
    IMAGE = "https://telegra.ph/file/a2a1fc1867d1508d1d325.jpg"
    #args = context.args
    #log_message = ""
    bugChannelLink = "//t.me/+ZI_wLUlD3sU1ODZl"
    supportLink = "//t.me/RiasGremorySupportGroup"
    chat = update.effective_chat
    BUG_DETAILS = message.text.split(' ', 1)
    user = update.effective_user
    bot = context.bot
    try:
        chat_id = SUPPORT_CHAT_ID
    except TypeError:
        update.effective_message.reply_text("Bruh, this will work like `/bug <report about a bug>`, don't try to touch my boobs in that manner..")
    to_send = " ".join(BUG_DETAILS)
    #req_by = f"<b>Requested By:</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    to_send = to_send.replace("/","#")
    to_send = to_send.replace("!bug","#bug")
    to_send = to_send.replace("@RiasXbot","")
    buttons = [
        [InlineKeyboardButton("👾Reports👾", url=bugChannelLink)],
        [InlineKeyboardButton("💕Rias Support💕", url=supportLink)]
    ]

    msg = f"Ara your report details Submitted successfully.\n"
    if len(to_send.split(" ")) >= 2:
        try:
            to_send = f"{to_send}\nRequester: @{user.username}\nRequester ID: {user.id}\n\nFrom Chat: {chat.title}\nChat Username: @{chat.username}\nChat ID: {chat.id}\n"
            update.effective_message.reply_photo(
	        IMAGE,
                caption=msg,
                parse_mode=ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            bot.sendMessage(int(chat_id), str(to_send))
        except TelegramError:
            LOGGER.warning("Couldn't send to group %s", str(chat_id))
            update.effective_message.reply_text(
                "Couldn't send the message. Perhaps I'm not part of the report channel?"
            )
    else:
        #to_send = f"{to_send}\n Requested By : {mention_html(user.id, html.escape(user.first_name))}\n From Chat: <b>{html.escape(chat.title)}:</b>\n"
        update.effective_message.reply_text("Bruh, this will work like `/bug <report about a bug>`, don't fuck with me..")
__help__ = """
/bug <report text>*:* Sends a report text mentioned by user directly to
private channel of Rias Support.

*NOTE:* it will also collect user's information, specially their Telegram ID.
So, think twice before spamming this command without any reason.
"""

BUG_HANDLER = DisableAbleCommandHandler("bug", bug, run_async=True)

dispatcher.add_handler(BUG_HANDLER)

__mod_name__ = "Bug Reports"

__handlers__ = [
    BUG_HANDLER
]
