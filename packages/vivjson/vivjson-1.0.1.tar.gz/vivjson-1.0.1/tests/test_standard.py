"""Unit-test for Standard library

Run `python3 -m pytest tests/test_standard.py` in parent directory.

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
        ('a = 10; if (a > 5) { a += 100 }', 'a', 110, False),
        ('a = 10; if (a > 5) { a += 100 } else { a -= 100 }', 'a', 110, False),
        ('a = 1; if (a > 5) { a += 100 } else { a -= 100 }', 'a', -99, False),
        ('a = 1; if (a > 5) { a += 100 } elseif (a < 0) { a -= 100 }', 'a', 1, False),
        ('x = if (true) { a = 100 } else { a = -100 }', 'x', {"a": 100}, False),
        ('x = if (true) { := 100 } else { := -100 }', 'x', 100, False),
        ('a = -1, x = if (a < 0) {:= "-"} elseif (a == 0) {:="zero"} else {:="+"}', 'x', "-", False),
        ('a = 0, x = if (a < 0) {:= "-"} elseif (a == 0) {:="0" :="zero" x=0} else {:="+"}', 'x', "zero", False),
        ('a = 1.5, x = if (a < 0) {:= "-"} elseif (a == 0) {:="zero"} else {:="+"}', 'x', "+", False),
        ('a = -0.01, b = -1, result = "" ' \
         'if (a < 0) { if (b < 0) { result = "< <" } else { result = "< >=" } } ' \
         'else { if (b < 0) { result = ">= <" } else { result = ">= >=" } }',
         'result', "< <", False),
        ('a = -10, b = 100000, result = "" ' \
         'if (a < 0) { if (b < 0) { result = "< <" } else { result = "< >=" } } ' \
         'else { if (b < 0) { result = ">= <" } else { result = ">= >=" } }',
         'result', "< >=", False),
        ('a = 0, b = -1e-3, result = "" ' \
         'if (a < 0) { if (b < 0) { result = "< <" } else { result = "< >=" } } ' \
         'else { if (b < 0) { result = ">= <" } else { result = ">= >=" } }',
         'result', ">= <", False),
        ('a = -1, b = -1e-8, result = "" ' \
         'if (a < 0) { if (b < 0) { result = "< <" } else { result = "< >=" } } ' \
         'else { if (b < 0) { result = ">= <" } else { result = ">= >=" } }',
         'result', "< <", False),
        ('a = -10, b = 100000, result = "" ' \
         'if (a < 0) { if (b < 0) { result = "< <" } /* else { result = "< >=" } */ } ' \
         'else { if (b < 0) { result = ">= <" } else { result = ">= >=" } }',
         'result', "", False),
        ('a = -0.01, b = -1, result = "", ' \
         'if (a < 0 and b < 0) { result = "< <" } '\
         'elseif (a < 0 and b >= 0) { result = "< >=" } ' \
         'elseif (a >= 0 and b < 0) { result = ">= <" } ' \
         'else { result = ">= >=" }',
         'result', "< <", False),

        ('a = [] do {a += 1, a += 2}', 'a', [1, 2], False),
        ('a = [] do {a += 1, break, a += 2}', 'a', [1], False),
        ('i=0, do {i += 1, continue}', 'i', None, True),
        ('i=0, do {i += 1, if (i <= 10) {continue}}', 'i', 11, False),
        ('x = do {i = 100, a = true, b = null}', 'x', {"i": 100, "a": True, "b": None}, False),

        ('i = 0; while (i < 10) { a = i;  i += 1}', 'i', 10, False),
        ('_i = 0; while (_i < 10) { a = _i;  _i += 1}', '_i', 10, False),
        ('i = 0; while (true) { i+=1 }', 'i', None, True),  # Infinite loop
        ('i = 0; while (true) { i+=1 if (i >= 3) {break} }', 'i', 3, False),
        ('i = 0, x = [], while (i < 10) { i += 1 if (i < 5) {continue} x += i }', 'x', [5, 6, 7, 8, 9, 10], False),
        ('i = 1 a = while (i < 10) { return(100) }', '[i, a]', 100, False),  # 100 is returned because {i = 1, a = while (i < 10) { return(100) }, return([i, a])}
        ('i = 1 a = while (i < 10) { i += 1 }', '[i, a]', [10, {}], False),
        ('i = 1 a = while (i < 10 { i += 1 })', '[i, a]', [10, {}], False),
        ('i = 1; a = while (i < 10; { i += 1 })', '[i, a]', [10, {}], False),
        ('i = 1 a = while (i < 10) { last = i, i += 1 }', '[i, a]', [10, {"last": 9}], False),
        ('i = 1 a = while (i < 10) { := i, i += 1 }', '[i, a]', [10, 9], False),

        ('i = 10; for (; i >= 0; i -= 2) { a = i }', 'i', -2, False),
        ('for (i = 0; i < 20; i += 1) { a = i; }', '[a, i]', [None, None], False),
        ('a = null, for (i = 0; i < 20; ; ; ) { i += 1, a = i }', '[i, a]', None, True),  # Arguments is too much.
        ('a = null, for (i = 0; i < 20; ; ) { i += 1, a = i }', '[i, a]', [None, 20], False),
        ('a = null, for (i = 0; i < 20; ) { i += 1, a = i }', '[i, a]', [None, 20], False),
        ('a = null, for (i = 0; i < 20) { i += 1, a = i }', '[i, a]', [None, 20], False),
        ('i = 0; for () { i+=1 }', 'i', None, True),  # Infinite loop
        ('i = 0; for (;;) { i+=1 }', 'i', None, True),  # Infinite loop
        ('i = 0; for (;;i+=1) { i+=0.5 }', 'i', None, True),  # Infinite loop
        ('i = 0; for (;;) { i = 1 break i = 2 }', 'i', 1, False),
        ('i = 0; for (;;) { i += 1 continue i = 2 break }', 'i', None, True),  # Infinite loop
        ('i = 1 a = for (; i < 10; i += 1) { return(100) }', '[i, a]', 100, False),  # 100 is returned because {i = 1, a = for (; i < 10; i += 1) { return(100) }, return([i, a])}
        ('i = 1 a = for (; i < 10; i += 1; { return(100) })', '[i, a]', 100, False),  # 100 is returned because {i = 1, a = for (; i < 10; i += 1; { return(100) }), return([i, a])}
        ('a = for (i = 0; i < 10; i += 1) {}', '[i, a]', [None, {"i": 10}], False),
        ('a = for (i = 0; i < 10; i += 1) {:=false}', '[i, a]', [None, False], False),
        ('i = null, for (i = 0) {break}', 'i', 0, False),
        ('i = 0, for (i < 0) {break}', 'i', 0, False),

        ('x = [], for (a in [3, 5, 1]) {x += a * 2}', 'x', [6, 10, 2], False),
        ('x = "", for (a in ["foo", "bar", "baz"]) {x += a + "," }', 'x', "foo,bar,baz,", False),
        ('x = [], list = [3, 5, 1], for (a in list) {x += a * 2}', '[x, list]', [[6, 10, 2], [3, 5, 1]], False),
        ('x = {}, list = {x: 3, y: 5, z: 1}, for (a in list) {x[a[0]] = a[1]*2}', 'x', {"x": 6, "y": 10, "z": 2}, False),
        ('list = [{x: 3, y: 5}], z = null, for (a in list) {z = a.x}', 'z', 3, False),
        ('list = [{x: 3, y: 5}], for (a in list) {a.x = 2}', 'list.0.x', 3, False),
        ('list = [{x: 3, y: 5}], z = null, for (a in list) {a.x = 2, z = a.x}', 'z', 2, False),
        ('list = [{x: 3, y: 5}], for (a in list) {a.x = 2}', 'list', [{"x": 3, "y": 5}], False),
        ('list = {"x": {"y": 5}}, for (a in list) {a[1]["y"] = 1}', 'list', {"x": {"y": 5}}, False),
        ('x = [], list = 1, for (a in list) {x += a * 2}', 'x', None, True),  # Array or Block is permitted.
        ('"foo": 10, "bar": 30, "baz": 20, max=-1, for (pair in .) {if (max < pair[1]) {max = pair[1]}}', 'max', 30, False),

        ('', '[1.0, int(1.0), int(2.8), int("10.3"), int("1e3")]', [1.0, 1, 2, 10, 1000], False),
        ('x = "3.5"', 'int(x)', 3, False),
        ('', 'int()', None, True),  # The argument is necessary.
        ('', 'int("x")', None, True),  # The argument must be number.
        ('', 'int(true)', None, True),  # The argument must be number.
        ('', 'int([1])', None, True),  # The argument must be number.
        ({"a": float('nan')}, 'int(a)', None, True),  # NaN can not be converted.
        ({"a": float('inf')}, 'int(a)', None, True),  # Infinity can not be converted.

        ('', '[10, float(10)]', [10, 10.0], False),
        ('x = "3.5"', 'float(x)', 3.5, False),
        ('', 'float()', None, True),  # The argument is necessary.
        ('', 'float("x")', None, True),  # The argument must be number.
        ('', 'float(true)', None, True),  # The argument must be number.

        ('', 'string(3 + 2)', '5', False),
        ('x = 1.5', 'string(x)', '1.5', False),
        ('', 'string(true)', 'true', False),
        ('', 'string(false)', 'false', False),
        ('', 'string(null)', 'null', False),
        ('', 'string()', None, True),  # The argument is necessary.

        ('', 'len("")', 0, False),
        ('', 'len("abc")', 3, False),
        ('a = len("xyz")', 'a', 3, False),
        ('a = "xyz"', 'len(a)', 3, False),
        ('a = "αβz"', 'len(a)', 3, False),  # multi-byte character "αβ"
        ('', 'len([])', 0, False),
        ('', 'len(["abc", "12345"])', 2, False),
        ('', 'len({})', 0, False),
        ('', 'len({"a": 1, "b": true, "c": null})', 3, False),
        ('', 'len()', None, True),  # The argument is necessary.
        ('', 'len(2)', None, True),  # The argument must be array, block, string
        ('', 'len(true)', None, True),  # The argument must be array, block, string
        ('', 'len(null)', None, True),  # The argument must be array, block, string

        ('a = [], insert(a, 0, 10)', 'a', [10], False),
        ('a = [1, 2, 3, 4, 5], insert(a, len(a), [null, true, false, "text"])', 'a', [1, 2, 3, 4, 5, [None, True, False, "text"]], False),
        ('a = [1, 2, 3, 4, 5], insert(a, len(a), {"x": null})', 'a', [1, 2, 3, 4, 5, {"x": None}], False),
        ('a = [1, 2, 3], insert(a, len(a), 10)', 'a', [1, 2, 3, 10], False),
        ('a = [1, 2, 3], insert(a, 3, 10)', 'a', [1, 2, 3, 10], False),
        ('a = [1, 2, 3], insert(a, 1, 10)', 'a', [1, 10, 2, 3], False),
        ('a = [1, 2, 3], insert(a, 0, 10)', 'a', [10, 1, 2, 3], False),
        ('a = [1, 2, 3], insert(a, -0, 10)', 'a', [10, 1, 2, 3], False),
        ('a = [1, 2, 3], insert(a, -1, 10)', 'a', [1, 2, 10, 3], False),
        ('a = [1, 2, 3], insert(a, -3, 10)', 'a', [10, 1, 2, 3], False),
        ('a = [1, 2, 3], insert(a, 4, 10)', 'a', None, True),  # Out of range
        ('a = [1, 2, 3], insert(a, -4, 10)', 'a', None, True),  # Out of range
        ('a = [1, 2, 3], insert(a, true, 10)', 'a', None, True),  # Index must be number.
        ('a = [1, 2, 3], insert(a, 3)', 'a', None, True),  # Lack the inserted value.
        ('a = [1, 2, 3], insert(a)', 'a', None, True),  # Lack index and the inserted value.
        ('a = 1, insert(a, 0, 10)', 'a', None, True),  # Array is needed.
        ('a = [1, 2, 3, 4, 5, 6], insert(a, len(a), 10)', 'a', None, True),  # Limit of max array size

        ('', 'strip("abc")', "abc", False),
        ('a = "abc"', 'strip(a)', "abc", False),
        ({'a': "\n 　\r abc \n\t"}, 'strip(a)', "abc", False),  # multi-byte character "　"
        ({'a': "\n 　\r αβ \n\t"}, 'strip(a)', "αβ", False),  # multi-byte character "　" and "αβ"
        # ('', 'strip("\n 　\r abc \n\t")', "abc", False),
        # ('a = "\n 　\r abc \n\t"', 'strip(a)', "abc", False),
        # ('a = "\n 　\r αβ \n\t"', 'strip(a)', "αβ", False),
        ('', 'strip()', None, True),  # The argument is necessary.

        ('', 'type(1)', "int", False),
        ('a = 1.5', 'type(a)', "float", False),
        ('', 'type(1.5)', "float", False),
        ('', 'type(1e3)', "float", False),
        ('', 'type("1")', "string", False),
        ('', 'type(true)', "boolean", False),
        ('', 'type(false)', "boolean", False),
        ('', 'type(null)', "null", False),
        ('', 'type([1,2,3])', "array", False),
        ('x = [1, [2, 3]]', 'type(x[1])', "array", False),
        ('', 'type([])', "array", False),
        ('', 'type({"a":1,"b":2})', "block", False),
        ('x = [1, {"a":1,"b":2}]', 'type(x[1])', "block", False),
        ('', 'type({})', "block", False),
        ('function enclosure(a) {x = a, function closure(y) {return(x + y)}, return(closure)}, z1 = enclosure(100)', 'type(z1)', "function", False),
        ('function x2(a) {return(a*2)}', 'type(x2)', "function", False),
        ('function x2(a) {return(a*2)}, foo = x2', 'type(foo)', "function", False),
        ('function x2(a) {return(a*2)}, foo = [x2]', 'type(foo.0)', "function", False),
        ('', 'type(len)', "function", False),
        ('', 'type(print)', "function", False),
        ('', 'type(for)', None, True),  # Parse error
        ('', 'type(break)', None, True),  # Parse error
        ('', 'type()', None, True),  # The argument is necessary.
        ('', 'type(1, 2)', None, True),  # Only one argument is necessary.
    )
)

def test_function(prepared_expression, target_expression, expected_value,
                  is_error):
    """Unit-test for Standard library

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
    config = Config(max_depth=10, max_array_size=6, nan='NaN',
                    enable_tag_detail=True)

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
