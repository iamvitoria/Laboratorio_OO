import importlib.util

def import_class(module_name, class_name):
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print(f'Module: {module_name} not found')
        return None
    else:
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        return getattr(module, class_name)