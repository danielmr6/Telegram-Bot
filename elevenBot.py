import datetime

# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hola! Soc Eleven, un bot bàsic en creixement.")
    
def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Tinc disponibles les comandes \start, \help i \hora.")
    
def hora(update, context):
    time_message = str(datetime.datetime.now())
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=time_message)

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('/home/daniel/Documentos/FIB/Q6/LP/Telegram/Projecte/token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('hora', hora))

# engega el bot
updater.start_polling()
updater.idle()