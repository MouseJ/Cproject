from subprocess import check_output
import telebot
import time

bot = telebot.TeleBot("6548205940:AAE-haeJBg4b91HDOB6NYUA1LSXl4CV0YKQ")#токен бота
user_id = 5082727140 #id вашего аккаунта
@bot.message_handler(content_types=["text"])
def main(message):
   if (user_id == message.chat.id): #проверяем, что пишет именно владелец
      comand = message.text  #текст сообщения
      try: #если команда невыполняемая - check_output выдаст exception
         bot.send_message(message.chat.id, check_output(comand, shell = True))
      except:
         bot.send_message(message.chat.id, "Invalid input") #если команда некорректна
if __name__ == '__main__':
    while True:
        try:#добавляем try для бесперебойной работы
            bot.polling(none_stop=True)#запуск бота
        except:
            time.sleep(10)#в случае падения
