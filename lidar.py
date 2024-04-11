import PyLidar3
import matplotlib.pyplot as plt
import math
import time


port = "/dev/ttyUSB0" #linux
# which Lidar is connected:"
# for instance /dev/ttyUSB0
Obj = PyLidar3.YdLidarX4(port)

x=[0]*360
y=[0]*360
x[0] = 0
y[0] = 0
if(Obj.Connect()):
    
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    plt.figure(1)

    t = time.time() # start time
    data = next(gen)
    delta = time.time() - t


    while (delta) < 30: #scan for 30 seconds
        delta = time.time() - t
        print(delta)
        data = next(gen)
        
        for angle in range (0,360) :
            if(data[angle] >300):
                x[angle] = data[angle]* math.cos(math.radians(angle))
                y[angle] = data[angle]* math.sin(math.radians(angle))
        plt.cla()
        plt.ylim(-2000,2000)
        plt.xlim(-2000,2000)
        plt.scatter(x,y,c='r',s=8)
        
        plt.pause(0.05)
    plt.savefig('foo.png')
    plt.close("all")
    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")
