import pathlib

import pytest
from src.decorators import log


def test_success_log_in_console(capsys):

    @log()
    def foo(a, b):
        return a + b
    result = foo(2, 3)
    assert result == 5
    capture = capsys.readouterr()
    assert capture.out == "Функция foo выполнена!\n"

def test_error_in_file(tmp_path: pathlib.Path):
    log_file = tmp_path / "log.txt"

    @log(str(log_file))
    def foo_2(a, b):
        return a + b

    with pytest.raises(TypeError):
        foo_2(1, "2")

    content = log_file.read_text(encoding="utf-8")
    assert content == "Функция foo_2 не выполнена! Произошла ошибка TypeError: unsupported operand type(s) for +: 'int' and 'str',входные параметры: ((1, '2'), {}).\n"


