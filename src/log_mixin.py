"""
Модуль с миксином для логирования создания объектов.
"""


class LogMixin:
    """
    Миксин для логирования создания объектов.
    При создании объекта выводит информацию о классе и параметрах.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Инициализирует миксин и логирует создание объекта."""
        # Сохраняем аргументы для логирования
        self._init_args = args
        self._init_kwargs = kwargs

        # Вызываем следующий __init__ в MRO
        super().__init__(*args, **kwargs)

        # После инициализации всех родителей - логируем
        print(f"Создан объект класса {self._simple_repr()}")

    def _simple_repr(self) -> str:
        """Упрощенный repr для логирования без доступа к атрибутам."""
        class_name = self.__class__.__name__

        # Формируем строку параметров из сохраненных аргументов
        repr_parts = []

        # Обрабатываем позиционные аргументы
        for i, arg in enumerate(self._init_args):
            if isinstance(arg, str):
                repr_parts.append(f"'{arg}'")
            else:
                repr_parts.append(str(arg))

        # Обрабатываем именованные аргументы
        for key, value in self._init_kwargs.items():
            if isinstance(value, str):
                repr_parts.append(f"{key}='{value}'")
            else:
                repr_parts.append(f"{key}={value}")

        return f"{class_name}({', '.join(repr_parts)})"

    def __repr__(self) -> str:
        """
        Формальное строковое представление объекта.
        Реализация в дочерних классах.
        """
        # Базовая реализация - дочерние классы должны переопределять
        return f"{self.__class__.__name__}()"
