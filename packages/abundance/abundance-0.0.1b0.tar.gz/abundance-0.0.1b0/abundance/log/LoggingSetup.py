import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import colorama
from colorama import Fore, Style

# 初始化 colorama
colorama.init()

# 定义不同日志级别的颜色
COLORS = {
    logging.DEBUG: Fore.CYAN,
    logging.INFO: Fore.GREEN,
    logging.WARNING: Fore.YELLOW,
    logging.ERROR: Fore.RED,
    logging.CRITICAL: Fore.MAGENTA
}

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        # 保存原始的 format 函数返回的消息
        original_msg = super().format(record)
        # 获取当前日志级别的颜色
        color = COLORS.get(record.levelno, '')
        # 为消息添加颜色
        colored_msg = f"{color}{original_msg}{Style.RESET_ALL}"
        return colored_msg

class LoggingSetup:
    _instance = None

    def __new__(cls, env):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_logging(env)
        return cls._instance

    def _init_logging(self, env):
        # 从环境中获取日志相关配置
        log_levels = env.get('logging.level', {})
        log_format = env.get('logging.format', '%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        log_datefmt = env.get('logging.datefmt', '%Y-%m-%d %H:%M:%S')
        log_file_config = env.get('logging.file', {})
        log_file_location = log_file_config.get('location', '/')
        log_file_name = log_file_config.get('name', 'abundance.log')
        log_segment = log_file_config.get('segment', 'time')  # 新增日志分割方式配置，默认为按时间分割
        log_maxBytes = log_file_config.get('max-size', 10 * 1024 * 1024)
        log_backupCount = log_file_config.get('max-history', 50)
        log_encoding = log_file_config.get('encoding', 'utf-8')

        # 禁用默认的日志配置
        logging.getLogger().handlers.clear()

        # 创建日志记录器
        for key, level in log_levels.items():
            logger = logging.getLogger(key)
            logger.setLevel(getattr(logging, level))

            # 检查是否已经有控制台处理器，没有则添加
            has_console_handler = any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)
            if not has_console_handler:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(getattr(logging, level))
                # 使用彩色格式化器
                console_formatter = ColoredFormatter(log_format, datefmt=log_datefmt)
                console_handler.setFormatter(console_formatter)
                logger.addHandler(console_handler)

            # 如果配置了日志文件，则添加相应的 FileHandler
            if log_file_config:
                full_log_file_path = os.path.join(log_file_location, log_file_name)
                path = os.path.dirname(full_log_file_path)
                if path and not os.path.exists(path):
                    os.makedirs(path, exist_ok=True)

                # 检查是否已经有文件处理器，没有则添加
                has_file_handler = any(isinstance(handler, (TimedRotatingFileHandler, RotatingFileHandler)) for handler in logger.handlers)
                if not has_file_handler:
                    if log_segment == "time":
                        # 按时间分割日志文件，每天一个文件，保留50个文件，设置 delay=True
                        file_handler = TimedRotatingFileHandler(full_log_file_path, when='D', backupCount=log_backupCount,
                                                                encoding=log_encoding, delay=True)
                    else:
                        # 设置 delay=True
                        file_handler = RotatingFileHandler(full_log_file_path, maxBytes=log_maxBytes,
                                                           backupCount=log_backupCount,
                                                           encoding=log_encoding, delay=True)
                    file_handler.setLevel(getattr(logging, level))
                    file_formatter = logging.Formatter(log_format, datefmt=log_datefmt)
                    file_handler.setFormatter(file_formatter)
                    logger.addHandler(file_handler)