import time

class Stopper:

    def __init__(self, time):

        self.time = time

        return

    def run(self):

        time.sleep(self.time)

        return 0.0