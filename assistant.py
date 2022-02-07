from pyrogram import Client, filters

string = 'BQCxfVS_aOu83JTOGcvh7yHZWjxoUK6nspXKU8xkM-y7q_bUaBg4IQtdBbNfMEELbkAxXm8irtlT65u6R_SwKmJDeFOKqngbZaXSYCUQ0wYQhoygcPhiPIovxVgXQz348snlauBGdsDw98zQmI664vZk99e5Fz2tF7xGxl8irBxPizNngnRSFZmV8ta3Kx3ZqOSULW3IH7vFljfu0eAmYPp1wjCkCwlurbTLI9ErlgPv_ti8AFM7XoZlU7rifjY65ghb8k4olIdEcwYBl95nENGI8XniIZlrUH9fn20o6Zp27zntG0b44ZWdNXCHww1iD5fBHp-V0QVTBek-TX8s-zBIViedZgA'
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
        list = [count, cat, user_id]
        print(list)
        return list
    if cat == 'mallu':
        count = bubu.get_chat_invite_link_members_count(main_channel, link)
        list = [count, cat, user_id]
        print(list)
        return list


bubu.start()