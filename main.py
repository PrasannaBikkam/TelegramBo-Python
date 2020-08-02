import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler, messagequeue as mq
from telegram.utils.request import Request
from telegram import KeyboardButton,ReplyKeyboardMarkup,Update,Bot,InlineKeyboardMarkup
from uuid import uuid4

updater=Updater('1320336253:AAH_fr9StOyRlCJq_BPCXQm1dO_fy5HiY0c',use_context=True)
dp=updater.dispatcher

def main():
    dp.add_handler(CommandHandler('register',register_command))
    dp.add_handler(MessageHandler(Filters.contact,send_contact_callback))
    updater.start_polling()
    updater.idle()

# def webhook(update):
#     dp.process_update(update)

def register_command(update,context):
    chat_id=update.message.chat_id
    send_contact_button=KeyboardButton(text="Tap to Register", request_contact=True)
    reply_markup=ReplyKeyboardMarkup([[send_contact_button]],resize_keyboard=True,one_time_keyboard=True)
    update.message.reply_text("click the below button to register with paylahBot",reply_markup=reply_markup)

def send_contact_callback(update,context):
    contact = update.effective_message.contact
    phone = contact.phone_number
    update.message.reply_text("Your Phone number has been updated! "+phone)

if __name__=='__main__':
    main()
