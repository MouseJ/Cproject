from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import subprocess

# Глобальная переменная для хранения состояния утилиты (запущена ли утилита)
utility_running = False

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для управления консолью.')

# Функция для обработки текстовых сообщений и выполнения команд
def execute_command(update: Update, context: CallbackContext) -> None:
    global utility_running

    # Получаем текст сообщения от пользователя
    command = update.message.text

    # Если утилита запущена, то попытаемся обработать команду выхода из утилиты
    if utility_running:
        if command.lower() == 'выйти из утилиты':
            # Завершаем утилиту
            utility_running = False
            update.message.reply_text('Вы успешно вышли из утилиты.')
            return

    # Если утилита не запущена, то выполняем обычные команды
    if not utility_running:
        # Выполняем команду в терминале
        result = subprocess.run(command.split(), capture_output=True, text=True)
        # Отправляем результат выполнения команды пользователю
        update.message.reply_text(result.stdout)

        # Если команда запускает утилиту, устанавливаем флаг utility_running в True
        if 'утилита' in command.lower():  # Здесь нужно заменить "утилита" на ключевые слова, по которым можно определить, что запущена утилита
            utility_running = True

# Функция для отображения кнопок
def show_buttons(update: Update, context: CallbackContext) -> None:
    reply_markup = ReplyKeyboardMarkup(
        [[KeyboardButton('Выйти из утилиты')]],
        resize_keyboard=True
    )
    update.message.reply_text('Нажмите на кнопку, чтобы выйти из утилиты.', reply_markup=reply_markup)

def main() -> None:
    # Инициализация бота
    updater = Updater("7000016669:AAG3ylodmwXDUwuETZioHGbR75vhuo_pLAU")  # Замените "YOUR_TOKEN" на ваш токен API

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрация обработчика текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, execute_command))

    # Регистрация обработчика кнопок
    dispatcher.add_handler(CommandHandler("show_buttons", show_buttons))

    # Запуск бота
    updater.start_polling()

    # Бот будет работать до тех пор, пока не нажата комбинация Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
