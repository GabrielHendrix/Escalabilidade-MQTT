from sys import argv
import paho.mqtt.client as mqtt
import threading
import time
import os


def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(len(msg.payload)))


def run():
    mqttc = mqtt.Client()
    mqttc.on_message = on_message
    mqttc.connect(str(argv[2]), 1883, 60)
    mqttc.subscribe(str(argv[3]), 0)
    mqttc.loop_forever()


def main():
    number_of_subscribers = 1
    new_number_of_subscribers = 2
    if len(argv) < 3:
        print("Args: type_of_test broker_host topic")
        print("Options for type_of_test: payloadTest / publisherTest / publisherAndSubscriberTest")
        print("Exemplo: payloadTest localhost teste")
        exit(0)
    init_time = time.time()
    if str(argv[1]) == "publisherAndSubscriberTest":
        while (time.time() - init_time) < 600:
            if (time.time() - init_time) > 120:
                new_number_of_subscribers = 2
            if (time.time() - init_time) > 240:
                new_number_of_subscribers = 4
            if (time.time() - init_time) > 360:
                new_number_of_subscribers = 8
            if (time.time() - init_time) > 480:
                new_number_of_subscribers = 16


            for _ in range(new_number_of_subscribers - number_of_subscribers):
                number_of_subscribers = new_number_of_subscribers
                threading.Thread(target=run).start()
        os.system("killall python3")
    else:
        run()

if __name__ == "__main__":
    main()
