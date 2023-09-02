import telebot

API_TOKEN = '6048445093:AAGZIK0JIPJHzdlELYBQw2MzjJUBW5OA2ms'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
kupi moi slon
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    reply='vse govoryat '+ message.text+' kupi slon a to arabam sdam'
    bot.reply_to(message,reply )


bot.infinity_polling()