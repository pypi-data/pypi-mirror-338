# instance/component.py
from typing import Type

from abundance.core.instance.instance_container import Instance

class component:


    def __init__(self, cls: Type):
        self.cls = cls
        # 将被装饰的类添加到注册列表中
        Instance.registered_components.append(cls)

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)