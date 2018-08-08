# mongodb://<dbuser>:<dbpassword>@ds153851.mlab.com:53851/c4t_movie
import mongoengine


host = "ds153851.mlab.com"
port = 53851
db_name = "c4t_movie"
user_name = "admin"
password = "admin123456"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())