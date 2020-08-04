import logging
import os
from logging.handlers import RotatingFileHandler

'''
调用方式：
logger = logger.Logger(logPath, logFileName, logMaxFileSize, logMaxFileNum, logOutType, logLevel).getLogger()
logger.debug("debug")
logger.info("info")
logger.error("info")

    # logOutType == terminal: 只打印到命令行
    # logOutType == file: 只打印到日志文件
    # logOutType == all: 同时打印到日志文件和命令行
    # logLevel = 'CRITICAL','ERROR','WARNING','INFO','DEBUG'

'''


class Logger:

    def __init__(self, logPath, logFileName, logMaxFileSize=30, logMaxFileNum=10,
                 logOutType="all", logLevel="DEBUG"):
        self.logMaxFileSize = int(logMaxFileSize)
        self.logMaxFileNum = int(logMaxFileNum)
        self.logger = logging.getLogger()
        self.logger.setLevel(logLevel.upper())#.upper()字符串全部转换成大写字母
        info = '''
                logOutType == terminal: 只打印到命令行
                logOutType == file: 只打印到日志文件
                logOutType == all: 同时打印到日志文件和命令行
                logLevel = 'CRITICAL','ERROR','WARNING','INFO','DEBUG'
            '''
        self.logFileName = os.path.join(logPath, logFileName +'.log')
        self.fileOrTerminal = logOutType.lower()#.lower()字符串全部转换成小写

    def getLogger(self):
        logFormatter = logging.Formatter(
            fmt='%(asctime)s,%(msecs)d %(filename)s[%(lineno)d] [%(levelname)s] %(message)s [tid:%(thread)s '
                'funName:%(funcName)s]')

        def onlyFile():
            logFileHandler = RotatingFileHandler(filename=self.logFileName, mode='a', maxBytes=self.logMaxFileSize,
                                     encoding='utf8', backupCount=self.logMaxFileNum)
            logFileHandler.setFormatter(logFormatter)
            self.logger.addHandler(logFileHandler)
            return self.logger

        def onlyTerminal():
            logStreamHandler = logging.StreamHandler()
            logStreamHandler.setFormatter(logFormatter)
            self.logger.addHandler(logStreamHandler)
            return self.logger

        def fileAndTerminal():
            onlyFile()
            onlyTerminal()
            return self.logger

        choiceDict = {
            "terminal": onlyTerminal,
            "file": onlyFile,
            "all": fileAndTerminal,
        }

        if choiceDict.get(self.fileOrTerminal):
            return choiceDict.get(self.fileOrTerminal)()
        else:
            return choiceDict.get("file")()
