from email.errors import MessageDefect
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import os
import time, asyncio

from telegram import Bot

b_channel = -1001705364943
app = Client('AD',
api_id=2236912,
api_hash='2a8db2b1122af3f39aaa6bd8b3f4c935',
bot_token='5195630815:AAEK_blBb1GJPZi1HZOpCRPAXi6bwHM69zc')

print('bot_started')

def check_sub(chat_id, user_id):
    try:
        app.get_chat_member(chat_id, user_id)
        return True
    except Exception:
        return False

def delete_all(chat_id , list):
    app.delete_messages(chat_id, list)

@app.on_message(filters.me & filters.text)
def get_msg(__, m:Message):
    m_list = m.text.split()
    if 'subscribed' in m_list:
        m.delete()
    if '@Manybot' in m_list:
        m.delete()
        m.reply_text('Hello Dude Welcome.... ❤️',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['Web Series']
            ], resize_keyboard=True
        ))


@app.on_message(filters.text)
def start(__, m:Message):
    if m.text.startswith('W') or m.text.startswith('/web'):
        cs = check_sub(b_channel, m.from_user.id)
        print(cs)
        if cs == False:
            time.sleep(4)
            list = [*range(m.message_id, m.message_id+12)]
            print(list)
            for x in list:
                app.delete_messages(chat_id=m.chat.id, message_ids=x)
            m.reply_photo('https://telegra.ph/file/8d0301a99851b72562148.jpg',
            caption=f'**Wait a minute. you should join our backup channel to use me!.🤫 \n\nബോട്ട് തുടന്ന് ഉപയോഗിക്കുന്നതിനു ബാക്കപ്പ് ചാനലിൽ ജോയിൻ ചെയണ്ടതുണ്ട് 😤**',
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('Join Now', url='https://t.me/+-IFbhk8D2Fk0OWVl')]
                ]
            ))


# @app.on_message(filters.text)
# def check_text(__, m:Message):
#     # get_msg(__, m)
#     delete_all(m)
app.run()