class password:
    def __init__(self,lowerRange,upperRange):
        self.criteriaMetCount = 0
        self.fourCriteriaMetCount = 0
        if not isinstance(lowerRange,int) or not isinstance(upperRange, int):
            raise ValueError('lowerRange and upperRange should be ints')
        if lowerRange > upperRange or lowerRange == upperRange:
            raise ValueError('password lowerRange should be smaller than upperRange')
        self._lowerRange = lowerRange
        self._upperRange = upperRange
        for i in range(lowerRange,upperRange+1):
            if self._allRules(i):
                self.criteriaMetCount += 1
            if self._extraRuleIncluded(i):
                self.fourCriteriaMetCount += 1

    def _isSixDigits(self,number):
        if len(str(number)) == 6:
            return True
        else:
            return False

    def _twoAdjacentIdenticalDigits(self, number):
        number = str(number)
        for i in range(1,len(number)):
            a = number[i]
            b = number[i-1]
            if a == b:
                return True
        return False

    def _leftToRightIncreasesOrSame(self, number):
        number = str(number)
        for i in range(1, len(number)):
            a = number[i]
            b = number[i - 1]
            if a < b:
                return False
        return True

    def _allRules(self, number):
        if self._isSixDigits(number):
            if self._leftToRightIncreasesOrSame(number):
                if self._twoAdjacentIdenticalDigits(number):
                    return True
        return False

    def _containsTwo(self, number):
        number = str(number)
        numberSet = set(number)
        for i in numberSet:
            if number.count(i) == 2:
                return True
        return False

    def _extraRuleIncluded(self, number):
        if self._allRules(number):
            if self._containsTwo(number):
                return True
        return False
