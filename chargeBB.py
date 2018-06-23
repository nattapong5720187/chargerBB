#Mys_Separate display
#Mys_Don't have Button and ZigBee

import Adafruit_BBIO.UART as UART
import serial
import time 
from time import sleep
import Adafruit_BBIO.GPIO as GPIO
import os
from websocket import create_connection
import json
from datetime import datetime
import guicharger as gui

#Connect server
#time.sleep(60)
ws = create_connection("ws://192.168.73.85/ocpp/1")

UART.setup("UART2")

MysCkWire = 0
MysInsert = 0
Send_Start = 0
MysCkStop = 0
rand=1
energy=0
MysCK = 0
MysStartPrice = 300
MysCardid = "Mys"
MysText = "Employee"
Mystype = "Prepaid"
MysCkCardOO = 0
transactionId = 0

ser = serial.Serial(port = "/dev/ttyO2", baudrate=115200, timeout=1)

def mian_start():
	global MysCkWire
	global MysInsert
	gui.pic_main_start(1)
	gui.update()
	MysInsert = 0
	MysCkWire = 0
	print "Tag Card\n"
	
def check_autentication(card_id):
	global MysStartPrice
	global MysCardid
	global MysText
	global Mystype
	
	print "Show Card\n"
	print card_id
	ws.send('[2, "BQMYei0kseAoZ2aij7mbTs37UNGCFLhv", "Authorize", {"idTag":"'+ card_id +'"}]')
	result = ws.recv()
	result_json = json.loads(result)
	return result_json
			
def autentication(card_id,amount,name_user):
	gui.card_show(1)

	MysStartPrice = amount
	MysCardid = card_id
	MysText = name_user
	Mystype = "Prepaid"
	
	gui.set_energy(MysText,MysCardid,MysStartPrice,Mystype)

	gui.pic_ev_card(1)
	gui.update()
	print "Card Correct\n"

	time.sleep(3)
	ser.write("CARD$1$end")	#Card correct

def non_autentication():
	gui.pic_ev_lnvalid(1)
	gui.update()
	ser.write("RE$end")	#RESET Command
			
def push_start():
	gui.pic_ev_start(1)   #Push Start
	gui.clear_card_label(1)
	gui.update()
	print "Push Start\n"
	
def plug_In():
	global MysCkCardOO 
	global MysCkStop
	global MysCkWire
	global MysInsert
	global MysCK
	global Send_Start
	
	MysCK = 0  # Check D5
	MysCkCardOO = 0
	MysCkStop = 1
	gui.pic_ev_insert_wire(1)
	gui.clear_card_label(1)
	gui.update()
	Mysinsert = 0
	MysCkWire = 1
	Send_Start = 1
	print "Plug In\n"
	
def send_start_one_time(time_now,chargeType):
	global Send_Start
	global transactionId
	global MysCardid 
	if Send_Start == 1:
		ws.send('[2, "ZeERlwkKOEdm9qaCnTUpDXI95bxr1ot3", "StatusNotification", {"timestamp": "'+time_now+'", "status": "Charging", "connectorId": '+chargeType+', "errorCode": "NoError"}]')
		result_json_status = json.loads(ws.recv())
		print("Received : ", result_json_status)
		ws.send('[2, "XHgRau8AcLOUezhYFvZWKMi83DeP1bvC", "StartTransaction", {"connectorId": '+chargeType+', "meterStart": 0, "idTag": "'+ MysCardid +'", "timestamp": "'+ time_now+'"}]')
		result_json_start = json.loads(ws.recv())
		transactionId = str(result_json_start[2]['transactionId'])
		print("Received : ", transactionId)
		Send_Start = 0
	
	print "D5"
	
def send_metervalues(chargeType,energy,current,price):
	global MysCkStop
	global MysCK
	MysCkStop = 1
	print "Charge"
	if MysCK==1:
		gui.card_showEnergy(1)
	
	ws.send('[2, "uIDHeJPq6QESJEKY2Tu1qzimdxgfBQNW", "MeterValues", {"connectorId": '+chargeType+', "meterValue": {"sampledValue": {"value": '+ energy +', "unit": "Wh"}}}]')
	receive_Meter = json.loads(ws.recv())
	print("Received : ", receive_Meter)
	gui.set_energy_start(energy,current,price)

