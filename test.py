import vlc
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
def verde_on():
    GPIO.output(11, GPIO.HIGH)
        
def verde_off():
    GPIO.output(11, GPIO.LOW)
    
def amarelo_on():
    GPIO.output(13, GPIO.HIGH)
        
def amarelo_off():
    GPIO.output(13, GPIO.LOW)
        
def branco_on():
    GPIO.output(15, GPIO.HIGH)
        
def branco_off():
    GPIO.output(15, GPIO.LOW)
while True:
    i = 0
    while i < 25:
        verde_on()
        sleep(0.10)
        verde_off()
        amarelo_on()
        sleep(0.10)
        amarelo_off()
        branco_on()
        sleep(0.10)
        branco_off()
        i+=1
    b = 0
    for b in range(20):
        if (b % 2) == 0:
            verde_on()
            amarelo_on()
            branco_on()
            sleep(0.5)
        else:
            verde_off()
            amarelo_off()
            branco_off()
            sleep(0.5)
        b+=1

player.stop()