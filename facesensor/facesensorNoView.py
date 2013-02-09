from SimpleCV import Camera,Display
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

myCamera = Camera(prop_set={'width':320,'height':240})

while True:
  frame = myCamera.getImage()
  faces = frame.findHaarFeatures('face')
  if faces:
    for face in faces:
	  print "Face at: " + str(face.coordinates())
    GPIO.output(25,GPIO.HIGH)
  else:
    print "No faces detected."
    GPIO.output(25,GPIO.LOW)
  sleep(.1)
