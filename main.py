from random import sample

import telebot
import time
import sqlite3
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup
#database config
connection = sqlite3.connect('users.db')
curser = connection.cursor()
create_table_query ="""
    CREATE TABLE IF NOT EXISTS users(
        id integer PRIMARY KEY,
        first_name text,
        last_name text,
        phone_number text
    );
"""
curser.execute(create_table_query)
connection.commit()
connection.close()
sample_data_query ="""
    INSERT INTO users (id, first_name, last_name, phone_number)
    VALUES (?, ?, ?, ?)
"""
sample_data = [
    (12344, 'ehsan', 'ghadiri', '0911122339'),
    (14343, "Erfan", "Saberi", "123456789"),
    (24344, "Ali", "Rezaei", "987654321"),
]
with sqlite3.connect('users.db') as connection:
    curser = connection.cursor()
    curser.executemany(sample_data_query,sample_data)

fetch_data_query = """
    SELECT * FROM users;

"""
rows = []
with sqlite3.connect('users.db') as connection:
    curser = connection.cursor()
    curser.execute(fetch_data_query)
    rows = curser.fetchall()
for row in rows:
    print(f'ID:{row[0]}, fname:{row[1]}, lname:{row[2]}, phone_number:{row[3]}')


bot = telebot.TeleBot('7554967329:AAEAY2pgTlmEF0d9NbQYKzRyR7u6Du3lwJs')
#create menu button
reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_keyboard.add("ارز", "راهنما")



@bot.message_handler(func=lambda message: True)
def check_button(message):
    if message.text == '':
        pass
    elif message.text == '':
        pass
    elif message.text == '':
        pass
    else:
        bot.send_message(message, f'گزینه انتخابی رو پیدا نکردم/')
        bot.send_message(message, '/start')



#defining buttons
button1 = InlineKeyboardButton(text='Dollar', callback_data= 'button_dollar')
button2 = InlineKeyboardButton(text='Gold', callback_data= 'button_gold')
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(button1, button2)


#message handler for /start
user_ID = []
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'خوش اومدی عزیزم', reply_markup=reply_keyboard)
    if message.chat.id not in user_ID:
        user_ID.append(message.chat.id)



@bot.message_handler(commands=['help'])
def welcome(message):
    # bot.send_message(message.chat.id, 'welcome to my bot.')
    bot.reply_to(message,'Hello to my bot.\n What is your name?',reply_markup=inline_keyboard)


    bot.register_next_step_handler(message, process_name)
def process_name(message):
    name = message.text
    bot.send_message(message.chat.id, f'Hello {name}.\nHow old are you?')

    bot.register_next_step_handler(message, process_age)
def process_age(message):
    age = message.text
    bot.send_message(message.chat.id, f'your are {age} years old.\n Thank You')
    print(user_ID)

#call back button
@bot.callback_query_handler(func=lambda call: True)
def check_button(call):
    if call.data == 'button_dollar':
        bot.answer_callback_query(call.id, 'هنوز قیمت ها تعریف نشده', show_alert=True)

    elif call.data == 'button_gold':
        bot.answer_callback_query(call.id, 'قیمت ها هنوز نیومدن :(')




@bot.message_handler(commands=['sudo'])
def sudo(message):
    for id in user_ID:
        bot.send_message(id, 'I LOVE YOU!')



@bot.message_handler(content_types=['document', 'audio', 'voice', 'sticker', 'emoji'])
def handle_docs_audio(message):
    if message.audio:
        bot.reply_to(message, 'this is a audio file')
    elif message.document:
        bot.reply_to(message, 'this is a document')
    elif message.voice:
        bot.reply_to(message, 'this is a voice message')
    elif message.sticker:
        bot.reply_to(message, 'this is a sticker message')
    elif message.emoji:
        bot.reply_to(message, 'this is a emoji')

@bot.message_handler(regexp="ارز")
def handle_2024(message):
    bot.reply_to(message, 'الان نمیتونم بگم')


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