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


@pytest.mark.parametrize(
    "character",
    [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
    ],
)
def test_is_symbol_false(lexer, character):
    assert lexer.is_symbol(character) is False
    assert lexer.is_symbol(character.upper()) is False


@pytest.mark.parametrize(
    "character",
    [
        "~",
        "`",
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "_",
        "-",
        "+",
        "=",
        "{",
        "}",
        "[",
        "]",
        "|",
        "\\",
        ";",
        ":",
        "'",
        '"',
        "<",
        ">",
        ",",
        ".",
        "/",
        "?",
    ],
)
def test_is_symbol_true(lexer, character):
    assert lexer.is_symbol(character) is True
