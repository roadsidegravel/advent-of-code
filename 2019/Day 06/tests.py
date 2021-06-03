import unittest

from UniversalOrbitMap import Object
class ObjectTests(unittest.TestCase):
    def test_COMObject(self):
        name = 'COM'
        orbits = None
        COMObject = Object(name,orbits)
        self.assertEqual(name, COMObject.name)
        self.assertEqual(orbits, COMObject.orbitsObject)
    def test_COMObjectOrbitNumber(self):
        COMObject = Object('COM',None)
        self.assertEqual(0, COMObject.orbitCount)
    def test_AAAorbitsCOMOrbitNumber(self):
        COMObject = Object('COM',None)
        AAAObject = Object('AAA',COMObject)
        self.assertEqual(0, COMObject.orbitCount)
        self.assertEqual(1, AAAObject.orbitCount)
    def test_raiseErrorIfOrbitsIsWrongType(self):
        with self.assertRaises(TypeError) as e:
            ErrorObject = Object('AAA',5)
        self.assertEqual('orbitsObject should be an Object or None',str(e.exception))

from UniversalOrbitMap import OrbitMap
class OrbitMapTests(unittest.TestCase):
    def test_EmptyOrbitMap(self):
        dataString = []
        orbitMap = OrbitMap(dataString)
        self.assertEqual(1,len(orbitMap.objects))
        self.assertEqual(1,len(orbitMap.objectNames))
        self.assertEqual(orbitMap.objects[0].name,orbitMap.objectNames[0])
    def test_OrbitMapCOMoAAA(self):
        dataString = ['COM)AAA']
        orbitMap = OrbitMap(dataString)
        self.assertEqual(2,len(orbitMap.objects))
        self.assertEqual(2,len(orbitMap.objectNames))
    def test_OrbitMapAvoidDuplicatesCOMoAAAxCOMoBBBxAAAoCCC(self):
        dataString = ['COM)AAA','COM)BBB','AAA)CCC']
        orbitMap = OrbitMap(dataString)
        self.assertEqual(4,len(orbitMap.objects))
        self.assertEqual(['COM','AAA','BBB','CCC'],orbitMap.objectNames)
    def test_CountEmptyOrbitMap(self):
        dataString = []
        orbitMap = OrbitMap(dataString)
        self.assertEqual(0, orbitMap.totalNumberOfOrbits)
    def test_CountOrbitMapCOMoAAA(self):
        dataString = ['COM)AAA']
        orbitMap = OrbitMap(dataString)
        self.assertEqual(1, orbitMap.totalNumberOfOrbits)
    def test_CountOrbitMapAvoidDuplicatesCOMoAAAxCOMoBBBxAAAoCCC(self):
        dataString = ['COM)AAA','COM)BBB','AAA)CCC']
        orbitMap = OrbitMap(dataString)
        self.assertEqual(4, orbitMap.totalNumberOfOrbits)
    #problem encountered
    def test_ConstructOutOfOrder(self):
        dataString = ['AAA)CCC','COM)BBB','COM)AAA']
        orbitMap = OrbitMap(dataString)
        print(orbitMap.objectNames)
        self.assertEqual(4,orbitMap.totalNumberOfOrbits)
    def test_InfiniteBackLogLoopRaisesError(self):
        dataString = ['AAA)CCC']
        with self.assertRaises(RecursionError) as e:
            orbitMap = OrbitMap(dataString)
        self.assertEqual('@constructOrbitmapFromDataList: goThroughList: backlog did not shrink',str(e.exception))

from UniversalOrbitMap import ConstructOrbitMapFromDataFile
class TestsDay6Part2(unittest.TestCase):
    def setUp(self):
        path = 'example2'
        self.example2Map = ConstructOrbitMapFromDataFile(path)
    def tearDown(self):
        self.example2Map = None
    def test_BuildListOfAncestors(self):
        ancestorListYou = self.example2Map.BuildListOfAncestorNames('YOU')
        self.assertEqual(['K', 'J', 'E', 'D', 'C', 'B', 'COM'] , ancestorListYou,'ancestors of YOU')
        ancestorListSAN = self.example2Map.BuildListOfAncestorNames('SAN')
        self.assertEqual(['I', 'D', 'C', 'B', 'COM'],ancestorListSAN,'ancestors of SAN')
    def test_FindCommonAncestorNames(self):
        commonDaddyNames = self.example2Map.FindCommonAncestorNames('YOU','SAN')
        self.assertEqual(['D', 'C', 'B', 'COM'],commonDaddyNames)
    def test_CalculateOrbitsBetweenTwoNames(self):
        betweenOrbits = self.example2Map.CalculateOrbitsBetweenTwoNames('YOU','SAN')
        self.assertEqual(4,betweenOrbits)




if __name__ == '__main__':
    unittest.main()
