from pydoc import text
from time import time
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
from assistant import get_channel_status, check_link_Count
from helper.data import *
from helper.auto import check_approval
import time
from apscheduler.schedulers.background import BackgroundScheduler

main_channel = -1001715136040
m_channel =  -1001697877778
web_channel = -1001560868604

app = Client('web', config_file='config.ini')

@app.on_message(filters.command('start'))
def start(__, m: Message):
    user_name = m.from_user.first_name
    user_id = m.from_user.id
    check_id = check_user(user_id)
    print(check_id)
    if check_id == True:
        m.reply_text("**Welcome back Dude! How's Going\n\nWhich channel you want to Access? 😍**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('Mallu & indian Videos', callback_data='mallu')],
                    [InlineKeyboardButton('HD videos (blacked, brazzers, etc..)', callback_data='hd')],
                    [InlineKeyboardButton('Lesbian Videos Only', callback_data='lesb')],
                    [InlineKeyboardButton('Web Seies Direct Videos', callback_data='web')]
                ]
            ))
        return

    if check_id == False:
        add_user(user_name, user_id)
    m.reply_text(f"""**Hello {m.from_user.first_name} 🙋🏻‍♀️\n\nWeͤlcͨoͦmͫeͤ
    \nSo do you want to use our referral system and gain access to our Adult Videos Channel?**""",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Yes', callback_data='agree'),
            InlineKeyboardButton('No', callback_data='disAgree')]
        ]
    ))
@app.on_callback_query(filters.regex('agree'))
def agree(__, c:CallbackQuery):
    c.edit_message_text('**Alright Bro! \n\nWhich channel you want to Access? 😍**',
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Mallu & indian Videos', callback_data='mallu')],
            [InlineKeyboardButton('HD videos (blacked, brazzers, etc..)', callback_data='hd')],
            [InlineKeyboardButton('Lesbian Videos Only', callback_data='lesb')],
            [InlineKeyboardButton('Web Seies Direct Videos', callback_data='web')]
        ]
    ))

@app.on_callback_query(filters.regex('disAgree'))
def disagree(__, c:CallbackQuery):
    c.edit_message_text('Alright Bro! Come back again when you changed your mind.😠')

@app.on_callback_query(filters.regex('mallu'))
def mallu_channel(__, c:CallbackQuery):
    video_files = get_file_count('mallu')
    c.edit_message_text(f"""**Good Choice! We have almost `{video_files}` Indian Videos in our Channel.

How you can gain access?  🤔

1. Click the Generate Link button
2. Copy the generated link and share it with your friends or other adult groups.
3. Click the Check Status button to track your link.
4. If 15 members have joined our main channel through your link. We will send you our video channel invitation link immideatly.

 
Thank you ❤️**""", 
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Generate Link', callback_data='gen_link_m')]
        ]
    ))

@app.on_callback_query(filters.regex('gen_link_m'))
def mallu_link(__, c:CallbackQuery):
    user_id = c.message.chat.id
    check_link = check_user_link('mallu', user_id)
    if check_link == False:
        link = app.create_chat_invite_link(main_channel)
        add_user_link('mallu', user_id, link.invite_link)
        l1 = c.message.reply_text(f'**Hi I found a best adult channel. Here we see all the adult web series. Join fast and watch The most beautiful and hot series out there. 😍😍😍**\n\n {link.invite_link}')
        c.message.reply_text(f'Here you go. share this link with your friends or other adult groups. 🔥🔥', reply_to_message_id=l1.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('Check Status', callback_data='check_link_status_m')]
            ]
        ))
    else:
        c.edit_message_text(f'**Yeah! You already Generated a Link for Mallu and Indian videos.\n\nHere : {check_link}\n\nShare with your friends. and check Status.😍**',
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('Check Status', callback_data='check_link_status_m')]
            ]
        ))

@app.on_callback_query(filters.regex('check_link_status_m'))
def link_count(__, c:CallbackQuery):
    user_id = c.message.chat.id
    name = c.message.chat.first_name
    link = get_link('mallu', user_id)
    cnt = check_link_Count(link)
    c_v =check_vip('mallu', user_id)
    if c_v == True:
        c.answer('You already have an access.')
    c.answer(f'Hello! {name} \n\n {cnt} members joined through your link. 🙂', show_alert=True)


def auto_check():
    result = check_approval()
    if result == None:
        return
    cat =  result[1]
    user_id = result[2]
    if cat == 'mallu':
        c_v = check_vip(cat, user_id)
        if c_v == True:
            return
        else:
            l = app.create_chat_invite_link(m_channel, member_limit=1)
            add_vip(user_id,cat, l.invite_link)
            app.send_message(user_id, f"""Hello! Good news 🎊

15 member joined using your link. Thank you for your efforts
Here is your reward. Indian Videos Channel! 🤗😍

Link: {l.invite_link}

Please note ⚠️. Only one person can join if you share it with others who have lost your access.""") 
    if cat == 'web':
        c_v = check_vip(cat, user_id)
        if c_v == True:
            return
        else:
            l = app.create_chat_invite_link(web_channel, member_limit=1)
            add_vip(user_id,cat, l.invite_link)
            app.send_message(user_id, f"""Hello! Good news 🎊

15 member's joined using your link. Thank you for your efforts
Here is your reward. Indian Hot Web Series Channel! 🤗😍

Link: {l.invite_link}

Please note ⚠️. Only one person can join if you share it with others who have lost your access."""
) 
    
    return

update_files()

scheduler = BackgroundScheduler()


scheduler.add_job(auto_check, 'interval' , seconds=30)


scheduler.start()

scheduler = BackgroundScheduler()


scheduler.add_job(update_files, 'interval' , seconds=60)


scheduler.start()



app.run()