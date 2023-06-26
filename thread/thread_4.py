#-*-coding:utf-8-*-
import threading
import time
import random

THREAD_NUM = 3

def allworkersdone():
    print('all workers done.')

b = threading.Barrier(THREAD_NUM, action = allworkersdone)

def work(name):
    t = random.randint(3, 10)
    time.sleep(t)
    print(f'worker {name} used {t} secs.')
    b.wait()

    print(f'worker {name} now have a rest.')

def main():
    threads = []
    names = ['A', 'B', 'C']
    for i in range(THREAD_NUM):
        t = threading.Thread(target = work, args=(names[i],))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        print("{} done".format(t))

if __name__ == '__main__':
    main()