#Reset Members
# Use Real Time Clock By Mys


from Tkinter import *
from PIL import Image, ImageTk
import Adafruit_BBIO.UART as UART
import serial
import time 
from time import sleep
import Adafruit_BBIO.GPIO as GPIO
import Tkinter as tk
import os
from time import gmtime, strftime
from datetime import datetime
import sys
import datetime
import smbus
import time

global root
global w
ser4 = serial.Serial(port = "/dev/ttyO4", baudrate=115200, timeout=1)  #ZigBee

root=tk.Tk()
root.title("EGAT")

## windown size
canvas_width = 480
canvas_height = 800
w = Canvas(root, width=canvas_width, height=canvas_height)

## Path Image ##
page1   = Image.open("/home/debian/geany_bbb/ev_pic/egat4.jpg")


## ImageTk Library
main_start1 = ImageTk.PhotoImage(page1)


## Add image to Array
my_images = []
my_images.append(main_start1)	  #Array 0


canvas = w.create_image(0, 0,anchor=NW,image=my_images[0])
w.pack()	
root.config(cursor='none')
root.attributes('-fullscreen', True)		

def main_start1(event):
	
	#clear_data_label(1)
	
	w.itemconfig(canvas, image = my_images[0])	
	
L1 = StringVar() 
L2 = StringVar() 
L3 = StringVar() 
L4 = StringVar()
L5 = StringVar() 
L6 = StringVar() 
L7 = StringVar() 
L8 = StringVar()
L9 = StringVar() 
L10 = StringVar()
L11 = StringVar() 
L12 = StringVar() 
L13 = StringVar() 
L14 = StringVar()
L15 = StringVar() 
L16 = StringVar() 
L17 = StringVar() 
L18 = StringVar() 
L19 = StringVar() 
L20 = StringVar() 

	
def show_data(event):
	
	global line1
	global line2
	global line3
	global line4
	global line5
	global line6
	global line7
	global line8
	global line9
	global line10
	global line11
	global line12
	global line17
	
	line1 = tk.Label(text='line1',textvariable=L1, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')
	line2 = tk.Label(text='line2',textvariable=L2, font=("Tahoma",16),fg = 'green', bg='black',width=32,anchor='w')
	line3 = tk.Label(text='line3',textvariable=L3, font=("Tahoma",16),fg = 'green', bg='black',width=32,anchor='w')
	line4 = tk.Label(text='line4',textvariable=L4, font=("Tahoma",16),fg = 'green', bg='black',width=32,anchor='w')
	line5 = tk.Label(text='line5',textvariable=L5, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line6 = tk.Label(text='line6',textvariable=L6, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line7 = tk.Label(text='line7',textvariable=L7, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line8 = tk.Label(text='line8',textvariable=L8, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line9 = tk.Label(text='line9',textvariable=L9, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line10 = tk.Label(text='line10',textvariable=L10, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line11 = tk.Label(text='line11',textvariable=L11, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line12 = tk.Button(root, text='Reset !',bg='black',fg='red',font=("Tahoma",50), width=8,height=4,command=press_button)
	#line13 = tk.Label(text='',textvariable=L13, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')
	#line14 = tk.Label(text='',textvariable=L14, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')
	#line15 = tk.Label(text='',textvariable=L15, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')
	#line16 = tk.Label(text='',textvariable=L16, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')
	line17 = tk.Label(text='line17',textvariable=L17, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')

	
	line1.pack()
	line2.pack()
	line3.pack()
	line4.pack()
	line5.pack()
	line6.pack()
	line7.pack()
	line8.pack()
	line9.pack()
	line10.pack()
	line11.pack()
	line12.pack()
	#line13.pack()
	#line14.pack()
	#line15.pack()
	#line16.pack()
	line17.pack()


	w.create_window(245,108,window=line1)
	w.create_window(245,148,window=line2)
	w.create_window(245,188,window=line3)
	w.create_window(245,228,window=line4)
	w.create_window(245,258,window=line5)
	w.create_window(245,298,window=line6)
	w.create_window(245,338,window=line7)
	w.create_window(245,378,window=line8)
	w.create_window(245,428,window=line9)
	w.create_window(245,468,window=line10)
	w.create_window(245,508,window=line11)
	w.create_window(245,588,window=line12)
	#w.create_window(245,468,window=line13)
	#w.create_window(245,508,window=line14)
	#w.create_window(245,548,window=line15)
	#w.create_window(245,548,window=line16)
	w.create_window(245,60,window=line17)



	
def clear_data(event):
	w.destroy()


	
def close(event):
        
	w.destroy()
	root.withdraw()
	#root.destroy()
	
def show_data2 (event):

	global line1
	global line2
	global line3
	global line4
	global line5
	global line6
	global line7
	global line8
	global line9
	global line10
	global line11
	global line12
	global line13
	global line14
	global line15
	global line16
	global line17
	global line18
	global line19
	global line20
	
	line1 = tk.Label(text='line1',textvariable=L1, font=("Tahoma",16),fg = 'green', bg='black',width=32,anchor='w')
	line2 = tk.Label(text='line2',textvariable=L2, font=("Tahoma",16),fg = 'green', bg='black',width=32,anchor='w')
	line3 = tk.Label(text='line3',textvariable=L3, font=("Tahoma",16),fg = 'green', bg='black',width=32,anchor='w')
	line4 = tk.Label(text='line4',textvariable=L4, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')
	line5 = tk.Label(text='line5',textvariable=L5, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line6 = tk.Label(text='line6',textvariable=L6, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line7 = tk.Label(text='line7',textvariable=L7, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line8 = tk.Label(text='line8',textvariable=L8, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line9 = tk.Label(text='line9',textvariable=L9, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line10 = tk.Label(text='line10',textvariable=L10, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line11 = tk.Label(text='line11',textvariable=L11, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line12 = tk.Label(text='line12',textvariable=L12, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line13 = tk.Label(text='line13',textvariable=L13, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line14 = tk.Label(text='line14',textvariable=L14, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line15 = tk.Label(text='line15',textvariable=L15, font=("Tahoma",16),fg = 'lightblue', bg='black',width=10,anchor='w')
	line16 = tk.Button(root, text='Stop Register!',bg='black',fg='red',font=("Tahoma",28), width=16,height=2,command=press_button2)
	line17 = tk.Label(text='line17',textvariable=L17, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')
	line19 = tk.Label(text='line19',textvariable=L19, font=("Tahoma",16),fg = 'lightblue', bg='black',width=10,anchor='w')
	line20 = tk.Label(text='line20',textvariable=L20, font=("Tahoma",16),fg = 'lightblue', bg='black',width=10,anchor='w')



	
	line1.pack()
	line2.pack()
	line3.pack()
	line4.pack()
	line5.pack()
	line6.pack()
	line7.pack()
	line8.pack()
	line9.pack()
	line10.pack()
	line11.pack()
	line12.pack()
	line13.pack()
	line14.pack()
	line15.pack()
	line16.pack()
	line17.pack()
	line19.pack()
	line20.pack()


	w.create_window(245,108,window=line1)
	w.create_window(245,148,window=line2)
	w.create_window(245,188,window=line3)
	w.create_window(245,228,window=line4)
	w.create_window(245,268,window=line5)
	w.create_window(245,303,window=line6)
	w.create_window(245,338,window=line7)
	w.create_window(245,373,window=line8)
	w.create_window(245,408,window=line9)
	w.create_window(245,443,window=line10)
	w.create_window(245,478,window=line11)
	w.create_window(245,513,window=line12)
	w.create_window(245,548,window=line13)
	w.create_window(245,583,window=line14)
	w.create_window(105,633,window=line15)
	w.create_window(264,633,window=line19)
	w.create_window(423,633,window=line20)
	w.create_window(245,718,window=line16)
	w.create_window(245,60,window=line17)

def show_data3 (event):

	global line1
	global line2
	global line3
	global line4
	global line5
	global line6
	global line7
	global line8
	global line9
	global line10
	global line11
	global line12
	global line13
	global line14
	global line15
	global line16
	global line17
	global line18
	global line19
	global line20
	
	line1 = tk.Label(text='line1',textvariable=L1, font=("Tahoma",16),fg = 'green', bg='black',width=32,anchor='w')
	line2 = tk.Label(text='line2',textvariable=L2, font=("Tahoma",16),fg = 'green', bg='black',width=32,anchor='w')
	line3 = tk.Label(text='line3',textvariable=L3, font=("Tahoma",16),fg = 'green', bg='black',width=32,anchor='w')
	line4 = tk.Label(text='line4',textvariable=L4, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')
	line5 = tk.Label(text='line5',textvariable=L5, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line6 = tk.Label(text='line6',textvariable=L6, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line7 = tk.Label(text='line7',textvariable=L7, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line8 = tk.Label(text='line8',textvariable=L8, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line9 = tk.Label(text='line9',textvariable=L9, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line10 = tk.Label(text='line10',textvariable=L10, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line11 = tk.Label(text='line11',textvariable=L11, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line12 = tk.Label(text='line12',textvariable=L12, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line13 = tk.Label(text='line13',textvariable=L13, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line14 = tk.Label(text='line14',textvariable=L14, font=("Tahoma",16),fg = 'orange', bg='black',width=32,anchor='w')
	line15 = tk.Label(text='line15',textvariable=L15, font=("Tahoma",16),fg = 'lightblue', bg='black',width=10,anchor='w')
	line16 = tk.Button(root, text='Reboot',bg='black',fg='red',font=("Tahoma",28), width=7,height=2,command=press_button3)
	line17 = tk.Label(text='line17',textvariable=L17, font=("Tahoma",16),fg = 'white', bg='black',width=32,anchor='w')
	line18 = tk.Button(root, text='Stop',bg='black',fg='red',font=("Tahoma",28), width=7,height=2,command=press_button3_2)
	line19 = tk.Label(text='line19',textvariable=L19, font=("Tahoma",16),fg = 'lightblue', bg='black',width=10,anchor='w')
	line20 = tk.Label(text='line20',textvariable=L20, font=("Tahoma",16),fg = 'lightblue', bg='black',width=10,anchor='w')



	
	line1.pack()
	line2.pack()
	line3.pack()
	line4.pack()
	line5.pack()
	line6.pack()
	line7.pack()
	line8.pack()
	line9.pack()
	line10.pack()
	line11.pack()
	line12.pack()
	line13.pack()
	line14.pack()
	line15.pack()
	line16.pack()
	line17.pack()
	line18.pack()
	line19.pack()
	line20.pack()


	w.create_window(245,108,window=line1)
	w.create_window(245,148,window=line2)
	w.create_window(245,188,window=line3)
	w.create_window(245,228,window=line4)
	w.create_window(245,268,window=line5)
	w.create_window(245,303,window=line6)
	w.create_window(245,338,window=line7)
	w.create_window(245,373,window=line8)
	w.create_window(245,408,window=line9)
	w.create_window(245,443,window=line10)
	w.create_window(245,478,window=line11)
	w.create_window(245,513,window=line12)
	w.create_window(245,548,window=line13)
	w.create_window(245,583,window=line14)
	w.create_window(105,633,window=line15)
	w.create_window(264,633,window=line19)
	w.create_window(423,633,window=line20)
	w.create_window(125,718,window=line16)
	w.create_window(245,60,window=line17)
	w.create_window(345,718,window=line18)
	
def ReadTemp():
	
	global cTemp
	global pressure
	global humidity
	global MysTemp
	global MysPress
	global MysHumid
	
	# Get I2C bus
	bus = smbus.SMBus(1)
	
	# BME280 address, 0x76(118)
	# Read data back from 0x88(136), 24 bytes
	b1 = bus.read_i2c_block_data(0x77, 0x88, 24)
	
	# Convert the data
	# Temp coefficients
	dig_T1 = b1[1] * 256 + b1[0]
	dig_T2 = b1[3] * 256 + b1[2]
	if dig_T2 > 32767 :
	    dig_T2 -= 65536
	dig_T3 = b1[5] * 256 + b1[4]
	if dig_T3 > 32767 :
	    dig_T3 -= 65536
	
	# Pressure coefficients
	dig_P1 = b1[7] * 256 + b1[6]
	dig_P2 = b1[9] * 256 + b1[8]
	if dig_P2 > 32767 :
	    dig_P2 -= 65536
	dig_P3 = b1[11] * 256 + b1[10]
	if dig_P3 > 32767 :
	    dig_P3 -= 65536
	dig_P4 = b1[13] * 256 + b1[12]
	if dig_P4 > 32767 :
	    dig_P4 -= 65536
	dig_P5 = b1[15] * 256 + b1[14]
	if dig_P5 > 32767 :
	    dig_P5 -= 65536
	dig_P6 = b1[17] * 256 + b1[16]
	if dig_P6 > 32767 :
	    dig_P6 -= 65536
	dig_P7 = b1[19] * 256 + b1[18]
	if dig_P7 > 32767 :
	    dig_P7 -= 65536
	dig_P8 = b1[21] * 256 + b1[20]
	if dig_P8 > 32767 :
	    dig_P8 -= 65536
	dig_P9 = b1[23] * 256 + b1[22]
	if dig_P9 > 32767 :
	    dig_P9 -= 65536
	
	# BME280 address, 0x76(118)
	# Read data back from 0xA1(161), 1 byte
	dig_H1 = bus.read_byte_data(0x77, 0xA1)
	
	# BME280 address, 0x76(118)
	# Read data back from 0xE1(225), 7 bytes
	b1 = bus.read_i2c_block_data(0x77, 0xE1, 7)
	
	# Convert the data
	# Humidity coefficients
	dig_H2 = b1[1] * 256 + b1[0]
	if dig_H2 > 32767 :
	    dig_H2 -= 65536
	dig_H3 = (b1[2] &  0xFF)
	dig_H4 = (b1[3] * 16) + (b1[4] & 0xF)
	if dig_H4 > 32767 :
	    dig_H4 -= 65536
	dig_H5 = (b1[4] / 16) + (b1[5] * 16)
	if dig_H5 > 32767 :
	    dig_H5 -= 65536
	dig_H6 = b1[6]
	if dig_H6 > 127 :
	    dig_H6 -= 256
	
	# BME280 address, 0x76(118)
	# Select control humidity register, 0xF2(242)
	#		0x01(01)	Humidity Oversampling = 1
	bus.write_byte_data(0x77, 0xF2, 0x01)
	# BME280 address, 0x76(118)
	# Select Control measurement register, 0xF4(244)
	#		0x27(39)	Pressure and Temperature Oversampling rate = 1
	#					Normal mode
	bus.write_byte_data(0x77, 0xF4, 0x27)
	# BME280 address, 0x76(118)
	# Select Configuration register, 0xF5(245)
	#		0xA0(00)	Stand_by time = 1000 ms
	bus.write_byte_data(0x77, 0xF5, 0xA0)
	
	time.sleep(0.5)
	
	# BME280 address, 0x76(118)
	# Read data back from 0xF7(247), 8 bytes
	# Pressure MSB, Pressure LSB, Pressure xLSB, Temperature MSB, Temperature LSB
	# Temperature xLSB, Humidity MSB, Humidity LSB
	data = bus.read_i2c_block_data(0x77 , 0xF7, 8)
	
	# Convert pressure and temperature data to 19-bits
	adc_p = ((data[0] * 65536) + (data[1] * 256) + (data[2] & 0xF0)) / 16
	adc_t = ((data[3] * 65536) + (data[4] * 256) + (data[5] & 0xF0)) / 16
	
	# Convert the humidity data
	adc_h = data[6] * 256 + data[7]
	
	# Temperature offset calculations
	var1 = ((adc_t) / 16384.0 - (dig_T1) / 1024.0) * (dig_T2)
	var2 = (((adc_t) / 131072.0 - (dig_T1) / 8192.0) * ((adc_t)/131072.0 - (dig_T1)/8192.0)) * (dig_T3)
	t_fine = (var1 + var2)
	cTemp = (var1 + var2) / 5120.0
	fTemp = cTemp * 1.8 + 32
	
	# Pressure offset calculations
	var1 = (t_fine / 2.0) - 64000.0
	var2 = var1 * var1 * (dig_P6) / 32768.0
	var2 = var2 + var1 * (dig_P5) * 2.0
	var2 = (var2 / 4.0) + ((dig_P4) * 65536.0)
	var1 = ((dig_P3) * var1 * var1 / 524288.0 + ( dig_P2) * var1) / 524288.0
	var1 = (1.0 + var1 / 32768.0) * (dig_P1)
	p = 1048576.0 - adc_p
	p = (p - (var2 / 4096.0)) * 6250.0 / var1
	var1 = (dig_P9) * p * p / 2147483648.0
	var2 = p * (dig_P8) / 32768.0
	pressure = (p + (var1 + var2 + (dig_P7)) / 16.0) / 100
	
	# Humidity offset calculations
	var_H = ((t_fine) - 76800.0)
	var_H = (adc_h - (dig_H4 * 64.0 + dig_H5 / 16384.0 * var_H)) * (dig_H2 / 65536.0 * (1.0 + dig_H6 / 67108864.0 * var_H * (1.0 + dig_H3 / 67108864.0 * var_H)))
	humidity = var_H * (1.0 -  dig_H1 * var_H / 524288.0)
	if humidity > 100.0 :
	    humidity = 100.0
	elif humidity < 0.0 :
	    humidity = 0.0
	
	## Output data to screen
	MysTemp = ("%.2f" %cTemp)
	cTemp =  ("Temperature : %.2f C" %cTemp)
	MysPress = ("%.2f" %pressure)
	#print "Temperature in Fahrenheit : %.2f F" %fTemp
	pressure = ("Pressure : %.2f hPa " %pressure)
	MysHumid = ("%.2f" %humidity)
	humidity = ("Relative Humidity : %.2f %%" %humidity)
	
	
global chkButton
global i
global Mysloop2
Mysloop2 =0
i=0
chkButton = 0

def press_button():
	global i
	print ('Button Press')
	os.remove(cardResetPlug)
	os.remove(cardResetAir)
	os.remove(cardResetLight)
	print ('Delete File')
	with open(cardResetPlug,'w') as f:
		f.close() 
	with open(cardResetAir,'w') as f:
		f.close() 
	with open(cardResetLight,'w') as f:
		f.close() 
	i=-1
	
def press_button2():
	global Mysloop2
	print ('Button2 Press')
	Mysloop2 = 1
	w.destroy()
	
def press_button3():
	print ('Button3 Press')
	w.destroy()
	root.destroy()
	os.system('reboot')
	
def press_button3_2():
	print ('Button3 Press')
	w.destroy()
	root.withdraw()
	#root.destroy()
	#os.system('sudo shutdown now')
	
def SetTime():
	os.system('hwclock -s -f /dev/rtc1')
	os.system('hwclock -w')
Mysdate2=0

homeID = "M0003"
cardOn = "/media/CARD/On.txt"
cardPlug = "/media/CARD/Plug.txt"
cardAir = "/media/CARD/Air.txt"
cardLight = "/media/CARD/Light.txt"
cardResetPlug = "/media/CARD/ResetPlug.txt"
cardResetAir = "/media/CARD/ResetAir.txt"
cardResetLight = "/media/CARD/ResetLight.txt"
MysDevices = 0
MysDevicesA = 0
MysDevicesL = 0
MysID=[[] for x in xrange(70)]
MysIDA=[[]*3 for x in xrange(70)]
MysIDL=[[] for x in xrange(70)]
Display=[[] for x in xrange(70)]
i=0
j=0
k=0


def AskReset():
	global page
	global MysDevices  # Plug
	global MysDevicesA  # Air
	global MysDevicesL  # Air
	global homeID
	global MysID   # Plug
	global MysIDA # Air
	global MysIDL # Air
	global Display
	global i
	global j
	global k
	global root
	global w
	global Mysloop2
	global cTemp
	global pressure
	global humidity
	global MysTemp
	global MysPress
	global MysHumid
	global Mysdate2
	global Mysdate
	
	
	
	main_start1(1)
	show_data(1)
	#root.update()
	
	while True:
		
		Mysdate = int(strftime("%d",gmtime()))
		if Mysdate != Mysdate2:
			SetTime()
			Mysdate2 = Mysdate
			print ('Time has been set')
			
		print 'Reset'
		hour = strftime("%H",gmtime())
		hour = str((int(hour)+7)%24)
	
		i = 8
		while i>0:

			print (strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+'	Count Down ='+str(i))
			
			L3.set('Reset Members Press "Reset"')
			L4.set('Count Down = '+str(i))
			L6.set(cTemp)
			L7.set(pressure)
			L8.set(humidity)
			L1.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime()))
			#main_start1(1)
			root.update()
			i=i-1  
			print i
			time.sleep(1)                                                                                                                                                                                                                                             
			
		clear_data(1)
		break
		
	if i!=-2:
		
		print 'Read Card'
		with open(cardResetPlug,'r') as f:
				members2 = f.read()
				members = members2.split('\n')
				MysDevices = len(members)-1		
				i = 0
				while i<MysDevices:
					content = members[i].split('+')
					MysID[i] = content[0]
					i=i+1
				a=[[] for x in xrange(MysDevices)]
				a[0:MysDevices] = MysID[0:MysDevices]
				a = list(set(a))
				MysDevices = len(a)
				MysID=[[] for x in xrange(70)]
				print MysID
				MysID[0:MysDevices]= a[0:MysDevices]
				print ('MysDevices = '+str(MysDevices))
				
				MysID = sorted(MysID, reverse=True)
				
				os.remove(cardResetPlug)
				with open(cardResetPlug,'w') as f:
					f.close()
				i=0
				while i< MysDevices:
					
					file = open(cardResetPlug,"a")
					file.write(MysID[i]+'+ON\n')
					file.close()
					i=i+1
				
					
		with open(cardResetAir,'r') as f:
				members2 = f.read()
				members = members2.split('\n')
				MysDevicesA = len(members)-1
				
				a=[[] for x in xrange(MysDevicesA)]
				a[0:MysDevicesA] = members[0:MysDevicesA]
				a = list(set(a))
				members = a
				MysDevicesA = len(members)
				
				members = sorted(members, reverse=True)
				
				os.remove(cardResetAir)
				with open(cardResetAir,'w') as f:
					f.close()
				i=0
				while i< MysDevicesA:
					
					file = open(cardResetAir,"a")
					file.write(members[i]+'\n')
					file.close()
					i=i+1
					
				i = 0
				while i<MysDevicesA:
					content = members[i].split('+')
					MysIDA[i] = [content[0],content[1],content[1]]
					i=i+1
				print ('MysDevicesA = '+str(MysDevicesA))

				#MysIDA = sorted(MysIDA, reverse=True)
				
		with open(cardResetLight,'r') as f:
				members2 = f.read()
				members = members2.split('\n')
				MysDevicesL = len(members)-1
				
				i = 0
				while i<MysDevicesL:
					content = members[i].split('+')
					MysIDL[i] = content[0]
					i=i+1
				a=[[] for x in xrange(MysDevicesL)]
				a[0:MysDevicesL] = MysIDL[0:MysDevicesL]
				a = list(set(a))
				MysDevicesL = len(a)
				MysIDL=[[] for x in xrange(70)]
				MysIDL[0:MysDevicesL] = a[:]
				
				print ('MysDevicesL = '+str(MysDevicesL))
				
				MysIDL = sorted(MysIDL, reverse=True)
				
				os.remove(cardResetLight)
				with open(cardResetLight,'w') as f:
					f.close()
				i=0
				while i< MysDevicesL:
					
					file = open(cardResetLight,"a")
					file.write(MysIDL[i]+'+ON\n')
					file.close()
					i=i+1

		#print MysID	
		#print MysIDA	
		#print MysIDL		
		#MysID = list(set(MysID))
		#MysIDA = list(set(MysIDA))
		#MysIDL = list(set(MysIDL))	
		#seen = set()
		#uniq = []
		#for x in MysID:
			#if x not in seen:
				#uniq.append(x)
				#seen.add(x)
		#MysID = uniq
		
		#seen = set()
		#uniq = []
		#for x in MysIDA:
			#if x not in seen:
				#uniq.append(x)
				#seen.add(x)
		#MysIDA = uniq
		
		#seen = set()
		#uniq = []
		#for x in MysIDL:
			#if x not in seen:
				#uniq.append(x)
				#seen.add(x)
		#MysIDL = uniq
		
	
	w = Canvas(root, width=canvas_width, height=canvas_height,bg='black')
	canvas = w.create_image(0, 0,anchor=NW,image=my_images[0])
	w.pack()	
	main_start1(1)
	show_data2(1)


	while Mysloop2 == 0:
		
		print 'Register'
		zigbee = ser4.readline()
		message = zigbee.split('+')
		length_message = len(message)
		hour = strftime("%H",gmtime())
		hour = str((int(hour)+7)%24) 
		
		
		if len(zigbee) == 0:
			             
			print (strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+'	No Serial')
			
			for i in xrange(len(Display)):
				Display[i] = ''
			
			i = 0
			if MysDevices>0:
				while i<MysDevices:
					Display[i] = str(MysID[MysDevices-1-i])
					i=i+1
				i0 = i%5
				if i0 != 0:
					i = i+(5-i0)
			j = 0
			if MysDevicesA>0:
	
				while j<MysDevicesA:
					Display[i+j]=str(MysIDA[MysDevicesA-1-j][0])
					j=j+1
			k = i+j
			k0 = k%5
			if k0 != 0:
				k = k+(5-k0)
			
			j = 0
			if MysDevicesL>0:
				while j<MysDevicesL:
					Display[k+j]=str(MysIDL[MysDevicesL-1-j])
					j=j+1
			
			L1.set('')
			L2.set('')
			L3.set('')
			L4.set('Register Members of '+homeID)
			L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
			L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
			L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
			L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
			L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
			L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
			L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
			L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
			L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
			L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
			L15.set('A = '+str(MysDevicesA))
			L19.set('P = '+str(MysDevices))
			L20.set('L = '+str(MysDevicesL))
			L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
					
			root.update()
 
			
		else:
			print zigbee
			message = zigbee.split('+')
			length_message = len(message)		

			
			if length_message == 2:  #Reset Plug & Lighting
				
				if message[1] == 'ON\n' and len(message[0])==5: 

					#ser4.write(message[0]+'\n')  # confirm recieve
					file = open(cardOn,"a")
					file.write(strftime("%d %b %Y",gmtime())+","+hour+strftime(":%M:%S",gmtime())+",")
					file.write(zigbee)
					file.close()
	
					L1.set(message[0]+'+'+message[1])
					L2.set('')
					L3.set('')
					L4.set('Register Members of '+homeID)
					L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
					L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
					L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
					L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
					L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
					L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
					L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
					L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
					L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
					L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
					L15.set('A = '+str(MysDevicesA))
					L19.set('P = '+str(MysDevices))
					L20.set('L = '+str(MysDevicesL))
					L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
	
					root.update()
					
					if zigbee[0] == 'P':   #Plug  Finish
					
						MysID[MysDevices] = message[0]
						MysDevices=MysDevices+1
									
						a=[[] for x in xrange(MysDevices)]
						a[0:MysDevices] = MysID[0:MysDevices]
						a = list(set(a))
						if len(a) == MysDevices:
							
							file = open(cardResetPlug,"a")
							file.write(zigbee)
							file.close()
							MysID = sorted(MysID, reverse=True)
						else:
							MysDevices=MysDevices-1
							
					if zigbee[0] == 'A':   #Air V.Plug
					
						MysID[MysDevices] = message[0]
						MysDevices=MysDevices+1
									
						a=[[] for x in xrange(MysDevices)]
						a[0:MysDevices] = MysID[0:MysDevices]
						a = list(set(a))
						if len(a) == MysDevices:
							
							file = open(cardResetPlug,"a")
							file.write(zigbee)
							file.close()
							MysID = sorted(MysID, reverse=True)
						else:
							MysDevices=MysDevices-1
							
					if zigbee[0] == 'L':   #Light
					
						MysIDL[MysDevicesL] = message[0]
						MysDevicesL=MysDevicesL+1
									
						a=[[] for x in xrange(MysDevicesL)]
						a[0:MysDevicesL] = MysIDL[0:MysDevicesL]
						a = list(set(a))
						if len(a) == MysDevicesL:
							
							file = open(cardResetLight,"a")
							file.write(zigbee)
							file.close()
							MysIDL = sorted(MysIDL, reverse=True)
						else:
							MysDevicesL=MysDevicesL-1
									

					
			elif length_message == 3:  #Reset Air & Home
				
				if message[2] == 'A\n' and len(message[0])==5: 
				
					file = open(cardOn,"a")
					file.write(strftime("%d %b %Y",gmtime())+","+hour+strftime(":%M:%S",gmtime())+",")
					file.write(zigbee)
					file.close()

					L1.set('')
					L2.set(message[0]+'+ON\n')
					if message[1] == '1':
						L3.set('Switch status = ON')
					if message[1] == '0':
						L3.set('Switch status = OFF')
					L4.set('Register Members of '+homeID)
					L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
					L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
					L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
					L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
					L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
					L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
					L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
					L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
					L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
					L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
					L15.set('A = '+str(MysDevicesA))
					L19.set('P = '+str(MysDevices))
					L20.set('L = '+str(MysDevicesL))
					L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
					
					root.update()
					
					if MysDevicesA>0:  #Check duplicate
						i =0
						b =0
						while i<MysDevicesA:
							if MysIDA[i][0]==message[0]:
								i=i+1
								b=1
								break
							else:
								i=i+1
								
						if b ==0:
								MysIDA[MysDevicesA] = [message[0],message[1],'1']
								MysDevicesA=MysDevicesA+1
								file = open(cardResetAir,"a")
								file.write(zigbee)
								file.close()
								MysIDA= sorted(MysIDA, reverse=True)
					else:
						MysIDA[MysDevicesA] = [message[0],message[1],'1']
						MysDevicesA=MysDevicesA+1
						file = open(cardResetAir,"a")
						file.write(zigbee)
						file.close()
						MysIDA = sorted(MysIDA, reverse=True)
						
	print ("Start loop3")
	w = Canvas(root, width=canvas_width, height=canvas_height,bg='black')
	canvas = w.create_image(0, 0,anchor=NW,image=my_images[0])
	w.pack()	
	main_start1(1)
	show_data3(1)
	root.update()
	callPlug=0
	callAir=0
	
	for i in xrange(len(Display)):
		Display[i] = ''
		
	i = 0
	if MysDevices>0:
		while i<MysDevices:
			Display[i] = str(MysID[MysDevices-1-i])
			i=i+1
		i0 = i%5
		if i0 != 0:
			i = i+(5-i0)
	j = 0
	if MysDevicesA>0:

		while j<MysDevicesA:
			Display[i+j]=str(MysIDA[MysDevicesA-1-j][0])
			j=j+1
	k = i+j
	k0 = k%5
	if k0 != 0:
		k = k+(5-k0)
	
	j = 0
	if MysDevicesL>0:
		while j<MysDevicesL:
			Display[k+j]=str(MysIDL[MysDevicesL-1-j])
			j=j+1
	
	while True:  # Call Members
	
		Mysdate = int(strftime("%d",gmtime()))
		if Mysdate != Mysdate2:
			SetTime()
			Mysdate2 = Mysdate
			print ('Time has been set')
			
		zigbee = ser4.readline()
		hour = strftime("%H",gmtime())
		hour = str((int(hour)+7)%24)	
		
					
		if len(zigbee) == 0:
			             
			print (strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+'	No Serial')
			
			#L1.set('')
			#L2.set('')
			#L3.set('')
			L4.set('Register Members of '+homeID)
			L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
			L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
			L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
			L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
			L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
			L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
			L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
			L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
			L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
			L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
			L15.set('A = '+str(MysDevicesA))
			L19.set('P = '+str(MysDevices))
			L20.set('L = '+str(MysDevicesL))
			L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
			
			root.update()
			
			#print callPlug
			#print callAir
			
			if callPlug< MysDevices:
				print (MysID[MysDevices-1-callPlug]+'\n')
				ser4.write(MysID[MysDevices-1-callPlug]+'\n')
				callPlug = callPlug+1
				time.sleep(1)
			elif callAir<MysDevicesA:
				print (MysIDA[MysDevicesA-1-callAir][0]+'+'+MysIDA[MysDevicesA-1-callAir][2]+'\n')
				#ser4.write(MysIDA[MysDevicesA-1-callAir][0]+'+'+MysIDA[MysDevicesA-1-callAir][2]+'\n')
				ser4.write(MysIDA[MysDevicesA-1-callAir][0]+'+2\n')
				callAir = callAir+1
				time.sleep(1)
			else:
				ReadTemp()
				callAir=0
				callPlug = 0
			
			
		else:
			print zigbee
			message = zigbee.split('+')
			length_message = len(message)		

			
			if length_message == 2:  #Reset Plug & Lighting
				
				if message[1] == 'ON\n' and len(message[0])==5: 
					
					file = open(cardOn,"a")
					file.write(strftime("%d %b %Y",gmtime())+","+hour+strftime(":%M:%S",gmtime())+",")
					file.write(zigbee)
					file.close()

					L1.set(message[0]+'+'+message[1])
					L2.set('')
					L3.set('')
					L4.set('Register Members of '+homeID)
					L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
					L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
					L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
					L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
					L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
					L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
					L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
					L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
					L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
					L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
					L15.set('A = '+str(MysDevicesA))
					L19.set('P = '+str(MysDevices))
					L20.set('L = '+str(MysDevicesL))
					L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
	
					root.update()
					
					if zigbee[0] == 'P':   #Plug
					
						MysID[MysDevices] = message[0]
						MysDevices=MysDevices+1
									
						a=[[] for x in xrange(MysDevices)]
						a[0:MysDevices] = MysID[0:MysDevices]
						a = list(set(a))
						if len(a) == MysDevices:
							
							file = open(cardResetPlug,"a")
							file.write(zigbee)
							file.close()
							MysID = sorted(MysID, reverse=True)
						else:
							MysDevices=MysDevices-1
	
							
					if zigbee[0] == 'A':   #Air V Plug
					
						MysID[MysDevices] = message[0]
						MysDevices=MysDevices+1
									
						a=[[] for x in xrange(MysDevices)]
						a[0:MysDevices] = MysID[0:MysDevices]
						a = list(set(a))
						if len(a) == MysDevices:
							
							file = open(cardResetPlug,"a")
							file.write(zigbee)
							file.close()
							MysID = sorted(MysID, reverse=True)
						else:
							MysDevices=MysDevices-1

									
					if zigbee[0] == 'L':   #Light
					
						MysIDL[MysDevicesL] = message[0]
						MysDevicesL=MysDevicesL+1
									
						a=[[] for x in xrange(MysDevicesL)]
						a[0:MysDevicesL] = MysIDL[0:MysDevicesL]
						a = list(set(a))
						if len(a) == MysDevicesL:
							
							file = open(cardResetLight,"a")
							file.write(zigbee)
							file.close()
							MysIDL = sorted(MysIDL, reverse=True)
						else:
							MysDevicesL=MysDevicesL-1
				
				for i in xrange(len(Display)):
					Display[i] = ''	
							
				i = 0
				if MysDevices>0:
					while i<MysDevices:
						Display[i] = str(MysID[MysDevices-1-i])
						i=i+1
					i0 = i%5
					if i0 != 0:
						i = i+(5-i0)
				j = 0
				if MysDevicesA>0:
		
					while j<MysDevicesA:
						Display[i+j]=str(MysIDA[MysDevicesA-1-j][0])
						j=j+1
				k = i+j
				k0 = k%5
				if k0 != 0:
					k = k+(5-k0)
				
				j = 0
				if MysDevicesL>0:
					while j<MysDevicesL:
						Display[k+j]=str(MysIDL[MysDevicesL-1-j])
						j=j+1
	
								
					
			elif length_message == 3:  #Reset Air & Home
				
				if message[2] == 'A\n' and len(message[0])==5: 

					file = open(cardOn,"a")
					file.write(strftime("%d %b %Y",gmtime())+","+hour+strftime(":%M:%S",gmtime())+",")
					file.write(zigbee)
					file.close()
					
					L1.set('')
					L2.set(message[0]+'+ON\n')
					if message[1] == '1':
						L3.set('Switch status = ON')
					if message[1] == '0':
						L3.set('Switch status = OFF')
					
					L4.set('Register Members of '+homeID)
					L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
					L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
					L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
					L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
					L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
					L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
					L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
					L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
					L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
					L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
					L15.set('A = '+str(MysDevicesA))
					L19.set('P = '+str(MysDevices))
					L20.set('L = '+str(MysDevicesL))
					L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
					
					root.update()
					
					if MysDevicesA>0:  #Check duplicate
						i =0
						b =0
						while i<MysDevicesA:
							if MysIDA[i][0]==message[0]:
								i=i+1
								b=1
								break
							else:
								i=i+1
								
						if b ==0:
								MysIDA[MysDevicesA] = [message[0],message[1],'1']
								MysDevicesA=MysDevicesA+1
								file = open(cardResetAir,"a")
								file.write(zigbee)
								file.close()
								MysIDA = sorted(MysIDA, reverse=True)

					else:
						MysIDA[MysDevicesA] = [message[0],message[1],'1']
						MysDevicesA=MysDevicesA+1
						file = open(cardResetAir,"a")
						file.write(zigbee)
						file.close()
						MysIDA = sorted(MysIDA, reverse=True)
				
				for i in xrange(len(Display)):
					Display[i] = ''		
					
				i = 0
				if MysDevices>0:
					while i<MysDevices:
						Display[i] = str(MysID[MysDevices-1-i])
						i=i+1
					i0 = i%5
					if i0 != 0:
						i = i+(5-i0)
				j = 0
				if MysDevicesA>0:
		
					while j<MysDevicesA:
						Display[i+j]=str(MysIDA[MysDevicesA-1-j][0])
						j=j+1
				k = i+j
				k0 = k%5
				if k0 != 0:
					k = k+(5-k0)
				
				j = 0
				if MysDevicesL>0:
					while j<MysDevicesL:
						Display[k+j]=str(MysIDL[MysDevicesL-1-j])
						j=j+1

				
			elif length_message == 22:  #Light
			
				if message[21] == 'L\n':
					
					file = open(cardLight,"a")
					file.write(strftime("%d %b %Y,",gmtime())+hour+strftime(":%M:%S,",gmtime()))
					file.write(zigbee)
					file.close()
					
					L1.set(message[0]+'+'+message[1]+'+'+message[2]+'+'+message[3]+'+'+message[4]+'+'+message[5]+'+'+message[6])
					L2.set(message[7]+'+'+message[8]+'+'+message[9]+'+'+message[10]+'+'+message[11]+'+'+message[12]+'+'+message[13])
					L3.set(message[14]+'+'+message[15]+'+'+message[16]+'+'+message[17]+'+'+message[18]+'+'+message[19]+'+'+message[20])
					L4.set('Register Members of '+homeID)
					L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
					L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
					L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
					L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
					L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
					L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
					L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
					L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
					L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
					L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
					L15.set('A = '+str(MysDevicesA))
					L19.set('P = '+str(MysDevices))
					L20.set('L = '+str(MysDevicesL))
					L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
					
					root.update()
                               
			
			elif length_message == 10: # Plug
			
				if message[9] == 'P\n':

					file = open(cardPlug,"a")
					file.write(strftime("%d %b %Y",gmtime())+","+hour+strftime(":%M:%S",gmtime())+",")
					file.write(zigbee)
					file.close()

					L1.set(message[0])
					L2.set('V='+zigbee[6]+zigbee[7]+zigbee[8]+zigbee[9]+'.'+zigbee[10]+zigbee[11]+'  I='+zigbee[13]+zigbee[14]+zigbee[15]+'.'+zigbee[16]+zigbee[17]+zigbee[18]+'  E='+message[8])
					L3.set('')
					L4.set('Register Members of '+homeID)
					L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
					L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
					L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
					L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
					L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
					L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
					L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
					L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
					L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
					L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
					L15.set('A = '+str(MysDevicesA))
					L19.set('P = '+str(MysDevices))
					L20.set('L = '+str(MysDevicesL))
					L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
					
					root.update()
							
				#if message[9] == 'A\n':

					#file = open(cardAir,"a")
					#file.write(strftime("%d %b %Y",gmtime())+"	"+hour+strftime(":%M:%S",gmtime())+"	")
					#file.write(zigbee)
					#file.close()

					#L1.set(message[0])
					#L2.set('V='+zigbee[6]+zigbee[7]+zigbee[8]+zigbee[9]+'.'+zigbee[10]+zigbee[11]+'  I='+zigbee[13]+zigbee[14]+zigbee[15]+'.'+zigbee[16]+zigbee[17]+zigbee[18]+'  E='+message[8])
					#L3.set('Switch = '+message[9])
					#L4.set('Register Members of '+homeID)
					#L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
					#L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
					#L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
					#L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
					#L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
					#L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
					#L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
					#L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
					#L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
					#L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
					#L15.set('A = '+str(MysDevicesA))
					#L19.set('P = '+str(MysDevices))
					#L20.set('L = '+str(MysDevicesL))
					#L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
					
					#root.update()
					
			elif length_message == 7: # Air message 2
			
				if message[6] == 'A\n':

					file = open(cardAir,"a")
					file.write(strftime("%d %b %Y",gmtime())+","+hour+strftime(":%M:%S",gmtime())+",")
					file.write(zigbee)
					file.close()

					messageAir = (message[1]+'+'+message[2]+'+'+message[3]+'+'+message[4]+'+'+message[5]+'\n')
					
					L1.set(message[0])
					L2.set('')
					if message[1] == '1':
						L3.set('Switch = ON   '+message[2]+'C'+'   '+message[5]+'%')
					if message[1] == '0':
						L3.set('Switch = OFF   '+message[2]+'C'+'   '+message[5]+'%')
					
					length_message = 0
					ckairloop = 0
					
					while length_message!= 10 and ckairloop<15:
						
						ser4.write(MysIDA[MysDevicesA-callAir][0]+'+'+MysIDA[MysDevicesA-callAir][2]+'\n')
						zigbee = ser4.readline()
						print zigbee
						message = zigbee.split('+')
						length_message = len(message)
						ckairloop =ckairloop+1
						
						if length_message == 22:  #Light
			
							if message[21] == 'L\n':
								
								file = open(cardLight,"a")
								file.write(strftime("%d %b %Y,",gmtime())+hour+strftime(":%M:%S,",gmtime()))
								file.write(zigbee)
								file.close()
								#print zigbee[0]
								#name = str(zigbee[1]+zigbee[2]+zigbee[3]+zigbee[4]+zigbee[5])
								
								L1.set(message[0]+'+'+message[1]+'+'+message[2]+'+'+message[3]+'+'+message[4]+'+'+message[5]+'+'+message[6])
								L2.set(message[7]+'+'+message[8]+'+'+message[9]+'+'+message[10]+'+'+message[11]+'+'+message[12]+'+'+message[13])
								L3.set(message[14]+'+'+message[15]+'+'+message[16]+'+'+message[17]+'+'+message[18]+'+'+message[19]+'+'+message[20])
								L4.set('Register Members of '+homeID)
								L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
								L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
								L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
								L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
								L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
								L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
								L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
								L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
								L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
								L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
								L15.set('A = '+str(MysDevicesA))
								L19.set('P = '+str(MysDevices))
								L20.set('L = '+str(MysDevicesL))
								L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
								
								root.update()
								
						elif length_message == 2:  #Reset Plug & Lighting
				
							if message[1] == 'ON\n' and len(message[0])==5: 
								
								file = open(cardOn,"a")
								file.write(strftime("%d %b %Y",gmtime())+","+hour+strftime(":%M:%S",gmtime())+",")
								file.write(zigbee)
								file.close()
			
								L1.set(message[0]+'+'+message[1])
								L2.set('')
								L3.set('')
								L4.set('Register Members of '+homeID)
								L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
								L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
								L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
								L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
								L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
								L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
								L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
								L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
								L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
								L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
								L15.set('A = '+str(MysDevicesA))
								L19.set('P = '+str(MysDevices))
								L20.set('L = '+str(MysDevicesL))
								L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
				
								root.update()
								
								if zigbee[0] == 'P':   #Plug
								
									MysID[MysDevices] = message[0]
									MysDevices=MysDevices+1
												
									a=[[] for x in xrange(MysDevices-1)]
									a[0:MysDevices] = MysID[0:MysDevices]
									a = list(set(a))
									if len(a) == MysDevices:
										
										file = open(cardResetPlug,"a")
										file.write(zigbee)
										file.close()
										MysID = sorted(MysID, reverse=True)
									else:
										MysDevices=MysDevices-1
				
										
								if zigbee[0] == 'A':   #Air V Plug
								
									MysID[MysDevices] = message[0]
									MysDevices=MysDevices+1
												
									a=[[] for x in xrange(MysDevices-1)]
									a[0:MysDevices] = MysID[0:MysDevices]
									a = list(set(a))
									if len(a) == MysDevices:
										
										file = open(cardResetPlug,"a")
										file.write(zigbee)
										file.close()
										MysID = sorted(MysID, reverse=True)
									else:
										MysDevices=MysDevices-1
			
												
								if zigbee[0] == 'L':   #Light
								
									MysIDL[MysDevicesL] = message[0]
									MysDevicesL=MysDevicesL+1
												
									a=[[] for x in xrange(MysDevicesL-1)]
									a[0:MysDevicesL] = MysIDL[0:MysDevicesL]
									a = list(set(a))
									if len(a) == MysDevicesL:
										
										file = open(cardResetLight,"a")
										file.write(zigbee)
										file.close()
										MysIDL = sorted(MysIDL, reverse=True)
									else:
										MysDevicesL=MysDevicesL-1
										
								zigbee = ser4.readline()
								print zigbee
								message = zigbee.split('+')
								length_message = len(message)
										
										
							for i in xrange(len(Display)):
								Display[i] = ''
										
							i = 0
							if MysDevices>0:
								while i<MysDevices:
									Display[i] = str(MysID[MysDevices-1-i])
									i=i+1
								i0 = i%5
								if i0 != 0:
									i = i+(5-i0)
							j = 0
							if MysDevicesA>0:
					
								while j<MysDevicesA:
									Display[i+j]=str(MysIDA[MysDevicesA-1-j][0])
									j=j+1
							k = i+j
							k0 = k%5
							if k0 != 0:
								k = k+(5-k0)
							
							j = 0
							if MysDevicesL>0:
								while j<MysDevicesL:
									Display[k+j]=str(MysIDL[MysDevicesL-1-j])
									j=j+1
												
								
						elif length_message == 3:  #Reset Air & Home
							
							if message[2] == 'A\n' and len(message[0])==5: 
							
								#ser4.write(message[0]+'\n')  # confirm recieve
			
								file = open(cardOn,"a")
								file.write(strftime("%d %b %Y",gmtime())+","+hour+strftime(":%M:%S",gmtime())+",")
								file.write(zigbee)
								file.close()
								
								L1.set('')
								L2.set(message[0]+'+ON\n')
								if message[1] == '1':
									L3.set('Switch status = ON')
								if message[1] == '0':
									L3.set('Switch status = OFF')
								L4.set('Register Members of '+homeID)
								L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
								L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
								L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
								L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
								L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
								L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
								L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
								L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
								L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
								L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
								L15.set('A = '+str(MysDevicesA))
								L19.set('P = '+str(MysDevices))
								L20.set('L = '+str(MysDevicesL))
								L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
								
								root.update()
								
								if MysDevicesA>0:  #Check duplicate
									i =0
									b =0
									while i<MysDevicesA:
										if MysIDA[i][0]==message[0]:
											i=i+1
											b=1
											break
										else:
											i=i+1
											
									if b ==0:
											MysIDA[MysDevicesA] = [message[0],message[1],'1']
											MysDevicesA=MysDevicesA+1
											file = open(cardResetAir,"a")
											file.write(zigbee)
											file.close()
											MysIDA = sorted(MysIDA, reverse=True)
											
								else:
									MysIDA[MysDevicesA] = [message[0],message[1],'1']
									MysDevicesA=MysDevicesA+1
									file = open(cardResetAir,"a")
									file.write(zigbee)
									file.close()
									MysIDA = sorted(MysIDA, reverse=True)
									
								zigbee = ser4.readline()
								print zigbee
								message = zigbee.split('+')
								length_message = len(message)

							
							for i in xrange(len(Display)):
								Display[i] = ''
									
							i = 0
							if MysDevices>0:
								while i<MysDevices:
									Display[i] = str(MysID[MysDevices-1-i])
									i=i+1
								i0 = i%5
								if i0 != 0:
									i = i+(5-i0)
							j = 0
							if MysDevicesA>0:
					
								while j<MysDevicesA:
									Display[i+j]=str(MysIDA[MysDevicesA-1-j][0])
									j=j+1
							k = i+j
							k0 = k%5
							if k0 != 0:
								k = k+(5-k0)
							
							j = 0
							if MysDevicesL>0:
								while j<MysDevicesL:
									Display[k+j]=str(MysIDL[MysDevicesL-1-j])
									j=j+1
					
					if length_message == 10: # Air message 2
						if message[9] == 'A\n':
							
							file = open(cardAir,"a")
							file.write(strftime("%d %b %Y",gmtime())+","+hour+strftime(":%M:%S",gmtime())+",")
							file.write(zigbee)
							file.close()
			
							L2.set('V='+zigbee[6]+zigbee[7]+zigbee[8]+zigbee[9]+'.'+zigbee[10]+zigbee[11]+'  I='+zigbee[13]+zigbee[14]+zigbee[15]+'.'+zigbee[16]+zigbee[17]+zigbee[18]+'  E='+message[8])
					
						L4.set('Register Members of '+homeID)
						L5.set(Display[0]+'  '+Display[1]+'  '+Display[2]+'  '+Display[3]+'  '+Display[4])
						L6.set(Display[5]+'  '+Display[6]+'  '+Display[7]+'  '+Display[8]+'  '+Display[9])
						L7.set(Display[10]+'  '+Display[11]+'  '+Display[12]+'  '+Display[13]+'  '+Display[14])
						L8.set(Display[15]+'  '+Display[16]+'  '+Display[17]+'  '+Display[18]+'  '+Display[19])
						L9.set(Display[20]+'  '+Display[21]+'  '+Display[22]+'  '+Display[23]+'  '+Display[24])
						L10.set(Display[25]+'  '+Display[26]+'  '+Display[27]+'  '+Display[28]+'  '+Display[29])
						L11.set(Display[30]+'  '+Display[31]+'  '+Display[32]+'  '+Display[33]+'  '+Display[34])
						L12.set(Display[35]+'  '+Display[36]+'  '+Display[37]+'  '+Display[38]+'  '+Display[39])
						L13.set(Display[40]+'  '+Display[41]+'  '+Display[42]+'  '+Display[43]+'  '+Display[44])
						L14.set(Display[45]+'  '+Display[46]+'  '+Display[47]+'  '+Display[48]+'  '+Display[49])
						L15.set('A = '+str(MysDevicesA))
						L19.set('P = '+str(MysDevices))
						L20.set('L = '+str(MysDevicesL))
						L17.set(strftime("%d %b %Y",gmtime())+"  "+hour+strftime(":%M:%S",gmtime())+"  Temp = "+str(MysTemp)+"C")
						
						root.update()
					
					#messageAir = (message[0]+'+'+message[1]+'+'+message[2]+'+'+message[3]+'+'+message[4]+'+'+message[5]+'+'+message[6]+'+'+message[7]+'+'+message[8]+'+'+messageAir)
					#print messageAir
			
				
root.bind('<Escape>',close)	
ReadTemp()
AskReset()	
    			

