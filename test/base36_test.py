import unittest
import base36
import sys

class TestBase36(unittest.TestCase):
  def setUp(self):
    self.b36 = base36.Base36()
    
  def testEncodeNonNumber(self):
    self.assertRaises(TypeError, self.b36.base36encode, "!ABC")
  
  def testEncodeNegativeNumber(self):
    self.assertRaises(ValueError, self.b36.base36encode, -10)
  
  def testEncodeInt(self): 
    encodedResult = self.b36.base36encode(8372683)
    self.assertEquals("4ZGEJ", encodedResult)
  
  def testDecodeBase36(self):
    decodeResult = self.b36.base36decode('4ZGEJ')
    self.assertEquals(8372683, decodeResult)