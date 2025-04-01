import inspect
import logging

from abundance.banner.AbundanceApplicationBannerPrinter import AbundanceApplicationBannerPrinter
from abundance.core.env.ApplicationEnvironment import ApplicationEnvironment
from abundance.banner.BannerMode import BannerMode
from abundance.core.instance.instance_container import InstanceContainer, Instance
from abundance.loader.PropertyLoader import PropertyLoader
from abundance.loader.ResourceLoader import ResourceLoader
from abundance.log.LoggingSetup import LoggingSetup
from abundance.util.StopWatch import StopWatch


class AbundanceApplication:
    BANNER_LOCATION_PROPERTY_VALUE = "banner.txt"
    BANNER_LOCATION_PROPERTY = "abundance.banner.location"
    logger = logging.getLogger(__name__)
    mainApplicationClass = None
    bannerMode = None
    banner = None
    resourceLoader = None
    environment = None
    def __init__(self):
        self.banner_mode = BannerMode.CONSOLE
        self.log_startup_info = True
        self.add_command_line_properties = True
        self.add_conversion_service = True
        self.headless = True
        self.register_shutdown_hook = True
        self.additional_profiles = []
        self.allow_bean_definition_overriding = True
        self.lazy_initialization = False
        self.application_context = None
        self.mainApplicationClass = self.deduceMainApplicationClass()
        self.stopWatch = None

    def deduceMainApplicationClass(self):
        # 获取当前的调用栈信息
        stack = inspect.stack()
        for frame_info in stack:
            # 获取当前帧的全局变量
            frame = frame_info.frame
            # 获取当前帧正在执行的函数名
            function_name = frame.f_code.co_name
            if function_name == "main":
                # 获取定义该函数的模块名
                module_name = frame.f_globals.get('__name__')
                if module_name:
                    try:
                        # 获取该模块对象
                        module = __import__(module_name)
                        return module
                    except ImportError:
                        pass
        return None

    def _run(self):
        stopWatch = StopWatch()
        stopWatch.start()

        try:
            environment = self.prepare_environment()
            self.prepare_container()
            LoggingSetup(environment)
            self.printBanner(environment)
        except Exception as e:
            self.logger.error(f"运行时发生错误: {e}")
        stopWatch.stop()
        self.stopWatch = stopWatch


    @staticmethod
    def run():
        app = AbundanceApplication()
        app._run()
        return app

    def prepare_environment(self):
        environment = self.getOrCreateEnvironment()

        # 初始化环境
        PropertyLoader(environment)

        return environment

    def prepare_container(self):
        # 组件注册和依赖注入
        container = InstanceContainer()
        for component_cls in Instance.registered_components:
            instance = component_cls()
            name = component_cls.__name__
            container.register(name, instance)
            print(f"Registered component: {name}")

        for component_cls in Instance.registered_components:
            instance = container.get(component_cls.__name__)
            print(f"Resolving dependencies for: {component_cls.__name__}")
            container.resolve_dependencies(instance)

    def getOrCreateEnvironment(self):
        if self.environment is not None:
            return self.environment
        else:
            # 使用单例模式获取 ApplicationEnvironment 实例
            self.environment = ApplicationEnvironment()
            return self.environment

    def printBanner(self, environment):
        if self.banner_mode == BannerMode.OFF:
            return None
        else:
            resourceLoader = self.resourceLoader or ResourceLoader()

            bannerPrinter = AbundanceApplicationBannerPrinter(resourceLoader, self.banner)
            if self.bannerMode == BannerMode.LOG:
                return bannerPrinter.print(environment, self.logger.info)
            else:
                bannerPrinter.print(environment, print)