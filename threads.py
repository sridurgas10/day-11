import threading

def even_num():
    for i in range(1,9):
        if i%2==0:
            print(i)
        else:
            continue

def odd_num():
    for j in range(1,9):
        if j%2==0:
           continue
        else:
            print(j)

t1=threading.Thread(target=even_num)
t2=threading.Thread(target=odd_num)

t1.start()
t2.start()

t1.join()
t2.join()

print("done")

  