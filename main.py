import os
from dotenv import load_dotenv
from typing import Final
from telegram import Update
from telegram.ext import Application,ContextTypes,CommandHandler,MessageHandler

load_dotenv()

TOKEN:Final = os.environ.get('TOKEN')
BOT_USERNAME : Final = os.environ.get('BOT_USERNAME')


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello world!!!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a help command')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


# Responses
    
def handle_response(text: str) -> str:
    if "hello" in text:
        return 'Hello world'
    

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start' , start_command))
    app.add_handler(CommandHandler('help' , help_command))
    app.add_handler(CommandHandler('custom' , custom_command))


    print("Polling...")
    app.run_polling(poll_interval=3)