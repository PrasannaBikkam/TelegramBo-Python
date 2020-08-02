from telegram.ext.dispatcher import run_async
from telegram import Bot

@run_async
def bot_send_message(bot: Bot,chat_id,text,parse_mode=None,reply_markup=None,disable_web_page_preview=True):
    bot.send_message(chat_id=chat_id,parse_mode=parse_mode,text=text,reply_markup=reply_markup,disable_web_page_preview=disable_web_page_preview)
