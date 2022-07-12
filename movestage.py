import serial
import argparse

def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("MR", type=int, help="Move right")
    parser.add_argument("-P", "--port", type=str, default='/dev/ttyUSB1', help='port')
    #ttyUSB0 is rotation stage and 1 is linear stage with the setup in 119, as of 20220712
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parsing()

    ser = serial.Serial(port=args.port, baudrate=9600)
    ser.flush()
    ser.write('MR {}\r\n'.format(args.MR))
    print("stage moved")
    ser.close()
