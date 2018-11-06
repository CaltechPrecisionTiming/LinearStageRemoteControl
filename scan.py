import argparse
import os

def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument("SCANS", type=int, help="Number of scans")
    parser.add_argument("MR", type=int, help="How much to move right")
    parser.add_argument("-N", "--N_evts", type=int, default=501, help="Number of events per scan; default=1000")
    parser.add_argument("-D", "--delay", type=float, default=150, help="Delay time (ns); default=150")
    parser.add_argument("-T", "--trigger", type=float, default=0.1, help="Trigger level; default=0.1")
    parser.add_argument("-F", "--filename", type=str, default="/home/lab-cpt03/LabData/Linus/180508/waveform_2pulses_", help="Name of files to be saved; do not add .dat")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parsing()
    N_scans = args.SCANS
    name = args.filename
    mr = args.MR

    #for x in range(0, N_scans):

    os.system("/home/lab-cpt03/DRS/drs-5.0.6/drs_cldaq " + str(args.N_evts) + ' ' + str(args.trigger) + ' '+ str(args.delay) + ' '+ str(args.filename) + ' '+ str(N_scans) + ' ' + str(mr) ) # Run data acquisition system

        #os.system("/home/lab-cpt03/programs/TimingDAQ/DRSclDat2Root --input_file=/home/lab-cpt03/LabData/Linus/180508/waveform_2pulses_" + str(x)+".dat --config=./config/CPTLab/DRS_trial180504.config") # Run root conversion code



        #os.system("/home/lab-cpt03/RemoteStation sudo python movestage.py " + str(args.MR)) # Run stage moving code

    #    os.system("sudo python movestage.py " + str(args.MR)) # Run stage moving code
