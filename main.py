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
import os
import models
import webapp2
from django.utils import simplejson as json
from google.appengine.ext.webapp import template

import urlshort
import base36

class MainHandler(webapp2.RequestHandler):
  def get(self):
    values = {
      'title': 'jjbshort'
    }
    path = os.path.join(os.path.dirname(__file__), 'web/index.html')
    self.response.out.write(template.render(path, values, False))

class ShortenURLHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('Shorten URL')
  def post(self):
    returnData = {
      'success': False
    }
    try:
      data = None
      if self.request.get("long_url") != None:
        data = dict()
        data['long_url'] = self.request.get("long_url")
        data['custom_short_code'] = self.request.get("custom_short_code")
      else:
        data = json.loads(self.request.body)
      
      urlShort = urlshort.URLShort()
      returnData = urlShort.shorten(data) 
      
      models.ShortLink(
        OriginalURL=urlShort.getOriginalURL(),
        ShortCode=urlShort.getShortCode()
      ).put()
      self.response.write(json.dumps(returnData))
      return
    except Exception, error:
      returnData['exception'] = error
      self.response.write(json.dumps(returnData))
      return
    self.response.write(json.dumps(returnData))
    return
            
class CustomShortCodeHandler(webapp2.RequestHandler):
  def get(self, shortCode):
    try:
      shortLink = models.ShortLink.all().filter('ShortCode = ', shortCode).get()
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
  ('/(.*)', CustomShortCodeHandler)
], debug=True)
