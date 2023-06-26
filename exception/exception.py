#-*-coding:utf-8-*-

import time
import socket

def main():
    PAGE_SIZE = 0
    try:

        a = 100 / 2
        # a == a
  
    except ZeroDivisionError as e:
        print('catch zero division exception')
    
    except Exception as e:
        print(f'catch all exception: {e}')
        
    finally:
        print("close file in finally")
        #f.close()


if __name__ == '__main__':
    main()



