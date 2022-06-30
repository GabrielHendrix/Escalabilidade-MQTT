#!/usr/bin/python

"""
Baseado em 
https://hackmd.io/@ramonfontes/iot-dojot

Modificado para receber como parametro o tempo entre mensagens.
"""

import os
import time
import random
import logging
import threading

from time import sleep
from sys import argv
import sys

logging.basicConfig(level="INFO")

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        print( "base init", file=sys.stderr )
        super(StoppableThread, self).__init__()
        self._stopper = threading.Event()          # ! must not use _stop

    def stopit(self):                              #  (avoid confusion)
        print( "base stop()", file=sys.stderr )
        self._stopper.set()                        # ! must not use _stop

    def stopped(self):
        return self._stopper.is_set()              # ! must not use _stop



class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
 
    # function using _stop function
    def stop(self):
        self._stop.set()
 
    def stopped(self):
        return self._stop.isSet()
 
    def run(self):
        type_of_test = argv[1]
        node = argv[2]
        topic = argv[3]
        attribute = argv[4]
        timeMsg = argv[5]
        data = ""

        port = "1883"

        sleep(1)
        while True:
            if self.stopped():
                sys.exit()
                
                return
            #data = "a"   
            cmd = "mosquitto_pub -h {} -t {} -m \"{}\" -p {}"
            cmd = cmd.format(node, topic, data, port)
            logging.info(cmd)
            os.system(cmd)
            if str(type_of_test) == "payloadTest":
                data += "a"
                # sleep(0.0001)
            else:
                sleep(int(timeMsg)/1000)
    
def main():
    number_of_publishers = 1
    new_number_of_publishers = 2
    threads = []
    if len(argv) < 5:
        print("Args: type_of_test broker_host topic attribute time_between_pubs_ms")
        print("Options for type_of_test: payloadTest / publisherTest / publisherAndSubscriberTest")
        print("Exemplo: payloadTest localhost teste oi 1000")
        exit(0)
        
    if str(argv[1]) == "payloadTest":
        thread = MyThread()
        thread.start()
    else:
        if str(argv[1]) == "publisherTest":
            rounds = 1
        if str(argv[1]) == "publisherAndSubscriberTest":
            rounds = 5
        for _ in range(rounds):
            init_time = time.time()
            print(_)
            while (time.time() - init_time) < 120:
                if (time.time() - init_time) > 10:
                    new_number_of_publishers = 2
                if (time.time() - init_time) > 20:
                    new_number_of_publishers = 4
                if (time.time() - init_time) > 40:
                    new_number_of_publishers = 8
                if (time.time() - init_time) > 50:
                    new_number_of_publishers = 16
                if (time.time() - init_time) > 60:
                    new_number_of_publishers = 32
                if (time.time() - init_time) > 70:
                    new_number_of_publishers = 64
                if (time.time() - init_time) > 80:
                    new_number_of_publishers = 128
                if (time.time() - init_time) > 90:
                    new_number_of_publishers = 256
                if (time.time() - init_time) > 100:
                    new_number_of_publishers = 512
                if (time.time() - init_time) > 110:
                    new_number_of_publishers = 1024
                
            
                for _ in range(new_number_of_publishers - number_of_publishers):
                    number_of_publishers = new_number_of_publishers
                    thread = MyThread()
                    thread.start()
                    threads.append(thread)
                    
            for thread in threads:
                thread.stop()
            # thread.join()
        exit()
    

if __name__ == "__main__":
    main()
