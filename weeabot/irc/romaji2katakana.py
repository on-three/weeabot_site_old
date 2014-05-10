# vim: set ts=2 expandtab:
"""

Module: romaji2katakana.py
Desc: use local lib or www.sljfaq.org to turn romaji into katakana
Author: on_three
Email: on.three.email@gmail.com
DATE: Tuesday, Jan 14th 2013

  The web service has the best transliteration i've seen so far,
  but i'm defaulting to local implementation in hopes i can 
  improve it.
  
"""
from bs4 import BeautifulSoup
import string
import re
from jpn.transliterate import romaji2katakana as transliterate
from twisted.python import log
from twisted.web.client import getPage

class GetKatakana(object):
  '''
  Encapsulates network or local tranform from romaji to katakana
  '''
  class HTMLResponse(object):
    '''
    Functor that wraps a HTML response
    '''
    def __init__(self, callback_handler, romaji, channel):
      self._callback_handler = callback_handler
      self._romaji = romaji
      self._channel = channel
    def __call__(self, response):
      #extract katakana from response and invoke callback with stored info
      soup = BeautifulSoup(response)
      katakana = soup.find('td', {'class': 'katakana-string'}).text.strip()
      self._callback_handler(self._romaji, self._channel, katakana)

  class HTMLError(object):
    '''
    functor that wraps an HTML error
    '''
    def __init__(self, callback_handler):
      self._callback_handler = callback_handler
    def __call__(self, response):
      self._callback_handler(response)

  def __init__(self, callback, error_callback):
    '''
    Provide asynchronous callbacks for results to be retured
    '''
    self.callback = callback
    self.error_callback = error_callback

  def lookup(self, romaji, channel, use_webservice=False):
    '''
    Initiate an asynchronous transform of romaji to katakana
    This can be done by a local handler (default use_webservice=False)
    Or a network service www.
    '''
    if not use_webservice:
      katakana = transliterate(romaji)
      self.callback(romaji, channel, katakana)
    else:
      #initiate a network lookup of romaji to katakana
      result = getPage('http://www.sljfaq.org/cgi/e2k.cgi?word={romaji}'.format(romaji=romaji))
      result.addCallbacks(
        callback = GetKatakana.HTMLResponse(self.callback, romaji, channel),
        errback = GetKatakana.HTMLError(self.error_callback))



