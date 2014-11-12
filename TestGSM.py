import Adafruit_BBIO.UART as UART
import serial
import time 
from time import sleep
import os

ser4 = serial.Serial(port = "/dev/ttyO4", baudrate=115200, timeout=1)  #ZigBee
ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=115200, timeout=1) #GSM




#ser1.write('AT+IPR=115200\r')
#print 'Set Baud Rate'
#GSM = ser1.readlines()
#print GSM

#ser1.write('AT&W\r')
#print 'Write Setting'
#GSM = ser1.readlines()
#print GSM
#ser1.write('AT+QIDEACT=1\r')
#print 'Disconnect'
#GSM = ser1.readline()
#print GSM

#ser1.write('AT+QHTTPCFG="contextid",1\r')
#print 'contextid'
#GSM = ser1.readline()
#print GSM
#length_gsm = len(GSM)
#if length_gsm >20:
	#GSM = ser1.readlines()
#print GSM

#ser1.write('AT+QHTTPCFG="responseheader",0\r')
#print 'responseheader'
#time.sleep(1)
#GSM = ser1.readline()
#print GSM

#ser1.write('AT+QICSGP=1,1,"internet","True","true",1\r')
#print 'internet'
#GSM = ser1.readline()
#print GSM

#ser1.write('AT+QIACT=1\r')
#print 'connect'
#time.sleep(3)
#GSM = ser1.readline()
#GSM = ser1.readline()
#print GSM
#if(GSM == "OK\r\n"):
	#print ('Internet Connection Established')
#else :
	#print ('Internet Connection Fail. ..')
		
#ser1.write('AT+QHTTPURL=60,80\r') #47
#time.sleep(1)
#GSM = ser1.readline()

#ser1.write('http://202.44.37.130/testing/EGAT/gettime.php?\r')
#ser1.write('http://202.44.37.130/testing/EGAT/gettime.php?\r')

##time.sleep(1)
#GSM = ser1.readline()
##print GSM

#ser1.write('AT+QHTTPGET=80\r')
##print 'HTTP_GET'
#time.sleep(2)
#GSM = ser1.readline()
#GSM = ser1.readline()
#print GSM

#ser1.write('AT+QHTTPREAD=80\r')
##print 'HTTP_GET'
#time.sleep(2)
#GSM = ser1.readlines()
#print GSM

#print ('GSM END')
	
while True:	
	
	#ser4.write('A0003+0\n')
	ser4.write('P000X\n')
	#ser4.write('A0XXX+0\n')
	#print 'Hello Mys\n'
	GSM = ser4.readlines()
	print GSM



#os.system('hwclock -s -f /dev/rtc1')
#os.system('hwclock -w')


#os.system('hwclock -r -f /dev/rtc1')
#os.system('date')
