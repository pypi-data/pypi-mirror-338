"""Unit-test for Parser

Unit-test for Parser with Lexer

Run `python3 -m pytest tests/test_parser.py` in parent directory.

Environment:
- Python 3.9 or later
- pytest 8.3 or later

License:
Copyright 2025 benesult

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = 'Fumiaki Motegi <motegi@benesult.com>'
__date__ = '2025-04-04'

# pylint: disable=C0301, E0401, R0801, C0123

import pytest
from vivjson.viv import Viv
from vivjson.config import Config

@pytest.mark.parametrize(
    'prepared_expression, target_expression, expected_value, is_error', (
        ('a = 1.5', 'a', 1.5, False),
        ('a= 1.5e1', 'a', 15.0, False),
        ('a = 1.', 'a', None, True),  # Digit is needed after "."
        ('a =', 'a', None, True),  # Missing value
        ('a = {}, a.1 = {}, a.1.2 = true', 'a', {"1": {"2": True}}, False),
        ('a = {}, a.1/2 = {}', 'a', None, True),  # Invalid member
        ('[a, b] = [1, 3]', 'a', None, True),  # Invalid assignment
        ('a + 1 = 1', 'a', None, True),  # Invalid assignment
        ('a: ""', 'a', "", False),
        ('a = "text\'', 'a', None, True),  # Different quotation mark is invalid
        ('a = "text\\" b = 3', 'a', None, True),  # Missing end of "
        ('a = "text\\"', 'a', None, True),  # Missing end of "
        ('a = "text\\\\text"', 'a', 'text\\text', False),
        ('a = "text\ttext"', 'a', 'text\ttext', False),
        ('a = "\\u3042\\u3044\\u3046\\u3048\\u304a\\u304B"', 'a', 'あいうえおか', False),
        ('a = "\\u4a\\u3044"', 'a', None, True),  # Invalid unicode
        ('a = "\\u4a"', 'a', None, True),  # Invalid unicode
        ('a = "\\u"', 'a', None, True),  # Invalid unicode
        ('a = "x\\"y"', 'a', 'x"y', False),
        ('a = "x\\\'y"', 'a', "x'y", False),
        ('a = "x\\\\y"', 'a', "x\\y", False),
        ('a = "x\\/y"', 'a', "x/y", False),
        ('a = "x\\by"', 'a', "x\by", False),
        ('a = "x\\fy"', 'a', "x\fy", False),
        ('a = "x\\ny"', 'a', "x\ny", False),
        ('a = "x\\ry"', 'a', "x\ry", False),
        ('a = "x\\ty"', 'a', "x\ty", False),
        ('a : true', 'a', True, False),
        ('a := 1.5', 'a', None, True),  # := is invalid after Identifier.
        ('x = if (true) {:=10}', 'x', 10, False),
        ('x = if (true) {a:=10}', 'x', None, True),  # := is invalid after Identifier.
        ('x = if (true) {:=}', 'x', None, True),  # Missing value
        ('a = [1 5 {b: {c: 10} d: -20}] e = -100', 'a[-1].b.c + e', -90, False),
        ('a=[1 5 {b:{c:10} d:-20}] e=-100', 'a[-1].b.c+e', -90, False),
        ('a=[1 5 {b:{c:10} d:-20}] e=-100', 'a.-1.b.c+e', -90, False),
        ('a=[1 5 {b:{c:10} d:-20}] e=-100', 'a.-2', 5, False),
        ('a=[1 5 {b:{c:10} d:-20}] e=-100', 'a.-2.', None, True),  # It is invalid that a dot is the tail.
        ('a=[1 5 {b:{c:10} d:-20}] e=-100', 'a . \n -2', 5, False),
        ('a=[1 5 {b:{c:10} d:-20}] e=-100', 'a.2.b.c+e', -90, False),
        ('a=[1 5 {b:{c:10} d:-20}] e=-100', 'a.2. b.c+e', -90, False),
        ('a=[1 5 {b:{c:10} d:-20}] e=-100', 'a . 2 . b.c+e', -90, False),
        ('a\n=\n[1\n\n{b:{c:10} d:-20}]\ne\n\n=\n-100', 'a[-1]\n. \nb.c+e', -90, False),
        ('', '-3+1e-4*1000', -2.9, False),
        ('a = [5]', 'a[0', None, True), # It is invalid that the right bracket is lacked.
        ('{a = [5 }', '3', None, True), # It is invalid that the right bracket is lacked.
        ('', '3 *+ 4', 12, False),
        ('', '3 +* 4', None, True),  # +* is invalid
        ('', '(3 + 4 {1 + 2}', None, True),  # It is invalid that the right bracket is lacked.
        ('', '() + 2', None, True),  # It is invalid that there is no expression in group.
        ('a := 2', 'a', None, True),
        ('', '3 > 2 > -1', None, True),  # It should be fixed as 3 > 2 and 2 > -1.
        ('a = not false', 'a', True, False),
        ('a = not(false)', 'a', True, False),
        ('a = true and not false', 'a', True, False),
        ('a = !false', 'a', None, True),  # ! is invalid
        ('function x2(a) {return(a * 2)}', 'x2(4)', 8, False),
        ('function x2(a){return(a*2)}', 'x2(4+2)', 12, False),
        ('function x2() {}', 'x2(1)', {}, False),
        ('function x2() a = 3', 'a', None, True),  # Function needs block (statements).
        ('function test(a + b) {}', 'test()', None, True),  # Invalid parameter
        ('function test(break a) {}', 'test()', None, True),  # Invalid modifier
        ('function run(function worker) {worker()}', 'a', None, False),
        ('function run(function) {return}', 'a', None, True),  # Identifier is needed after argument's modifier.
        ('function (a) {return}', 'a', None, True),  # Identifier is needed after function's modifier.
        ('a = 0\n\nif\n\n(\n\ntrue\n\n)\n\n{\n\na = 3\n\n}', 'a', 3, False),
        ('a = 0 if (true) {}', 'a', 0, False),
        ('a = -10, b = if (a < 0) {:= "-"} elseif (a == 0) {:= "0"} else {:= "+"}', 'b', '-', False),
        ('a = 1, b = if \n (a == 0) \n {:= "zero"} \n elseif \n (a == 1) \n {:= "one"} \n elseif \n (a == 2) \n {:= "two"} \n else \n {:= "other"}', 'b', 'one', False),
        ('if () { a = 3 }', 'a', None, True),  # Condition is necessary.
        ('if (true), a = 3', 'a', None, True),  # Block (operations) is necessary.
        ('if (true, a = 3)', 'a', None, True),  # Block (operations) is necessary.
        ('while () {i=0}', 'i', None, True),  # Condition is necessary.
        ('while (true)', 'i', None, True),  # Block (operations) is necessary.
        ('while {i = 0}', 'i', None, True),  # Condition (parenthesis) is necessary.
        ('for {i = 0}', 'i', None, True),  # Condition (parenthesis) is necessary.
        ('a = 0, for (i = 0; i < 20; i += 1; { a = 2 })', 'a', 2, False),
        ('for (i = 0; i < 20; i += 1; { a = 2 }', 'i', None, True),  # Both parentheses are necessary.
        ('for (i = 0; i < 20; i += 1)', 'i', None, True),  # Block (operations) is necessary.
        ('for (i = 0; i < 20; i += 1, a = 3)', 'a', None, True),  # Block (operations) is necessary.
        ('for ()', 'i', None, True),  # Block (operations) is necessary.
        ('for (3 in [2, 3]) {break}', 'i', None, True),  # Iterator needs Identifier for left-hand side.
        ('sum = 0, for (i = 5, i < 7, i += 1) {sum += i}', 'sum', 11, False),
        ('sum = 0, for (i = 5, i < 7, i += 1, i += 1) {sum += i}', 'sum', None, True),  # Number of argument is invalid.
        ('remove, a = 3', 'a', None, True),  # remove function needs argument.
        ('remove(), a = 3', 'a', None, True),  # remove function needs argument.
        ('remove(a', 'a', None, True),  # Missing ")"
        ('a = 3,a *= 5;a += 2\na = a - 27 a /= 4\tb = 3   a+=b', 'a', 0.5, False),
        ('a = 20, a = 30 # ', 'a', 30, False),
        ('a = 20 # , a = 30', 'a', 20, False),
        ('a = 20 // , a = 30', 'a', 20, False),
        ('a = /* 20, a = */ 30', 'a', 30, False),
        ('a = /* 20, a = 30', 'a', None, True),  # Missing "*/"
        ('a = 20 # abc\na = 30', 'a', 30, False),
        ('a /* = 20\na */ = 30', 'a', 30, False),
        ('a = 20 /* \na = 30 */', 'a', 20, False),
        ('a = [\n\n1\n\n2\n\n3\n\n]', 'a', [1, 2, 3], False),
        ('a = [\n1,\n2,\n3\n]', 'a', [1, 2, 3], False),
        ('a = [\n1,\n,\n3\n]', 'a', None, True),  # Missing 2nd value though delimiter is existed
        ('function test(\na\nb\nc\n)\n{return(a+b+c)}\nx=test(10, 100, 1000)', 'x', 1110, False),
        ('function test(\n\na\n#comment\nb\n\nc\n\n)\n{return(a+b+c)}\nx=test(10, 100, 1000)', 'x', 1110, False),
        ('function test(a, , c)\n{return(a+b+c)}\nx=test(10, 100, 1000)', 'x', None, True),  # Missing 2nd parameter though delimiter is existed
        ('function test(a, b, c)\n{return(a+b+c)}\nx=test(10, , 1000)' , 'x', 1010, False),  # Missing 2nd argument will be null.
    )
)

def test_parser(prepared_expression, target_expression, expected_value,
                is_error):
    """Unit-test for Parser

    Unit-test for Parser with Lexer

    Args:
        prepared_expression (str or dict): When the another expression,
                                 such as assignment, is needed before
                                 test, it is given here.
                                 Maybe this is '' mostly.
                                 str: Statements as VivJson
                                 dict: Value as Python's value
        target_expression (str): "return" method's argument as targeted
                                 expression.
        expected_value (Any): The expected value as Python's value
        is_error (bool): True if occurring error is expected,
                         False otherwise.
    """
    config = Config(max_depth=11)

    text = f'return({target_expression})'
    value, error_message = Viv.run(prepared_expression, text, config)
    assert (error_message != '') == is_error

    if isinstance(value, float):
        value = round(value, 10)
    assert value == expected_value

    if error_message == '' \
            and not isinstance(expected_value, bool) \
            and isinstance(expected_value, (int, float)):
        assert type(value) == type(expected_value)  # pylint: disable=C0123

@pytest.mark.parametrize(
    'is_only_json, expression, expected_value, is_error', (
        (True, '{"a": 3, "b": [true, null, 1.5e3]}', {"a": 3, "b": [True, None, 1500.0]}, False),
        (False, '{"a": 3, "b": [true, null, 1.5e3]}', {"a": 3, "b": [True, None, 1500.0]}, False),

        (True, '{"a": 3, "b": true}', {"a": 3, "b": True}, False),
        (False, '{"a": 3, "b": true}', {"a": 3, "b": True}, False),

        (True, '"a": -3, "b": true', {"a": -3, "b": True}, False),
        (False, '"a": -3, "b": true', {"a": -3, "b": True}, False),

        (True, '"a": 3, "b": true, return(a)', None, True),
        (False, '"a": 3, "b": true, return(a)', 3, False),

        (True, '{"a": 3 + 2, "b": true}', None, True),
        (False, '{"a": 3 + 2, "b": true}', {"a": 5, "b": True}, False),

        (True, '10', {}, False),
        (False, '10', {}, False),
    )
)

def test_json(is_only_json, expression, expected_value, is_error):
    """Unit-test of JSON for Parser

    Args:
        is_only_json (bool): is_only_json of Config
        expression (str): The targeted expression
        expected_value (Any): The expected value as Python's value
        is_error (bool): True if occurring error is expected,
                         False otherwise.
    """
    config = Config(enable_only_json=is_only_json)

    value, error_message = Viv.run(expression, config)
    assert (error_message != '') == is_error
    if isinstance(value, float):
        value = round(value, 10)
    assert value == expected_value
    assert type(value) == type(expected_value)

@pytest.mark.parametrize(
    'json, script, expected_value, is_error', (
        ('"a": 3, "b": true', 'return(a)', 3, False),
        ('"a": 3, "b": true', '', {"a": 3, "b": True}, False),
        ('"a": 3, "b": true', 'return("")', '', False),
        ('"a": 3, "b": true', 'return(a+2)', 5, False),
        ('"a": 3 + 2, "b": true', 'return(a)', None, True),  # "+" operator is not allowed in JSON.
        ('"a": 3, "b": true', 'a += 2, b = not b', {"a": 5, "b": False}, False),
        ('10', '', {}, False),  # The number(, string, boolean, null, array) can't be returned without script.
        ('10', 'return(_)', 10, False),
        ('false', '', {}, False),  # The number(, string, boolean, null, array) can't be returned without script.
        ('false', 'return(_)', False, False),
        ('test', '', {}, False),  # The number(, string, boolean, null, array) can't be returned without script.
        ('test', 'return(_)', 'test', False),
        ('null', '', {}, False),  # The number(, string, boolean, null, array) can't be returned without script.
        ('null', 'return(_)', None, False),
        ('[1, 2, 3]', '', {}, False),  # The number(, string, boolean, null, array) can't be returned without script.
        ('[1, 2, 3]', 'return(_)', [1, 2, 3], False),
    )
)

def test_json_and_script(json, script, expected_value, is_error):
    """Unit-test of JSON & Script for Parser

    Args:
        json (str): The targeted JSON value 
        expression (str): The targeted expression
        expected_value (Any): The expected value as Python's value
        is_error (bool): True if occurring error is expected,
                         False otherwise.
    """
    config = Config(enable_only_json=True)
    parsed, error_message = Viv.parse(json, config)
    assert (error_message != '') == is_error
    if error_message == '':
        assert parsed is not None
    else:
        assert parsed is None
    value, error_message = Viv.run(parsed, script)
    assert (error_message != '') == is_error
    if isinstance(value, float):
        value = round(value, 10)
    assert value == expected_value
    assert type(value) == type(expected_value)

def test_file():
    """Unit-test of file for Parser"""
    parsed, error_message = Viv.parse('tests/invalid_as_json.json')
    assert error_message != ''
    assert parsed is None
    parsed, error_message = Viv.parse('tests/invalid_as_json.viv')
    assert error_message == ''
    assert parsed is not None

    parsed, error_message = Viv.parse_file('tests/invalid_as_json.json')
    assert error_message != ''
    assert parsed is None
    parsed, error_message = Viv.parse_file('tests/invalid_as_json.viv')
    assert error_message == ''
    assert parsed is not None

    config = Config()
    assert config.get_enable_only_json() is False
    parsed, error_message = Viv.parse_file('tests/invalid_as_json.json', config)
    assert error_message != ''
    assert parsed is None
    assert config.get_enable_only_json() is False

    value, error_message = Viv.run('tests/array.viv')
    assert error_message == ''
    count = 0
    for v in value.values():
        assert v == [1, 2, 3]
        count += 1
    assert count == 8
