import unittest
import Pickling

class Testueel:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        self.all3List = [A,B,C]

class PicklingTests(unittest.TestCase):
    def test_saveAndLoad(self):
        testueel = Testueel('Jan',3,[24,23,22])
        a = testueel.A
        b = testueel.B
        c = testueel.C
        all3List = testueel.all3List
        #print(a,b,c,all3List)
        localFolder = 'SavedStates'
        fileName = 'testueel1'
        Pickling.pickleDump(testueel, localFolder, fileName)
        loadedTestueel = Pickling.pickleLoad(localFolder,fileName)
        loadedA =loadedTestueel.A
        loadedB =loadedTestueel.B
        loadedC =loadedTestueel.C
        loadedAll3List = loadedTestueel.all3List
        self.assertEqual(a,loadedA)
        self.assertEqual(b,loadedB)
        self.assertEqual(c,loadedC)
        self.assertEqual(all3List,loadedAll3List)
        
        




if __name__ == '__main__':
    unittest.main()