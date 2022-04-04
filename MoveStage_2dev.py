import serial
import argparse

def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("MA", type=int, help="Move to absolute position")
    parser.add_argument("-k", "--step2mm", type=float, default=3.96e-05  ,help="Conversion Factor (mm/step)")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parsing()

    rotation = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
    linear = serial.Serial(port='/dev/ttyUSB1', baudrate=9600)
    linear.flush()
    rotation.flush()
    linear.write('MA {}\r\n'.format(args.MA))
    rotation.write('MA {}\r\n'.format(args.MA))
    print("stage moved")
    rotation.close()
    linear.close()
