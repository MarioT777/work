import logging, logging.handlers,  os
#-*-conding:utf-8-*-
class Logger:
    def __init__(self,logOutType='all'):
        """
        :param 定义对应的程序模块名name，默认为root
        :param logOutType: 日志输出类型，terminal：输出到控制台；file：输出到文件；all：同时输出到控制台和文件
        """
        self.logPath = 'C:/Users/888/Desktop/logs'
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)
        # 设置日志文件名
        self.logFileName = self.logPath + '/' + 'info'
        # 设置日志等级
        self.logLevel = logging.DEBUG
        # 设置日志最大字节数
        self.logMaxFileNum = 30
        # 设置日志最大文件数
        self.logMaxFileSize = 10
        # 设置日志输出格式
        self.formatter = logging.Formatter(
            '%(asctime)s %(filename)s[%(lineno)d] [%(levelname)s]:%(message)s')
        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(self.logLevel)  # 输出到file的log等级的开关

        if logOutType == 'terminal':
            # 创建一个StreamHandler,用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(self.logLevel)

            # 将定义好的输出形式添加到handler
            ch.setFormatter(self.formatter)
            # 给logger添加handler
            self.logger.addHandler(ch)
        elif logOutType == 'all':
            # 创建一个StreamHandler,用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(self.logLevel)
            # 将定义好的输出形式添加到handler
            ch.setFormatter(self.formatter)
            # 给logger添加handler
            self.logger.addHandler(ch)
            # 创建一个handler写入所有日志
            fh = logging.handlers.RotatingFileHandler(filename=self.logFileName,
                                                      maxBytes=self.logMaxFileNum,
                                                      backupCount=self.logMaxFileSize)
            # 设置日志等级
            fh.setLevel(self.logLevel)

            # 将定义好的输出形式添加到handler
            fh.setFormatter(self.formatter)

            # 给logger添加handler
            self.logger.addHandler(fh)

        else:
            # 日志写入到文件
            # 创建一个handler写入所有日志
            fh = logging.handlers.RotatingFileHandler(filename=self.logFileName,
                                                      maxBytes=self.logMaxFileNum,
                                                      backupCount=self.logMaxFileSize)
            # 设置日志等级
            fh.setLevel(self.logLevel)
            # 设置handler的格式对象
            fh.setFormatter(self.formatter)
            # 将handler增加到logger中
            self.logger.addHandler(fh)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

if __name__ == "__main__":
    logger = Logger('terminal')
    logger.info("info")
    logger.debug("debug")
    logger.error("error")
    logger.warning("warning")
    logger.critical("critical")





