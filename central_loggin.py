import logging

class CentralLog:
    def __init__(self,level: str,logger_name: str)-> None:
        self.logger_name=logger_name
        self.logger_obj=logging.getLogger(self.logger_name)

        if level.lower() == "debug":
            self.level=logging.DEBUG
        elif level.lower() == "info":
            self.level=logging.INFO
        else:
            self.level=None
        self.logger_obj.setLevel(self.level)

    def debug(self,msg:str)->str:
        self.logger_obj.debug(msg)
        return self.logger_obj
            
    def info(self,msg:str)->str:
        self.logger_obj.info(msg)
        return self.logger_obj


dk_test=CentralLog("debug","api_connection")
dk_test.debug("I am the debug message ")
dk_test.info("I am the info message ")
print("done")
