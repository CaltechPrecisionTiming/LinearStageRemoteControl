import serial
import argparse

def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("MR", type=int, help="Move right")
    parser.add_argument("-k", "--step2mm", type=float, default=3.96e-05  ,help="Conversion Factor (mm/step)")
    parser.add_argument("-P", "--port", type=str, default='/dev/ttyUSB0', help='port')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parsing()

    ser = serial.Serial(port=args.port, baudrate=9600)
    ser.flush()
    ser.write('MR {}\r\n'.format(args.MR))
    print("stage moved")
    ser.close()
