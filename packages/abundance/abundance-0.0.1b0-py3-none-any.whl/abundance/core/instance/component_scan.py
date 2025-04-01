import os
import importlib

class ComponentScan:
    def __init__(self, scan_path):
        self.scan_path = scan_path

    def __call__(self, cls):
        scan_dir = self.scan_path

        for root, _, files in os.walk(scan_dir):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    module_path = os.path.join(root, file).replace(os.getcwd(), '').replace(os.sep, '.').replace('/', '.').lstrip('.').rstrip('.py')
                    try:
                        importlib.import_module(module_path)
                    except ImportError as e:
                        print(f"Failed to import {module_path}: {e}")

        return cls