import telebot
import time
bot = telebot.TeleBot('7554967329:AAEAY2pgTlmEF0d9NbQYKzRyR7u6Du3lwJs')

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    # bot.send_message(message.chat.id, 'welcome to my bot.')
    bot.reply_to(message,'this is a second message.')

@bot.message_handler(content_types=['document', 'audio', 'voice', 'sticker'])
def handle_docs_audio(message):
    if message.audio:
        bot.reply_to(message, 'this is a audio file')
    elif message.document:
        bot.reply_to(message, 'this is a document')
    elif message.voice:
        bot.reply_to(message, 'this is a voice message')
    elif message.sticker:
        bot.reply_to(message, 'this is a sticker message')

@bot.message_handler(regexp="2024")
def handle_2024(message):
    bot.reply_to(message, 'this is a 2024 message')


@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_tst_doc (message):
    bot.reply_to(message, 'this is a txt message')

def txt_message (message):
    return message.document.mime_type == 'text/plain'
@bot.message_handler(func=txt_message, content_types=['document'])
def handle_txt_message (message):
    bot.reply_to(message, 'this is a txt message...')

@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text == 'helloooo')
def send_hello(message):
    bot.reply_to(message, 'wooooowwwww')

while True:
    try:
        bot.polling(non_stop=True, timeout=5)  # زمان انتظار را تنظیم کنید
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)