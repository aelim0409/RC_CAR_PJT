from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import threading
import signal
import time
import sys
import mysql.connector


# servoMotor
mh = Raspi_MotorHAT(0x6F)
myMotor = mh.getMotor(2)
servo = mh._pwm

servo.setPWMFreq(50)

servo.setPWM(0, 0, 300)

##########

speed = 0
handle = 300

db = mysql.connector.connect(host='13.209.3.181', user='aelim', password='1234'
            , database='aelimDB', auth_plugin='mysql_native_password')
cur = db.cursor()

l = [0, 90, 150, 180]
def speed_t():
    saveSpeed = 0
    global speed
    while True:
        if speed == saveSpeed:
            pass
        else:
            saveSpeed = speed
            if speed > 0:
                myMotor.setSpeed(l[speed])
                myMotor.run(Raspi_MotorHAT.FORWARD)
            elif speed == 0:
                myMotor.run(Raspi_MotorHAT.RELEASE)
            elif speed < 0:
                myMotor.setSpeed(l[(-1)*speed])
                myMotor.run(Raspi_MotorHAT.BACKWARD)
        

def handle_t():
    saveHandle = 300
    global handle
    while True:
        if saveHandle == handle:
            pass
        else:
            servo.setPWM(0, 0, handle)
            saveHandle = handle


def db():
    global speed, handle
    while True:
        time.sleep(0.05)

        # 커서 연결
        db = mysql.connector.connect(
            host='13.209.3.181',
            user='aelim',
            password='1234',
            database='aelimDB',
            auth_plugin='mysql_native_password'
        )
        cur = db.cursor()

        cur.execute("select * from info order by time desc limit 1")
        
        for (t,s, h) in cur:
            speed = s
            handle = h
            print(speed, handle)

        # 커서와 DB 연결 해제
        cur.close()
        db.close()


running = True

def signal_handler(signal, frame):
    global running
    running = False
    sys.exit(0)


thread1 = threading.Thread(target=speed_t)
thread2 = threading.Thread(target=handle_t)
thread3 = threading.Thread(target=db)

signal.signal(signal.SIGINT, signal_handler)

thread1.start()
thread2.start()
thread3.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        running = False
        break

thread1.join()
thread2.join()
thread3.join()

