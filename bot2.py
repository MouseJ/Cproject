from subprocess import check_output, CalledProcessError
import telebot
import time

bot = telebot.TeleBot("6548205940:AAE-haeJBg4b91HDOB6NYUA1LSXl4CV0YKQ")#токен бота
user_id = 5082727140 #id вашего аккаунта

@bot.message_handler(content_types=["text"])
def main(message):
    if (user_id == message.chat.id): #проверяем, что пишет именно владелец
        command = message.text  #текст сообщения
        try:
            output = check_output(command, shell=True, stderr=telebot.apihelper.proxy_urllib3.response_log)
            bot.send_message(message.chat.id, output.decode('utf-8')) # отправляем результат выполнения команды
        except CalledProcessError as e:
            bot.send_message(message.chat.id, f"Error: {e.returncode}") # отправляем код ошибки
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}") # отправляем другие ошибки

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True) # запуск бота
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10) # в случае падения
