import multiprocessing as mp
import time
def satu(number):
        print (0+number)
        time.sleep(1)
def dua(number):
        print(1+number)
        time.sleep(1)


if __name__ == "__main__":
    # p1 = mp.Process(target=satu, args=(1,))
    # p2 = mp.Process(target=dua, args=(1,))
    start = time.time()
    satu(1)
    dua(1)

    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    end= time.time()
    
    print(end -start)