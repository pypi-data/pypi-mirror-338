"""
    一个类装饰器是一个函数，它接受一个类作为参数，然后返回一个新的类<br>
    https://blog.csdn.net/wuShiJingZuo/article/details/134906377
"""
import threading


def global_singleton_class(cls):
    __instances = {}
    # 增加 __lock ，用于多线程
    __lock = threading.Lock()

    def get_instance(*args, **kwargs):
        with __lock:
            if cls not in __instances:
                __instances[cls] = cls(*args, **kwargs)
            return __instances[cls]

    return get_instance
