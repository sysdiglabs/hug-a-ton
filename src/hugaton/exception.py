class SysdigException(Exception):
    def __init__(self, msg=""):
        super().__init__(msg)
        print(f"{type(self).__name__} {msg}")
