import telebot
import time

# Замените 'YOUR_TOKEN' на токен вашего бота
TOKEN = '6848916148:AAG5q8lZtF5nyOphDbSIOMjg8QaPvYo1qbk'
# Замените 'YOUR_CHAT_ID' на ваш Telegram ID
CHAT_ID = '4178405946'
# Путь к файлу журнала SSH
LOG_FILE = '/var/log/auth.log'

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Функция для отправки сообщения в Telegram
def send_message(message):
    bot.send_message(CHAT_ID, message)

# Функция для мониторинга журнала SSH
def monitor_ssh_log():
    with open(LOG_FILE, 'r') as log:
        log.seek(0, 2)  # Переходим в конец файла
        while True:
            line = log.readline()
            if not line:
                time.sleep(0.1)  # Ждем новых записей
                continue
            if 'sshd' in line and 'Failed password' in line:
                send_message(f'Обнаружена попытка подключения SSH:\n{line}')

# Запуск мониторинга
if __name__ == "__main__":
    try:
        monitor_ssh_log()
    except KeyboardInterrupt:
        print("Прервано пользователем")
