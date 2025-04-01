import os


class PathUtils:
    def __init__(self):
        self.tmp_paths = {"resources:": ["resources/", ""]}

    @staticmethod
    def auto_fill_resources_path(data):
        if isinstance(data, str):
            if data.startswith(tuple(PathUtils().tmp_paths.keys())):
                for prefix in PathUtils().tmp_paths:
                    if data.startswith(prefix):
                        return PathUtils().get_resources_path(data, prefix, PathUtils().tmp_paths.get(prefix))
        elif isinstance(data, dict):
            new_data = {}
            for key, value in data.items():
                new_data[key] = PathUtils.auto_fill_resources_path(value)
            return new_data
        elif isinstance(data, list):
            return [PathUtils.auto_fill_resources_path(item) for item in data]
        return data

    @staticmethod
    def get_resources_path(path, prefix, locations):
        for location in locations:
            real_path = path.replace(prefix, location, 1)
            if os.path.exists(real_path):
                return real_path
        return path