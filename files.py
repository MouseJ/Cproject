import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton

ALLOWED_USERNAMES = ['5082727140']  # Список разрешенных юзернеймов

# Обработчик команды /start
def start(update: Update, context):
    user_id = str(update.effective_user.id)
    if user_id in ALLOWED_USERNAMES:
        keyboard = [[KeyboardButton("/Upload file")],
                    [KeyboardButton("/Show files"), KeyboardButton("/Delete file")],
                    [KeyboardButton("/Create folder")]]
        reply_markup = ReplyKeyboardMarkup(keyboard)
        update.message.reply_text('Привет! Чем могу помочь?', reply_markup=reply_markup)
    else:
        update.message.reply_text('Вы не авторизованы для использования этого бота.')

# Обработчик для загрузки файлов
def upload_file(update: Update, context):
    user_id = str(update.effective_user.id)
    if user_id not in ALLOWED_USERNAMES:
        update.message.reply_text('Вы не авторизованы для загрузки файлов.')
        return

    file_id = update.message.document.file_id
    file = context.bot.get_file(file_id)
    file.download(f'files/{file_id}.{file.file_path.split(".")[-1]}')  # Сохраняем файл на сервере с оригинальным расширением

    update.message.reply_text('Файл успешно загружен!')

# Обработчик команды /show_files для просмотра списка файлов
def show_files(update: Update, context):
    user_id = str(update.effective_user.id)
    if user_id not in ALLOWED_USERNAMES:
        update.message.reply_text('Вы не авторизованы для просмотра файлов.')
        return

    files = os.listdir('files')
    if files:
        files_list = "\n".join(files)
        update.message.reply_text(f"Список файлов:\n{files_list}")
    else:
        update.message.reply_text("На сервере нет файлов.")

# Обработчик команды /delete_file для удаления файла
def delete_file(update: Update, context):
    user_id = str(update.effective_user.id)
    if user_id not in ALLOWED_USERNAMES:
        update.message.reply_text('Вы не авторизованы для удаления файлов.')
        return

    update.message.reply_text('Выберите файл для удаления:')

def main():
    updater = Updater("6392649985:AAF5aNcBKmj3PyB3MOIEV6p2RFj05mx41CQ", use_context=True)  # Замените "YOUR_TOKEN" на ваш токен
    dp = updater.dispatcher

    # Добавляем обработчики команд и сообщений
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, upload_file))
    dp.add_handler(CommandHandler("show_files", show_files))
    dp.add_handler(CommandHandler("delete_file", delete_file))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
