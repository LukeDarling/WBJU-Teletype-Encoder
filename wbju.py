import serial, sys
from time import sleep

port = "/dev/cu.wchusbserial1410"
ser = serial.Serial(port, 115200)

with open(sys.argv[1]) as f:
    data = f.read()

if "--strip" in sys.argv[2:]:
    data = data.upper()
    i = 0
    for c in data:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ \r\n":
            data = data[:i] + data[(i + 1):]
        i += 1



x = ser.write(data)
ser.close()

if "--debug" in sys.argv[2:]:
    sys.stdout.write(data + "\n")
