import psutil
from time import sleep
from datetime import datetime
import socket
import psutil
import time






informations = []

while True:

    f = open("pub.log", "w")
    time.sleep(5)

    information = []

    information.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    information.append(' , ')

    cpu_usage = psutil.cpu_percent(interval = 1, percpu = True)
    cpu_usage_mean = round(sum(cpu_usage) / len(cpu_usage), 2)
    information.append(cpu_usage_mean)
    information.append(' , ')

    information.append(psutil.cpu_count(logical=True))
    information.append(' , ')


    information.append(psutil.virtual_memory()[2])
    information.append(' , ')

    information.append(round(psutil.virtual_memory()[3]/1000000000))
    information.append(' , ')




    disk_info = psutil.disk_usage("/")
    information.append(disk_info.used / 1024 / 1024 / 1024)
    information.append(' , ')



    'Host name usign socket library'
    host_ip = socket.gethostbyname(socket.gethostname())
    information.append(host_ip)






    for i in information:
        f.write(str(i))
    f.close()


    f = open("pub.log", "r")
    print(f.read())


    if psutil.virtual_memory()[2] > 80 :

        f = open("notification.log", "w")
        f.write("\n Memory usage over threshold! ,Memory usage has reached 95% \n")
        f.close()



    informations.append(information)
    information = []
