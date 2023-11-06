import telebot

# Get your bot token from BotFather: https://telegram.me/BotFather
BOT_TOKEN = ''

# Create a new TeleBot object
bot = telebot.TeleBot(BOT_TOKEN)

# Define a function to get the active users of a chat group


@bot.message_handler(commands=['total_users'])
def group_users_command(message):
    """Gets the active users of the chat group."""

    chat_id = message.chat.id
    user_id = message.from_user.id

    response = f'total users in the chat is {bot.get_chat_member_count(chat_id)}:\n'

    bot.send_message(chat_id, response)


@bot.message_handler(commands=['start'])
def start_command(message):
    """Gets the active users of the chat group."""

    chat_id = message.chat.id
    user_id = message.from_user.id

    response = 'what would you like to know\n'

    bot.send_message(chat_id, response)


# Start the Telegram bot
bot.polling()
