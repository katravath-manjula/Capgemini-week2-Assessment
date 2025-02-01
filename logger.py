class Logger:
    def log(self, message, level):
        if level == "error":
            print(f"{message}")
        elif level == "warning":
            print(f"{message}")
        else:  
            print(f"{message}")


logger = Logger()
logger.log("System started")  
logger.log("Low disk space", "warning")
logger.log("File not found", "error")
