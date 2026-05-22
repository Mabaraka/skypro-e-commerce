class LogInitMixin:
    """Миксин для автоматического логирования параметров инициализации объекта."""

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __init__(self, *args, **kwargs):
        print(self.__repr__())
        # Передаём дальше по MRO — BaseProduct.__init__ ожидает **kwargs
        super().__init__(**kwargs)
