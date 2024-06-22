

def outer(func):
    def inner():
        print("to sleep")
        func()
        print("wake up")
    return inner

def sleep():
    import time
    import random
    print ("sleeping")
    time.sleep(random.randint(1, 5))

fn = outer(sleep)
print("fn is ", type(fn))
fn()
