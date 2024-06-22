import time
import threading
def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)



if __name__ == '__main__':
    t1 = threading.Thread(target=sing,args=('唱',))
    t2 = threading.Thread(target=dance,args=('跳',))
    t1.start()
    t2.start()