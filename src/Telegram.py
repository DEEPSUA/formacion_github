# Instalar la librería python-telegram-bot: pip3 install python-telegram-bot
# Guardar el script en un fichero llamado telegram.py
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

updater = Updater(token='TOKEN', use_context=True) # TOKEN es el token de nuestro bot de Telegram
dp = updater.dispatcher
jq = updater.job_queue

def currentChatInfo(update: Update, context: CallbackContext):
    update.effective_message.reply_text(update.effective_chat.to_json())
  
dp.add_handler(CommandHandler('currentChatInfo', currentChatInfo))

updater.start_polling()
updater.idle()
# Ejecutar el script: python3 telegram.py
# Escribir al bot de Telegram: /currentChatInfo