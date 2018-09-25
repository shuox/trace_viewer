#!/usr/bin/env python3

import argparse
import sys,re,os

# 55681:SOS          vcpu 0-436   [000] .... 889251407412: acrn_ioreq_complete_request: ioreq[ffff88003e288000] complete, create ts[889251360652] [889251366716] [889251367458] [889251368012] [0] [0] [0]
def ioreq_hv_ts(filename):
    interval1 = 0
    interval2 = 0
    interval3 = 0
    interval4 = 0
    interval5 = 0
    interval6 = 0
    print("open file {}".format(filename))
    pa = re.compile(r'\[(\d*)\]')
    count = 0
    with open(filename) as f:
        for line in f.readlines():
            ts = pa.findall(line)
            if int(ts[-5]) == 0 or int(ts[-6]) == 0 or int(ts[-4]) == 0:
                continue
            count = count + 1
            #interval6 += int(ts[-1]) - int(ts[-2])
            #interval5 += int(ts[-2]) - int(ts[-3])
            interval4 += int(ts[-3]) - int(ts[-4])
            interval3 += (int(ts[-4]) - int(ts[-5]))
            interval2 += (int(ts[-5]) - int(ts[-6]))
            interval1 += (int(ts[-6]) - int(ts[-7]))
        print("interval1 {}".format(interval1/count))
        print("interval2 {}".format(interval2/count))
        print("interval3 {}".format(interval3/count))
        print("interval4 {}".format(interval4/count))
        print("count {}".format(count))
        #print("interval5 {}".format(interval5/count))
        #print("interval6 {}".format(interval6/count))

def parse_init():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--logfile',
                        required=True,
                        help='log file')
    return parser

if __name__ == "__main__":
    print("haha")
    parser = parse_init()
    args = parser.parse_args()

    logfile = args.logfile

    ioreq_hv_ts(logfile)
