import socket
import psutil
import datetime
from colorama import init, Fore, Back, Style

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address, hostname, hostname[-3:]

print(Fore.GREEN+"Dirección IP de la PC:", get_ip_address())



def get_system_info():
    #Obtiene el total de RAM
    ram = psutil.virtual_memory().total
    #Lo convierto a scring para solo mostrar los primeros digitos 
    totalRam = str(ram)[:2]

    #funcion para obtener total de particiones en disco
    partitions = psutil.disk_partitions()
    total_particiones = [partitions.device for partitions in partitions]

    #Lista de usuarios
    users = psutil.users()
    total_usuarios = [users.name for users in users]

    #tiempo de inicio (boot) 
    #hora en la que se encendio la PC
    uptime = psutil.boot_time()
    
    print(Fore.BLUE +  "RAM ( GB ): ", totalRam)
    print(Fore.BLUE + "Memoria RAM Libre (bytes)): " ,psutil.virtual_memory().available)
    print(Fore.WHITE + "Uso de Disco ( % ): " ,psutil.disk_usage('/').percent)
    print(Fore.GREEN + "Lista de Particiones (x Letra): ", total_particiones)
    print(Fore.MAGENTA + "Usuario: ", total_usuarios)
    print(Fore.LIGHTYELLOW_EX + "Fecha y Hora en la que se encendio la PC: ",datetime.datetime.fromtimestamp(uptime).strftime('%Y-%m-%d %H:%M:%S'))
   

    system_info = {
        "RAM ( GB )": totalRam,
        # "CPU Usage": psutil.cpu_percent(),
        "Memoria RAM (Libre)": psutil.virtual_memory().available,
        "Uso de Disco ( % )": psutil.disk_usage('/').percent,
        "Lista de Particiones (x Letra)": total_particiones,
        "Usuario": total_usuarios,
        "Fecha y Hora en la que se encendio la PC": datetime.datetime.fromtimestamp(uptime).strftime('%Y-%m-%d %H:%M:%S'),
        #"Lista de servicios Activos": list(psutil.win_service_iter())
        
    }
    # return system_info

print( Fore.CYAN + "-Simón Pintado", get_system_info())
input("Enter para salir...")