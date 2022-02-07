import pymongo
from assistant import check_auto_link_count

myclient = pymongo.MongoClient('mongodb+srv://kannnappan04:kannan123@cluster0.xxc0o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = myclient['bot_data']
links = db['links']


def check_approval():
    res = links.find()
    for x in res:
        cat = x['cat']
        user_id = x['user_id']
        link = x['link']
        cc = check_auto_link_count(cat, user_id, link)
        if cc[0] >= 5:
            print(cc[0])
    return cc

