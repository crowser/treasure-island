"""基础数据结构"""


class Config(dict):
    """config init"""

    def __init__(self, config, defaults=None):
        super().__init__(defaults or {})
        for key in dir(config):
            if key.isupper():
                self[key] = getattr(config, key)
