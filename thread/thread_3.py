#-*-coding:utf-8-*-
import threading
import time
import random

items = []
con = threading.Condition()

def consume():
    global items
    global con
    while True:
        con.acquire()
        if len(items) == 0:
            print('wait for item')
            con.wait()

        v = items.pop()
        print(f'consume item: {v}')
        con.release()

        time.sleep(0.1)

def produce():
    global items
    global con
    while True:
        con.acquire()

        v = random.randint(0, 1000)
        items.append(v)
        print(f'produce item: {v}')
        con.notify()
        con.release()

        time.sleep(1)


def main():
    pt = threading.Thread(target = produce)
    ct = threading.Thread(target = consume)

    pt.start()
    ct.start()

    pt.join()
    print("pt done")

if __name__ == '__main__':
    main()