from FlawedFrequencyTransmission import FlawedFrequencyTransmission as FFT
#https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
from timeit import default_timer as timer
start = timer()
path = 'InputDay16.txt'
fft = FFT(path)
output = fft.applySeveralPhasesOnCurrentSignal(100)
reference = '70856418'
print(f'Day 16, part 1: the first eight digits are {output} ({reference})')
end = timer()
print(f'It took: {end - start}') 