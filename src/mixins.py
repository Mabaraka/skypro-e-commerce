class LogInitMixin:
    """Миксин для автоматического логирования параметров инициализации объекта."""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"[INIT] Создан объект класса '{class_name}'")
        if args:
            print(f"       Позиционные аргументы (args): {args}")
        if kwargs:
            print(f"       Именованные аргументы (kwargs): {kwargs}")
        # Передаём дальше по MRO — BaseProduct.__init__ ожидает **kwargs
        super().__init__(**kwargs)
