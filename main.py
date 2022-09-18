import telebot
import datetime



bot = telebot.TeleBot('5586996454:AAEcrUpY12cWspCpjJ51E0kFShePIdgmB8A')

def week_detect():
    week = datetime.date(2022, 9, 18).isocalendar()[1]

    return week

def time_detection():
    time_now = datetime.time

    return time_now

@bot.message_handler(commands=['start', 'help'])
def start(message):
    user_name = message.from_user.username
    bot.send_message(message.chat.id, 'Приветствую '+user_name+', студент лгту, тут ты можешь узнать:\n1⃣ Какая следующая пара \n2⃣  Какие сегодня пары \n3⃣  Какая сейчас неделя(зеленая или белая')

@bot.message_handler()
def get_user_text(message):
    msgtxt = message.text
    if msgtxt.lower() == "неделя":
        week_number = week_detect()
        if week_number % 2 == 0:
            bot.send_message(message.chat.id, 'Зелёная')
        else:
            bot.send_message(message.chat.id, 'Белая')

bot.polling(none_stop=True)