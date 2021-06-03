#https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
#tweede antwoord:
"""
I know this answer is for a question from a while back, but if you don't want to import math and you just want to round up, this works for me.
>>> int(21 / 5)
4
>>> int(21 / 5) + (21 % 5 > 0)
5
The first part becomes 4 and the second part evaluates to "True" if there is a remainder, which in addition True = 1; False = 0. So if there is no remainder, then it stays the same integer, but if there is a remainder it adds 1.
"""

class Production:
    def __init__(self,outcomeDict,reagentiaDict):
        self.outcomeDict = outcomeDict
        self.reagentiaDict = reagentiaDict

    def costToProduce(self,demandString):
        splitDemand = demandString.split(' ')
        amount = int(splitDemand[0])
        what = splitDemand[1]
        reactionRepetitions = 1
        if what in self.outcomeDict:
            quantity = self.outcomeDict[what]
            if quantity < amount:
                ratioIntRoundedUp = int(amount // quantity) + (amount % quantity > 0)
                reactionRepetitions = ratioIntRoundedUp
        returnString = ''
        for i in self.reagentiaDict:
            reagentiaAmount = self.reagentiaDict[i]*reactionRepetitions
            reagentiaName = i
            returnString += f'{reagentiaAmount} {reagentiaName}, '
        result = returnString[0:-2]
        return result

    def reagentiaAndOutcomeFor(self,demandString):
        splitDemand = demandString.split(' ')
        amount = int(splitDemand[0])
        what = splitDemand[1]
        reactionRepetitions = 1
        if what in self.outcomeDict:
            quantity = self.outcomeDict[what]
            if quantity < amount:
                ratioIntRoundedUp = int(amount//quantity)+(amount%quantity > 0)
                reactionRepetitions = ratioIntRoundedUp
        reagentiaString = ''
        for i in self.reagentiaDict:
            reagentiaAmount = self.reagentiaDict[i] * reactionRepetitions
            reagentiaName = i
            reagentiaString += f'{reagentiaAmount} {reagentiaName}, '
        reagentiaResult = reagentiaString[0:-2]
        outcomeString = ''
        for j in self.outcomeDict:
            outcomeAmount = self.outcomeDict[j] * reactionRepetitions
            outcomeName = j
            outcomeString += f'{outcomeAmount} {outcomeName}, '
        outcomeResult = outcomeString[0:-2]
        return reagentiaResult, outcomeResult


    def __repr__(self):
        return f'{self.reagentiaDict} => {self.outcomeDict}'

class Nanofactory:
    def __init__(self,path):
        self.productionList = []
        self.constructProductionsFromPath(path)

    def constructProductionsFromPath(self,path):
        with open(path) as file:
            rawData = file.readlines()
        for raw in rawData:
            strippedRaw = raw.strip()
            splitRaw = strippedRaw.split(' => ')
            reagentiaRaw = splitRaw[0]
            reagentiaSplit = reagentiaRaw.split(', ')
            reagentiaDict = {}
            for r in reagentiaSplit:
                rSplit = r.split(' ')
                reagentiaDict[rSplit[1]] = int(rSplit[0])
            outcomeRaw = splitRaw[1]
            oSplit = outcomeRaw.split(' ')
            outcomeDict = {}
            outcomeDict[oSplit[1]] = int(oSplit[0])
            newProduction = Production(outcomeDict,reagentiaDict)
            self.productionList.append(newProduction)

    def stringToAmountAndWhat(self,stringeling):
        split = stringeling.split(' ')
        amount = int(split[0])
        what = split[1]
        return amount, what

    def addToDictionary(self,dictionary,amount,what):
        if what in dictionary:
            oldAmount = dictionary[what]
            dictionary[what] = int(oldAmount) + int(amount)
        else:
            dictionary[what] = int(amount)

    def stringToList(self,stringeling):
        resultList = []
        if ', ' in stringeling:
            split = stringeling.split(', ')
            for s in split:
                resultList.append(s)
        else:
            resultList.append(stringeling)
        return resultList.copy()


    def costToProduce(self,demandsString):
        demandsList = self.stringToList(demandsString)
        demandDict = {}
        leftoverDict = {}
        oreDict = {}
        for j in demandsList:
            jAmount, jWhat = self.stringToAmountAndWhat(j)
            self.addToDictionary(demandDict,jAmount,jWhat)
        while len(demandsList) > 0:
            for s in demandsList:
                sAmount,sWhat = self.stringToAmountAndWhat(s)
                if sWhat == 'ORE':
                    self.addToDictionary(oreDict,sAmount,sWhat)
                    del demandDict['ORE']
            dList = [i for i in demandDict]
            for d in dList:
                dAmount = demandDict[d]
                dWhat = d
                if dWhat in leftoverDict:
                    pAmount = leftoverDict[dWhat]
                    if pAmount > dAmount:
                        dAmount = 0
                        leftoverDict[dWhat] = pAmount-dAmount
                    else:
                        dAmount = dAmount-pAmount
                        del leftoverDict[dWhat]
                if dAmount == 0:
                    del demandDict[dWhat]
                for p in self.productionList:
                    if dWhat in p.outcomeDict and dAmount > 0:
                        dString = f'{dAmount} {dWhat}'
                        todoString, madeString = p.reagentiaAndOutcomeFor(dString)
                        del demandDict[dWhat]
                        todoList = self.stringToList(todoString)
                        for x in todoList:
                            xAmount, xWhat = self.stringToAmountAndWhat(x)
                            self.addToDictionary(demandDict,xAmount,xWhat)
                        madeList = self.stringToList(madeString)
                        for x in madeList:
                            xAmount, xWhat = self.stringToAmountAndWhat(x)
                            if xWhat == dWhat:
                                xAmount -= dAmount
                            if xAmount > 0:
                                self.addToDictionary(leftoverDict, xAmount, xWhat)
            demandsList = []
            for y in demandDict:
                yString = f'{demandDict[y]} {y}'
                demandsList.append(yString)
        return oreDict['ORE']

class CargoHoldToFuel:
    def __init__(self, nanofactoryObject, cargoHold = 1000000000000):
        self.nanofactory = nanofactoryObject
        self.cargoHold = cargoHold
        self.fuel = self.produceFuel()

    def produceFuel(self):
        def fuelString(amount):
            return f'{amount} FUEL'
        def costForAmount(amount):
            result = self.nanofactory.costToProduce(fuelString(amount))
            return result
        amountAbove = 1
        costAbove = costForAmount(amountAbove)
        while costAbove < self.cargoHold:
            amountAbove = amountAbove*2
            costAbove = costForAmount(amountAbove)
        amountBelow = amountAbove//2
        costBelow = costForAmount(amountBelow)
        difference = amountAbove-amountBelow
        while difference > 1:
            amountCenter = amountAbove-difference//2
            costCenter = costForAmount(amountCenter)
            if costCenter > self.cargoHold:
                amountAbove = amountCenter
                costAbove = costForAmount(amountAbove)
            else:
                amountBelow = amountCenter
                costBelow = costForAmount(amountBelow)
            difference = amountAbove-amountBelow
        #print(f'{costBelow}\n{costCenter}\n{costAbove}\n')
        return amountBelow







    def __repr__(self):
        return str(self.productionList)