import pytest

from puglang.lang.lexer import Lexer


@pytest.fixture
def lexer():
    return Lexer()


def test_lexer_is_not_none(lexer):
    assert lexer is not None
