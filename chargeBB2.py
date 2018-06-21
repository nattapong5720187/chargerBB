#Mys_Separate display
#Mys_Don't have Button and ZigBee

from Tkinter import *
from PIL import Image, ImageTk
import Adafruit_BBIO.UART as UART
import serial
import time 
from time import sleep
import Adafruit_BBIO.GPIO as GPIO
import Tkinter as tk
import os

#GPIO.setup("P8_8",GPIO.IN)


UART.setup("UART2")
#UART.setup("UART4")

root=tk.Tk()



varEnergy = StringVar()
varCurrent = StringVar()


varCard_id = StringVar()
varCard_type = StringVar()
varMoney = StringVar()
varText = StringVar()
varMysEnergy = StringVar()


enable=False

root.title("My Image ")

data = {}
data_show = {}

energy=0

## windown size
canvas_width = 480
canvas_height = 800
touch=0
w = Canvas(root, width=canvas_width, height=canvas_height)

## Path Image ##
ev_main_start   = Image.open("/home/debian/geany_bbb/ev_pic/ev_main_start.jpg")
ev_card   = Image.open("/home/debian/geany_bbb/ev_pic/ev_card22.jpg")
ev_start = Image.open("/home/debian/geany_bbb/ev_pic/ev_btn_start.jpg")
ev_insert_wire = Image.open("/home/debian/geany_bbb/ev_pic/ev_insert_wire0.jpg")
ev_charge0  = Image.open("/home/debian/geany_bbb/ev_pic/ev_charge00.jpg")
ev_charge1  = Image.open("/home/debian/geany_bbb/ev_pic/ev_charge11.jpg")
ev_main_stop = Image.open("/home/debian/geany_bbb/ev_pic/ev_main_stop.jpg")
ev_stop = Image.open("/home/debian/geany_bbb/ev_pic/ev_btn_stop.jpg")
ev_remove_wire = Image.open("/home/debian/geany_bbb/ev_pic/ev_remove_wire0.jpg")
ev_lnvalid = Image.open("/home/debian/geany_bbb/ev_pic/ev_Invalid.jpg")
#ev_bg   = Image.open("/home/debian/geany_bbb/ev_pic/version1/ev_bg.jpg")

## ImageTk Library
photo_main_start = ImageTk.PhotoImage(ev_main_start)
photo_ev_card = ImageTk.PhotoImage(ev_card)
photo_ev_start = ImageTk.PhotoImage(ev_start)
photo_insert_wire = ImageTk.PhotoImage(ev_insert_wire)
photo_ev_charge0 = ImageTk.PhotoImage(ev_charge0)
photo_ev_charge1 = ImageTk.PhotoImage(ev_charge1)
photo_ev_main_stop = ImageTk.PhotoImage(ev_main_stop)
photo_ev_stop = ImageTk.PhotoImage(ev_stop)
photo_remove_wire = ImageTk.PhotoImage(ev_remove_wire)
photo_lnvalid = ImageTk.PhotoImage(ev_lnvalid)

## Add image to Array
my_images = []
my_images.append(photo_main_start)	  #Array 0
my_images.append(photo_ev_card)  	  #Array 1
my_images.append(photo_ev_start)  	  #Array 2
my_images.append(photo_insert_wire)   #Array 3
my_images.append(photo_ev_charge0)	  #Array 4
my_images.append(photo_ev_charge1)    #Array 5
my_images.append(photo_ev_main_stop)  #Array 6
my_images.append(photo_ev_stop)       #Array 7
my_images.append(photo_remove_wire)   #Array 8
my_images.append(photo_lnvalid)       #Array 9


