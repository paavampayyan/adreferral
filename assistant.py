from pyrogram import Client, filters

string = 'BQCG0mE2JEQfI4115jalb_EMuWpDP88C9Evj788NPlch4UazdZMG3RU9wS0sb4UMBZ0y2QTZZO0WaUhGuf95t5AiNPT5O3rigzhj5LJzlZJACV-oMsZuRFjoJZY0vOpSNL2PPHjeuo91nXIlI382inoUpEEtucmjqlBKCSgk6gzpWXW61pSxSZ45nUJbTgO0PSCtGOVYMk1Ao1YdO7LKVuFRKpwwSyuY22lX0mfzMEf2g38Dm4q8m86ZG346KT5cBoV13D-jA1wp8Dd5gRI77oOfxBd_fEXJqfsCyObpHW2Xug64Bfp12rEwFcINHuniLbGGwo1Wxt5yJHk4vk5cXqzpViedZgA'
mallu_channel = -1001697877778
main_channel = -1001715136040
web_channel = -1001560868604
m_channel =  -1001697877778

bubu = Client(string, api_id=1280226, api_hash='40c6be639fd3e699783cbb43c511cef0')

def get_channel_status(chat_id):
    files = 0
    for x in bubu.search_messages(chat_id, filter='video'):
        files= files+1
    return files

def check_link_Count(link):
    count = bubu.get_chat_invite_link_members_count(main_channel, link)

    return count

def check_auto_link_count(cat, user_id, link):
    if cat =='web':
        count = bubu.get_chat_invite_link_members_count(main_channel, link)
        return count, cat, user_id
    if cat == 'mallu':
        count = bubu.get_chat_invite_link_members_count(main_channel, link)
        return count, cat, user_id


bubu.start()