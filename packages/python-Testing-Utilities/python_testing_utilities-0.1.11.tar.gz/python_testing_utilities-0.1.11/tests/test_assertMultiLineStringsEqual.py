import unittest

import python_Testing_Utilities as undertest

str1Name="str1"
str2Name="str2"

class test_assertMultiLineStringsEqual(unittest.TestCase):
  def test_emptyStrings(self):
    self.assertEqual(undertest.areMultiLinesStringsEqual("","",str1Name, str2Name),None)

  def test_passNone(self):
    self.assertEqual(undertest.areMultiLinesStringsEqual(None,None,str1Name, str2Name),None)

  def test_sameStrings(self):
    self.assertEqual(undertest.areMultiLinesStringsEqual("A","A",str1Name, str2Name),None)

  def test_diffSingleLineStrings(self):
    expRes = "Strings both have 1 lines\n"
    expRes += "Mismatched line numbers: [1]\n"
    expRes += "str1-----\n"
    expRes += "*001: A:\n"
    expRes += "\n"
    expRes += "str2-----\n"
    expRes += "*001: B:\n"
    expRes += "\n"
    self.assertEqual(undertest.areMultiLinesStringsEqual("A","B",str1Name, str2Name),expRes)

  def test_String1Longer(self):
    expRes = "Strings both have 1 lines\n"
    expRes += "Mismatched line numbers: [1]\n"
    expRes += "str1-----\n"
    expRes += "*001: Aaaaa:\n"
    expRes += "\n"
    expRes += "str2-----\n"
    expRes += "*001: B:\n"
    expRes += "\n"
    self.assertEqual(undertest.areMultiLinesStringsEqual("Aaaaa","B",str1Name, str2Name),expRes)

  def test_String2Longer(self):
    expRes = "Strings both have 1 lines\n"
    expRes += "Mismatched line numbers: [1]\n"
    expRes += "str1-----\n"
    expRes += "*001: A:\n"
    expRes += "\n"
    expRes += "str2-----\n"
    expRes += "*001: Bbbbbb:\n"
    expRes += "\n"
    self.assertEqual(undertest.areMultiLinesStringsEqual("A","Bbbbbb",str1Name, str2Name),expRes)

  def test_diffMiddleLineOf3(self):
    expRes = "Strings both have 3 lines\n"
    expRes += "Mismatched line numbers: [2]\n"
    expRes += "str1-----\n"
    expRes += " 001: A:\n"
    expRes += "*002: x:\n"
    expRes += " 003: B:\n"
    expRes += "\n"
    expRes += "str2-----\n"
    expRes += " 001: A:\n"
    expRes += "*002: y:\n"
    expRes += " 003: B:\n"
    expRes += "\n"
    self.assertEqual(undertest.areMultiLinesStringsEqual("A\nx\nB","A\ny\nB",str1Name, str2Name),expRes)

  def test_String1MoreLines(self):
    expRes = "str1 lines:4\n"
    expRes += "str2 lines:3\n"
    expRes += "Mismatched line numbers: [3, 4]\n"
    expRes += "str1-----\n"
    expRes += " 001: A:\n"
    expRes += " 002: A:\n"
    expRes += "*003: A:\n"
    expRes += "*004: A:\n"
    expRes += "\n"
    expRes += "str2-----\n"
    expRes += " 001: A:\n"
    expRes += " 002: A:\n"
    expRes += "*003: :\n"
    expRes += "\n"
    self.assertEqual(undertest.areMultiLinesStringsEqual("A\nA\nA\nA","A\nA\n",str1Name, str2Name),expRes)

  def test_String2MoreLines(self):
    expRes = "str1 lines:3\n"
    expRes += "str2 lines:7\n"
    expRes += "Mismatched line numbers: [3, 4, 5, 6, 7]\n"
    expRes += "str1-----\n"
    expRes += " 001: A:\n"
    expRes += " 002: A:\n"
    expRes += "*003: :\n"
    expRes += "\n"
    expRes += "str2-----\n"
    expRes += " 001: A:\n"
    expRes += " 002: A:\n"
    expRes += "*003: A:\n"
    expRes += "*004: A:\n"
    expRes += "*005: A:\n"
    expRes += "*006: A:\n"
    expRes += "*007: :\n"
    expRes += "\n"
    self.assertEqual(undertest.areMultiLinesStringsEqual("A\nA\n","A\nA\nA\nA\nA\nA\n",str1Name, str2Name),expRes)

  def test_String1None(self):
    expRes = "str1 lines:None\n"
    expRes += "str2 lines:7\n"
    expRes += "Mismatched line numbers: [ ALL ]\n"
    expRes += "str1-----\n"
    expRes += " ** NONE **\n"
    expRes += "\n"
    expRes += "str2-----\n"
    expRes += "*001: A:\n"
    expRes += "*002: A:\n"
    expRes += "*003: A:\n"
    expRes += "*004: A:\n"
    expRes += "*005: A:\n"
    expRes += "*006: A:\n"
    expRes += "*007: :\n"
    expRes += "\n"
    self.assertEqual(undertest.areMultiLinesStringsEqual(None,"A\nA\nA\nA\nA\nA\n",str1Name, str2Name),expRes)

  def test_String2None(self):
    expRes = "str1 lines:4\n"
    expRes += "str2 lines:None\n"
    expRes += "Mismatched line numbers: [ ALL ]\n"
    expRes += "str1-----\n"
    expRes += "*001: A:\n"
    expRes += "*002: A:\n"
    expRes += "*003: A:\n"
    expRes += "*004: A:\n"
    expRes += "\n"
    expRes += "str2-----\n"
    expRes += " ** NONE **\n"
    expRes += "\n"
    self.assertEqual(undertest.areMultiLinesStringsEqual("A\nA\nA\nA",None,str1Name, str2Name),expRes)
