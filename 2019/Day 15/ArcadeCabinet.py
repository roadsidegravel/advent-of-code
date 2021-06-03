from Intcode import computer as Computer
from Painter import Map, Representation
import tkinter

#https://gordonlesti.com/use-tkinter-without-mainloop/
#https://stackoverflow.com/questions/21440731/tkinter-getting-key-pressed-event-from-a-function
nextMove = 0

class ArcadeCabinet:
    def __init__(self,intcodeList):
        self.brain = Computer(intcodeList,automaticMode=True)
        self.screen = Map()
        screenDictionary = {0: ' ', 1: 'W', 2: 'B', 3: '=', 4: 'O',16:'X',34:'X'}
        self.screenRepresentation = Representation('screen', screenDictionary)
        self.score = 0
        self.ballX = 0
        self.paddleX =0

    def startTkinterGame(self, autoPilot = False):
        def keyReleased(event):
            global nextMove
            if event.keysym == 'Left':
                nextMove = 1
            if event.keysym == 'Right':
                nextMove = -1
            if event.keysym == 'Up':
                nextMove = 0
            print('key released')


        self.root = tkinter.Tk()
        self.root.geometry('800x800')
        self.text = tkinter.Text(self.root, width = 900, height = 900)#,height = self.root.winfo_height(),width = self.root.winfo_width(),state=tkinter.DISABLED)
        self.root.bind('<KeyRelease>',keyReleased)
        self.text.pack()
        self.brain.intcode[0] = 2
        self.brain.run()
        self.populateScreen()
        remaining = self.countObjectsOnScreenFromKey(2)
        global nextMove
        while remaining > 0:
            if autoPilot:
                if self.ballX > self.paddleX:
                    nextMove = 1
                elif self.ballX < self.paddleX:
                    nextMove = -1
                else:
                    nextMove = 0
            if not self.brain.running:
                if nextMove != None:
                    self.brain.automaticModeTakeInputAndUnpauze(nextMove)
                nextMove = None
            self.populateScreen()
            self.text.delete(1.0, tkinter.END)
            self.text.insert(tkinter.END,self.constructTkinterText(self.screenRepresentation))
            self.root.update_idletasks()
            self.root.update()
    def startGame(self):
        self.brain.run()

    def populateScreen(self):
        for i in range(int(len(self.brain.outputs)/3)):
            fromLeft = self.brain.outputs[i*3]
            fromTop  = self.brain.outputs[i*3+1]
            what = self.brain.outputs[i*3+2]
            if fromLeft == -1 and fromTop == 0:
                self.score = what
            else:
                if what == 3:
                    self.paddleX = fromLeft
                elif what == 4:
                    self.ballX = fromLeft
                self.screen.setValueAtCoordinates(-fromLeft, -fromTop, what)

    def printScreen(self):
        self.screen.printMap(pretty=True,myReprensation=self.screenRepresentation)
        print(f'score is: {self.score}')
    def constructTkinterText(self,myReprensation):
        returnString = ''
        printRepresentation = myReprensation
        map = self.screen
        minX = 0
        maxX = 0
        minY = 0
        maxY = 0
        for i in map.knownCoordinatesObjects:
            if i.x < minX:
                minX = i.x
            if i.x > maxX:
                maxX = i.x
            if i.y < minY:
                minY = i.y
            if i.y > maxY:
                maxY = i.y
        printWidth = abs(minX)+1+abs(maxX)
        printHeight = abs(minY)+1+abs(maxY)
        printGrid = [0 for c in range(printHeight)]
        for i in range(printHeight):
            printGrid[i] = [0 for r in range(printWidth)]
        startx = printWidth-maxX-1
        starty = printHeight-maxY-1
        for r in range(printHeight):
            for c in range(printWidth):
                printGrid[r][c] = printRepresentation.convertKeyToValue(printGrid[r][c])
        for i in map.knownCoordinatesObjects:
            col = i.x+startx
            row = i.y+starty
            value = printRepresentation.convertKeyToValue(i.value)
            printGrid[row][col] = value
        for i in range(printHeight):
            printString = ''
            for j in range(printWidth):
                printString += printGrid[printHeight-i-1][j]+' '
            returnString += printString+'\n'
        returnString += '\n'
        returnString += f'Score: {self.score} with {self.countObjectsOnScreenFromKey(2)} blocks left.'
        return returnString

    def countObjectsOnScreenFromKey(self,objectKey):
        result = 0
        for i in self.screen.knownCoordinatesObjects:
            if i.value == objectKey:
                result += 1
        return result




def constructArcadeCabinetFromPath(path):
    rawData = []
    with open(path) as file:
        rawData = file.readlines()
    rawIntcode = rawData[0].split(',')
    intcode = []
    for i in range(0, len(rawIntcode)):
        intcode.append(int(rawIntcode[i]))
    result = ArcadeCabinet(intcode)
    return result