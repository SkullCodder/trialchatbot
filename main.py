import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Create a new bot instance
bot = telegram.Bot(token='YOUR_TOKEN_HERE')

# Define a command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a bot. How can I help you?")

# Define a message handler
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Create an updater and attach the handlers
updater = Updater(token='YOUR_TOKEN_HERE', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start polling for new updates
updater.start_polling()
updater.idle()
