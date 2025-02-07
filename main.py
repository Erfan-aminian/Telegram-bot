from random import sample
from db_config import Config
import telebot
import time
import sqlite3
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#Config.GetUsers()
# BOT API
bot = telebot.TeleBot('7554967329:AAEAY2pgTlmEF0d9NbQYKzRyR7u6Du3lwJs')
@bot.message_handler(regexp='الهه')
def echo(message):
    bot.send_message(message.chat.id, "عرفان عاشق الهه است و حاضره جونشو بده بخاطرش :))")

@bot.message_handler(regexp='ازدواج')
def echo2(message):
    bot.send_message(message.chat.id, "معلومه صد در صد!!!")

@bot.message_handler(regexp='عرفان')
def echo3(message):
    bot.send_message(message.chat.id, "عرفان شوهر آینده الهه قراره بشه. هنوز الهه عاشقش نشده ولی خیلی خیلی دوستش داره :))" )



# gorupe setting
@bot.message_handler(content_types=['new_chat_members'])
def new_chat_members(message):
    for user in message.new_chat_members:
        if not user.is_bot:  # اگر کاربر ربات نبود
            if user.username:  # اگر یوزرنیم دارد
                welcome_msg = f"سلام {user.first_name} (@{user.username}) خوش اومدی! 🌟"
            else:  # اگر یوزرنیم ندارد
                welcome_msg = f"سلام {user.first_name} خوش اومدی! 🎉"
            bot.send_message(message.chat.id, welcome_msg)
        elif user.id == bot.get_me().id:  # اگر خود بات به گروه اضافه شد
            bot.send_message(message.chat.id, "ممنون که من رو به گروه اضافه کردید! 🤖")
# is user admin
def is_user_admin(chat_id, user_id):
    admins = bot.get_chat_administrators(chat_id)
    for admin in admins:
        if admin.user.id == user_id:
            return True
    return False
@bot.message_handler(func=lambda message: message.text == "پین")
def pin_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if is_user_admin(chat_id, user_id):
        if message.reply_to_message:
            bot.pin_chat_message(chat_id, message.reply_to_message.message_id)
            bot.reply_to(message.reply_to_message,"پیام مدنظرت رو با موفقیت پین کردم")
        else:
            bot.reply_to(message, "کدوم پیام رو میخوای پین کنی؟ \n برام ریپلای کن")
    else:
        bot.send_message(message.chat.id, "فقط ادمین میتونه پیامی رو پین کنه :(")





# create first menu button

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
button = KeyboardButton(text='send my info', request_contact=True)
reply_keyboard.add("ارز","راهنما",button,"تماس با ما")

#message handler for /start
user_ID = []
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='خوش اومدی عزیزم', reply_markup=reply_keyboard)
    if message.chat.id not in user_ID:
        user_ID.append(message.chat.id)

# message handler for contact
@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        contact_info = (
            f"شماره تماس: {message.contact.phone_number}\n"
            f"نام: {message.contact.first_name}\n"
            f"نام خانوادگی: {message.contact.last_name if message.contact.last_name else 'وجود ندارد'}\n"
            f"شناسه کاربر: {message.contact.user_id if message.contact.user_id else 'وجود ندارد'}"
        )
        bot.send_message(message.chat.id, text=contact_info)
        data = (
            message.contact.user_id,
            message.contact.first_name,
            message.contact.last_name,
            message.contact.phone_number,
        )
        Config().AddUser(data)
    else:
        bot.send_message(message.chat.id, text="اطلاعات تماس دریافت نشد.")


# Button dollar and gold
reply_keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_keyboard2.add("دلار","طلا")


# message button dollar and gold
button1 = InlineKeyboardButton(text='Dollar', callback_data= 'button_dollar')
button2 = InlineKeyboardButton(text='Gold', callback_data= 'button_gold')
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(button1, button2)


@bot.message_handler(func=lambda message: True)
def check_button(message):
    if message.text == 'ارز':
        bot.reply_to(message,"قیمت کدوم رو می خوای از پایین انتخاب کن", reply_markup=reply_keyboard2)
    elif message.text == 'راهنما':
        bot.reply_to(message,"ما تو این ربات قیمت دلار، طلا و .. رو نمایش میدیم تو به کدومش نیاز داری ؟")
    elif message.text == 'تماس با ما':
        bot.reply_to(message,"برنامه نویس این ربات عرفان هست ")
    else:
        bot.send_message(message.chat.id, 'الهه گفت من باشعورممممممم')
        #bot.send_message(message.chat.id, '/start')
        Config.GetUsers()



@bot.callback_query_handler(func=lambda call: call.data == "/help")
def handle_help_callback(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "این بخش راهنماست...")

@bot.message_handler(commands=['help'])
def welcome(message):
    # bot.send_message(message.chat.id, 'welcome to my bot.')
    bot.reply_to(message,'Hello to my bot.\n What is your name?',reply_markup=inline_keyboard)


#   bot.register_next_step_handler(message, process_name)
# def process_name(message):
#     name = message.text
#     bot.send_message(message.chat.id, f'Hello {name}.\nHow old are you?')
#
#     bot.register_next_step_handler(message, process_age)
# def process_age(message):
#     age = message.text
#     bot.send_message(message.chat.id, f'your are {age} years old.\n Thank You')
#     print(user_ID)


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






# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
# def handle_tst_doc (message):
#     bot.reply_to(message, 'this is a txt message')
#
# def txt_message (message):
#     return message.document.mime_type == 'text/plain'


# @bot.message_handler(func=txt_message, content_types=['document'])
# def handle_txt_message (message):
#     bot.reply_to(message, 'this is a txt message...')

# @bot.message_handler(commands=['hello'])
# @bot.message_handler(func=lambda msg: msg.text == 'helloooo')
# def send_hello(message):
#     bot.reply_to(message, 'wooooowwwww')


# start bot
while True:
    try:
        bot.polling(non_stop=True, timeout=5)  # زمان انتظار را تنظیم کنید
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)