#https://stackabuse.com/creating-and-deleting-directories-with-python/
#https://wiki.python.org/moin/UsingPickle
#https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/
import os, pickle


def pickleDump(toBePickled,relativePath,fileName):
    dirPath = _returnDirPath(relativePath)
    if not os.path.isdir(dirPath):
        os.mkdir(dirPath)
    filePath = _returnFilePath(dirPath,fileName)
    with open(filePath,'wb') as f: #open for writing in binary format
        pickle.dump(toBePickled,f) 
    
def pickleLoad(relativePath,fileName):
    dirPath = os.path.join(relativePath)
    if not os.path.isdir(dirPath):
        raise Exception('folder not found')
    filePath = _returnFilePath(dirPath,fileName)    
    if not os.path.isfile(filePath):
        raise Exception('file not not found')
    with open(filePath,'rb') as f: #open for reading in binary format
        result = pickle.load(f) 
    return result

def _returnDirPath(relativePath):
    dirPath = os.path.join(relativePath)
    return dirPath

def _returnFilePath(dirPath,fileName):
    filePath = os.path.join(dirPath+'/'+fileName+'.p')
    return filePath