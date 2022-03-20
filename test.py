import os

def main():
    print('Start testing the camera A')
    i2c = "i2cset -y 10 0x24 0x24 0x02"
    os.system(i2c)
    capture(1)

    print('Start testing the camera B') 
    i2c = "i2cset -y 10 0x24 0x24 0x12"
    os.system(i2c)
    capture(2)

    print('Start testing the camera C')
    i2c = "i2cset -y 10 0x24 0x24 0x22"
    os.system(i2c)
    capture(3)

    print('Start testing the camera D')
    i2c = "i2cset -y 10 0x24 0x24 0x32"
    os.system(i2c)
    capture(4)
    
def capture(cam):
    cmd = "libcamera-still -o capture_%d.jpg" % cam
    os.system(cmd)

if __name__ == "__main__":
    main()