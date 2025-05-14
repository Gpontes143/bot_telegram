import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from textoclass import texto

load_dotenv()

texto_inicial = texto.texto_inicial()

TOKEN = os.getenv('TOKEN')


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text= texto_inicial)

if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).build()
    

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()
