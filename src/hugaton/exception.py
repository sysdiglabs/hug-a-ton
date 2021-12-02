class SysdigException(Exception):
    def __init__(self, msg="", *args, **kwargs):
        super().__init__(msg, args, kwargs)
        print(f"{type(self).__name__} {msg}")
