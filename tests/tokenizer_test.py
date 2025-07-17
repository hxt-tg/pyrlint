from pyrlint.tokenizer import RTokenizer, RTokenType
import os


def highlight(statements):
    result_str = ''
    rt = RTokenizer(statements)
    while True:
        t = rt.next_token()
        if not t:
            break
        if t.type == RTokenType.ID:
            result_str += f'\033[34m' + t.content + f'\033[0m'
        elif t.type == RTokenType.OPER:
            result_str += f'\033[33m' + t.content + f'\033[0m'
        elif t.type == RTokenType.STRING:
            result_str += f'\033[36m' + t.content + f'\033[0m'
        elif t.type == RTokenType.UOPER:
            result_str += f'\033[35m' + t.content + f'\033[0m'
        elif t.type == RTokenType.NUMBER:
            result_str += f'\033[32m' + t.content + f'\033[0m'
        elif t.type == RTokenType.COMMENT:
            result_str += f'\033[31m' + t.content + f'\033[0m'
        elif t.is_comma or t.is_whitespace or t.is_right_bracket or t.is_left_bracket:
            result_str += t.content
        else:
            result_str += f'<{t}>' + t.content
    return result_str


def print_tokenize(statements, print_repr=False):
    if print_repr:
        print(repr(statements))
    rt = RTokenizer(statements)
    while True:
        t = rt.next_token()
        if not t:
            break
        print(t)


def test_void():
    print(">>> TEST VOID")
    print_tokenize("")


def test_simple():
    print(">>> TEST SIMPLE")
    print_tokenize("(")
    print_tokenize(")")
    print_tokenize("[")
    print_tokenize("]")
    print_tokenize("{")
    print_tokenize("}")
    print_tokenize(",")
    print_tokenize(";")


def test_comment():
    print(">>> TEST COMMENT")
    print_tokenize('#')
    print_tokenize('# foo #')
    # TODO: ?


def test_numbers():
    print(">>> TEST NUMBERS")
    print_tokenize("1")
    print_tokenize("10")
    print_tokenize("0.1")
    print_tokenize("1.")
    print_tokenize(".2")
    print_tokenize("1e-7")
    print_tokenize("1.2e+7")
    print_tokenize("2e")
    print_tokenize("3e+")
    print_tokenize("0x")
    print_tokenize("0x0")
    print_tokenize("0xDEADBEEF")
    print_tokenize("0xcafebad")
    print_tokenize("1L")
    print_tokenize("0x10L")
    print_tokenize("1000000L")
    print_tokenize("1e6L")
    print_tokenize("1.1L")
    print_tokenize("1e-3L")
    print_tokenize("2i")
    print_tokenize("4.1i")
    print_tokenize("1e-2i")


def test_operators():
    print(">>> TEST OPERATORS")
    print_tokenize("+")
    print_tokenize("-")
    print_tokenize("*")
    print_tokenize("/")
    print_tokenize("^")
    print_tokenize(">")
    print_tokenize(">=")
    print_tokenize("<")
    print_tokenize("<=")
    print_tokenize("==")
    print_tokenize("!=")
    print_tokenize("!")
    print_tokenize("&")
    print_tokenize("|")
    print_tokenize("~")
    print_tokenize("->")
    print_tokenize("<-")
    print_tokenize("->>")
    print_tokenize("<<-")
    print_tokenize("$")
    print_tokenize(":")  # TODO: Is that valid?
    print_tokenize("=")
    print_tokenize(":=")


def test_user_operators():
    print(">>> TEST USER_OPERATORS")
    print_tokenize("%%")
    print_tokenize("%test test%")


def test_string():
    print(">>> TEST STRING")
    print_tokenize("\"test\"")
    print_tokenize("\" '$\t\r\n\\\"\"")
    print_tokenize("\"\"")
    print_tokenize("''")
    print_tokenize("'\"'")
    print_tokenize("'\\\"'")
    print_tokenize("'\n'")
    print_tokenize("'foo bar \\U654'")


def test_identifiers():
    print(">>> TEST IDENTIFIERS")
    print_tokenize(".")
    print_tokenize("...")
    print_tokenize("..1")
    print_tokenize("..2")
    print_tokenize("foo")
    print_tokenize("FOO")
    print_tokenize("f1")
    print_tokenize("a_b")
    print_tokenize("ab_")
    print_tokenize("`foo`")
    print_tokenize("`$@!$@#$`")
    print_tokenize("`a\n\"'b`")
    print_tokenize("Áqc1")
    print_tokenize("Áqc1Á")


def test_whitespaces():
    print(">>> TEST WHITESPACES")
    print_tokenize(" ")
    print_tokenize("      ")
    print_tokenize("\t\n")
    print_tokenize("\u00A0")
    print_tokenize("  \u3000  ")
    print_tokenize(" \u00A0\t\u3000\r  ")


def test_others():
    print(">>> TEST OTHERS")
    print_tokenize("1 ** 2", print_repr=True)
    print_tokenize("r\"(abc)\"", print_repr=True)
    print_tokenize("R\"(abc)\"", print_repr=True)
    print_tokenize("r\"{abc}\"", print_repr=True)
    print_tokenize("r'[abc]'", print_repr=True)
    print_tokenize("R'{abc}'", print_repr=True)
    print_tokenize("r'(abc", print_repr=True)
    print_tokenize("rep('.')", print_repr=True)
    print_tokenize("'abc\ndef'", print_repr=True)
    print_tokenize("`a \\` b`", print_repr=True)
    print_tokenize("<<chunk>>", print_repr=True)
    print_tokenize("区 <- 42", print_repr=True)


def test():
    test_void()
    test_simple()
    test_comment()
    test_numbers()
    test_operators()
    test_user_operators()
    test_string()
    test_identifiers()
    test_whitespaces()
    test_others()


def test_highlight(file_name):
    with open(file_name, 'r', encoding='utf8') as fi:
        print(highlight(fi.read()))


if __name__ == "__main__":
    # test()
    # test_highlight(os.path.join(os.path.dirname(__file__), 'test_data', 'test_2.R'))
    with open(os.path.join(os.path.dirname(__file__), 'test_data', 'test_2.R'), encoding='utf8') as fi:
        tokenizer = RTokenizer(fi.read())
        while True:
            token = tokenizer.next_token()
            if not token:
                break
            print(token)