ser = serial.Serial(port = "/dev/ttyO2", baudrate=115200, timeout=1)
#ser4 = serial.Serial(port = "/dev/ttyO4", baudrate=9600, timeout=1)
rand=1
switch=0
show=0
Mys = 0
MysCK = 0
MysCkWire = 0
MysInsert = 0
MysStartPrice = 300
MysCardid = "Mys"
MysText = "Employee"
Mystype = "Prepaid"
MysCkStop = 0
MysCkCardOO = 0


	
def pic_main_start(evant):
	
	#clear_data_label(1)
	
	w.itemconfig(canvas, image = my_images[0])	

def pic_ev_card(evant):
	
	w.itemconfig(canvas, image = my_images[1])
	
def pic_ev_start(evant):
	
	w.itemconfig(canvas, image = my_images[2])

def pic_ev_insert_wire(evant):
	
	w.itemconfig(canvas, image = my_images[3])
	
def pic_ev_charge0(evant):
	
	w.itemconfig(canvas, image = my_images[4])
	
def pic_ev_charge1(evant):
	
	w.itemconfig(canvas, image = my_images[5])

def pic_ev_main_stop(evant):
	
	w.itemconfig(canvas, image = my_images[6])
	
def pic_ev_stop(evant):
	
	w.itemconfig(canvas, image = my_images[7])

def pic_ev_remove_wire(evant):
	
	w.itemconfig(canvas, image = my_images[8])

def pic_ev_lnvalid(evant):
	
	w.itemconfig(canvas, image = my_images[9])

	
def card_show(evant):
	
	global var_card_id
	global var_card_type
	global var_card_text
	global var_money

	
	
	var_card_id = tk.Label(text='12345678',textvariable=varCard_id, font=("Tahoma",16),bg='white',width=30,anchor='w')
	var_card_type = tk.Label(text='Prepaid',textvariable=varCard_type, font=("Tahoma",20),bg='white',width=10,anchor='w')
	var_card_text = tk.Label(text='Prepaid',textvariable=varText, font=("Tahoma",16),bg='white',width=30,anchor='w')
	var_money = tk.Label(text='200',textvariable=varMoney, font=("Tahoma",20),bg='white',width=10,anchor='w')
	#var_labal = tk.Label(text='Card ID:',font=("Tahoma",16),bg='white')  #Helvetica
	var_card_id.pack()
	var_card_type.pack()
	var_card_text.pack()
	var_money.pack()
	#var_labal.pack()
	

	

	#w.create_window(100,100,window=var_labal)
	#w.create_window(285,103,window=canvas_text2)
	w.create_window(310,155,window=var_card_id)
	w.create_window(310,220,window=var_card_text)
	w.create_window(230,310,window=var_money)
	w.create_window(285,390,window=var_card_type)
	
def card_showEnergy(evant):
	
	global var_card_id
	global var_card_type
	global var_money
	global var_card_text
	
	
	var_card_id = tk.Label(text='12345678',textvariable=varCard_id, font=("Tahoma",20),bg='white',width=10,anchor='w')
	var_card_text = tk.Label(text='Prepaid',textvariable=varText, font=("Tahoma",20),bg='white',width=10,anchor='w')
	var_money = tk.Label(text='200',textvariable=varMoney, font=("Tahoma",20),bg='white',width=10,anchor='w')
	var_card_type = tk.Label(text='',textvariable=varCard_type, font=("Tahoma",20),bg='white',width=1,anchor='w')
	#var_labal = tk.Label(text='Card ID:',font=("Tahoma",16),bg='white')  #Helvetica
	var_card_id.pack()
	var_card_type.pack()
	var_card_text.pack()
	var_card_type.pack()
	#var_money.pack()
	#var_labal.pack()
	

	

	#w.create_window(100,100,window=var_labal)
	#w.create_window(285,103,window=canvas_text2)
	w.create_window(270,157,window=var_card_id)
	w.create_window(270,231,window=var_card_text)
	w.create_window(270,310,window=var_money)
	w.create_window(200,380,window=var_card_type)

def data_show(evant):
	
	global var_energy
	global var_current
	global var_money
	
	

