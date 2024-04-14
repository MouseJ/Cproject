import discord
from discord.ext import commands
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot, ParseMode

# Конфигурация Discord
DISCORD_TOKEN = 'h'
DISCORD_CHANNEL_ID = YOUR_DISCORD_CHANNEL_ID

# Конфигурация Telegram
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'

# Инициализация клиентов Discord и Telegram
discord_bot = commands.Bot(command_prefix='!')
telegram_bot = Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

# Функция для пересылки текстовых сообщений из Discord в Telegram
def send_text_to_telegram(message):
    telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

# Функция для пересылки изображений из Discord в Telegram
def send_image_to_telegram(image_url):
    telegram_bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=image_url)

# Обработчик сообщений в Discord
@discord_bot.event
async def on_message(message):
    if message.author == discord_bot.user:
        return
    if message.channel.id == DISCORD_CHANNEL_ID:
        if message.content:
            send_text_to_telegram(f"{message.author.name}: {message.content}")
        for attachment in message.attachments:
            if attachment.url.endswith(('png', 'jpg', 'jpeg', 'gif')):
                send_image_to_telegram(attachment.url)

# Обработчик команды в Telegram
def telegram_command(update, context):
    chat_id = update.message.chat_id
    text = ' '.join(context.args)
    discord_channel = discord_bot.get_channel(DISCORD_CHANNEL_ID)
    discord_bot.loop.create_task(discord_channel.send(text))

# Определение хэндлеров для Telegram
telegram_handlers = [
    CommandHandler('say', telegram_command),
    MessageHandler(Filters.text & (~Filters.command), telegram_command)
]
for handler in telegram_handlers:
    updater.dispatcher.add_handler(handler)

# Запуск ботов
discord_bot.run(DISCORD_TOKEN)
updater.start_polling()
updater.idle()
