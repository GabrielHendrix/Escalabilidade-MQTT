#!/bin/bash

delay=1; # customize it
while true; do
#ps -C  python3 test.py 10 -o pid=3138477,%mem=,vsz= >> /tmp/mem.log
     ps -C  python3 -o %cpu=,%mem= >> mem.dat
     gnuplot show_mem.plt
     sleep $delay
done 
