# README #

### About ###

JJB URL Shortner

http://jjbshort.appspot.com

### How to use ###

* A POST /shorten_url endpoint with json payload {long_url:..., custom_short_code(optional): ...} -> returns {success: true/false, short_code} [Raise an error if the user asks for a custom code but cannot be assigned. If custom is not requested, assign a alphanumeric code of length 6]
* A /{custom_short_code} endpoint which redirects to a long url

### Tradeoffs ###


### What's missing ###

* Refactoring of code to enforce SOLID design principles
* Unit Tests
* Proper 6 character alpha numeric code generator
* More robust validation on URLs
* Better documentation
* Better error handling on generating redirect and post
* Catch all 404 for invalid URIs
* REST API version header

### Testing ###
```
$ sudo easy_install gaetestbed
$ sudo easy_install nose
$ sudo easy_install nosegae
$ sudo easy_install webtest
```