import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

a = [24, 25, 8, 7, 12, 16, 20, 21]


def lightUp(ledNumber,period):    
    ledNumber = a[ledNumber]
    GPIO.setup(ledNumber, GPIO.OUT)
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)

#n = 4
#p = 3
#lightUp(n,p)

def blink(ledNumber, blinkCount, blinkPeriod):
    ledNumber = a[ledNumber]
    GPIO.setup(ledNumber, GPIO.OUT)
    for i in range(blinkCount):
        GPIO.output(ledNumber, 1)
        time.sleep(blinkPeriod)
        GPIO.output(ledNumber, 0)
        time.sleep(blinkPeriod)
        
#n = 4
#k = 3
#p = 2
#blink(n, k, p)

def runningLight(count, period):
    for i in range(count):
        for j in range(8):
            lightUp(j,period)
        
#n = 1
#p = 1
#runningLight(n, p)

#for i in []:
#    GPIO.setup(i, GPIO.OUT)
#    PIO.output(i, 0)
    

def runningDark(count, period):
    for i in range(8):
        GPIO.setup(a[i], GPIO.OUT)
        GPIO.output(a[i], 1)
    for i in range(count):
        for j in range(8):
            GPIO.output(a[j], 0)
            time.sleep(period)
            GPIO.output(a[j], 1)
    for i in range(8):
        GPIO.output(a[i], 0)
#n = 1
# = 2
#runningDark(n, p)

def decToBinList(decNumber):
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        if decNumber%2 == 0:
            decNumber = decNumber//2
        else:
            b[i] = 1
            decNumber = decNumber//2
    return(b[::-1])
#n = 255
#lightNumber(n)


def lightNumber(decNumber):
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        if decNumber%2 == 0:
            decNumber = decNumber//2
        else:
            b[i] = 1
            decNumber = decNumber//2
    for i in range(8):
        if b[i] == 1:
            GPIO.setup(a[i], GPIO.OUT)
            GPIO.output(a[i], 1)
    time.sleep(3)
    for i in a:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, 0)
#n = 255
#lightNumber(n)


def runningPattern(pattern, direction):
    b = decToBinList(direction)
    c = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for j in range(pattern):
        for i in range(8):
            c[i] = b[(i + 1)%8]
        b = c[::]
        print(c)
        c = c[::-1]

        for i in range(8):
            if c[i] == 1:
                GPIO.setup(a[i], GPIO.OUT)
                GPIO.output(a[i], 1)
        time.sleep(3)
        for i in a:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, 0)
        c = c[::-1]



n = 3
s = 2
lightNumber(n)
runningPattern(s, n)