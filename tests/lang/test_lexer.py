import pytest

from puglang.lang.lexer import Lexer, LexicalError


@pytest.fixture
def simple_expression():
    return "i=1"


@pytest.fixture
def lexer():
    return Lexer()


def test_lexer_is_not_none(lexer):
    assert lexer is not None


def test_lexer_load_source_code(lexer, simple_expression):
    lexer.load(simple_expression)


def test_lexer_fails_without_load(lexer):
    with pytest.raises(LexicalError):
        lexer.lex()


def test_lexer_loads_and_lex(lexer, simple_expression):
    lexer.load(simple_expression)
    lexer.lex()
