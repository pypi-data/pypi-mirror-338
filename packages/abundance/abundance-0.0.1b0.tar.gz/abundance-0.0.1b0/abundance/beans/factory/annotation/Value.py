from abundance.core.env.ApplicationEnvironment import ApplicationEnvironment


class Value:
    def __init__(self, key_path, default=None):
        """
        初始化 Value 类，接收键路径和默认值
        :param key_path: 键路径，用于从环境配置中获取值
        :param default: 默认值，如果键路径对应的配置值不存在则使用该默认值
        """
        self.key_path = key_path
        self.default = default

    def __call__(self, func):
        """
        使类的实例可调用，作为装饰器使用
        :param func: 被装饰的函数
        :return: 包装后的函数
        """

        def wrapper(*args, **kwargs):
            value = ApplicationEnvironment().get(self.key_path, self.default)
            # 调用原函数并传递获取到的值
            return func(value, *args, **kwargs)
        return wrapper