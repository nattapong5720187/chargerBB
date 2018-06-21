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
from websocket import create_connection
import json
from datetime import datetime
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#GPIO.setup("P8_8",GPIO.IN)
#Connect server
#time.sleep(60)
ws = create_connection("ws://192.168.73.85/ocpp/1")
#ws = create_connection("ws://203.154.39.161:21001/ocpp_1_6/charger1/")


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
Check_Start = 1


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
a = dict()


	
def pic_main_start(evant):
	
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
	global Check_Start

	while True:
		
		serBuffer = ser.readline()
		
				
		if len(serBuffer) == 0:
			
			if MysCkWire == 1:
				MysInsert = MysInsert+1
				print MysInsert
				
				if MysInsert > 30:
					
					MysInsert = 0
					MysCkWire = 0
					ser.write("RE$end")	#RESET Command
					print "Tag Card\n"
					break
				
			else:
				MysInsert = 0
				MysCkWire = 0
				print "___\n"
				break
				
		else:
			print serBuffer
			message = serBuffer.split('$')
			length_message = len(message)
			
			if message[0] == 'D1':   #Tag Card
				MysCK = 0  # Check D5
				MysCkStop = 1
				pic_main_start(1)
				#clear_card_label(1)
				root.update()
				MysInsert = 0
				MysCkWire = 0
				MysCkCardOO = 0
				print "Tag Card\n"
				break
		
			if message[0] == 'D2' and length_message ==3 :	#Show Card
				MysCK = 0  # Check D5
				MysCkStop = 1
				card_id = message[1]
				print "Show Card\n"
				print card_id
				MysCkCardOO = MysCkCardOO+1
				if MysCkCardOO >1:
					clear_card_label(1)
				ws.send('[2, "BQMYei0kseAoZ2aij7mbTs37UNGCFLhv", "Authorize", {"idTag":"'+ card_id +'"}]')
				result = ws.recv()
				result_json = json.loads(result)
				print result_json
				if result_json[2]['idTagInfo']['status'] == "Accepted":
						#amount = result_json[2]['idTagInfo']['amount']
						#name_user = result_json[2]['idTagInfo']['name']
						card_show(1)

						MysStartPrice = 200.00
						MysCardid = card_id
						MysText = "KuyMung"
						Mystype = "Prepaid"

						varCard_id.set(MysCardid)
						varMysEnergy.set("")
						varText.set(MysText)
						varMoney.set(str(MysStartPrice))
						varCard_type.set(Mystype)
						
						pic_ev_card(1)
						root.update()
						print "Card Correct\n"
				
						#time.sleep(3)
						MysInsert = 0
						MysCkWire = 0
						ser.write("CARD$1$end")	#Card correct
						break

				else:

						pic_ev_lnvalid(1)
						root.update()
						#ser.write("CARD$1$end")	#Card correct
						ser.write("RE$end")	#RESET Command
						#time.sleep(2)
						#pic_main_start(1)
						#root.update()
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
				Check_Start = 1
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
				if Check_Start == 1:
					ws.send('[2, "ZeERlwkKOEdm9qaCnTUpDXI95bxr1ot3", "StatusNotification", {"timestamp": "'+time_now+'", "status": "Charging", "connectorId": '+chargeType+', "errorCode": "NoError"}]')
					result_json_status = json.loads(ws.recv())
					print("Received : ", result_json_status)
					ws.send('[2, "XHgRau8AcLOUezhYFvZWKMi83DeP1bvC", "StartTransaction", {"connectorId": '+chargeType+', "meterStart": 0, "idTag": "'+ MysCardid +'", "timestamp": "'+ time_now+'"}]')
					result_json_start = json.loads(ws.recv())
					transactionId = result_json_start[2]['transactionId']
					print("Received : ", transactionId)
					Check_Start = 0
				
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
						ws.send('[2, "ZeERlwkKOEdm9qaCnTUpDXI95bxr1ot3", "StatusNotification", {"timestamp": "'+time_now+'", "status": "Available", "connectorId": '+chargeType+', "errorCode": "NoError"}]')
						ws.send('[2, "xkgU2inssohvi7b3Im2BTjxZGkMEJgYk", "StopTransaction", {"transactionId": 1, "timestamp": "'+ time_now +'", "idTag": "'+ MysCardid +'","meterStop": '+energy+'}]')
						result = ws.recv()
						print("Received : ",  result)

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
					ws.send('[2, "uIDHeJPq6QESJEKY2Tu1qzimdxgfBQNW", "MeterValues", {"transactionId": 1, "connectorId": '+chargeType+', "meterValue": {"sampledValue": {"value": '+ energy +', "unit": "kWh"}}}]')
					result = ws.recv()
					print("Received : ", result)

				
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
root.attributes('-fullscreen', False)
root.mainloop()
