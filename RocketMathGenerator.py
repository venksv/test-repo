import random
import time
import winsound

class MathSum:
    def __init__(self, op1, op2, inpAnswer, actAnswer):
        self.op1 = op1
        self.op2 = op2
        self.answer = inpAnswer

        #print("In __init__. Op1: " + str(op1) + ", Op2: " + str(op2) + ", Answer: " + str(inpAnswer) + ", Actual: " + str(actAnswer))
        if (inpAnswer == actAnswer):
            #print("Setting correct ...")
            self.status = "Correct"
        else:
            #print("Setting wrong ...")
            self.status = "Wrong"

        #print("Status: " + self.status)

    def getOp1(self):
        return (self.op1)

    def getOp2(self):
        return (self.op2)

    def getStatus(self):
        return (self.status)

    def getAnswer(self):
        return(self.answer)

def add(op1, op2):
    return (op1 + op2)

def subtract(op1, op2):
    return (op1 - op2)

def multiply(op1, op2):
    return (op1 * op2)

def divide(op1, op2):
    return (op1/op2)

answers = dict()
operation = {"+" : add,
             "-" : subtract,
             "*" : multiply,
             "/" : divide             
             }

currOp = "+"
quesAnswered = 1

t0 = time.time()
timeLimit = 10

try:
    while((time.time() - t0) < timeLimit):
        op1 = random.randint(1, 10)
        op2 = random.randint(1, 10)
        print ("\n" + str(op1).rjust(4))
        print (currOp, str(op2).rjust(2),"\n","------")
        userAnswer = int(input("  "))
        #print ("You answered", userAnswer)
        answers[quesAnswered] = MathSum(op1, op2, userAnswer, operation[currOp](op1, op2))
        quesAnswered += 1

except IOError as err:
    print("IO Error: " + str(err))
    
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second
winsound.Beep(Freq,Dur)

corrAnswerCount = 0
print ("\nResults: ")
for i in answers.keys():
    if (answers[i].getStatus() == "Correct"):
        corrAnswerCount += 1
        
    print(str(i)+".", str(answers[i].getOp1()), currOp,
          str(answers[i].getOp2()), "=", str(answers[i].getAnswer()),
          "-->", answers[i].getStatus())
    #print("You answered:", str(answers[i].getAnswer()), "which is", answers[i].getStatus())

if (corrAnswerCount == len(answers)):
    print("CONGRATULATIONS Mallika!! YOU ROCK!!")
else:
    print("UH-OH! You only got", corrAnswerCount, "out of", len(answers), "correct! Keep at it!!")
