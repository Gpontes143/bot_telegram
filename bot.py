import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o token do ambiente
TOKEN = os.getenv('TOKEN')


# Configuração do logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Função de comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    # Cria a aplicação com o token do bot
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Adiciona o handler para o comando /start
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)
    
    # Inicia o polling
    application.run_polling()
