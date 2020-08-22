from multiprocessing import Process
import time
import threading

def f(name):
    print ('hello', name)

def w(x):
    time.sleep(x)

if __name__ == '__main__':
    # defining the processes
    p = Process(target=f, args=('bob',))
    q = threading.Thread(target=w, args=(5,))
    print('processing starting...')

    # starting the processes
    q.start()
    p.start()
    print('and now joining...')

     # wait until q is completely executed
    q.join()
    p.join()
    print('and now finished.')