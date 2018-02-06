from multiprocessing import Pool
import os, time, random

def long_time_tast(name):
    print('Run tast %s (%s)...' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 30)
    end = time.time()
    print('Task %s runs %0.2f seconds.' %(name, (end -start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    ppp = Pool(4)
    for i in range(5):
        ppp.apply_async(long_time_tast, args=(i,))
    print('Waiting for all subprocess done...')
    ppp.close()
    ppp.join()
    print('All subprocesses done.')