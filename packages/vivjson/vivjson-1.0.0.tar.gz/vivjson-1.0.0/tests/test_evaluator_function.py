"""Unit-test for function in Evaluator

Unit-test for function call and its definition

Run `python3 -m pytest tests/test_evaluator_function.py` in
parent directory.

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
__date__ = '2025-03-30'

# pylint: disable=C0301, E0401, R0801

import pytest
from vivjson.viv import Viv
from vivjson.config import Config

@pytest.mark.parametrize(
    'prepared_expression, target_expression, expected_value, is_error', (
        ('function x2(a) {return(a * 2)}', 'x2(1.5)', 3.0, False),
        ('function x2(a) {return(a*2)}', 'x2(3)', 6, False),
        ('x = test(1), function test(a) {return(a*100)}', 'x', None, True),  # Error because certain function is executed before its definition.
        ('function test(a) {return(a*100)}, x = [test(1)], function test(a) {return(a+10)}, x += test(1)', 'x', [100, 11], False),
        ('function test() {for (i = 0; i < 10; i += 1) { if (i > 5) {return(i)}}}', 'test()', 6, False),
        ('function test() {i = 0, for (; i < 10; i += 1) { if (i > 5) {return(i)}}}', 'test()', 6, False),
        ('function test() {i = 0, for (; i < 10; i += 1) { if (i > 5) {break}}, return(i)}', 'test()', 6, False),
        ('function test() {i = 0, for (; i < 10; i += 1) { if (i > 5) {break}}}', 'test()', {"i": 6}, False),
        ('function test(a) {for (i = 0; i < 10; i += 1) {a /= 2}, return(a)}', 'test(100)', 0.09765625, False),
        ('function test(a) {for (i = 0; i < 10; i += 1) { if (i >= 5) {continue}, a /= 2}, return(a)}', 'test(100)', 3.125, False),
        ('function test(a) {for (i = 0; i < 10; i += 1) { if (i >= 5) {break}, a /= 2}, return(a)}', 'test(100)', 3.125, False),
        ('function test(a) {i = 0, for (; i < 10; i += 1) { if (i >= 5) {continue}, a /= 2}, b = a}', 'test(100)', {"i": 10, "b": 3.125}, False),
        ('function test(a) {i = 0, for (; i < 10; i += 1) { if (i >= 5) {break}, a /= 2}, b = a}', 'test(100)', {"i": 5, "b": 3.125}, False),
        ('function test(a) {i = 0, for (; i < 10; i += 1) { if (i >= 5) {return("foo")}, a /= 2}, b = a}', 'test(100)', "foo", False),
        ('function test() {sum = 0 for (i = 0; i < 10; i += 1) {sum += i}}, a = test()', 'a', {'sum': 45}, False),
        ('function test() {sum = 0 for (i = 0; i < 10; i += 1) {sum += i} := sum}, a = test()', 'a', 45, False),
        ('function test() {sum = 0 for (i = 0; i < 10; i += 1) {sum += i} := sum sum += 100}, a = test()', 'a', 45, False),
        ('function test() {sum = 0 for (i = 0; i < 10; i += 1) {sum += i} := sum sum += 100 return(sum)}, a = test()', 'a', 145, False),
        ('function test() {a = 10}, x = test()', 'x', {"a": 10}, False),
        ('function test() {a = 10, a = 20}, x = test()', 'x', {"a": 20}, False),
        ('function test() {a = 10, a += 20}, x = test()', 'x', {"a": 30}, False),
        ('function test() {a = 10, break, a += 20}, x = test()', 'x', None, True),  # It is invalid that there is "break" just under the function.
        ('function test() {a = 10, continue, a += 20}, x = test()', 'x', None, True),  # It is invalid that there is "continue" just under the function.
        ('function test() {a = 10, return, a += 20}, x = test()', 'x', {"a": 10}, False),
        ('function add(a, b) {return(a + b)} x = add(3, 2, 1)', 'x', 5, False),
        ('function add_dirty(a, b) {return(a + b + _[2])}, x = add_dirty(3, 2, 1)', 'x', 6, False),
        ('function add_whole() { sum = 0 for (value in _) { sum += value } return(sum) }, x = add_whole(-5, 10, 1.5)', 'x', 6.5, False),
        ('function test(a, b) { return (string(a) + ", " + string(b)) }, x = test(100)', 'x', '100, null', False),
        ('function enclosure(a) {x = a, function closure(y) {return(x + y)}, return(closure)}, z1 = enclosure(100), z2 = enclosure(200), a = z1(5), b = z2(10)', '[a, b]', [105, 210], False),  # Closure
        ('a = ">", b= null, function run(function worker) {a="::", worker()}, run({b = a + " test"})', 'b', ':: test', False),  # Anonymous function in argument.
        ('a = ">", function run(function worker) {worker()}, b= null, a="::", run({b = a + " test"})', 'b', ':: test', False),  # Anonymous function in argument.
        ('a = ">", b= null, function run(function worker) {a="::", worker()}, run() {b = a + " test"}', 'b', ':: test', False),  # Anonymous function in argument.
        ('a = ">", b= null, function run(function worker) {a="::", worker()}, run {b = a + " test"}', 'b', ':: test', False),  # Anonymous function in argument.
        ('a = ">", b= null, function run(function worker) {a="::", worker()}, c = run {b = a + " test"}', 'c', {}, False),  # Anonymous function in argument.
        ('a = ">", b= null, function run(function worker) {a="::", worker(), :=100}, c = run {b = a + " test"}', 'c', 100, False),  # Anonymous function in argument.
        ('a = [1, 2, 3], function x2(before, list, after) {for (i = 0; i < len(list); i += 1) {list[i] *= 2}, return([before, list, after])}, b = x2(a, a, a)', '[a, b]', [[1, 2, 3], [[1, 2, 3], [2, 4, 6], [1, 2, 3]]], False),  # Call by value
        ('a = [1, 2, 3], function x2(before, reference list, after) {for (i = 0; i < len(list); i += 1) {list[i] *= 2}, return([before, list, after])}, b = x2(a, a, a)', '[a, b]', [[2, 4, 6], [[1, 2, 3], [2, 4, 6], [1, 2, 3]]], False),  # Call by reference
        ('a = {"x": 10, "y": 20}, function x2(before, map, after, k) {for (pair in map) {map[pair[0]] = pair[1] * 2}, k *= 2, return([before, map, after, k])}, b = 30, c = x2(a, a, a, b)', '[a, b, c]', [{"x": 10, "y": 20}, 30, [{"x": 10, "y": 20}, {"x": 20, "y": 40}, {"x": 10, "y": 20}, 60]], False),  # Call by value
        ('a = {"x": 10, "y": 20}, function x2(before, reference map, after, reference k) {for (pair in map) {map[pair[0]] = pair[1] * 2}, k *= 2, return([before, map, after, k])}, b = 30, c = x2(a, a, a, b)', '[a, b, c]', [{"x": 20, "y": 40}, 30, [{"x": 10, "y": 20}, {"x": 20, "y": 40}, {"x": 10, "y": 20}, 60]], False),  # Call by reference
        ('function import(a) {return(a*2)}', 'import(3)', None, True),  # "import" is reserved word.
        ('function super(a) {return(a*2)}', 'super(3)', None, True),  # "super" is reserved word.
        ('', 'fake()', None, True),  # fake function is not existed.
    )
)

def test_function(prepared_expression, target_expression, expected_value,
                  is_error):
    """Unit-test for function in Evaluator

    Unit-test for function call and its definition

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
    config = Config(max_depth=14)

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

def test_depth():
    """Unit-test for max depth."""
    text = 'function test() {for (i = 0; i < 10; i += 1) { if (i > 5) {return(i)}}}, return(test())'
    value, error_message = Viv.run(text, Config(max_depth=9))
    assert error_message != ''
    assert value is None

    value, error_message = Viv.run(text, Config(max_depth=10))
    assert error_message == ''
    assert value == 6

def test_first_class():
    """Unit-test for 1st class."""
    value, error_message = Viv.run("tests/func_array.viv")
    assert error_message == ''
    assert value == [15, [15, 5, 50, 2], [15, 5, 50, 2], [15, 5, 50, 2], 3, [3, 100, 100.0, "100"], [3, 100, 100.0, "100"], [3, 100, 100.0, "100"]]
