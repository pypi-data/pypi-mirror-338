def config_me(conf_cls):
    """
    A decorator to dynamically inject a configuration object into a class instance.

    This decorator adds an instance of the specified configuration class (`conf_cls`) 
    as an attribute (`_config`) to the decorated class. It preserves the original 
    `__init__` method of the decorated class and ensures that the configuration 
    object is initialized before the original initialization logic is executed.

    Args:
        conf_cls (type): The configuration class to be instantiated and injected 
                            into the decorated class.

    Returns:
        function: The decorated class with the `_config` attribute added.

    Example:
        class Config:
            def __init__(self):
                self.setting = "default"

        @config_me(Config)
        class MyClass:
            def __init__(self, name):
                self.name = name

        obj = MyClass("example")
        print(obj._config.setting)  # Output: "default"
    """
    def decorator(self):
        init = self.__init__

        def wrapper(self, *args, **kwargs):
            self._config = conf_cls()
            init(self, *args, **kwargs)

        self.__init__ = wrapper
        return self
    return decorator