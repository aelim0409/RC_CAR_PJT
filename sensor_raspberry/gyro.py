import RPi.GPIO as GPIO
import time
import smbus


btn1 = 16
btn2 = 20
btn3 = 21

PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

speed = 0

bus = smbus.SMBus(1)
Device_Address = 0x68

GPIO.setmode(GPIO.BCM)

GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def MPU_Init() :
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)

    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr) :
    #Accelero and Gyro value are 16 - bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr + 1)

    #concatenate higher and lower value
    value = ((high << 8) | low)

    #to get signed value from mpu6050
    if (value > 32768) :
        value = value - 65536
    return value


def btn1_pressed(channel):
    global speed
    if speed > 3:
        speed = 3
    elif speed < 0:
        speed = 1
    else:
        speed += 1

    print("Btn1")

def btn2_pressed(channel):
    global speed
    speed = 0
    print("Btn2 STOP")

def btn3_pressed(channel):
    global speed
    if speed < -3:
        speed = -3
    elif speed > 0:
        speed = -1
    else:
        speed -= 1
    print("Btn3")

GPIO.add_event_detect(btn1, GPIO.FALLING, callback=btn1_pressed, bouncetime=200)
GPIO.add_event_detect(btn2, GPIO.FALLING, callback=btn2_pressed, bouncetime=200)
GPIO.add_event_detect(btn3, GPIO.FALLING, callback=btn3_pressed, bouncetime=200)

MPU_Init()



try:
    while True:
        acc_y = read_raw_data(ACCEL_YOUT_H)

        ay = acc_y / 16384.0 + 2.0
        print(ay)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
