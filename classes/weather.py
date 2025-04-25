class Weather:
    def __init__(self, lst):
        self.lst = lst
    def __contains__(self, item):
        if item in self.lst:
            return True
        else:
            return False
w1 = Weather(["temperature", "humidity", "carbon emission"])
print("Humidity" in w1)
