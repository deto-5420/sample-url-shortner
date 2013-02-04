import models
import base36
from django.utils import simplejson as json

## URL Shortner Class
class URLShort():
  def __init__(self):
    self.shortCode = None
    self.originalURL = None
    self.returnData = {
      'success': False
    }
  
  def shorten(self, data):
    try:
      if self.processHasOriginalURL(data) and self.processHasCustomShortCode(data):
        self.returnData['success'] = True
        self.returnData['short_code'] = self.shortCode
        return self.returnData
      elif self.processHasOriginalURL(data) and not self.processHasCustomShortCode(data):
        self.generateCustomShortCode()
        self.returnData['success'] = True
        self.returnData['short_code'] = self.shortCode
        return self.returnData
    except Exception, error:
      self.returnData['exception'] = error
      return self.returnData
    return self.returnData
  
  def getOriginalURL(self):
    return self.originalURL
  
  def getShortCode(self):
    return self.shortCode
      
  def processHasOriginalURL(self, longURLData):
    if type(longURLData) is dict and longURLData.has_key('long_url') and len(longURLData['long_url']) > 0:
      # make the URL short
      self.originalURL = str(longURLData['long_url'])
      return True
    return False
      
  def processHasCustomShortCode(self, customShortCodeData):
    if type(customShortCodeData) is dict and customShortCodeData.has_key('custom_short_code') and len(customShortCodeData['custom_short_code']) > 0:
      self.shortCode = str(customShortCodeData['custom_short_code'])
      return True
    return False
  
  def generateCustomShortCode(self):
    counterModel = models.Counter.get_or_insert('SHORT')
    longNumCounter = long(counterModel.ShortCounter)
    counterModel.ShortCounter+=1
    counterModel.put()
    self.shortCode = base36.Base36().base36encode(longNumCounter)
