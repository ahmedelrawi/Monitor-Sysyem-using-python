import psutil
from time import sleep
from datetime import datetime
import socket
import psutil
import time



information = []
# f = open("pub.log.txt", "w")
f = open("pub.log.txt", "a")
# f_note = open("notification_log.txt", "w")
f_note = open("notification_log.txt", "a")




while True:


    if psutil.virtual_memory()[2] > 80 :


        x = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f_note.write(f"at {x} Memory usage over threshold! ,Memory usage has reached 95% \n")



        
    else:


        information.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        'Code to trace the temperature at any device.'
        # information.append(psutil.sensors_temperatures())

        cpu_usage = psutil.cpu_percent(interval = 1, percpu = True)
        cpu_usage_mean = round(sum(cpu_usage) / len(cpu_usage), 2)
        information.append(cpu_usage_mean)
        information.append(psutil.cpu_count(logical=True))


        information.append(psutil.virtual_memory()[2])
        information.append(round(psutil.virtual_memory()[3]/1000000000))



        disk_info = psutil.disk_usage("/")
        information.append(round(disk_info.used / 1024 / 1024 / 1024,2))



        'Host name usign socket library'
        host_ip = socket.gethostbyname(socket.gethostname())
        information.append(host_ip)


        for i in information:

            f.write(str(i))
            f.write(" ")

        else:

            f.write("\n")
        
        
        information = []
        

    time.sleep(3)

f.close()
f_note.close()
