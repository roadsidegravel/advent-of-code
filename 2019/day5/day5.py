"""
expanded intcode computer
lets properly program it this time
"""

"""
#https://stackoverflow.com/questions/17544307/how-do-i-run-python-script-using-arguments-in-windows-command-line
#first test, get the script running from powershell with a parameter
import sys
print(str(sys.argv[1]))
#werkt
"""

import sys,cmd

#testdata or real data?
#-------------------------------------------------------
test = True
if (str(sys.argv[1]) == "test"):
    test = True
elif (str(sys.argv[1]) == "real"):
    test = False
else:
    print("parameter not understood, test or real, exiting")
    quit()

"""print(test)
works, test true or false and exit if not understood
"""

#load the data
#--------------------------------------------------------
data = []
if (test):
    #wiredata = open("3inputtest", "r").readlines()
    #print("There is no testdata for day5, loading real data")
    data = open("5inputtest", "r").readlines()
elif (not test):
    data = open("5input", "r").readlines()
#print(opcode) #works

#extract
#--------------------------------------------------------
#https://www.tutorialspoint.com/python/string_split.htm
#https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
#https://stackoverflow.com/questions/509211/understanding-slice-notation
opcodes = data[0].split(',')

class intcomputer:
    """
    intcomputer starts at position 0
    decypher it
    last two digits: command, 02 means multiply, 01 means add, 03 means get input, 04 means give output
    other digits: parameter 0 or imediate mode 1 for the parameters for the command, leading zero's discarded
        0 means go to that housenumber, break down the door and drag the number inside out
        1 means you already got the number, he turned himself in
    execute command (dont edit command values whilst executing! store in string orso)
    move to the next position, repeat cycle till intcode ends 99
    """
    opcodes = []
    position = 0
    running = True
    def loadOpcodes(self,opcodes):
        self.opcodes = opcodes
    def setposition(self,newpos):
        if newpos < 0:
            print("intcomputer newpos out of range ",newpos)
            self.running = False
        elif newpos > len(opcodes)-1:
            print("intcomputer newpos out of range ",newpos)
            self.running = False
        else:
            self.position = newpos
    #https://stackoverflow.com/questions/1547145/defining-private-module-functions-in-python (second answer)
    #https://www.smallsurething.com/private-methods-and-attributes-in-python/
    def __someday(self,comstring):
        print("someday we'll implement ",comstring)
        self.running = False
    def __thefckdidyoudo(self,a,b,c):
        print("the fck did you do ",a," ",b," @pos ",c)
        self.running = False
    def run(self):
        string = self.opcodes[self.position]
        pos = self.position
        #decypher
        command = ""
        param = ["0","0","0"]
        if len(string) == 1 or len(string) == 2:
            command = string
        else:
            command = string[-2:]
            newparam = string[:-2]
            if len(newparam) > len(param):
                print("command parameters not understood ",string," @pos ",pos)
                self.running = False
            for x in range(0,len(newparam)):
                j =x+1
                if newparam[-j] == "1":
                    param[x] = "1"
        #perform
        if command == "01" or command == "1":
            #add a+b r
            a = 0
            b = 0
            paramA = param[0]
            if paramA == "0":
                a = self.opcodes[int(self.opcodes[pos+1])]
            elif paramA == "1":
                a = self.opcodes[pos+1]
            else:
                self.__thefckdidyoudo(param,string,pos)
            paramB = param[1]
            if paramB == "0":
                b = self.opcodes[int(self.opcodes[pos+2])]
            elif  paramB == "1":
                b = self.opcodes[pos+2]
            else:
                self.__thefckdidyoudo(param,string,pos)
            r = str(int(a)+int(b))
            paramR = param[2]
            if paramR == "1":
                print("write destination should never be immediate mode")
                self.__thefckdidyoudo(param,string,pos)
            elif paramR == "0":
                self.opcodes[int(self.opcodes[pos+3])] = r
            else:
                self.__thefckdidyoudo(param,string,pos)
            self.setposition(pos+4)
        elif command == "02" or command == "2":
            #multiply a*b r
            a = 0
            b = 0
            paramA = param[0]
            if paramA == "0":
                a = self.opcodes[int(self.opcodes[pos+1])]
            elif paramA == "1":
                a = self.opcodes[pos+1]
            else:
                self.__thefckdidyoudo(param,string,pos)
            paramB = param[1]
            if paramB == "0":
                b = self.opcodes[int(self.opcodes[pos+2])]
            elif  paramB == "1":
                b = self.opcodes[pos+2]
            else:
                self.__thefckdidyoudo(param,string,pos)
            r = str(int(a)*int(b))
            paramR = param[2]
            if paramR == "1":
                print("write destination should never be immediate mode")
                self.__thefckdidyoudo(param,string,pos)
            elif paramR == "0":
                self.opcodes[int(self.opcodes[pos+3])] = r
            else:
                self.__thefckdidyoudo(param,string,pos)
            self.setposition(pos+4)
        #https://docs.python.org/3/tutorial/inputoutput.html
        #https://docs.python.org/dev/library/cmd.html
        #https://docs.python.org/dev/library/functions.html#input
        elif command == "03" or command == "3":
            #get input, store it
            #cmd03 = inputcmd()
            #cmd03.cmdloop() #overkill for what we need, but interesting stuff
            #https://stackoverflow.com/questions/21388541/how-do-you-check-in-python-whether-a-string-contains-only-numbers
            inputreceived = False
            failsafe = 0
            r = ""
            while not inputreceived:
                r = input("intcomputer requires an input: ")
                if r == "":
                    print("input cannot be empty")
                if not r.isdigit():
                    print("input should be a number")
                else: 
                    print("input ",r,"accepted, continuing")
                    inputreceived = True
                failsafe = failsafe+1
                if failsafe > 5:
                    print("Too many input attempts, aborting")
                    self.running = False
                    break          
            paramR = param[2]
            if paramR == "1":
                print("write destination should never be immediate mode")
                self.__thefckdidyoudo(param,string,pos)
            elif paramR == "0":
                self.opcodes[int(self.opcodes[pos+1])] = r
            else:
                self.__thefckdidyoudo(param,string,pos)
            self.setposition(pos+2)
        elif command == "04" or command == "4":
            #give output
            r = ""         
            paramR = param[2]
            if paramR == "1":
                r = self.opcodes[pos+1]
            elif paramR == "0":
                r = self.opcodes[int(self.opcodes[pos+1])]
            else:
                self.__thefckdidyoudo(param,string,pos)
            print("intcomputer output: ",r)
            self.setposition(pos+2)
        elif command == "05" or command == "5":
            self.__someday(command)
        elif command == "99":
            print("intcode 99 reached")
            self.running = False
        else:
            print("command not understood ", string, " @pos ", pos)
            self.running = False

#https://docs.python.org/3/library/cmd.html based on example
class inputcmd(cmd.Cmd):
    intro = "Intcomputer requires input"
    prompt = "input: "
    file = None
    
                      
curintcomputer = intcomputer()
curintcomputer.loadOpcodes(opcodes)
safegaurd = 0
while curintcomputer.running:
    curintcomputer.run()
    safegaurd = safegaurd+1
    if (safegaurd > 100):
        print("safegaurd reached, stopping while loop")
        break
  
