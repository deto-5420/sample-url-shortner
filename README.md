# README #

### About ###

JJB URL Shortner

http://jjbshort.appspot.com

### How to use ###

* A POST /shorten_url endpoint with json payload {long_url:..., custom_short_code(optional): ...} -> returns {success: true/false, short_code} [Raise an error if the user asks for a custom code but cannot be assigned. If custom is not requested, assign a alphanumeric code of length 6]
* A /{custom_short_code} endpoint which redirects to a long url

### Tradeoffs ###

- Using an in memory database would be beneficial for tracking multiple links that get submitted and mapping them to a single short URL code.  Redis/MemCache offer significantly faster read/write times than disk and could be used to improve performance and user experience.

Redirects 
- GAE's redirect with permanent=True flag command uses a 301 redirect to forward you to the new URI.  the 302 redirect will update your page but not change the address bar which may cause confusion to users.  They may believe that the URL shortner is hosting the content when it's not.

### What's missing ###

* Handle Duplicate Codes

### Testing ###
```
$ sudo easy_install gaetestbed
$ sudo easy_install nose
$ sudo easy_install nosegae
$ sudo easy_install webtest

# There is a bug with GAE test case so you need to remove /usr/local/bin/dev_appserver.pyc before every test case run
$ rm /usr/local/bin/dev_appserver.pyc
$ nosetests --with-gae
```