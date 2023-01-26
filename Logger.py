import sys
class Logger: 
    def __init__(self, filepath = None):
        self.logfile = filepath if filepath else "stdout";

    def _write_log(self, level, message):
        # Date\t level\t message
        # 7-strlen(level), 7 = longest level string (verbose) - characters in level to equal space the log
        data = "%s - [%s]%s - %s" % (datetime.now(), level, 7-strlen(level), message) 
        with (open(self.logfile, "a") if self.logfile != "stdout" else sys.stdout) as out: 
            out.write(data)

    # Define wrapper functions
    def info(self, message):
        return self._write_log("INFO", message)

    def warn(self, message):
        return self._write_log("WARN", message)

    def error(self, message):
        return self._write_log("ERROR", message)

    def verbose(self, message):
        return self._write_log("VERBOSE", message)

    def debug(self, message):
        return self._write_log("DEBUG", message)

if __name__ == "__main__":
    pass # We are an import!
