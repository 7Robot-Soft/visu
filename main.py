#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from interface import Interface
from settings import HOST, PORT
import argparse
import socket
sys.path.append("../atp")
from channel import Channel
from math import pi

def callback(visu, name, args):
    if name == "pos":
        #visu.moveRotateRobot(args["x"]*100+150, args["y"]*100+100, -args["theta"]/pi*180)
        visu.moveRotateRobot((args["x"]+1.5-0.15)*200, (-args["y"]+1-0.15)*200, 90-(args["theta"]/pi*180))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("host", nargs="?", help="Set host to connect.")
    parser.add_argument("port", nargs="?", help="Set port to connect.")
    args = parser.parse_args()

    if args.host:
        host = args.host
    else:
        host = HOST

    if args.port:
        port = args.port
    else:
        port = PORT

    print("Connecting to %s:%s…" %(host, port))
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode='rw')

    print("Launching interface…")
    inter = Interface()

    print("Creating channel…")
    channel = Channel(f.buffer, lambda name, args, visu = inter:
            callback(visu, name, args), proto = "asserv")

    print("All done!")

    sys.exit(inter.getAppHandle().exec_())
