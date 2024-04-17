import time
from threading import Thread, Lock

class StingySpendy:
    money = 100     # Initial amount of money
    mutex = Lock()  # Mutex to control access to the shared resource
    
    def stingy(self):
        for i in range(1000000):    # Stingy will increment the money by 10
            self.mutex.acquire()    # Lock the mutex before accessing the shared resource
            self.money += 10        # Increment the money by 10
            self.mutex.release()    # Release the mutex after accessing the shared resource
        print("Stingy done")
        
    def spendy(self):
        for i in range(1000000):    # Spendy will decrement the money by 10
            self.mutex.acquire()    # Lock the mutex before accessing the shared resource
            self.money -= 10        # Decrement the money by 10
            self.mutex.release()    # Release the mutex after accessing the shared resource
        print("Spendy done")
        
    # If either stingy or spendy tries to access the shared resource, the mutex will be locked. If the mutex is already locked, the thread will wait until the mutex is unlocked. The thread will be blocked until the mutex is unlocked.
    
    def main(self):
        stingy_thread = Thread(target=self.stingy)
        spendy_thread = Thread(target=self.spendy)
        stingy_thread.start()
        spendy_thread.start()
        stingy_thread.join()
        spendy_thread.join()
        print(f"Final amount of money: {self.money}")
        
ss = StingySpendy()
ss.main()