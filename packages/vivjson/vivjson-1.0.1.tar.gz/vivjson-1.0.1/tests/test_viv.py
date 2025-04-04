"""Unit-test for Viv class

Unit-test for "run", "parse_text", ...

Run `python3 -m pytest tests/test_viv.py` in parent directory.

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
__date__ = '2025-03-27'

# pylint: disable=C0301, E0401

import datetime
from math import isnan
import pytest
from vivjson.viv import Viv, Json, Method
from vivjson.config import Config
from vivjson.statement import Literal, Return
from vivjson.tokens import Token

def test_run():  # pylint: disable=R0915
    """Unit-test for "Viv.run" method."""
    value, error_message = Viv.run("3", "2", "return(_[0] + _[1])")
    assert error_message == ''
    assert value == 5

    value, error_message = Viv.run("3", "2", "return(_)")
    assert error_message == ''
    assert value == [3, 2]

    value, error_message = Viv.run("5", "return(_*2)")
    assert error_message == ''
    assert value == 10

    value, error_message = Viv.run("a:3,b:2,return(a+b)")
    assert error_message == ''
    assert value == 5

    value, error_message = Viv.run(["{a:3,b:2}", "{return(a+b)}"])
    assert error_message == ''
    assert value == 5

    value, error_message = \
        Viv.run(("x=", "+", "{a:3,b:2}", "return(x.a+x.b)"))
    assert error_message == ''
    assert value == 5

    value, error_message = Viv.run('{"foo": 3, "bar": 2}', "return(foo + bar)")
    assert error_message == ''
    assert value == 5
    value, error_message = Viv.run('{"foo": 3, "bar": 2}', "return('foo' in .)")
    assert error_message == ''
    assert value is True
    value, error_message = Viv.run('{"foo": 3, "bar": 2}', "return(qux)")
    assert error_message == ''
    assert value is None  # null
    value, error_message = Viv.run('{"foo": 3, "bar": 2}', "return('qux' in .)")
    assert error_message == ''
    assert value is False

    data = '{"foo": 10, "bar": 30, "baz": 20}'
    value, error_message = Viv.run(data)
    assert error_message == ''
    assert value == {"foo": 10, "bar": 30, "baz": 20}
    # print(value)  # {'foo': 10, 'bar': 30, 'baz': 20}
    # print(type(value))  # <class 'dict'>

    value, error_message = Viv.run(data, 'return(foo)')
    assert error_message == ''
    assert value == 10
    # print(value)  # 10
    # print(type(value))  # <class 'int'>

    value, error_message = Viv.run(data, 'return(qux)')
    assert error_message == ''
    assert value is None
    # print(value)  # None
    # print(type(value))  # <class 'NoneType'>

    value, error_message = Viv.run(data, 'return("qux" in .)')
    assert error_message == ''
    assert value is False
    # print(value)  # False
    # print(type(value))  # <class 'bool'>

    value, error_message = Viv.run(data, 'return(foo + bar + baz)')
    assert error_message == ''
    assert value == 60
    # print(value)  # 60

    code = 'max=-1, for (pair in pairs) {if (max < pair[1]) {max = pair[1]}}, return(max)'
    value, error_message = Viv.run('pairs = ', '+', data, code)
    assert error_message == ''
    assert value == 30
    # print(value)  # 30
    value, error_message = Viv.run('pairs = ' + data, code)
    assert error_message == ''
    assert value == 30
    # print(value)  # 30
    code = 'max=-1, for (pair in .) {if (max < pair[1]) {max = pair[1]}}, return(max)'
    value, error_message = Viv.run(data, code)
    assert error_message == ''
    assert value == 30
    # print(value)  # 30
    code = '_max=-1, for (pair in .) {if (_max < pair[1]) {_max = pair[1]}}, return(_max)'
    value, error_message = Viv.run(data, code)
    assert error_message == ''
    assert value == 30
    # print(value)  # 30

    value, error_message = Viv.run()
    assert error_message == ''
    assert value == {}

    value, error_message = Viv.run("x=", 3)
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run(("x=", "+"))
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run("x=", "+", "+", "+")
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run("x=", "+", Config(max_depth=3))
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run("x=", "+", {"a": 3})
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run({"___a___": 3})
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run(("+", "{a:3,b:2}"))
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run("tests/call_6.viv")
    assert error_message == ''
    assert value == 6

    value, error_message = Viv.run("tests/empty.viv")
    assert error_message == ''
    assert value == {}

    value, error_message = Viv.run("tests/broken.viv")
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run("tests/dummy.viv")
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run("tests/call_6.vev")
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run("")
    assert error_message == ''
    assert value == {}

    value, error_message = Viv.run("tests/a5b7c9.json", "tests/axb-c.viv")
    assert error_message == ''
    assert value == 26

    value, error_message = Viv.run("tests/a5b7c9.json", "return(a+b+c)")
    assert error_message == ''
    assert value == 21

    value, error_message = Viv.run("tests/dog2cat3.json",
                                       "sum = 0; for (a in _) {sum += a.number}; return(sum)")
    assert error_message == ''
    assert value == 5

    value, error_message = Viv.run({"x":[1,2],"y":True},"return(if(y){:=x[0]}else{:=x[1]})")
    assert error_message == ''
    assert value == 1

    value, error_message = Viv.run({"x":[1,2],"y":False},"return(if(y){:=x[0]}else{:=x[1]})")
    assert error_message == ''
    assert value == 2

    value, error_message = Viv.run({"x":[1,2]},{"y":True},"return(if(y){:=x[0]}else{:=x[1]})")
    assert error_message == ''
    assert value == 1

    value, error_message = Viv.run({"x":[1,2]},{"y":False},"return(if(y){:=x[0]}else{:=x[1]})")
    assert error_message == ''
    assert value == 2

    value, error_message = Viv.run({"x":1},"y: x", {"x":10}, "y += x, return(y)")
    assert error_message == ''
    assert value == 11

    value, error_message = Viv.run({"x": {"y": 1}}, "return(x.y)")
    assert error_message == ''
    assert value == 1

    value, error_message = Viv.run({"x": [1]}, "return(x.0)")
    assert error_message == ''
    assert value == 1

    value, error_message = Viv.run({"x": {"0": 1}}, "return(x.0)")
    assert error_message == ''
    assert value == 1

    value, error_message = Viv.run({"x": {0: 1}}, "return(x.0)")
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run({"x": Literal(Token(Token.Type.NUMBER, lexeme="100"))}, "return(x)")
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run({"x":datetime.datetime.now(),"y":False},"return(if(y){:=x.year}else{:=x.month})")
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run("a = [1, 2, 3, 4, 5]", Config(max_array_size=4))
    assert error_message != ''
    assert value is None

def test_parse_and_run():
    """Unit-test for "Viv.parse" and "Viv.run" method."""
    parsed, error_message = \
        Viv.parse("3", "2", "return(_[0] + _[1])", Config(max_depth=3))
    assert error_message == ''
    assert parsed is not None

    value, error_message = Viv.run(parsed)
    assert error_message == ''
    assert value == 5

    parsed, error_message = \
        Viv.parse({"x":[1,2]},{"y":True},"return(if(y){:=x[0]}else{:=x[1]})")
    assert error_message == ''
    assert parsed is not None

    value, error_message = Viv.run(parsed)
    assert error_message == ''
    assert value == 1

    parsed, error_message = Viv.parse("return(foo + bar)")
    assert error_message == ''
    assert parsed is not None
    value, error_message = Viv.run('{"foo":3, "bar": 2}', parsed)
    assert error_message == ''
    assert value == 5
    # print(value);  # 5

def test_parse_file_and_run():
    """Unit-test for "Viv.parse_file" and "Viv.run" method."""
    parsed, error_message = Viv.parse_file("tests/call_6.viv")
    assert error_message == ''
    assert parsed is not None

    value, error_message = Viv.run(parsed)
    assert error_message == ''
    assert value == 6

    parsed, error_message = Viv.parse_file(5)
    assert error_message != ''
    assert parsed is None

    parsed, error_message = Viv.parse_file("tests/empty.viv")
    assert error_message == ''
    assert parsed is not None

    value, error_message = Viv.run(parsed)
    assert error_message == ''
    assert value == {}

    parsed, error_message = Viv.parse_file("tests/invalid.txt")
    assert error_message != ''
    assert parsed is None

def test_parse_text_and_run():
    """Unit-test for "Viv.parse_text" and "Viv.run" method."""
    parsed, error_message = Viv.parse_text("return(3 + 2)")
    assert error_message == ''
    assert parsed is not None

    value, error_message = Viv.run(parsed)
    assert error_message == ''
    assert value == 5

    parsed, error_message = Viv.parse_text("return(3")
    assert error_message != ''
    assert parsed is None

    parsed, error_message = Viv.parse_text(3)
    assert error_message != ''
    assert parsed is None

def test_run_with_variables():
    """Unit-test for "Viv.run" method."""
    parsed, error_message = Viv.parse_text("return(x.a+x.b)")
    assert error_message == ''
    assert isinstance(parsed.statements, list)
    assert isinstance(parsed.statements[0], Return)
    text = str(parsed.statements[0])
    assert text == 'return(x["a"] + x["b"])'

    variable = {"x": {"a": 70, "b": 30}}

    value, error_message = Viv.run(variable, parsed)
    assert error_message == ''
    assert value == 100

    value, error_message = Viv.run(1, parsed)
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run(variable, 3)
    assert error_message != ''
    assert value is None

    parsed, error_message = \
        Viv.parse_text("return(if(y){:=x[0]}else{:=x[1]})")
    assert error_message == ''
    variable = {"x":[1,2],"y":True}
    value, error_message = Viv.run(variable, parsed)
    assert error_message == ''
    assert value == 1

    variable["y"] = False
    value, error_message = Viv.run(variable, parsed)
    assert error_message == ''
    assert value == 2

    parsed, error_message = \
        Viv.parse("y: x", {"x":10}, "y += x, return(y)")
    assert error_message == ''
    assert parsed is not None

    value, error_message = Viv.run({"x": 100}, parsed)
    assert error_message == ''
    assert value == 110

    parsed, error_message = Viv.parse_text("return(x.0)")
    assert error_message == ''
    assert isinstance(parsed.statements, list)

    value, error_message = Viv.run({"x": [100]}, parsed)
    assert error_message == ''
    assert value == 100

    value, error_message = Viv.run({"x": {"0": 100}}, parsed)
    assert error_message == ''
    assert value == 100

    value, error_message = Viv.run({"x": {0: 100}}, parsed)
    assert error_message != ''
    assert value is None

TEST_MAKE_INSTANCE_AND_RUN_DATA = (
    ([3, 8], 11, False),
    ([3, None], 3, False),
    ([True, False], True, False),
    (['foo', 'bar'], 'foobar', False),
    ([['foo', 'bar'], 'baz'], ['foo', 'bar', 'baz'], False),
    ([('foo', 'bar'), 'baz'], None, True),
    ((('foo', 'bar'), 'baz'), None, True),
    ([{'foo': 2, 'bar': 5}, {'baz': 10}], {'foo': 2, 'bar': 5, 'baz': 10}, False),
    ([{'foo': 2, 'bar': 5}, {1: 10}], None, True),
    ([1, [datetime.datetime.now(), 2]], None, True),
    ([{'foo': 2, 'bar': 5}, {'baz': datetime.datetime.now()}], None, True),
)

def test_make_instance_and_run():  # pylint: disable=R0915
    """Unit-test for "Viv.make_instance" and "Viv.run" method."""
    code = '_x = 3 ' \
           'function add(a, b) { ' \
           '  return(a + b) ' \
           '} ' \
           'y = true'

    instance, error_message = Viv.make_instance(code)
    assert error_message == ''
    assert instance is not None

    for data in TEST_MAKE_INSTANCE_AND_RUN_DATA:
        result, error_message = Viv.run(instance, Method('add', data[0]))
        assert (error_message == '') != data[2]
        assert result == data[1]

    parsed, error_message = Viv.parse(code)
    assert error_message == ''
    assert parsed is not None
    instance, error_message = Viv.make_instance(parsed)
    assert error_message == ''
    assert instance is not None
    for data in TEST_MAKE_INSTANCE_AND_RUN_DATA:
        result, error_message = Viv.run(instance, Method('add', data[0]))
        assert (error_message == '') != data[2]
        assert result == data[1]

    result, error_message = Viv.run(instance, Method('add', [100, -10]))
    assert error_message == ''
    assert result == 90

    result, error_message = Viv.run(Method('add', [100, -10]), instance)
    assert error_message == ''
    assert result == 90

    instance, error_message = Viv.make_instance(
        'function add(a, b) { '
        '  return(a + b) '
        '} '
        'y = 3 / 0'
    )
    assert error_message != ''
    assert instance is None

    instance, error_message = Viv.make_instance(
        'function div(a, b) { '
        '  return(a / b) '
        '} '
        'function _div(a, b) { '
        '  return(a / b) '
        '} '
        'y = 3 / 2'
    )
    assert error_message == ''
    assert instance is not None
    result, error_message = Viv.run(instance, Method('div', [10, 0]))
    assert error_message != ''
    assert result is None
    result, error_message = Viv.run(instance, Method('div', [10, 2]))
    assert error_message == ''
    assert result == 5
    result, error_message = Viv.run(instance, Method('div', (10, 2)))
    assert error_message == ''
    assert result == 5
    result, error_message = Viv.run(instance, Method('_div', [10, 2]))
    assert error_message != ''
    assert result is None
    result, error_message = Viv.run(datetime.datetime.now(), Method('div', [10, 10]))
    assert error_message != ''
    assert result is None
    result, error_message = Viv.run(instance, Method('add', [3, 2]))
    assert error_message != ''
    assert result is None
    result, error_message = Viv.run(instance, Method(1, [3, 2]))
    assert error_message != ''
    assert result is None
    result, error_message = Viv.run(instance, Method('div', {"a": 3, "y": 2}))
    assert error_message != ''
    assert result is None

    instance, error_message = Viv.make_instance(True)
    assert error_message != ''
    assert instance is None

    code = "function test(x, y) {" \
            "  z = x.a + x.b.1 + y" \
            "  return(z)" \
            "}"
    map_x = {"a": 100, "b": [1.0, 2.0]}
    instance, error_message = Viv.make_instance(code)
    assert error_message == ''
    assert instance is not None
    result, error_message = Viv.run(instance, Method("test", [map_x, 3]))
    assert error_message == ''
    assert result == 105.0

    data = '["foo", 10, [{"bar": null, "baz": "test"}, false]]'
    instance, error_message = Viv.make_instance(data)
    assert error_message == ''
    assert instance is not None
    value, error_message = Viv.run(instance, "return(_[2][0]['bar'])")
    assert error_message == ''
    assert value is None  # null
    # print(value)  # None (null is represented as None in Python.)
    value, error_message = Viv.run(instance, "return(_.2.-2.baz)")
    assert error_message == ''
    assert value == 'test'
    # print(value)  # test

    code = 'function add(a, b) {' \
           '  return(a + b)' \
           '}'
    instance, error_message = Viv.make_instance(code)
    assert error_message == ''
    assert instance is not None
    value, error_message = Viv.run(instance, Method('add', [10, 20]))
    assert error_message == ''
    assert value == 30
    # print(value)  # 30
    value, error_message = Viv.run(instance, 'return(add(10, 20))')
    assert error_message == ''
    assert value == 30
    # print(value)  # 30

    code = "function add(a, b) {" \
           "  return(a + b)" \
           "}" \
           "c = [20, false]"
    instance, error_message = Viv.make_instance(code)
    assert error_message == ''
    assert instance is not None
    value, error_message = Viv.run(instance, '{"foo":3, "bar": 2}', 'return(add(foo, bar))')
    assert error_message == ''
    assert value == 5
    # print(value)  # 5
    value, error_message = Viv.run(instance, Method("add", [3, 2]))
    assert error_message == ''
    assert value == 5
    # print(value)  # 5

    value, error_message = Viv.run(instance, "return(c[0])")
    assert error_message == ''
    assert value == 20
    # print(value)  # 20

@pytest.mark.parametrize(
    'inf, nan, prepared_expression, target_expression, expected_value, is_error', (
        ('Infinity', 'NaN', '"a": {"x": Infinity}', 'a.x', float('inf'), False),
        ('Infinity', 'NaN', '"a": {"x": Infinity}', 'a.x + 1', float('inf'), False),
        ('Infinity', 'NaN', '"a": {"x": -Infinity}', 'a.x', float('-inf'), False),
        ('Infinity', 'NaN', '"a": {"x": -Infinity}', 'a.x + 1', float('-inf'), False),
        ('Infinity', 'NaN', '"a": {"x": NaN}', 'a.x', float('nan'), False),
        ('Infinity', 'NaN', '"a": {"x": NaN}', 'a.x + 1', float('nan'), False),
        (None, None, '"a": {"x": Infinity}', 'a.x', None, False),
        (None, None, '"a": {"x": Infinity}', 'a.x + 1', 1, False),
        (None, None, '"a": {"x": -Infinity}', 'a.x', None, False),
        (None, None, '"a": {"x": -Infinity}', 'a.x + 1', 1, False),
        (None, None, '"a": {"x": NaN}', 'a.x', None, False),
        (None, None, '"a": {"x": NaN}', 'a.x + 1', 1, False),
    )
)

def test_run_inf_nan(inf, nan, prepared_expression, target_expression, expected_value, is_error):  # pylint: disable=R0913
    """Unit-test for "Viv.run" method and infinity/nan"""
    config = Config(infinity=inf, nan=nan)
    statement = f'{prepared_expression}; return({target_expression})'
    value, error_message = Viv.run(statement, config)
    assert (error_message != '') == is_error
    if isinstance(expected_value, float) and isnan(expected_value):
        assert isnan(value) is True
    else:
        assert value == expected_value
    if inf is not None and nan is not None and not is_error:
        value, error_message = Viv.run(prepared_expression, config)
        text = Viv.make_string(value, config)
        assert text == f'{{{prepared_expression}}}'

def test_run_inf_nan_with_file():
    """Unit-test for "Viv.run" method and infinity/nan with a JSON file."""
    value, error_message = Viv.run('tests/inf_nan.json')
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run('tests/inf_nan.json', Config(infinity="Infinity", nan="NaN"))
    assert error_message == ''
    assert isinstance(value, dict)
    assert value["normal"] == 1.5
    assert value["inf"] == float('inf')
    assert value["negative_inf"] == float('-inf')
    assert isnan(value["nan"])
    assert value["str"] == "1.5"

def test_json():  # pylint: disable=R0915
    """Unit-test for JSON."""
    text1 = "{\"a\": 5, \"b\": [2, 1]}"
    # Valid as Script's code and JSON's value
    value, error_message = Viv.run(text1)
    assert error_message == ''
    assert Viv.make_string(value) == text1
    # Valid as JSON's value
    value, error_message = Viv.run(Json(text1))
    assert error_message == ''
    assert Viv.make_string(value) == text1

    text2 = "{\"a\": 3 + 2, \"b\": [2, 1]}"
    # Valid as Script's code and JSON's value
    value, error_message = Viv.run(text2)
    assert error_message == ''
    assert Viv.make_string(value) == text1
    # Invalid as JSON's value: 3 + 2
    value, error_message = Viv.run(Json(text2))
    assert error_message != ''  # Error
    assert value is None  # Result is nothing

    code = "return(a)"
    text1 = "{\"a\": 5, \"b\": [2, 1]}"
    # Valid as Script's code and JSON's value
    value, error_message = Viv.run(text1, code)
    assert error_message == ''
    assert value == 5
    # Valid as JSON's value
    value, error_message = Viv.run(Json(text1), code)
    assert error_message == ''
    assert value == 5

    text2 = "{\"a\": 3 + 2, \"b\": [2, 1]}"
    # Valid as Script's code and JSON's value
    value, error_message = Viv.run(text2, code)
    assert error_message == ''
    assert value == 5
    # Invalid as JSON's value: 3 + 2
    value, error_message = Viv.run(Json(text2), code)
    assert error_message != ''  # Error
    assert value is None  # Result is nothing

    data = '{"foo": 3}'
    code = 'return(foo)'
    value, error_message = Viv.run(Json(data), code)
    assert error_message == ''
    assert value == 3
    # print(value)  # 3

    code = "return(_)"
    text1 = "5"
    # Valid as Script's code and JSON's value
    value, error_message = Viv.run(text1, code)
    assert error_message == ''
    assert value == 5
    # Valid as JSON's value
    value, error_message = Viv.run(Json(text1), code)
    assert error_message == ''
    assert value == 5

    text2 = "10 / 2"
    # Valid as Script's code and JSON's value
    value, error_message = Viv.run(text2, code)
    assert error_message == ''
    assert value == 5
    # Invalid as JSON's value: 10 / 2
    value, error_message = Viv.run(Json(text2), code)
    assert error_message != ''  # Error
    assert value is None  # Result is nothing

    code = "return(a)"
    text1 = "{\"a\": Infinity}"
    # *** With configuration ***
    config = Config()
    config.set_infinity("Infinity")
    # Valid as Script's code and JSON's value
    value, error_message = Viv.run(text1, code, config)
    assert error_message == ''
    assert value == float('inf')
    # Valid as JSON's value
    value, error_message = Viv.run(Json(text1), code, config)
    assert error_message == ''
    assert value == float('inf')

    # *** Without configuration ***
    # Valid as Script's code and JSON's value
    # However, Infinity is treated as the undefined variable.
    # So the evaluated result will be null.
    value, error_message = Viv.run(text1, code)
    assert error_message == ''
    assert value is None  # None
    # Invalid as JSON's value because the value of key-value is not
    # number, string, boolean, object, array, or null.
    # The above Infinity is not string because it is not surrounded
    # with quotation marks.
    value, error_message = Viv.run(Json(text1), code)
    assert error_message != ''  # Error
    assert value is None  # Result is nothing

    code = "return(_)"
    text1 = "Infinity"
    # *** With configuration ***
    config = Config()
    config.set_infinity("Infinity")
    # Valid as Script's code and JSON's value
    value, error_message = Viv.run(text1, code, config)
    assert error_message == ''
    assert value == float('inf')
    # Valid as JSON's value
    value, error_message = Viv.run(Json(text1), code, config)
    assert error_message == ''
    assert value == float('inf')

    # *** Without configuration ***
    # Valid as Script's code and JSON's value
    # However, it is treated as String.
    value, error_message = Viv.run(text1, code)
    assert error_message == ''
    assert value == text1
    # Valid as JSON's value
    # However, it is treated as String.
    value, error_message = Viv.run(Json(text1), code)
    assert error_message == ''
    assert value == text1

@pytest.mark.parametrize(
    'value, expected_string, inf, nan', (
        (2, '2', None, None),
        (1.5, '1.5', None, None),
        (1.0, '1.0', None, None),
        (float('inf'), '', None, None),
        (float('inf'), 'Infinity', 'Infinity', None),
        (float('inf'), '', None, 'NaN'),
        (float('inf'), 'Infinity', 'Infinity', 'NaN'),
        (float('-inf'), '', None, None),
        (float('-inf'), '-Infinity', 'Infinity', None),
        (float('-inf'), '', None, 'NaN'),
        (float('-inf'), '-Infinity', 'Infinity', 'NaN'),
        (float('nan'), '', None, None),
        (float('nan'), '', 'Infinity', None),
        (float('nan'), 'NaN', None, 'NaN'),
        (float('nan'), 'NaN', 'Infinity', 'NaN'),
        (True, 'true', None, None),
        (False, 'false', None, None),
        ("abcd", 'abcd', None, None),
        (None, 'null', None, None),
        ([], '[]', None, None),
        ([1,2], '[1, 2]', None, None),
        ((), '[]', None, None),
        (('a','b'), '["a", "b"]', None, None),
        ({}, '{}', None, None),
        ({'a': 3.0, 'b': True}, '{"a": 3.0, "b": true}', None, None),
        ({'a': 3.0, 'b': {"c": [True, None]}}, '{"a": 3.0, "b": {"c": [true, null]}}', None, None),
    )
)

def test_make_string(value, expected_string, inf, nan):
    """Unit-test for "Viv.make_string" method."""
    config = Config(infinity=inf, nan=nan)
    string = Viv.make_string(value, config=config)
    assert string == expected_string
