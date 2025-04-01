# autotest_databridge/route.py

# 初始化路由映射表
ROUTE_MAPPING = {}

# 定义路由注解
def route(path):
    def decorator(func):
        ROUTE_MAPPING[path] = func
        return func
    return decorator