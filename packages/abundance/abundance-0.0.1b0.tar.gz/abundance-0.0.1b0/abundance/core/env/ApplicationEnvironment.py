from abundance.core.env.Environment import Environment
from abundance.util.path_utils import PathUtils


class ApplicationEnvironment(Environment):
    # 类属性，用于保存单例实例
    _instance = None

    def __new__(cls, source=None):
        # 如果实例还未创建，则创建一个新实例
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # 在这里进行初始化操作
            cls._instance.property_sources = source
        return cls._instance

    def get(self, key_path=None, default=None):
        return PathUtils.auto_fill_resources_path(super().get(key_path, default))