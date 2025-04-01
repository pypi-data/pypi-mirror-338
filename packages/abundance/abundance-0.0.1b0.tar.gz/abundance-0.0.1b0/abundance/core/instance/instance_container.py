import importlib
import inspect
from typing import Any, Dict, Type

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class InstanceContainer(metaclass=SingletonMeta):
    def __init__(self):
        self._components: Dict[str, Any] = {}

    def register(self, name: str, instance: Any):
        if name not in self._components:
            self._components[name] = instance

    def get(self, name: str) -> Any:
        return self._components.get(name)

    def resolve_dependencies(self, instance: Any):
        # 获取实例的类型注解
        annotations = getattr(instance.__class__, '__annotations__', {})
        for attr_name, attr_type in annotations.items():
            type_obj = annotations.get(attr_name).cls
            if hasattr(type_obj, '__name__'):
                type_name = type_obj.__name__
            else:
                type_name = str(type_obj)
            instance_instance = self.get(type_name)
            if instance_instance:
                setattr(instance, attr_name, instance_instance)

class Instance:
    # 用于存储被装饰的类
    registered_components = []
    def __init__(self, name: str):
        self.__name = name

    def __get__(self, instance, owner):
        return self

    def __set_name__(self, owner, name):
        self.__name = name

    def get_name(self):
        return self.__name