def stopTransaction(time_now,chargeType,energy,MysStartPrice2):
	global MysCkStop
	global MysCkWire
	global MysInsert
	global MysCK
	global MysCardid
	global MysText
	global Mystype
	global transactionId
	
	print "Show Card  Stop\n"
	print(transactionId)
	ws.send('[2, "ZeERlwkKOEdm9qaCnTUpDXI95bxr1ot3", "StatusNotification", {"timestamp": "'+time_now+'", "status": "Available", "connectorId": '+chargeType+', "errorCode": "NoError"}]')
	receive_status_stop = json.loads(ws.recv())
	print("Received : ",  receive_status_stop)
	ws.send('[2, "xkgU2inssohvi7b3Im2BTjxZGkMEJgYk", "StopTransaction", {"transactionId": '+transactionId+', "timestamp": "'+ time_now +'", "idTag": "'+ MysCardid +'","meterStop": '+energy+'}]')
	receive_stop = json.loads(ws.recv())
	print("Received : ",  receive_stop)
	
	gui.clear_card_label(1)
	gui.card_show(1)
	gui.set_energy(MysText,MysCardid,MysStartPrice2,Mystype)

	gui.pic_ev_card(1)
	gui.update()

	time.sleep(3)
	MysCkStop = 0

	MysCK = 0  # Check D5
	MysInsert = 0
	MysCkWire = 0
	gui.clear_card_label(1)
	gui.pic_ev_stop(1)
	gui.update()
	print "Push Stop\n"
	ser.write("CARD$1$end")	#Card correct
	
def heartbeat():
	ws.send('[2, "ZeERlwkKOEdm9qaCnTUpDXI95bxr1ot3", "Heartbeat", {}]')
	receive_heartbeat = json.loads(ws.recv())
	return receive_heartbeat
	
def reservation():
	recv = heartbeat()
	if recv[0] == 2:
		reserv = recv[3]['idTag']
		exp = recv[3]['expiryDate']
		ws.send('[3, "ZeERlwkKOEdm9qaCnTUpDXI95bxr1ot3",{"status":"Accepted"}]')
		print reserv
		print exp
		
def timer90():
	global MysCkWire
	global MysInsert
	if MysCkWire == 1:
		MysInsert = MysInsert+1
		print MysInsert
		
		if MysInsert > 90:
			
			MysInsert = 0
			MysCkWire = 0
			ser.write("RE$end")	#RESET Command
			print "Tag Card\n"
		
	else:
		MysInsert = 0
		MysCkWire = 0
		print "___\n"
		
def switch_pic_charging():
	global rand
	if rand == 1:
		gui.pic_ev_charge1(1)
		gui.update()
		rand=0
	else:
		gui.pic_ev_charge0(1)
		gui.update()
		rand=1
	
def readSerial():
	global MysCK
	global MysStartPrice
	global MysCkCardOO 

	while True:
		time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		serBuffer = ser.readline()
		heartbeat()
		reservation()
		time.sleep(1)
				
		if len(serBuffer) == 0:
			timer90()
			break
					
		else:
			print serBuffer
			message = serBuffer.split('$')
			length_message = len(message)
			
			if message[0] == 'D1':   #Tag Card
				mian_start()
				break
				
			
			if message[0] == 'D2' and length_message ==3:	#Show Card
				card_id = message[1]
				keep_auten = check_autentication(card_id)
				if keep_auten[2]['idTagInfo']['status'] == "Accepted":
					amount = keep_auten[2]['idTagInfo']['amount']
					name_user = keep_auten[2]['idTagInfo']['name']
					autentication(card_id,amount,name_user)
				else:
					non_autentication()
					
				break
				
				
			if message[0] == 'D3':   #Push Start
				push_start()
				break
				
			if message[0] == 'D4':	#Plug In
				plug_In()
				break
				
			if message[0] == 'D5' and length_message == 8:	#Energy
				MysCK = MysCK + 1
				energy = message[1]
				current = message[2]
				price = message[3]
				commandCharge = message[4]
				chargeType = message[5]		
				TagCard = message[6]	
				MysStartPrice2 = float(MysStartPrice-(float(price)))
					
				send_start_one_time(time_now,chargeType)
				
				if MysCK > 15000:   #Mys Add
					MysCk = 2
				
				if message[6] == '1':
					if MysCkStop == 1:
						stopTransaction(time_now,chargeType,energy,MysStartPrice2)
						break
					
				if message[6] == '0':
					send_metervalues(chargeType,energy,current,price)
					switch_pic_charging()
					break
				
	gui.restart(10, readSerial)
	


gui.set_and_run(readSerial)
