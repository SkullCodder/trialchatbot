from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function for the /start command


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hello, I'm a Telegram bot. How can I assist you?")

# Define a function for the /help command


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm here to echo back any message you send me.")

# Define a function for echoing back messages


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)

# Define the main function to start the bot


def main():
    # Your bot's token
    token = "1925876251:AAFv-MKqysOlq1GdSk0wBP4gc3C6zHr8Rp0"

    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add the handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Add the handler for the /help command
    dp.add_handler(CommandHandler("help", help))

    # Add the handler for echoing back messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
