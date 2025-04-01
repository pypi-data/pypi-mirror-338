import logging
import os
from abundance.loader.Resource import Resource

logger = logging.getLogger(__name__)

class ResourceLoader:
    def __init__(self):
        self.sources = None

    def get_resource(self, location):
        try:
            if os.path.exists(location):
                with open(location, 'rb') as f:
                    self.sources = Resource(f.read())
            else:
                self.sources = Resource(None)
        except PermissionError as pe:
            logger.error(f"没有权限访问文件 {location}: {pe}")
            self.sources = Resource(None)
        except OSError as ose:
            logger.error(f"打开文件 {location} 时发生错误: {ose}")
            self.sources = Resource(None)
        except Exception as e:
            logger.error(f"处理文件 {location} 时发生未知错误: {e}")
            self.sources = Resource(None)
        return self.sources