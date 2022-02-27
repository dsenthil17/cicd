import argparse
import sys

if __name__=='__main__':

    parser = argparse.ArgumentParser(
        description="Script for print message",
        usage='''printmessage.py [-h] -m'''
    )
    parser.add_argument('-m', '--input-msg', dest='msg')
    args = parser.parse_args(sys.argv[1:])

    print args.msg
