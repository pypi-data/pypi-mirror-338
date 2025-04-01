from abundance.core.instance.instance_container import InstanceContainer
from abundance.bridge.route import ROUTE_MAPPING

class Bridge:
    SERVICE_INSTANCES = {}

    def bridge(self, route_str, params=None):
        """
        主入口函数，根据路由和参数进行分发调用
        :param route_str: 路由字符串
        :param params: 实际参数字典
        :return: 调用结果
        """

        method = self.SERVICE_INSTANCES.get(route_str)
        if method:
            if params: return method(params)
            else: return method()
        else:
            handler = ROUTE_MAPPING.get(route_str)
            if handler:
                # 查找对应的服务实例
                for service in InstanceContainer()._components.values():
                    if hasattr(service, handler.__name__):
                        self.SERVICE_INSTANCES[route_str] = getattr(service, handler.__name__)
                        if params: return getattr(service, handler.__name__)(params)
                        else: return getattr(service, handler.__name__)()


        return {"error": f"Route {route_str} not found"}