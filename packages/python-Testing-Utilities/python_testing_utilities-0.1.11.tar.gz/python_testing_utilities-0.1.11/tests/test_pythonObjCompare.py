#Main test file
import unittest
import python_Testing_Utilities as undertest

class test_main(unittest.TestCase):
  def af(self,a,b,res,msg):
    if res:
        self.assertTrue(undertest.objectsEqual(a,b),msg=msg)
        self.assertTrue(undertest.objectsEqual(b,a),msg=msg)
    else:
        self.assertFalse(undertest.objectsEqual(a,b),msg=msg)
        self.assertFalse(undertest.objectsEqual(b,a),msg=msg)

  def test_differentTypes(self):
    self.assertFalse(undertest.objectsEqual("A",123),msg="Different types should not be Equal")

  def test_none(self):
    self.assertTrue(undertest.objectsEqual(None,None),msg="Different None types")

  def test_strings(self):
    self.assertTrue(undertest.objectsEqual("A","A"),msg="Strings Equal")
    self.assertFalse(undertest.objectsEqual("A","B"),msg="Strings Equal")

  def test_numbers(self):
    self.assertTrue(undertest.objectsEqual(1,1),msg="Nubers Equal")
    self.assertFalse(undertest.objectsEqual(1,2),msg="Nubers Equal")

  def test_list(self):
    listA = []
    listB = ["a"]
    listC = ["a","b"]
    listD = ["a","b",123]
    listE = ["a","b",123, []]
    listF = ["a","b",123, ["z"]]
    listG = ["a","b",123, ["z","x"]]
    listAA = []
    listBB = ["a"]
    listC2 = ["b", "a"]
    listC3 = ["z", "a"]


    self.af(listA,listA,True,msg="Equal")
    self.af(listB,listB,True,msg="Equal")
    self.af(listC,listC,True,msg="Equal")
    self.af(listD,listD,True,msg="Equal")
    self.af(listE,listE,True,msg="Equal")
    self.af(listF,listF,True,msg="Equal")
    self.af(listG,listG,True,msg="Equal")

    self.af(listA,listAA,True,msg="Equal")
    self.af(listB,listBB,True,msg="Equal")
    self.af(listC,listC2,True,msg="String lists with different order should be equal")
    self.af(listC,listC3,False,msg="String lists of same length with different contents should be different")

    self.af(listA,listB,False,msg="Equal")
    self.af(listA,listC,False,msg="Equal")
    self.af(listA,listD,False,msg="Equal")
    self.af(listA,listE,False,msg="Equal")
    self.af(listA,listF,False,msg="Equal")
    self.af(listA,listG,False,msg="Equal")

    self.af(listB,listC,False,msg="Equal")
    self.af(listB,listD,False,msg="Equal")
    self.af(listB,listE,False,msg="Equal")
    self.af(listB,listF,False,msg="Equal")
    self.af(listB,listG,False,msg="Equal")

    listRep = ["a", "a", "a"]
    listRep2 = ["a", "b", "a"]
    self.af(listRep,listRep2,False,msg="List with repeating elements failing diff")
    self.af(listRep,listRep,True,msg="List with repeating elements failing same")
    self.af(listRep2,listRep2,True,msg="List with repeating elements failing same")

    NestedListRep = [["a"], ["a"], ["a"]]
    NestedListRep2 = [["a"], ["b"], ["a"]]
    self.af(NestedListRep,NestedListRep2,False,msg="Nested list with repeating elements failing diff")
    self.af(NestedListRep,NestedListRep,True,msg="Nested list with repeating elements failing same")
    self.af(NestedListRep2,NestedListRep2,True,msg="List with repeating elements failing same")

  def test_recursiveList(self):
    listA = []
    listB = []
    listA.append(listB)
    listB.append(listA)
    gotExp = False
    try:
        self.af(listA,listB,False,msg="Recursive list not equal")
    except undertest.DataObjectToComplexToCompare:
        gotExp = True
    self.assertTrue(gotExp, msg="Exception not raised")

  def test_badString(self):
      listA = []
      listB = [listA]
      listC = ["LIS:" + str(listA)]

      self.af(listB,listC,False,msg="String matchin list fails")


  def test_dict(self):
    listA = {}
    listB = {"a":"a"}
    listC = {"a":"a", "B":"b"}
    listD = {"a":"a", "B":123}
    listE = {"a":"a", "B":123, "C": {} }
    listF = {"a":"a", "B":123, "C": {"a": "a"} }
    listG = {"a":"a", "B":123, "C": {"a": "a", "b": "b"} }

    listAA = {}
    listBB = {"a":"a"}
    listC2 = {"B":"b", "a":"a"}
    listC3 = {"a":"a", "B":"bb"}

    self.af(listA,listA,True,msg="Equal")
    self.af(listB,listB,True,msg="Equal")
    self.af(listC,listC,True,msg="Equal")
    self.af(listD,listD,True,msg="Equal")
    self.af(listE,listE,True,msg="Equal")
    self.af(listF,listF,True,msg="Equal")
    self.af(listG,listG,True,msg="Equal")

    self.af(listA,listAA,True,msg="Equal")
    self.af(listB,listBB,True,msg="Equal")
    self.af(listC,listC2,True,msg="Dicts with different order should be equal")
    self.af(listC,listC3,False,msg="Dict with same keys but different contents should be different")

    self.af(listA,listB,False,msg="Equal")
    self.af(listA,listC,False,msg="Equal")
    self.af(listA,listD,False,msg="Equal")
    self.af(listA,listE,False,msg="Equal")
    self.af(listA,listF,False,msg="Equal")
    self.af(listA,listG,False,msg="Equal")

    self.af(listB,listC,False,msg="Equal")
    self.af(listB,listD,False,msg="Equal")
    self.af(listB,listE,False,msg="Equal")
    self.af(listB,listF,False,msg="Equal")
    self.af(listB,listG,False,msg="Equal")

    listRep = ["a", "a", "a"]
    listRep2 = ["a", "b", "a"]
    self.af(listRep,listRep2,False,msg="List with repeating elements failing diff")
    self.af(listRep,listRep,True,msg="List with repeating elements failing same")
    self.af(listRep2,listRep2,True,msg="List with repeating elements failing same")

    NestedListRep = [["a"], ["a"], ["a"]]
    NestedListRep2 = [["a"], ["b"], ["a"]]
    self.af(NestedListRep,NestedListRep2,False,msg="Nested list with repeating elements failing diff")
    self.af(NestedListRep,NestedListRep,True,msg="Nested list with repeating elements failing same")
    self.af(NestedListRep2,NestedListRep2,True,msg="List with repeating elements failing same")
#test dict and list combinations

#test list and dict combinations

  def test_assertObjectsEqual(self):
    # basic check that we can call and keys are ignored
    obj1 = { "A": "a" }
    obj2 = { "A": "a", "id": "dddd"}

    undertest.assertObjectsEqual(
      unittestTestCaseClass=self,
      first=obj1,
      second=obj2,
      msg="Failed",
      ignoredRootKeys=["id"]
    )

  def test_assertObjectsEqualBytes(self):
    # check bytes objects
    obj1 = b"abc"
    obj2 = b"abc"
    obj3 = b"def"

    undertest.assertObjectsEqual(
      unittestTestCaseClass=self,
      first=obj1,
      second=obj2,
      msg="Failed",
      ignoredRootKeys=[]
    )

    try:
      undertest.assertObjectsEqual(
        unittestTestCaseClass=self,
        first=obj1,
        second=obj3,
        msg="Failed",
        ignoredRootKeys=[]
      )
    except AssertionError:
      gotExp = True
    self.assertTrue(gotExp, msg="AssertionError not raised")
