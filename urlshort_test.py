import unittest
from django.utils import simplejson as json
import urlshort

class TestURLShort(unittest.TestCase):
  def setUp(self):
    self.localhostShortenURL = "http://localhost:8080/shorten_url"
    self.urlS = urlshort.URLShort() 
  def testBadJSON(self):
    returnValue = self.urlS.shorten(self.localhostShortenURL, "notjson")
    self.assertEquals({'success': False},returnValue)
    
  def testProcessLongURLNotDict(self):
    longURLData = json.loads('["long_url","http://this-is-an-array-not-a-dict.com/"]')
    returnValue = self.urlS.processLongURL(longURLData)
    self.assertFalse(returnValue)

  def testProcessingLongURLIncorrectKey(self):
    longURLData = json.loads('{"wrong_key_long_url":"http://nooooooooooooooo.com/"}')
    returnValue = self.urlS.processLongURL(longURLData)
    self.assertFalse(returnValue)
  
  def testProcessingLongURLEmptyString(self):
    longURLData = json.loads('{"long_url":""}')
    returnValue = self.urlS.processLongURL(longURLData)
    self.assertFalse(returnValue) 
  
  # Need test case to validate correct URL format via Regex  
  
  def testProcessingLongURL(self):
    longURLData = json.loads('{"long_url":"http://nooooooooooooooo.com/"}')
    returnValue = self.urlS.processLongURL(longURLData)
    self.assertTrue(returnValue)
    
    
  def testProcessCustomShortCodeNotDict(self):
    customShortCodeData = json.loads('["custom_short_code","this-is-an-array-not-a-dict.com"]')
    returnValue = self.urlS.processLongURL(customShortCodeData)
    self.assertFalse(returnValue)

  def testProcessingCustomShortCodeIncorrectKey(self):
    customShortCodeData = json.loads('{"wrong_key_custom_short_code":"nooooo"}')
    returnValue = self.urlS.processLongURL(customShortCodeData)
    self.assertFalse(returnValue)

  def testProcessingCustomShortCodeEmptyString(self):
    customShortCodeData = json.loads('{"custom_short_code":""}')
    returnValue = self.urlS.processLongURL(customShortCodeData)
    self.assertFalse(returnValue) 

  # Need test case to validate correct lenght and format via Regex  
  
  def testProcessingCustomShortCode(self):
    customShortCodeData = json.loads('{"custom_short_code":"nooooo"}')
    returnValue = self.urlS.processLongURL(customShortCodeData)
    self.assertTrue(returnValue)
    
  