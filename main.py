#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urlparse
import simplejson as json
import models

class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('JJB Short!')

class ShortenURLHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('Shorten URL')
  def post(self):
    # Parse Inputs {long_url:..., custom_short_code(optional): ...} 
    data = None
    returnData = {
      'success': False
    }
    try: 
      data = json.loads(self.request.body)
      counterModel = models.Counter.get_or_insert('SHORT')
      shortCode = None
      notCustomCode = True
      originalURL = None
      
      # Handle long URL
      if type(data) is dict and data.has_key('long_url') and len(data['long_url']) > 0:
        # make the URL short
        originalURL = str(data['long_url'])
        shortCode = hex(counterModel.ShortCounter)
      
      # Handle custom code  
      if type(data) is dict and data.has_key('custom_short_code') and len(data['custom_short_code']) > 0:
        shortCode = str(data['custom_short_code'])
        notCustomCode = False
      
      # Parse base URI
      baseURI = urlparse.urlparse(self.request.url)
      shortURL = baseURI.scheme + "://" + baseURI.netloc + "/" + str(shortCode)
      # If uri exists, return false
      
      shortLink = models.ShortLink.all().filter('ShortURL = ', shortURL).get()
      if shortLink != None:
        returnData.success = false
        self.response.write(returnData)
        return
        
      returnData = {
        'success': True,
        'short_code': shortURL
      }
      # Save URL Model
      models.ShortLink(
        OriginalURL=originalURL,
        ShortURL=shortURL
      ).put()
      # Increment Counter
      if notCustomCode:
        counterModel.ShortCounter+=1
        counterModel.put()
        
      # Generate Response  {success: true/false, short_code}
      self.response.write(returnData)
      return
    except Exception, error:

      self.response.write(returnData)
      return

    self.response.write(returnData)
    return
    
class CustomShortCodeHandler(webapp2.RequestHandler):
  def get(self):
    try:
      shortLink = models.ShortLink.all().filter('ShortURL = ', self.request.uri).get()
      if shortLink == None:
        self.response.write('Short URL not found')
      self.redirect(str(shortLink.OriginalURL), permanent=True)
      return
    except Exception, error:
      self.response.write(error)
      return


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/shorten_url', ShortenURLHandler),
  ('/.*', CustomShortCodeHandler)
], debug=True)
