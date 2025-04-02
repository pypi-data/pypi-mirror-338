from datetime import datetime
import json
import inspect


class ct_logging:
    def __init__(self, logLocations, mode=""):
        self.timegenerated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.Loglocation = logLocations
        self.currentfile = (inspect.getframeinfo(
            inspect.currentframe().f_back).filename).split("/")[-1]
        self.mode = mode
        with open((self.Loglocation)+"/logFile.json", "w+") as LogFIle:
            start = json.dumps([])
            LogFIle.write(start)

    def createJsonFile(self, data):
        data = [data]
        currentData = ""
        with open((self.Loglocation)+"/logFile.json", "r") as LogFIle:
            try:
                currentData = json.loads(LogFIle.read())
            except:
                currentData = LogFIle.read()
        with open((self.Loglocation)+"/logFile.json", "w") as LogFIle:
            newData = str(currentData)+str(data)
            newData = json.dumps(newData)
            LogFIle.write(newData)

    def __getCurrentTimeIso(self):
        currentTime = datetime.now()
        currentTimeIso = currentTime.isoformat()
        return currentTimeIso

    def error(self, message):
        log = {
            "timegenerated": self.timegenerated,
            "date_time": self.__getCurrentTimeIso(),
            "source_log": self.currentfile,
            "log_level": "ERROR",
            "message": message
        }
        self.createJsonFile(log)
        print(log)

    def info(self, message):
        log = {
            "timegenerated": self.timegenerated,
            "date_time": self.__getCurrentTimeIso(),
            "source_log": self.currentfile,
            "log_level": "INFO",
            "message": message
        }
        self.createJsonFile(log)
        print(log)

    def warning(self, message):
        log = {
            "timegenerated": self.timegenerated,
            "date_time": self.__getCurrentTimeIso(),
            "source_log": self.currentfile,
            "log_level": "WARNING",
            "message": message
        }
        self.createJsonFile(log)
        print(log)

    def critical(self, message):
        log = {
            "timegenerated": self.timegenerated,
            "date_time": self.__getCurrentTimeIso(),
            "source_log": self.currentfile,
            "log_level": "CRITICAL",
            "message": message
        }
        self.createJsonFile(log)
        print(log)

    def debug(self, message):
        if (self.mode == "debug"):
            log = {
                "timegenerated": self.timegenerated,
                "date_time": self.__getCurrentTimeIso(),
                "source_log": self.currentfile,
                "log_level": "DEBUG",
                "message": message
            }
            self.createJsonFile(log)
            print(log)
