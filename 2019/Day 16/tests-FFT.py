import unittest
from unittest.mock import  patch
from FlawedFrequencyTransmission import FlawedFrequencyTransmission as FFT


class FFTExampleTests(unittest.TestCase):
    def setUp(self):
        path = 'Example1.txt'
        self.fft = FFT(path)
    def tearDown(self):
        self.fft = None
    def test_loadFromPath(self):
        loadedSignal = self.fft.startSignal
        referenceSignal = '12345678'
        self.assertEqual(referenceSignal,loadedSignal)
    def test_applyFirstPhase(self):
        self.fft.applyPhaseOnCurrentSignal()
        currentSignal = self.fft.currentSignal
        referenceSignal = '48226158'
        self.assertEqual(referenceSignal,currentSignal)
    def test_applyTwoPhases(self):
        self.fft.applyPhaseOnCurrentSignal()
        self.fft.applyPhaseOnCurrentSignal()
        currentSignal = self.fft.currentSignal
        referenceSignal = '34040438'
        self.assertEqual(referenceSignal,currentSignal)
    def test_applySeveralPhases2(self):
        self.fft.applySeveralPhasesOnCurrentSignal(2)
        currentSignal = self.fft.currentSignal
        referenceSignal = '34040438'
        self.assertEqual(referenceSignal,currentSignal)
    def test_applySeveralPhases3(self):
        self.fft.applySeveralPhasesOnCurrentSignal(3)
        currentSignal = self.fft.currentSignal
        referenceSignal = '03415518'
        self.assertEqual(referenceSignal,currentSignal)
    def test_applySeveralPhases4(self):
        self.fft.applySeveralPhasesOnCurrentSignal(4)
        currentSignal = self.fft.currentSignal
        referenceSignal = '01029498'
        self.assertEqual(referenceSignal,currentSignal)

class FFTLargerInputExamples(unittest.TestCase):
    def test_Example2(self):
        path = 'Example2.txt'
        fft = FFT(path)
        output = fft.applySeveralPhasesOnCurrentSignal(100)
        reference = '24176176'
        self.assertEqual(reference,output)
    def test_Example3(self):
        path = 'Example3.txt'
        fft = FFT(path)
        output = fft.applySeveralPhasesOnCurrentSignal(100)
        reference = '73745418'
        self.assertEqual(reference,output)
    def test_Example4(self):
        path = 'Example4.txt'
        fft = FFT(path)
        output = fft.applySeveralPhasesOnCurrentSignal(100)
        reference = '52432133'
        self.assertEqual(reference,output)
        
        
        

        
        

if __name__ == '__main__':
    unittest.main()
