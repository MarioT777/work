import logging
from logging.handlers import RotatingFileHandler
import os
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)#输出到file的log等级的开关
#如果日志文件夹不存在，创建相应的文件夹
logdir='logs'#日志存放文件夹名称
if not os.path.exists(logdir):
    os.makedirs(logdir)
logPath=os.getcwd()+os.sep+logdir
if not os.path.isdir(logPath):
    os.makedirs(logPath)
# 每个日志的最大字节数，及最大的日志文件个数
logHandler=logging.handlers.RotatingFileHandler('filename',maxBytes=30,backupCount=10)
#将日志输出到屏幕
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[%(lineno)d] [%(levelname)s]:%(message)s')

#将日志输出到main.txt
logging.basicConfig(level=logging.DEBUG,
                    filename = '.\logs\info',
                    filemode= 'w',
                    format='%(asctime)s %(filename)s[%(lineno)d] [%(levelname)s]:%(message)s')

#将日志同时输出到屏幕和main.txt
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)#输出到file的log等级的开关
#1 创建一个handler,用于写入日志文件
filename='.\logs\info'
filemode= 'w'
fh=logging.FileHandler(filename,filemode)
fh.setLevel(logging.DEBUG)#输出到file的log等级的开关
#2 再创建一个handler,用来输出到屏幕
ch=logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#3 定义handler的输出格式
formatter=logging.Formatter('%(asctime)s %(filename)s[%(lineno)d] [%(levelname)s]:%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
#4 将logger添加到handler
logger.addHandler(fh)
logger.addHandler(ch)
#日志
logging.info('info')
logging.debug('debug')
logging.warning('warning')
logging.error('error')
logging.critical('critical')




