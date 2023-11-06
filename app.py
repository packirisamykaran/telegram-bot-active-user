import telebot

# Get your bot token from BotFather: https://telegram.me/BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Create a new TeleBot object
bot = telebot.TeleBot(BOT_TOKEN)

# Define a function to get the active users of a chat group


def get_active_users(chat_id):
    """Gets the active users of a chat group.

    Args:
        chat_id: The ID of the chat group.

    Returns:
        A list of the active users of the chat group.
    """

    active_users = []
    for member in bot.get_chat_members(chat_id):
        if member.status == 'online':
            active_users.append(member.user)
    return active_users

# Define a command handler for the bot


@bot.message_handler(commands=['active_users'])
def active_users_command(message):
    """Gets the active users of the chat group."""

    chat_id = message.chat.id
    active_users = get_active_users(chat_id)

    response = 'The active users of this chat group are:\n'
    for user in active_users:
        response += f'- {user.first_name}\n'

    bot.send_message(chat_id, response)


# Start the Telegram bot
bot.polling()
