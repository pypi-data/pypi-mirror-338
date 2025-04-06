import logging
import colorlog
import os


class Logger(logging.Logger):
    # 日志级别：（critical > error > warning > info > debug）
    CRITICAL = logging.CRITICAL
    FATAL = logging.FATAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET

    def __init__(self, name=None, file_name=None, console_level=None, file_level=None):
        """
        自定义日志对象
        :param name: logger名称，默认输出日志到控制台
        :param file_name: 输出文件路径，为None则不输出日志到文件
        :param console_level: 控制台日志级别
        :param file_level: 日志文件的日志级别
        """
        if name is None:
            name = 'default_pq_logger'
        
        # 调用父类初始化
        super().__init__(name)
        
        # 阻止日志消息从当前Logger向父级Logger传递
        self.propagate = False

        if console_level is None:
            console_level = self.DEBUG

        if file_level is None:
            file_level = self.WARNING  # # 默认只有error和critical级别才会写入日志文件

        # 指定最低日志级别：（critical > error > warning > info > debug）
        self.setLevel(level=self.DEBUG)

        # 控制台输出不同级别日志颜色设置
        self.color_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'purple',
        }

        # -------------------------
        # 输出到控制台
        # 日志格化字符串
        # -------------------------
        self.add_console_handler(level=console_level)

        # -------------------------
        # 输出到文件
        # -------------------------
        if file_name:
            self.add_file_handler(file_name=file_name, level=file_level)

    def set_name(self, name):
        """
        设置logger的名称，如果此名称的logger不存在，则创建一个新的logger
        如果新建的logger，需要通过：add_console_handler()或者add_file_handler()输出到控制台或者文件
        :param name: logger名称
        :return:
        """
        # 由于Logger类继承自logging.Logger，这里需要重新创建一个新的Logger实例
        # 保存当前的handlers
        handlers = self.handlers[:]
        # 清除当前handlers
        for handler in handlers:
            self.removeHandler(handler)
        
        # 创建新的Logger实例
        new_logger = Logger(name=name)
        
        # 将当前实例的属性复制到新实例
        self.__dict__.update(new_logger.__dict__)
        
        # 重新添加handlers
        for handler in handlers:
            self.addHandler(handler)

    def set_level(self, level=logging.INFO):
        self.setLevel(level)

    def add_console_handler(self, level=logging.DEBUG):
        """
        输出到控制台
        :param level: 日志级别
        :return:
        """
        console_fmt = '%(log_color)s%(asctime)s: %(levelname)s %(message)s'
        console_formatter = colorlog.ColoredFormatter(fmt=console_fmt, log_colors=self.color_config)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(level)
        self.addHandler(console_handler)

    def add_file_handler(self, file_name: str, level=logging.WARNING):
        """
        输出到文件
        :param file_name:
        :param level: 日志级别
        :return:
        """
        import json_log_formatter

        file_formatter = json_log_formatter.VerboseJSONFormatter()
        file_handler = logging.FileHandler(filename=file_name, mode='a', encoding='utf-8')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(level)
        self.addHandler(file_handler)

    def remove_file_handler(self, file_name: str):
        """
        删除输出到文件的handler
        :param file_name:
        :return:
        """
        # 遍历logger的handlers列表
        for handler in list(self.handlers):
            # 检查handler是否是FileHandler且其文件名匹配给定的文件名
            if isinstance(handler, logging.FileHandler):
                # handler.baseFilename 为绝对路径
                if handler.baseFilename == os.path.abspath(file_name):
                    # 从logger的handlers列表中移除handler
                    self.removeHandler(handler)
                    # 关闭handler以释放资源（可选）
                    handler.close()
                    # 如果确定不再需要handler，也可以删除对它的引用（可选）
                    del handler
                    break  # 如果只期望移除一个匹配的handler，则退出循环


# 创建默认的全局logger
log = Logger(name='default_pq_logger')

# ---------------------------------------------------------
# 外部可以访问的列表
# ---------------------------------------------------------
__all__ = ["log", "Logger"]
__all__.extend([name for name in globals().keys() if name.startswith("get")])
