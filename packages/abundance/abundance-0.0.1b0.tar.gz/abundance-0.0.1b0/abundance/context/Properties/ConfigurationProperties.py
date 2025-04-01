from abundance.core.env.ApplicationEnvironment import ApplicationEnvironment

def ConfigurationProperties(prefix):
    def decorator(cls):
        def wrapper():
            # 读取配置文件
            env = ApplicationEnvironment()
            instance = cls()
            # 遍历类的属性
            for attr in dir(instance):
                if not attr.startswith('__'):
                    # 构造配置文件中的属性名
                    config_key = f"{prefix}.{attr}"
                    # 获取配置文件中的属性值
                    value = env.get(config_key)
                    # 设置类的实例属性
                    if value is not None: setattr(instance, attr, value)
            return instance
        return wrapper
    return decorator