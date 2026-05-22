from src.mixins import LogInitMixin


class DummyUser(LogInitMixin):
    def __init__(self, name, age=None, **kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)


def test_repr_output():
    user = DummyUser("Bob", age=25)

    assert repr(user) == "DummyUser({'name': 'Bob', 'age': 25})"


def test_log_init_printing(capsys):
    _ = DummyUser("Alice", age=30)

    captured = capsys.readouterr()
    expected_output = "DummyUser({'name': 'Alice', 'age': 30})\n"
    assert captured.out == expected_output


def test_multiple_inheritance():
    class Base:
        def __init__(self, **kwargs):
            self.base_attr = True

    class AdvancedUser(LogInitMixin, Base):
        def __init__(self, name, **kwargs):
            self.name = name
            super().__init__(**kwargs)

    user = AdvancedUser("Charlie")

    assert user.base_attr is True
    assert "base_attr" in user.__dict__
