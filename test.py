import os

def main():
    #initCameras()
    startScanning()

def capture(cam, initFocus):

    if(initFocus):
        cmd = "libcamera-still -t 5000 -o focused_%d.jpg --autofocus" % cam
    else:
        cmd = "libcamera-still -t 1000 -n -o capture_%d.jpg" % cam
    
    os.system(cmd)


def initCameras():
    print('Start focusing the camera A')
    i2c = "i2cset -y 10 0x24 0x24 0x02"
    os.system(i2c)
    capture(1, True)

    print('Start focusing the camera B') 
    i2c = "i2cset -y 10 0x24 0x24 0x12"
    os.system(i2c)
    capture(2, True)

    print('Start focusing the camera C')
    i2c = "i2cset -y 10 0x24 0x24 0x22"
    os.system(i2c)
    capture(3, True)

    print('Start focusing the camera D')
    i2c = "i2cset -y 10 0x24 0x24 0x32"
    os.system(i2c)
    capture(4, True)

def startScanning():
    print('Start testing the camera A')
    i2c = "i2cset -y 10 0x24 0x24 0x02"
    os.system(i2c)
    capture(1, False)

    print('Start testing the camera B') 
    i2c = "i2cset -y 10 0x24 0x24 0x12"
    os.system(i2c)
    capture(2, False)

    print('Start testing the camera C')
    i2c = "i2cset -y 10 0x24 0x24 0x22"
    os.system(i2c)
    capture(3, False)

    print('Start testing the camera D')
    i2c = "i2cset -y 10 0x24 0x24 0x32"
    os.system(i2c)
    capture(4, False)

if __name__ == "__main__":
    main()