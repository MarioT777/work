import os
import configparser

from logger import Logger

# 项目路径
rootDir = os.path.split(os.path.realpath(__file__))[0]

# config.ini文件路径
configFilePath = os.path.join(rootDir, 'config.ini')


def getConfigValues(section, option):
    """
    根据传入的section获取对应的value
    :param section: ini配置文件中用[]标识的内容
    :param option:  ini配置文件中属性名字
    :return:        返回ini配置文件中对应属性的属性值
    """
    __config = configparser.ConfigParser()
    __config.read(configFilePath)
    return __config.get(section=section, option=option)

if __name__ == '__main__':
    # 读取日志的配置参数
    logOutType = getConfigValues('LogParam', 'logOutType')
    logPath = rootDir + getConfigValues('LogParam', 'logPath')
    logFileName = getConfigValues('LogParam', 'logFileName')
    logLevel = getConfigValues('LogParam', 'logLevel')
    logMaxFileNum = int(getConfigValues('LogParam', 'logMaxFileNum'))
    logMaxFileSize = int(getConfigValues('LogParam', 'logMaxFileSize'))  # 单位为M
    # 获取日志对象
    logger = Logger(logPath, logFileName, logMaxFileSize, logMaxFileNum, logOutType, logLevel).getLogger()

    logger.info('*' * 25 + '数据处理分析报告' + '*' * 25)

