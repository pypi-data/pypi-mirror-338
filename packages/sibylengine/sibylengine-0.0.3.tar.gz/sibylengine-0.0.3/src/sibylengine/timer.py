import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.total_time = 0.0
        self.count = 0
        
    def start_timing(self):
        if self.start_time is None:
            self.start_time = time.time()
        else:
            print("Timer is already running.")

    def end(self):
        if self.start_time is not None:
            elapsed = time.time() - self.start_time
            self.total_time += elapsed
            self.count += 1
            self.start_time = None
        else:
            print("Timer is not running.")
        
    def restart(self):
        self.end()
        self.total_time = 0.0
        self.count = 0

    def get(self):
        if self.count == 0:
            return 0.0
        return self.total_time / self.count
