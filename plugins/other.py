from pyrogram.types import Message
from pyrogram import Client as app
from pyrogram import filters
from pyrogram.types import CallbackQuery
from assistant import get_channel_status, check_link_Count
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from helper.data import *


main_channel = -1001715136040
web_channel = -1001560868604

@app.on_callback_query(filters.regex('hd'))
def hd_r(__, c:CallbackQuery):
    c.answer('Not Abalilable Right Now. Wll be added soon!',
    show_alert=True)

@app.on_callback_query(filters.regex('lesb'))
def lesb_r(__, c:CallbackQuery):
    c.answer('Not Abalilable Right Now. Wll be added soon!',
    show_alert=True)




@app.on_callback_query(filters.regex('web'))
def mallu_channel(__, c:CallbackQuery):
    video_files = get_file_count('web')
    c.edit_message_text(f"""**Good Choice! We have almost `{video_files}` files in our Web Series Channel.

How you can gain access?  🤔

1. Click the Generate Link button
2. Copy the generated link and share it with your friends or other adult groups.
3. Click the Check Status button to track your link.
4. If 5 members have joined our main channel through your link. We will send you our video channel invitation link immideatly.

 
Thank you ❤️**""", 
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Generate Link', callback_data='gen_link_w')]
        ]
    ))

@app.on_callback_query(filters.regex('gen_link_w'))
def mallu_link(client, c:CallbackQuery):
    user_id = c.message.chat.id
    check_link = check_user_link('web', user_id)
    if check_link == False:
        link = client.create_chat_invite_link(chat_id=main_channel)
        add_user_link('web', user_id, link.invite_link)
        l1 = c.message.reply_text(f'**Hi I found a best adult channel. Here we see all the adult web series. Join fast and watch The most beautiful and hot series out there. 😍😍😍**\n\n {link.invite_link}')
        c.message.reply_text(f'Here you go. share this link with your friends or other adult groups. 🔥🔥', reply_to_message_id=l1.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('Check Status', callback_data='check_link_status_w')]
            ]
        ))
    else:
        c.edit_message_text(f'**Yeah! You already Generated a Link for Mallu and Indian videos.\n\nHere : {check_link}\n\nShare with your friends. and check Status.😍**',
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('Check Status', callback_data='check_link_status_w')]
            ]
        ))

@app.on_callback_query(filters.regex('check_link_status_w'))
def link_count(__, c:CallbackQuery):
    user_id = c.message.chat.id
    name = c.message.chat.first_name
    link = get_link('web', user_id)
    cnt = check_link_Count(link)
    c_v =check_vip('web', user_id)
    if c_v == True:
        c.answer('You already have an access.')
    c.answer(f'Hello! {name} \n\n {cnt} members joined through your link. 🙂', show_alert=True)