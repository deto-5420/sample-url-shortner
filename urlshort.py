import urlparse
import models
from django.utils import simplejson as json

## URL Shortner Class
class URLShort():
  def __init__():
    
    baseURI = None
    data = None
    returnData = {
      'success': False
    }
  
  def shorten(self, currentURI, requestBody):
    baseURI = self.getBaseURI(currentURI)
    try:
      data = json.loads(requestBody)
    except:
      return self.returnData
    return self.returnData

  def getShortnedURL():
    return "short"
  
  def getOriginalURL():
    return "original"
      
  def processLongURL(self, longURLData):
    if type(longURLData) is dict and longURLData.has_key('long_url') and len(longURLData['long_url']) > 0:
      # make the URL short
      originalURL = str(longURLData['long_url'])
      shortCode = hex(counterModel.ShortCounter)
      return True
    return False
      
  def processCustomShortCode(self, customShortCodeData):
    if type(customShortCodeData) is dict and customShortCodeData.has_key('custom_short_code') and len(customShortCodeData['custom_short_code']) > 0:
      shortCode = str(customShortCodeData['custom_short_code'])
      notCustomCode = False
      return True
    return False
      
  def getBaseURI(self, requestURL):
    return urlparse.urlparse(requestURL)
