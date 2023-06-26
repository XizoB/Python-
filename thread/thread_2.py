#-*-coding:utf-8-*-
import threading
import time
import sys


sys.setswitchinterval(0.0000001)
a = 0

l = threading.Lock()
rl = threading.RLock()

def add():
    global a
    global l

    for i in range(1000):
        l.acquire()
        a = a + 1
        l.release()


def add_with_rlock():
    global a
    global rl

    for i in range(1000):
        rl.acquire()
        rl.acquire()
        a = a + 1
        rl.release()
        rl.release()

def main():
    global a

    threads =[]
    for i in range(5):
        # t = threading.Thread(target = add)
        t = threading.Thread(target = add_with_rlock)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f'****all threads finished. a = {a}')

if __name__ == '__main__':
    main()