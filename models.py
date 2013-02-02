from google.appengine.ext import db
from google.appengine.api import users

class ShortLink(db.Model):
  OriginalURL = db.StringProperty(default="")
  ShortURL = db.StringProperty(default="")
  
class Counter(db.Model):
  ShortCounter = db.IntegerProperty(default=1048576, required=True)