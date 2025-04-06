#Main test file
import unittest

import python_Testing_Utilities as undertest


class mock_TestCase():
  args = None
  kvargs = None
  def assertTrue(self, *args, **kvargs):
    self.args = args
    self.kvargs = kvargs
    return

class test_callService(unittest.TestCase): 
  def test_getWorks(self):
    headers = {}
    resultText, resultCode = undertest.callGetService(self, "http://www.google.com", headers, 5, [200])
    
    self.assertEqual(resultCode,200)
    expectedStart = "<!doctype html>"
    if not resultText.startswith(expectedStart):
      print(resultText)
      self.assertTrue(False)
    
  def test_getUnexpectedCode(self):
    mock = mock_TestCase()
    headers = {}
    resultText, resultCode = undertest.callGetService(mock, "http://www.google.com", headers, 5, [201])
    
    self.assertEqual(resultCode,None)
    self.assertEqual(mock.args, (False, ))
    self.assertEqual(mock.kvargs, {'msg': 'Did not get expected response'})

  def test_DeleteWorks(self):
    headers = {}
    resultText, resultCode = undertest.callDeleteService(self, "http://www.google.com", headers, 5, [405])

  def test_PostWorks(self):
    headers = {}
    data = {"TestTag": "TestValue"}
    resultText, resultCode = undertest.callPostService(self, "http://www.google.com", headers, data, 5, [405])
    
