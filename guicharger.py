import Tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()
varEnergy,varCurrent,varCard_id,varCard_type,varMoney,\
varText,varMysEnergy = (tk.StringVar() for i in range(7))
root.title("My Image ")
w = tk.Canvas(root, width=480, height=800)

## Path Image ##
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
canvas = None

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

def update():
           root.update()

def set_energy(MysCardid,MysText,MysStartPrice,Mystype):
           varCard_id.set(MysCardid)
           varMysEnergy.set("")
           varText.set(MysText)
           varMoney.set(str(MysStartPrice))
           varCard_type.set(Mystype)

def set_energy_start(energy,current,price):
	   varCard_id.set(str(float(energy)))
	   varText.set(str(float(current)))
	   varMoney.set(str(float(price)))
	   varCard_type.set("")

def set_and_run(callback):
           global canvas
           canvas = w.create_image(0, 0,anchor=tk.NW,image=my_images[0])
           w.pack()
           root.after(100, callback)		
           root.bind('<Escape>',close)
           root.config(cursor='none')
           root.attributes('-fullscreen', False)
           root.mainloop()

def restart(delay,callback):
           root.after(delay, callback)


