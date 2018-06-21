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
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Connect server
#time.sleep(60)
ws = create_connection("ws://192.168.73.85/ocpp/1")

UART.setup("UART2")

energy=0

ser = serial.Serial(port = "/dev/ttyO2", baudrate=115200, timeout=1)
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


def readSerial():
	global rand
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
			timer90()
			break
					
		else:
			print serBuffer
			message = serBuffer.split('$')
			length_message = len(message)
			
			if message[0] == 'D1':   #Tag Card
				MysCK = 0  # Check D5
				MysCkStop = 1
				gui.pic_main_start(1)
				#clear_card_label(1)
				gui.update()
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
					gui.clear_card_label(1)

				ws.send('[2, "BQMYei0kseAoZ2aij7mbTs37UNGCFLhv", "Authorize", {"idTag":"'+ card_id +'"}]')
				result = ws.recv()
				result_json = json.loads(result)
				print result_json
				if result_json[2]['idTagInfo']['status'] == "Accepted":
						amount = result_json[2]['idTagInfo']['amount']
						name_user = result_json[2]['idTagInfo']['name']
						gui.card_show(1)

						MysStartPrice = amount
						MysCardid = card_id
						MysText = name_user
						Mystype = "Prepaid"
						
						gui.set_energy(MysStartPrice,MysCardid,MysText,Mystype)

						gui.pic_ev_card(1)
						gui.update()
						print "Card Correct\n"
				
						time.sleep(3)
						MysInsert = 0
						MysCkWire = 0
						ser.write("CARD$1$end")	#Card correct
						break

				else:

						gui.pic_ev_lnvalid(1)
						gui.update()
						ser.write("RE$end")	#RESET Command
						break
				
				
			if message[0] == 'D3':   #Push Start

				MysCK = 0  # Check D5
				MysCkCardOO = 0
				MysCkStop = 1
				gui.pic_ev_start(1)   #Push Start
				gui.clear_card_label(1)
				gui.update()
				MysInsert = 0
				MysCkWire = 0
				print "Push Start\n"
				break
				
			if message[0] == 'D4':	#Plug In
				MysCK = 0  # Check D5
				MysCkCardOO = 0
				MysCkStop = 1
				gui.pic_ev_insert_wire(1)
				gui.clear_card_label(1)
				gui.update()
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
						ws.send('[2, "ZeERlwkKOEdm9qaCnTUpDXI95bxr1ot3", "StatusNotification", {"timestamp": "'+time_now+'", "status": "Available", "connectorId": '+chargeType+', "errorCode": "NoError"}]')
						receive_status_stop = json.loads(ws.recv())
						print("Received : ",  receive_status_stop)
						ws.send('[2, "xkgU2inssohvi7b3Im2BTjxZGkMEJgYk", "StopTransaction", {"transactionId": 1, "timestamp": "'+ time_now +'", "idTag": "'+ MysCardid +'","meterStop": '+energy+'}]')
						receive_stop = json.loads(ws.recv())
						print("Received : ",  receive_stop)
						
						gui.clear_card_label(1)
						gui.card_show(1)
						gui.set_energy(MysCardid,MysText,MysStartPrice2,Mystype)

						gui.pic_ev_card(1)
						gui.update()
				
						time.sleep(3)
						MysCkStop = 0
	
						MysCK = 0  # Check D5
						gui.pic_ev_stop(1)
						gui.clear_card_label(1)
						gui.update()
						print "Push Stop\n"
						ser.write("CARD$1$end")	#Card correct
						break
					
				if message[6] == '0':
					
					MysCkStop = 1
					print "Charge"
					if MysCK==1:
						gui.card_showEnergy(1)
					else:
						pass
					
					ws.send('[2, "uIDHeJPq6QESJEKY2Tu1qzimdxgfBQNW", "MeterValues", {"transactionId": 1, "connectorId": '+chargeType+', "meterValue": {"sampledValue": {"value": '+ energy +', "unit": "Wh"}}}]')
					receive_Meter = json.loads(ws.recv())
					print("Received : ", receive_Meter)
					gui.set_energy_start(energy,current,price)
				
					if rand == 1:
						gui.pic_ev_charge1(1)
						gui.update()
						rand=0
					else:
						gui.pic_ev_charge0(1)
						gui.update()
						rand=1
				
					break
				
	gui.restart(10, readSerial)


gui.set_and_run(readSerial)
