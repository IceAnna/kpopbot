import telebot
import re

subject='select'

API_TOKEN = '6048445093:AAGZIK0JIPJHzdlELYBQw2MzjJUBW5OA2ms'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    global subject
    subject='select'
    bot.reply_to(message, """
    1-матеша
    2-русский
    3-инглиш
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global subject
    text= message.text
    if subject=='select':
        if text=='1':
            reply='напиши пример,я решу "1024-(356*6/3+1)"'
            subject = 'math'
        elif text=='2':
            reply='nu sory v ananas idite'
            subject = 'rus'
        elif text=='3':
            reply='напиши текст на русском,я перведу'
            subject = 'eng'
    elif subject=='math':
        pattern ='^[0-9+-/\*\(\) ]*$'
        if re.match(pattern, text):
            reply = eval(text)
        else:
            reply = 'ERROR 404'
   # reply='vse govoryat '+ message.text+' kupi slon a to arabam sdam'
    bot.reply_to(message,reply )

bot.infinity_polling()