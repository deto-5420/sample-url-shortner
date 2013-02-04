from google.appengine.ext import db
from google.appengine.api import users

class ShortLink(db.Model):
  OriginalURL = db.StringProperty(default="")
  ShortCode = db.StringProperty(default="")
  
class Counter(db.Model):
  ShortCounter = db.IntegerProperty(default=60466176, required=True)