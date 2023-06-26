#-*-coding:utf-8-*-
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, v):
        threading.Thread.__init__(self)
        #super(threading.Thread, self).__init__()
        self.name = 'MyThread-2'
        self.value = v

    
    def run(self):
        for i in range(5):
            print(f'run in thread:{self.name}, value={self.value}')
            time.sleep(1)


def thread_1_run(v):
    t = threading.current_thread()
    for i in range(5):
        print(f'run in thread:{t.name}, value={v}')
        time.sleep(1)


def main():
    thread1 = threading.Thread(target = thread_1_run, name = 'MyThread-1', args=(1,))
    thread2 = MyThread(2)

    thread1.start()
    thread2.start()

    print('----------- all threads run')
    thread1.join()
    thread2.join()

    print('----------- all threads finished.')

if __name__ == '__main__':
    main()