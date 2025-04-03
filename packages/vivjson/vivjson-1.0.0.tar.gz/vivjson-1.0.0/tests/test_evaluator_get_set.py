"""Unit-test for get/set/injection in Evaluator

Unit-test for assignment, modification, getting, and variable

Run `python3 -m pytest tests/test_evaluator_get_set.py` in
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
__date__ = '2025-03-23'

# pylint: disable=C0301, E0401, R0801

import pytest
from vivjson.viv import Viv
from vivjson.config import Config

@pytest.mark.parametrize(
    'prepared_expression, target_expression, expected_value, is_error', (
        ({"a": 3}, 'a', 3, False),
        ({"a": NotImplemented}, 'a', None, True),  # Python's NotImplemented can't treated. --> ERROR
        ({"a": Config()}, 'a', None, True),  # Python's class instance can't treated. --> ERROR
        ({"a": "x", "b": "y"}, 'a', "x", False),
        ('a = 1.5', 'a', 1.5, False),
        ('a = 1.5, a+=0.5', 'a', 2.0, False),
        ('a = 3 > 2', 'a', True, False),
        ('a = 3 <= 2', 'a', False, False),
        ('a = "xyz", b = a == "xyz"', 'b', True, False),
        ('a = "xyz", b = a != "xyz"', 'b', False, False),
        ('a = {"x": 100}', 'a.x', 100, False),
        ('a = {"x": 100}', 'a.y', None, False),
        ('a = {"x": 100, "_y": 20}', 'a.x', 100, False),
        ('a = {x: 10}', 'a.x', 10, False),
        ('a: {x: -1e4}', 'a["x"]', -10000.0, False),
        ('"a": {"x": "true", y: "false"}', "a['x'] + '&' + a['y']", "true&false", False),
        ('a = [100 10 20]', 'a[0] + a[1] + a[2]', 130, False),
        ('a = [100 10 20] a[1] += 1000', 'a[0] + a[1] + a[2]', 1130, False),
        ('a = [1 5 {b: {c: 10} d: -20}]', 'a.2.b.c', 10, False),
        ('a = [1 5 {b: {c: 10} d: -20}]', 'a[2]["b"]["c"]', 10, False),
        ('a = [1 5 {b: {c: 10} d: -20}]', 'a[2].b["c"]', 10, False),
        ('a = [1 5 {b: {c: 10} d: -20}]', 'a[-1].b.c', 10, False),
        ('', 'a', None, False),  # The undefined variable's value is null.
        ('', 'a.b', None, False),  # The member's value of the undefined variable is null.
        ('', 'a["b"]', None, False),  # The member's value of the undefined variable is null.
        ('', 'a[1]', None, False),  # The member's value of the undefined variable is null.
        ('a = {}', 'a', {}, False),
        ('a = []', 'a', [], False),
        ('a = [true, 100]', 'a[0]', True, False),
        ('a = [true, 100]', 'a[1]', 100, False),
        ('a = [true, 100]', 'a[2]', None, False),  # null is gotten even if out of range
        ('a = [true, 100]', 'a[-1]', 100, False),
        ('a = [true, 100]', 'a[-2]', True, False),
        ('a = [true, 100]', 'a[-3]', None, False),  # null is gotten even if out of range
        ('a = [true, 100]', 'a[false]', None, True),  # boolean can not be used as index.
        ('a = [true, 100], a[0] = 20', 'a[0]', 20, False),
        ('a = [true, 100], x = 0, a[x] = 10', 'a[0]', 10, False),
        ('a = [true, 100], x = 0, a[x] = 10', 'a[x]', 10, False),
        ('a = [true, 100], x = 0', 'a.x', None, True),  # a.x is invalid.
        ('a = [true, 100], b = 2.5 * 0.4', 'a[b]', 100, False),
        ('a = [true, 100]', 'a[2.5 * 0.4]', 100, False),
        ('a = [true, 100]', 'a[2.5 * 0.3]', None, True),  # 2.5 * 0.3 = 0.75 is invalid as index.
        ('a = [true, 100], a[2] = 20', 'a[0]', None, True),  # a[2] makes error.
        ('a = [true, 100], a += [false, 20]', 'a', [True, 100, [False, 20]], False),
        ('a = {x: true y: 100} a += {x: false, y: 20}', 'a', {"x": True, "y": 120}, False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x["b"][0]', True, False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x["b"].0', True, False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b[0]', True, False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b.0', True, False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b.-2', True, False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b[-2]', True, False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b["0"]', None, True),  # The index of array must be number.
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b.1.0', "foo", False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b.1["0"]', "foo", False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b.1[0]', "foo", False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b.-1[0]', "foo", False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b[-1].0', "foo", False),
        ('x = {"a": 100, "b": [true, {"c": 3, "0": "foo"}]}', 'x.b.-1.0', "foo", False),
        ('a = {b: 3, c: {d: true, e: [null, "x", false]}}', 'a.c.e.1', "x", False),
        ('a = {b: 3, c: {d: true, e: [null, "x", false]}}', 'a["c"].e[-2]', "x", False),
        ('b = 1, a = {b: 3, c: {d: true, e: [null, "x", false]}}', 'a["c"].e[b]', "x", False),
        ('a = {b: 1, "c": 2}; a.d = 3', 'a["d"]', 3, False),
        ('a = [{"b": 1, c: 2}, 3], a[0].b = 5', 'a.0["b"]', 5, False),
        ('a = [{"b": 1, c: 2}, 3], a[0].b = 5', 'a.0. b', 5, False),
        ('a = [{"b": 1, c: 2}, 3], a[0].b = 5', 'a.0.*', None, True),  # .* is invalid.
        ('a = [{"b": 1, c: 2}, 3], a[0].b = 5', 'a.0. *', None, True),  # .* is invalid.
        ('a = {"0": 100, "1": 50}', 'a.0', 100, False),
        ('a = {"0": 100, "1": 50}, a.0 += 80', 'a.0', 180, False),
        ('a = {"0": [10, 30], "1": 50}, a.0 = 80', 'a.0', 80, False),
        ('a = {"0": [10, 30], "1": 50}, a.0.1 += 80', 'a.0[1]', 110, False),
        ('a = {"0": [10, 30], "1": 50}, a.0.1 += 80', 'a.0.1', 110, False),
        ('a = {"0": [10, [30, 70]], "1": 50}, a.0.1.1 += 80', 'a.0.1', [30, 150], False),
        ('a = [1, 2]', 'a[0.5]', None, True),  # Index must be integer.
        ('a = [1, 2]', 'a[1.0]', 2, False),
        ('a = [1, 2], a[0.5] = 1.5', 'a', None, True),  # Index must be integer.
        ('a = [1, 2], a[1.0] = 1.5', 'a', [1, 1.5], False),
        ('x = 10, y = if (x >= 0) { s = "+" } else { s = "-" }', 'y', {"s": "+"}, False),
        ('function x2(k) {return(_[0] * 2)}', 'x2(3)', 6, False),
        ('function x2(k) {_[0] *= 2 return(k)}', 'x2(3)', 6, False),
        ('function x2(k) {return(k * 2)}', 'x2(3)', 6, False),
        ('function x2(k) {k *= 2 return(_[0])}', 'x2(3)', 6, False),
        ('a = {b: 3}, function x2(k) {k.b *= 2 return(k.b)}', 'x2(a)', 6, False),
        ('a = {b: 3}, function x2(k) {k.b *= 2 return(_[0]["b"])}', 'x2(a)', 6, False),
        ('a = {b: 3}, function x2(k) {_[0]["b"] *= 2 return(k.b)}', 'x2(a)', 6, False),
        ('a = {b: 3}, function x2(k) {k.b *= 2 return(k.b)}, x2(a)', 'a.b', 3, False),
        ('a = {b: 3}, function x2(k) {return(k.b * 2)}', 'x2(a)', 6, False),
        ('while = 3, x = 2, while(x < 10) {x+=10}', '[while, x]', [3, 12], False),  # "while" is not reserved word.
        ('function while(a) { return(true) }', 'while(10)', True, False),  # "while" is not reserved word.
        ('for = 3', 'for', None, True),  # "for" is reserved word.
        ('import = 3', 'import', None, True),  # "import" is reserved word.
        ('super = 3', 'super', None, True),  # "super" is reserved word.
        ('___#RESULT#___ = 1', '___#RESULT#___', None, True),  # "RESULT#___ = 1" is ignored as comment.
        ('___i___ = 1', '___i___', None, True),  # It is invalid that both of prefix and suffix are "___".
        ('______ = 1', '______', None, True),  # It is invalid that both of prefix and suffix are "___".
        ('_____ = 1', '_____', 1, False),
        ('a = {b: 3, c:[2, 1]}, remove(a)', 'a', None, False),
        ('a = {b: 3, c:[2, 1]}, remove(a.b)', 'a', {"c": [2, 1]}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a.c)', 'a', {"b": 3}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a["b"])', 'a', {"c": [2, 1]}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a.c.0)', 'a', {"b": 3, "c": [1]}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a.c.1)', 'a', {"b": 3, "c": [2]}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a.c.-2)', 'a', {"b": 3, "c": [1]}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a.c.-1)', 'a', {"b": 3, "c": [2]}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a.c[-1])', 'a', {"b": 3, "c": [2]}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a["c"][-1])', 'a', {"b": 3, "c": [2]}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a["c"])', 'a', {"b": 3}, False),
        ('a = {b: 3, c:[2, 1]}, remove(a.c.2)', 'a', None, True),  # Out of range
        ('a = {b: 3, c:[2, 1]}, remove(a["c"][2])', 'a', None, True),  # Out of range
        ('a = {b: 3, c:[2, 1]}, remove(a["c"][-3])', 'a', None, True),  # Out of range
        ('a = {b: 3, c:[2, 1]}, remove(a.d)', 'a', {"b": 3, "c":[2, 1]}, False),  # Nothing
        ('a = {b: 3, c:[2, 1], d: {e: false, remove(c[1])}}', 'a', {"b": 3, "c":[2], "d": {"e": False}}, False),
        ('a = 100, do {a: 100, remove(a)}', 'a', 100, False),
        ('a = 100, do {remove(a)}', 'a', None, False),
        ('do {remove(a)}', 'a', None, False),
        ('a={x:[30, 2]}; b=a; b.x.1=5; remove(b.x.0)', '[a, b]', [{"x": [30, 2]}, {"x": [5]}], False),
    )
)

def test_get_set(prepared_expression, target_expression, expected_value,
                 is_error):
    """Unit-test for get/set expression in Evaluator

    Unit-test for assignment, modification, getting, and variable

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
    config = Config(max_depth=10)

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
