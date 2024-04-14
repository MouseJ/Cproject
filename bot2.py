from subprocess import check_output, CalledProcessError
import telebot
import time

bot = telebot.TeleBot("6548205940:AAE-haeJBg4b91HDOB6NYUA1LSXl4CV0YKQ")#токен бота
user_id = 5082727140 #id вашего аккаунта

def explain_error(returncode):
    error_map = {
        1: "Ошибка: Недостаточно прав",
        2: "Ошибка: Не удается найти указанный файл или каталог",
        126: "Ошибка: Необходимый файл является исполняемым, но не может быть выполнен",
        127: "Ошибка: Команда не найдена",
        128: "Ошибка: Неверный код выхода",
        130: "Ошибка: Процесс был прерван сигналом",
        255: "Ошибка: Выход за пределы допустимого диапазона кодов возврата"
        # Добавьте другие коды ошибок и их пояснения по необходимости
    }
    return error_map.get(returncode, "Неизвестная ошибка")

@bot.message_handler(content_types=["text"])
def main(message):
    if (user_id == message.chat.id): #проверяем, что пишет именно владелец
        command = message.text  #текст сообщения
        try:
            output = check_output(command, shell=True)
            bot.send_message(message.chat.id, output.decode('utf-8')) # отправляем результат выполнения команды
        except CalledProcessError as e:
            explanation = explain_error(e.returncode)
            bot.send_message(message.chat.id, explanation) # отправляем пояснение к ошибке
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка: {e}") # отправляем другие ошибки

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True) # запуск бота
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(10) # в случае падения
