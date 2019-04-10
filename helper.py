class Helper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

    @staticmethod
    def generateTimestamp():
        import time
        t = time.time()
        timestamp = int(t)
        timeArray = time.localtime(timestamp)
        otherStyleTime = time.strftime("%Y%m%d_%H%M%S", timeArray)
        return otherStyleTime

    @staticmethod
    def getdatetime():
        import time
        t = time.time()
        timestamp = int(t)
        timeArray = time.localtime(timestamp)
        otherStyleTime = time.strftime("%Y.%m.%d", timeArray)
        return otherStyleTime

    @staticmethod
    def validatepath(path):
        import os
        path = path.strip()
        isExists = os.path.exists(path)
        return isExists