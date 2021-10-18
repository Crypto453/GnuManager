import os
import time
import random
import colorama
from colorama import Fore

def principal_list():
	list_a = ["[1] Procesos", "[2] Instalar paquetes", "[3] USB", "[4] Ejecutar programa", "[5] Mi tarjeta de red", "[6] acceder a root", "[7] Editor de texto", "[8] ejecutar terminal", "[9] Cheese","[10] Descargar un archivo", "[00] Salir"]
	for list_x in list_a:
		print(random_random + list_x)
		time.sleep(0.1)
def processes_list():
	list_processes = ["[1] Ver procesos de red", "[2] Ver procesos de programas", "[3] Volver", "[00] Salir"]
	for list_p in list_processes:
		print(random_random + list_p)
		time.sleep(0.1)
def red_list():
	list_red = ["[1] Mi direccion IP local", "[2] Mi direccion IP publica", "[3] Nombre de mi maquina", "[4] Mi nombre de usuario", "[5] Volver", "[00] Salir"]
	for list_r in list_red:
		print(random_random + list_r)
		time.sleep(0.1)
def pendrive_list():
	list_pendrive = ["[1] Montar usb", "[2] Desmontar usb", "[3] Volver"]
	for list_pen in list_pendrive:
		print(list_pen)
		time.sleep(0.1)
def banner_banner():
	banner_banner = ("""
	 #####                #     #                                           
     #     # #    # #    # ##   ##   ##   #    #   ##    ####  ###### #####  
     #       ##   # #    # # # # #  #  #  ##   #  #  #  #    # #      #    # 
     #  #### # #  # #    # #  #  # #    # # #  # #    # #      #####  #    # 
     #     # #  # # #    # #     # ###### #  # # ###### #  ### #      #####  
     #     # #   ## #    # #     # #    # #   ## #    # #    # #      #    #  
     #####  #    #  ####  #     # #    # #    # #    #  ####  ###### #    #
     """)
	print(random_random + banner_banner)
	time.sleep(0.1)
def clear():
	os.system("clear")
def full():
	clear()
	banner_banner()

random_random = (random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.WHITE, Fore.YELLOW]))
clear()
banner_banner()
principal_list()
gnu = int(input("===> "))
if gnu == 1:
	while True:
		full()
		processes_list()
		pros = int(input("===> "))
		if pros == 1:
			try:
				os.system("netstat -tanp")
				break
			except:
				print(Fore.RED + "Error inesperado")
				break
		elif pros == 2:
			try:
				os.system("ps -aux")
				break
			except:
			    print(Fore.RED + "Error inesperado")
		elif pros == 3:
		    try:
		        os.system("python3 LinuxManager.py")
		    except:
		        print("Archivo no encontrado")
		elif pros == 00:
			break
		else:
		    print(Fore.RED + "ERROR")	

elif gnu == 2:
	full()
	try:
	    paquet = input(random_random + "Escriba el nombre del paquete \n que quiere instalar: ")
	    os.system(f"sudo apt install {paquet}")
	    print(Fore.YELLOW + "Pograma instalado")
	    os.system("python3 LinuxManager.py")
	except:
		print(Fore.RED + "Error al instalar programa")
elif gnu == 3:
	while True:
		full()
		pendrive_list()
		drive = int(input("===> "))
		if drive == 1:
			try:
				os.system("lsblk")
				drive_b = input(random_random + "Escriba el disco a montar \n Escriba /dev/nombre del disco \n==> ")
				drive_c = input(random_random + "Escriba la ruta donde quiere montar el dispositivo \n recomendable /media/user: ")	
				os.system(f"sudo mount -t vfat {drive_v} {drive_c}")
			except:
				print(Fore.RED + "Error al montar dispositivo")
		elif drive == 2:
			try:
				os.system("lsblk")
				con = input("Escriba el nombre del disco a desmontar: ")
				os.system(f"sudo umount {con}")
			except:
				print("error al desmontar dispositivo")
		elif drive == 3:
			os.system("python3 LinuxManager.py")
		elif drive == 00:
			break
		else:
			print(Fore.RED + "error, dijite un valor valido")
elif gnu == 4:
	while True:
		try:
			program = input("Escriba el nombre del programa a ejecutar: ")
			os.system(f"{program}")
			break
		except:
			print(Fore.RED + "Error al ejecutar el programa")
			break
elif gnu == 5:
	while True:
		full()
		red_list()
		network = int(input("===> "))
		if network == 1:
			os.system("sudo hostname -I")
			break
		elif network == 2:
			os.system("sudo curl ifconfig.me")
			break
		elif network == 3:
			os.system("hostname")
			break
		elif network == 4:
			os.system("whoami")
			break
		elif network == 5:
			os.system("python3 LinuxManager.py")
			break
		elif network == 00:
			break
		else:
			print(Fore.RED + "error, intente denuevo")
elif gnu == 6:
	os.system("sudo su")
elif gnu == 7:
	os.system("subl")
elif gnu == 8:
	os.system("termiantor")
elif gnu == 9:
	os.system("cheese")
elif gnu == 10:
	download = input("pegue la url del archivo a descargar: ")
	os.system(f"wget {download}")
else:
	print(Fore.RED + "Error, Dijite un valor valido")