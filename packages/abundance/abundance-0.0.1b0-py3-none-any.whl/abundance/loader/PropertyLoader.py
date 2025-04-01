import os
import yaml
import json
import logging

from abundance.util.data_utils import merge_data

logger = logging.getLogger(__name__)

class PropertyLoader:
    default_location = ['resources', 'resources/config', '/']
    default_name = ['application', 'bootstrap']
    default_prefix = ['yaml', 'yml', 'json']

    def __init__(self, environment):
        self.sources = None
        self._file_cache = {}
        self.load()
        environment.property_sources = self.sources


    def load(self):
        file_list = []
        # 拼接所有可能配置文件列表
        for location in self.default_location:
            for name in self.default_name:
                for prefix in self.default_prefix:
                    file_path = os.path.join(location, f"{name}.{prefix}")
                    file_list.append(file_path)

        final_data = None
        # 遍历找到的文件列表
        for file in file_list:
            if file in self._file_cache:
                data = self._file_cache[file]
            else:
                try:
                    if os.path.exists(file):
                        logger.info(f"Loading {file}")
                        # 判断文件是否以 .yaml 或 .yml 结尾
                        if file.endswith(('.yaml', '.yml')):
                            # 以只读模式打开 .yaml 文件，并指定编码为 utf-8
                            with open(file, 'r', encoding='utf-8') as f:
                                # 使用 yaml.safe_load 方法解析 .yaml 文件内容
                                data = yaml.safe_load(f)
                        # 判断文件是否以 .json 结尾
                        elif file.endswith('.json'):
                            # 以只读模式打开 .json 文件，并指定编码为 utf-8
                            with open(file, 'r', encoding='utf-8') as f:
                                # 使用 json.loader 方法解析 .json 文件内容
                                data = json.load(f)
                        else:
                            continue
                        self._file_cache[file] = data
                    else:
                        continue
                except (yaml.YAMLError, json.JSONDecodeError) as e:
                    # 若解析 .yaml 或 .json 文件时出现错误，使用日志记录错误信息
                    logger.error(f"解析文件 {file} 时出错: {e}")
                    continue
                except Exception as e:
                    # 若处理文件时出现其他未知错误，使用日志记录错误信息
                    logger.error(f"处理文件 {file} 时发生未知错误: {e}")
                    continue

            if final_data is None:
                # 如果最终数据还未初始化，将当前解析的数据赋值给最终数据
                final_data = data
            else:
                # 若最终数据已存在，调用 merge_data 方法将当前解析的数据合并到最终数据中
                final_data = merge_data(final_data, data)

        # 将最终合并后的数据赋值给类的实例变量 config_data
        self.sources = final_data