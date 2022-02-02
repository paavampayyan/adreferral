
import pymongo


myclient = pymongo.MongoClient('mongodb+srv://kannnappan04:kannan123@cluster0.xxc0o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = myclient['bot_data']
user_details = db['user_details']
links = db['links']
vip = db['vips']


def add_user(user_name, user_id):
    user_details.insert_one({'user_name':user_name, 'user_id': user_id})

def check_user(user_id):
    list = []
    res = user_details.find({'user_id': user_id})
    for x in res:
        list.append(x['user_id'])
    print(list)
    if user_id in list:
        return True
    else:
        return False

def add_user_link(cat, user_id, link):
    links.insert_one({'cat': cat, 'user_id': user_id, 'link': link})

def check_user_link(cat, user_id):
    list = []
    res = links.find({'cat': cat, 'user_id': user_id})
    for x in res:
        list.append(x['user_id'])
    print(list)
    if user_id in list:
        link = links.find_one({'cat': cat, 'user_id':user_id})
        return link['link']
    else:
        return False

def get_link(cat, user_id):
    res = links.find_one({'cat': cat, 'user_id': user_id})
    return res['link']

def check_vip(cat, user_id):
    list = []
    res = vip.find({'user_id': user_id, 'cat':cat})
    for x in res:
        list.append(x['user_id'])
    if user_id in list:
        return True
    else:
        return False

def add_vip(user_id, cat, link):
    vip.insert_one({'user_id': user_id, 'cat': cat, 'link':link})