
class Environment:
    property_sources = None

    def get(self, key_path=None, default=None):
        """
        根据给定的键路径从配置数据中获取对应的值。
        键路径是用点分隔的多级键名，用于在嵌套的字典和列表结构中查找值。
        如果在查找过程中某个键不存在或对应的值不是字典或列表类型，则返回默认值。
        :param key_path: 键路径，用点分隔的多级键名，例如 'level1.1.level2.key'
        :param default: 若未找到对应的值，返回的默认值，默认为 None
        :return: 找到的值或默认值
        """
        if key_path:
            keys = key_path.split('.')
            current = self.property_sources
            for key in keys:
                if isinstance(current, dict):
                    if key in current:
                        current = current[key]
                    else:
                        return default
                elif isinstance(current, list):
                    try:
                        index = int(key)
                        if 0 <= index < len(current):
                            current = current[index]
                        else:
                            return default
                    except ValueError:
                        return default
                else:
                    return default
            return current
        else:
            return self.property_sources