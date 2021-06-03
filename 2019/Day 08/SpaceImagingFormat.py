class SIFLayers:
    def __init__(self,data,width,height):
        self.width = width
        self.height = height
        self.buildLayerListFromData(data)
        self.fewestZeroLayerID = self.findLayerWithFewestZeroes()

    def buildLayerListFromData(self,data):
        dataString =str(data)
        self.layerList = []
        layerLength = self.width*self.height
        numberOfLayers = int(len(dataString)/layerLength)
        for i in range(0,numberOfLayers):
            startIndex = i*layerLength
            endIndex = (i+1)*layerLength
            layerString = dataString[startIndex:endIndex]
            self.layerList.append(layerString)

    def findLayerWithFewestZeroes(self):
        def countZeroesInLayer(layerNumber):
            layerString = self.layerList[layerNumber]
            result = layerString.count('0')
            return result
        findZeroCount = countZeroesInLayer(0)
        findZeroLayer = 0

        def compareLayerAgainstFindzeroCountAndLayer(layerNumber,findZeroCount,findZeroLayer):
            zeroCount = countZeroesInLayer(layerNumber)
            if zeroCount < findZeroCount:
                return zeroCount,layerNumber
            else:
                return findZeroCount,findZeroLayer

        for i in range(1,len(self.layerList)):
            findZeroCount,findZeroLayer = compareLayerAgainstFindzeroCountAndLayer(i,findZeroCount,findZeroLayer)
        return findZeroLayer

    def returnOnFewestZeroesLayerMultiplyOneCountByTwoCount(self):
        layerString = self.layerList[self.fewestZeroLayerID]
        oneCount = layerString.count('1')
        twoCount = layerString.count('2')
        result = oneCount*twoCount
        return result

def constructSIFLayersFromFile(path,width,height):
    rawData = []
    with open(path) as file:
        rawData = file.readlines()
    return SIFLayers(rawData[0],width,height)

class DecodedSIF:
    def __init__(self,SIFLayersObject):
        if not isinstance(SIFLayersObject,SIFLayers):
            raise TypeError('DecodedSIF requires a SIFLayers object')
        self.SIFLayersObject = SIFLayersObject
        self.pixelList = []
        self.constructPixelList()
        self.topVisiblePixelList = []
        self.constructTopVisiblePixelList()

    def constructPixelList(self):
        self.pixelList = []
        for h in range(0,len(self.SIFLayersObject.layerList[0])):
            pixelString = ''
            for i in range(0,len(self.SIFLayersObject.layerList)):
                pixelString += self.SIFLayersObject.layerList[i][h]
            self.pixelList.append(pixelString)

    def constructTopVisiblePixelList(self):
        self.topVisiblePixelList = []
        for i in range(0,len(self.pixelList)):
            result = '2'
            for j in range(0,len(self.pixelList[0])):
                k = self.pixelList[i][j]
                if result == '2':
                    if k == '0' or k == '1':
                        result = k
            self.topVisiblePixelList.append(result)

    def __repr__(self):
        result = ''
        row = ''
        newLine = '\n'
        rowCounter = 0
        for i in range(0,len(self.topVisiblePixelList)):
            p = self.topVisiblePixelList[i]
            if p == '1':
                row += 'X'
            else:
                row += ' '
            rowCounter += 1
            if rowCounter == self.SIFLayersObject.width:
                rowCounter = 0
                result += row
                row = ''
                if i < len(self.topVisiblePixelList)-1:
                    result += newLine
        return result

def constructDecodedSIFFromFile(path,width,height):
    SIFLayers = constructSIFLayersFromFile(path,width,height)
    return DecodedSIF(SIFLayers)

