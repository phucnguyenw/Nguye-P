from mongoengine import *

#name collection
class MovieABC(Document):
    title = StringField()
    link= StringField()