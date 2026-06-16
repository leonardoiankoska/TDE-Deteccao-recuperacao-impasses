import threading
import time

a = threading.Lock()
b = threading.Lock()

#---------------------------------------------------
def Thread1():
    print("Thread 1 tenta pegar A")
    a.acquire()
    print("Thread1 pegou A")

    time.sleep(1)

    print("Thread 1 tenta pegar B")
    b.acquire()
    print("Thread 1 pegou B")


    print("Thread 1 terminou")

    b.release()
    a.release()

#-----------------------------------------------------
def Thread2():
    print("Thread 2 tenta pegar B")
    b.acquire()
    print("Thread2 pegou B")
    time.sleep(1)


    print("Thread 2 tenta pegar A")
    a.acquire()
    print("Thread2 pegou A ")

    print("Thread 2 terminou")

    a.release()
    b.release()

#--------------------------------------------------
t1 = threading.Thread(target=Thread1)
t2 = threading.Thread(target=Thread2)

t1.start()
t2.start()

t1.join()
t2.join()
print("Fim")