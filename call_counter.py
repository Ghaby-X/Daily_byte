# This question is asked by Google. Create a class CallCounter that tracks the number of calls a client has made within the last 3 seconds. Your class should contain one method, ping(int t) that receives the current timestamp (in milliseconds) of a new call being made and returns the number of calls made within the last 3 seconds.
# Note: you may assume that the time associated with each subsequent call to ping is strictly increasing.

# Ex: Given the following calls to ping…

# ping(1), return 1 (1 call within the last 3 seconds)
# ping(300), return 2 (2 calls within the last 3 seconds)
# ping(3000), return 3 (3 calls within the last 3 seconds)
# ping(3002), return 3 (3 calls within the last 3 seconds)
# ping(7000), return 1 (1 call within the last 3 seconds)

class CallCounter:
    def __init__(self) -> None:
        self.time = []
    
    def ping(self, t: int) -> None:
        self.time.append(t)
        greater_idx = t - 3000
        count = 0
        
        for i in self.time:
            if i > greater_idx:
                count = count + 1
                
        print(count)
        return
    
counter = CallCounter()

counter.ping(1)     # return 1
counter.ping(300)   # return 2
counter.ping(3000)  # return 3
counter.ping(3002)  # return 3
counter.ping(7000)  # return 1