def bink_label(evant):
	
	global bink
	bink = tk.Label(text='', font=("Tahoma",12),bg='green',width=30,height=2,anchor='e')
	bink.pack()
	w.create_window(250,232,window=bink)

	
def clear_card_label(evant):
	
	var_card_id.destroy()
	var_card_type.destroy()
	var_card_text.destroy()
	var_money.destroy()
	
#def clear_1(evant):
#	var_card_id.destroy()
#	var_card_type.destroy()
#	var_money.destroy()
	
#	var_card_id.destroy()
	
def clear_data_label(evant):
	var_energy.destroy()
	var_current.destroy()
	var_money.destroy()

def clear_data():
	var_energy.destroy()

def reboot_pro():
	os.system("sudo reboot")
	
def close(event):
	root.withdraw()	
	
	card_show(0)
	clear_card_label(1)


def readSerial():
	global touch
	global Mys
	global rand
	global show
	global MysCK
	global MysCkWire
	global MysInsert
	global MysStartPrice
	global MysCardid 
	global MysText 
	global Mystype 
	global energy
	global current
	global price 
	global commandCharge 
	global chargeType 	
	global TagCard
	global MysStartPrice2
	global MysCkStop
	global MysCkCardOO

	while True:
		
		serBuffer = ser.readline()
		
				
		if len(serBuffer) == 0:
			
			if MysCkWire == 1:
				MysInsert = MysInsert+1
				print MysInsert
				
				if MysInsert > 90:
					
					MysInsert = 0
					MysCkWire = 0
					ser.write("RE$end")	#RESET Command
					print "Tag Card\n"
					break
				
			#elseif MysCkWire == 2:
				#ser.write("RE$end")	#RESET Command
				#print "Wait for RESET\n"
				#break
				
				
			else:
				MysInsert = 0
				MysCkWire = 0
				print "___\n"
				break
				
		else:
			print serBuffer
			message = serBuffer.split('$')
			length_message = len(message)
			
			#print length_message
			#length_message = len(message)
			
			if message[0] == 'D1':   #Tag Card
				MysCK = 0  # Check D5
				MysCkStop = 1
				pic_main_start(1)
				clear_card_label(1)
				root.update()
				MysInsert = 0
				MysCkWire = 0
				MysCkCardOO = 0
				print "Tag Card\n"
				break
				
			
			if message[0] == 'D2' and length_message ==3 :	#Show Card
				#touch=0
				MysCK = 0  # Check D5
				MysCkStop = 1
			
				card_id = message[1]
				print "Show Card\n"
				print card_id
				#card_show(1)
				#clear_card_label(1)
				MysCkCardOO = MysCkCardOO+1
				
				if MysCkCardOO >1:
					clear_card_label(1)

				if card_id == '2A958AAB' or card_id == '448A87AB' or card_id == '1A263C06' or card_id == 'E07E6915':
					
						card_show(1)

						MysStartPrice = 3000.00
						MysCardid = "Mr. Teratam Bunyagul"
						MysText = "Assistant Professor"
						Mystype = "Prepaid"

						varCard_id.set(MysCardid)
						varMysEnergy.set("")
						varText.set(MysText)
						varMoney.set(str(MysStartPrice))
						varCard_type.set(Mystype)


				else:
					
					if card_id == '3AF41805' or card_id == '3A1C6206' or card_id == '20F689AB':
						
							card_show(1)

							MysStartPrice = 3000.00
							MysCardid = "Mr. Teratam Bunyagul"
							MysText = "Assistant Professor"
							Mystype = "Prepaid"

							varCard_id.set(MysCardid)
							varMysEnergy.set("")
							varText.set(MysText)
							varMoney.set(str(MysStartPrice))
							varCard_type.set(Mystype)
				
					else:
	
							card_show(1)
							MysStartPrice = 200.00
							MysCardid = card_id
							MysText = "Employee"
							Mystype = "Prepaid"

							varCard_id.set(MysCardid)
							varMysEnergy.set("")
							varText.set(MysText)
							varMoney.set(str(MysStartPrice))
							varCard_type.set(Mystype)

				print "Card Correct\n"
				pic_ev_card(1)
				root.update()
				
				time.sleep(3)
				MysInsert = 0
				MysCkWire = 0
				ser.write("CARD$1$end")	#Card correct
				break
				
				
			if message[0] == 'D3':   #Push Start

				MysCK = 0  # Check D5
				MysCkCardOO = 0
				MysCkStop = 1
				pic_ev_start(1)   #Push Start
				clear_card_label(1)
				root.update()
				MysInsert = 0
				MysCkWire = 0
				print "Push Start\n"
				break
				
			if message[0] == 'D4':	#Plug In
				MysCK = 0  # Check D5
				MysCkCardOO = 0
				MysCkStop = 1
				pic_ev_insert_wire(1)
				clear_card_label(1)
				root.update()
				Mysinsert = 0
				MysCkWire = 1
				print "Plug In\n"
				break
				
			if message[0] == 'D5' and length_message == 8:	#Energy
				
				MysCK = MysCK + 1
				MysCkCardOO = 0
				energy = message[1]
				current = message[2]
				price = message[3]
				commandCharge = message[4]
				chargeType = message[5]		
				TagCard = message[6]	
				MysInsert = 0
				MysCkWire = 0
				#MysStartPrice2 = float(MysStartPrice-(float(price)/100.00))
				MysStartPrice2 = float(MysStartPrice-(float(price)))
				#MysStartPrice2 = 200
				
				print "D5"	
				
				if MysCK > 15000:   #Mys Add
					MysCk = 2
				
				if message[6] == '1':

					
					if MysCkStop == 1:
						print "Show Card  Stop\n"
						
						clear_card_label(1)
						card_show(1)
						varCard_id.set(MysCardid)
						varMysEnergy.set("")
						varText.set(MysText)
						varMoney.set(str(float(MysStartPrice2)))
						varCard_type.set(Mystype)

						pic_ev_card(1)
						root.update()
				
						time.sleep(3)
						MysCkStop = 0
	
						MysCK = 0  # Check D5
						pic_ev_stop(1)
						clear_card_label(1)
						root.update()
						print "Push Stop\n"
						ser.write("CARD$1$end")	#Card correct
						break
					
				if message[6] == '0':
					
					MysCkStop = 1
					print "Charge"
					if MysCK==1:
						card_showEnergy(1)
					else:
						pass
					
					varCard_id.set(str(float(energy)))
					varText.set(str(float(current)))
					varMoney.set(str(float(price)))
					varCard_type.set("")

				
					if rand == 1:
						pic_ev_charge1(1)
						root.update()
						rand=0
					else:
						pic_ev_charge0(1)
						root.update()
						rand=1
				
					break
				
			#if message[0] == 'D6':	#Push Stop
				#MysCK = 0
				
				#ser.write("CARD$1$end")	#Card correct
				#pic_ev_stop(1)
				#clear_card_label(1)
				#root.update()
				#print "Push Stop\n"
				#break
				
			if message[0] == 'D7':	#Plug Out
				MysCK = 0  # Check D5
				MysCkStop = 1
				MysCkCardOO = 0
				pic_ev_remove_wire(1)
				clear_card_label(1)
				root.update()
				MysInsert = 0
				MysCkWire = 0
				print "Plug Out\n"
				break
				
			else:
				pass
				
	root.after(10, readSerial)


canvas = w.create_image(0, 0,anchor=NW,image=my_images[0])
w.pack()

root.after(100, readSerial)		
root.bind('<Escape>',close)
#root.bind('<F1>',pic_bus1)
#root.bind('<F2>',pic_smile)
#root.bind('<F3>',pic_frown)
root.config(cursor='none')
root.attributes('-fullscreen', True)
root.mainloop()
