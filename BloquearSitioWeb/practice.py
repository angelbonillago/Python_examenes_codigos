import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_dir = hosts_path
host_temporal = "host"

buscar = "127.0.0.1"
#website_list=[]

website_list = [

]

from_hour = 1
to_hour = 23
ciclo = True
while ciclo:
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() <\
            dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("trabajando!!!")

        with open(hosts_dir, 'r+') as file:
            contenido = file.read()
            print(contenido)

            for website in website_list:
                if website in contenido:
                    pass  # si ya se encuentra el sitio, entonces no hago nada
                else:
                    file.write(buscar + " " + website + "\n")
    else:
        print("No trabajo")
        with open(hosts_dir, 'r+') as file:
            contenido = file.readlines()
            print(contenido)
            file.seek(0)#Se ubica en la posicion 0 del archivo
            for line in contenido:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(10) 
    #print("salir: Y/N")
    #x = input()
    #print(x)
    #if(x == 'Y' or x == 'y'):
    #    ciclo = False
