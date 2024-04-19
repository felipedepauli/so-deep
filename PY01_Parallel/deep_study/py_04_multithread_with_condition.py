import time
from threading import Thread, Condition

class StinySpendy:
    def __init__(self):
        self.money = 100         # The initial amount of money
        self.cv = Condition()      # The mutex (Lock) used to control access to the shared resource
    
    def stingy(self):
        for i in range(1_000_000):    
            self.cv.acquire()    # Lock the mutex before accessing the shared resource
            self.money += 10     # Increment the money by 10
            self.cv.notify()     # Notify the other thread that the condition has been met
            self.cv.release()    # Release the mutex after accessing the shared resource
        print("Stingy done")
        
    def spendy(self):
        for i in range(500_000):
            self.cv.acquire()       # Lock the mutex before accessing the shared resource
            while self.money < 20:
                self.cv.wait()      # Wait for the condition
            self.money -= 20        # Decrement the money by 10
            if self.money < 0:
                print("Money in the bank", self.money)
            self.cv.release()       # Release the mutex after accessing the shared resource
        print("Spendy done")
        
    def main(self):
        stingy_thread = Thread(target=self.stingy)
        spendy_thread = Thread(target=self.spendy)
        stingy_thread.start()
        spendy_thread.start()
        stingy_thread.join()
        spendy_thread.join()
        print(f"Final amount of money: {self.money}")
        
ss = StinySpendy()
ss.main()