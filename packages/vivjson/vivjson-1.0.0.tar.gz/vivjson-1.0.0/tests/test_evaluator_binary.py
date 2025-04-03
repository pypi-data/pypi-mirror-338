"""Unit-test for binary expression in Evaluator

Unit-test for "+", "*", "and", "<=", ...

Run `python3 -m pytest tests/test_evaluator_binary.py` in
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
__date__ = '2025-03-27'

# pylint: disable=C0301, E0401, R0801

import pytest
from vivjson.viv import Viv
from vivjson.config import Config

@pytest.mark.parametrize(
    'prepared_expression, target_expression, expected_value, is_error', (
        # for Evaluator._add
        ('', '{"a": 3, "b": 100} + {"0": "x", "#": true, "/*": false}', {"a": 3, "b": 100, "0": "x", "#": True, "/*": False}, False),  # block + block --> block
        ('', '{"a": 3, "b": 100} + {"0": "x", "#": true, "//": false, "y": -3}', None, True),  # block + block --> ERROR because max array size is limited as 5.
        ('', '{"a": 3, "b": 100} + {"a": -5}', {"a": -2, "b": 100}, False),  # block + block --> block
        ('', '{"a": 3, "b": 100} + [3, 0]', [{"a": 3, "b": 100}, 3, 0], False),  # block + array --> array
        ('', '{"a": 3} + [3, "a"]', [{"a": 3}, 3, "a"], False), # block + array --> array
        ('', '{"a": 3, "b": 100} + "a"', None, True),  # block + string --> ERROR
        ('', '{"a": 3, "b": 100} + 0', None, True),  # block + int --> ERROR
        ('', '{"a": 3, "b": 100} + 0.5', None, True),  # block + float --> ERROR
        ('', '{"a": 3, "b": 100} + false', None, True),  # block + boolean --> ERROR
        ('', '{"a": 3, "b": 100} + null', {"a": 3, "b": 100}, False),  # block + null --> block  (Adding null is meaningless.)
        ('', '[3, "a"] + {"a": 3}', [3, "a", {"a": 3}], False),  # array + block --> array
        ('', '[true, -1] + [+1, false]', [True, -1, [1, False]], False),  # array + array --> array
        ('', '[true, -1, +1, false] + ["a", null]', [True, -1, +1, False, ["a", None]], False),  # array + array --> array
        ('', '[true, -1, +1, false, "a"] + [null]', None, True),  # array + array --> ERROR because max array size is limited as 5.
        ('', '[8.5, null] + "*/"', [8.5, None, "*/"], False),  # array + string --> array
        ('', '[0, false, ] + 8', [0, False, 8], False),  # array + int --> array
        ('', '[0, false, 1, 2] + 8', [0, False, 1, 2, 8], False),  # array + int --> array
        ('', '[0, false, 1, 2, 3] + 8', None, True),  # array + int --> ERROR because max array size is limited as 5.
        ('', '["x", "y"] + 0.000001', ["x", "y", 0.000001], False),  # array + float --> array
        ('', '[3, "a"] + true', [3, "a", True], False),  # array + boolean --> array
        ('', '[0] + null', [0, None], False),  # array + null --> array  (Append null as element even if adding null.)
        ('', '"abc" + {"a": 0}', None, True),  # string + block --> ERROR
        ('', '"abc" + ["def"]', ["abc", "def"], False),  # string + array --> array
        ('', '"abc" + "def"', "abcdef", False),  # string + string --> string
        ('', '"0.0" + 1000', "0.01000", False),  # string + int --> string
        ('', '"88.88" + 1.75', "88.881.75", False),  # string + float --> string
        ('', '"100" + false', "100false", False),  # string + boolean --> string
        ('', '"null" + null', "null", False),  # string + null --> string  (Adding null is meaningless.)
        ('', '10000 + {"a": 0}', None, True),  # int + block --> ERROR
        ('', '10000 + [0]', [10000, 0], False),  # int + array --> array
        ('', '-5 + ".0"', "-5.0", False),  # int + str --> str
        ('', '3 + 2', 5, False),  # int + int --> int
        ('', '-3+-2', -5, False),  # int + int --> int
        ('', '1000000 + 0.1', 1000000.1, False),  # int + float --> float
        ('', '0 + false', False, False),  # int + boolean --> boolean
        ('', '0 + true', True, False),  # int + boolean --> boolean
        ('', '1 + false', True, False),  # int + boolean --> boolean
        ('', '1 + true', True, False),  # int + boolean --> boolean
        ('', '100 + null', 100, False),  # int + null --> int  (Adding null is meaningless.)
        ('', '1.5 + {"x": null}', None, True),  # float + block --> ERROR
        ('', '15e3 + [null, "x"]', [15000.0, None, "x"], False),  # float + array --> array
        ('', '1e-3+"a"', "0.001a", False),  # float + string --> string
        ('', '-0.01e+5+3', -997.0, False),  # float + int --> float
        ('', '5.6 + 8.2', 13.8, False),  # float + float --> float
        ('', '0.0 + false', False, False),  # float + boolean --> boolean
        ('', '0.0 + true', True, False),  # float + boolean --> boolean
        ('', '0.1 + false', True, False),  # float + boolean --> boolean
        ('', '0.1 + true', True, False),  # float + boolean --> boolean
        ('', '1e-10 + null', 1e-10, False),  # float + null --> float  (Adding null is meaningless.)
        ('', 'false + {"a": 3}', None, True),  # boolean + block --> ERROR
        ('', 'false + [3,]', [False, 3], False),  # boolean + array --> array
        ('', 'false + [3,2,1,0]', [False, 3, 2, 1, 0], False),  # boolean + array --> array
        ('', 'false + [4,3,2,1,0]', None, True),  # boolean + array --> ERROR because max array size is limited as 5.
        ('', 'true + "0"', "true0", False),  # boolean + string --> string
        ('', 'false + 0', False, False),  # boolean + int --> boolean
        ('', 'false + 1', True, False),  # boolean + int --> boolean
        ('', 'true + 0', True, False),  # boolean + int --> boolean
        ('', 'true + 1', True, False),  # boolean + int --> boolean
        ('', 'false + 0.0', False, False),  # boolean + float --> boolean
        ('', 'false + 0.1', True, False),  # boolean + float --> boolean
        ('', 'true + 0.0', True, False),  # boolean + float --> boolean
        ('', 'true + 0.1', True, False),  # boolean + float --> boolean
        ('', 'false + false', False, False),  # boolean + boolean --> boolean
        ('', 'false + true', True, False),  # boolean + boolean --> boolean
        ('', 'true + false', True, False),  # boolean + boolean --> boolean
        ('', 'true + true', True, False),  # boolean + boolean --> boolean
        ('', 'true + null', True, False),  # boolean + null --> boolean  (Adding null is meaningless.)
        ('', 'null + {"a": 3}', {"a": 3}, False),  # null + block --> block  (Adding null is meaningless.)
        ('', 'null + [false, [1, 2]]', [None, False, [1, 2]], False),  # null + array --> array  (Append null as element even if adding null.)
        ('', 'null + ""', "", False),  # null + string --> string  (Adding null is meaningless.)
        ('', 'null + "abc"', "abc", False),  # null + string --> string  (Adding null is meaningless.)
        ('', 'null + 0', 0, False),  # null + int --> int  (Adding null is meaningless.)
        ('', 'null + -1e2', -100.0, False),  # null + float --> float  (Adding null is meaningless.)
        ('', 'null + false', False, False),  # null + boolean --> boolean  (Adding null is meaningless.)
        ('', 'null + true', True, False),  # null + boolean --> boolean  (Adding null is meaningless.)
        ('x = len, y = len', 'x + y', None, True),  # function + function --> ERROR
        ('x = len, y = len', '3 + y', None, True),  # int + function --> ERROR
        ('x = len, y = len', 'x + 3', None, True),  # function + int --> ERROR
        ('function test() {return(1)}, x = test(), y = test()', 'x + y', 2, False),
        ('function test() {return(1)}, x = test, y = test', 'x + y', None, True),  # function + function --> ERROR
        ('function test() {return(1)}, x = test(), y = test', 'x + y', None, True),  # int + function --> ERROR
        ('function test() {return(1)}, x = test, y = test()', 'x + y', None, True),  # function + int --> ERROR
        ({"a": 3}, 'a + 2', 5, False),  # int + int --> int
        ({"a": (3,2)}, 'a + 2', None, True),  # Python's tuple can't treated. --> ERROR
                        # When tuple has simple structure, such as 1 dimensional tuple,
                        # converting to list is possible. However complex structure is
                        # given, it is so difficult. So it is not permitted.
        ({"a": NotImplemented}, 'a + 2', None, True),  # Python's NotImplemented can't treated. --> ERROR
        ({"a": Config()}, 'a + 2', None, True),  # Python's class instance can't treated. --> ERROR
        ({"a": "x", "b": "y"}, 'a + b', "xy", False),  # string + string --> string

        # for Evaluator._subtract
        ('', '{"a": 10, "b": 20, "c": 30} - {"b": 5, "c": 10}', {"a": 10, "b": 15, "c": 20}, False),  # block - block --> block
        ('', '{"a": 10, "b": 20} - {"b": 5, "c": 10}', {"a": 10, "b": 15, "c": -10}, False),  # block - block --> block
        ('', '{"a": 10, "b": 20} - {"c": 10, "d": -100, "e": 50, "f": 1}', None, True),  # block - block --> ERROR because max array size is limited as 5.
        ('', '{"a": 10, "b": 20, "c": 30} - ["b", "c"]', {"a": 10}, False),  # block - array --> block
        ('', '{"a": 10, "b": 20, "c": 30} - ["b", "c", 3]', None, True),  # block - array --> ERROR because there is number in array
        ('', '{"a": 10, "b": 20, "c": 30} - [true]', None, True),  # block - array --> ERROR because there is boolean in array
        ('', '{"a": 10, "b": 20, "c": 30} - "b"', {"a": 10, "c": 30}, False),  # block - string --> block
        ('', '{"a": 10, "b": 20, "c": 30} - "d"', {"a": 10, "b": 20, "c": 30}, False),  # block - string --> block
        ('', '{"a": 10} - 3', None, True),  # block - int --> ERROR
        ('', '{"a": 10} - 1.5', None, True),  # block - float --> ERROR
        ('', '{"a": 10} - true', None, True),  # block - boolean --> ERROR
        ('', '{"a": 10} - null', {"a": 10}, False),  # block - null --> block  (Removing null is meaningless.)
        ('', '[3, {"a": null}, {"a": null}] - {"a": null}', [3], False),  # array - block --> array
        ('', '[3, "a", null] - {"a": null}', [3, "a", None], False),  # array - block --> array
        ('', '[3, ["a", null], ["a", null]] - ["a", null]', [3], False),  # array - array --> array
        ('', '[3, ["a", null]] - ["a", null]', [3], False),  # array - array --> array
        ('', '[3, "a", null] - ["a", null]', [3, "a", None], False),  # array - array --> array
        ('', '[3, "a", "a"] - "a"', [3], False),  # array - string --> array
        ('', '[3, "a", "a"] - 3', ["a", "a"], False),  # array - int --> array
        ('', '[3, "a", "a"] - 3.0', ["a", "a"], False),  # array - float --> array
        ('', '[3, true, "a"] - true', [3, "a"], False),  # array - boolean --> array
        ('', '[3, false, "a"] - false', [3, "a"], False),  # array - boolean --> array
        ('', '[3, false, "a"] - true', [3, False, "a"], False),  # array - boolean --> array
        ('', '[3, "a", null] - null', [3, "a"], False),  # array - null --> array  (Remove null of element.)
        ('', '"abc: 3" - {"abc": 3}', None, True),  # string - block --> ERROR
        ('', '"large-dog&small-dog&2cat" - ["large-", "small-"]', "dog&dog&2cat", False),  # string - array --> string
        ('', '"large-dog&small-dog&2cat" - "dog"', "large-&small-&2cat", False),  # string - string --> string
        ('', '"large-dog&small-dog&2cat" - 2', None, True),  # string - int --> ERROR
        ('', '"large-dog&small-dog&200.5t" - 200.5', None, True),  # string - float --> ERROR
        ('', '"large-dog&small-dog&true" - true', None, True),  # string - boolean --> ERROR
        ('', '"large-dog&small-dog&null" - null', "large-dog&small-dog&null", False),  # string - null --> string  (Removing null is meaningless.)
        ('', '100 - {"100": 100}', None, True),  # int - block --> ERROR
        ('', '100 - [100]', None, True),  # int - array --> ERROR
        ('', '100 - "100"', None, True),  # int - string --> ERROR
        ('', '100 - 100', 0, False),  # int - int --> int
        ('', '100 - 100.5', -0.5, False),  # int - float --> float
        ('', '100 - 100.0', 0.0, False),  # int - float --> float
        ('', '100 - true', None, True),  # int - boolean --> ERROR
        ('', '100 - null', 100, False),  # int - null --> int  (Removing null is meaningless.)
        ('', '100.5 - {"100.5": 100.5}', None, True),  # float - block --> ERROR
        ('', '100.5 - [100.5]', None, True),  # float - array --> ERROR
        ('', '100.5 - "100.5"', None, True),  # float - string --> ERROR
        ('', '100.5 - 100', 0.5, False),  # float - int --> float
        ('', '100.5 - 100.5', 0.0, False),  # float - float --> float
        ('', '100.5 - 100.0', 0.5, False),  # float - float --> float
        ('', '100.5 - true', None, True),  # float - boolean --> ERROR
        ('', '100.5 - null', 100.5, False),  # float - null --> float  (Removing null is meaningless.)
        ('', 'true - {"true": true}', None, True),  # boolean - block --> ERROR
        ('', 'true - [true]', None, True),  # boolean - array --> ERROR
        ('', 'true - "true"', None, True),  # boolean - string --> ERROR
        ('', 'true - 1', None, True),  # boolean - int --> ERROR
        ('', 'true - 1.0', None, True),  # boolean - float --> ERROR
        ('', 'true - true', None, True),  # boolean - boolean --> ERROR
        ('', 'true - null', True, False),  # boolean - null --> boolean  (Removing null is meaningless.)
        ('', 'null - {}', None, True),  # null - block --> ERROR
        ('', 'null - {"null": null}', None, True),  # null - block --> ERROR
        ('', 'null - []', None, True),  # null - array --> ERROR
        ('', 'null - [100, 5]', None, True),  # null - array --> ERROR
        ('', 'null - "xyz"', None, True),  # null - string --> ERROR
        ('', 'null - 100', None, True),  # null - int --> ERROR
        ('', 'null - 100.5', None, True),  # null - float --> ERROR
        ('', 'null - true', None, True),  # null - boolean --> ERROR
        ('', 'null - null', None, False),  # null - null --> null
        ('function test() {return(1)}, x = test, y = test', 'x - y', None, True),  # function - function --> ERROR

        # for Evaluator._multiply
        ('', '{"a": 2} * {"a": 10, "b": 3}', {"a": 20, "b": None}, False),  # block * block --> block
        ('', '{"a": 2} * {"b": 3}', {"a": None, "b": None}, False),  # block * block --> block
        ('', '{"a": 2, "b": 3, "c": 4, "d": 5, "e": 6} * {"f": 1}', None, True),  # block * block --> ERROR because max array size is limited as 5.
        ('', '{"a": 2} * ["b", 3]', None, True),  # block * array --> ERROR
        ('', '{"a": 2} * "b"', None, True),  # block * string --> ERROR
        ('', '{"a": 2} * 3', None, True),  # block * int --> ERROR
        ('', '{"a": 2} * 3.5', None, True),  # block * float --> ERROR
        ('', '{"a": 2} * false', None, True),  # block * boolean --> ERROR
        ('', '{"a": 2} * null', None, False),  # block * null --> null
        ('', '[100] * {"b": 3}', None, True),  # array * block --> ERROR
        ('', '[100] * [3]', None, True),  # array * array --> ERROR
        ('', '[100, 3, 1e+2] * "|"', "100|3|100.0", False),  # array * string --> string  (Concatenate elements with delimiter)
        ('', '[100] * 5', [100, 100, 100, 100, 100], False),  # array * int --> array  (for initialization of array)
        ('', '[100] * 6', None, True),  # array * int --> ERROR because max array size is limited as 5.
        ('', '[100, "a"] * 2', [100, "a", 100, "a"], False),  # array * int --> array  (for initialization of array)
        ('', '[100, "a"] * 3', None, True),  # array * int --> ERROR because max array size is limited as 5.
        ('', '[100] * 3.7', [100, 100, 100], False),  # array * float --> array  (for initialization of array)
        ('', '[100, "a"] * 2.7', [100, "a", 100, "a"], False),  # array * float --> array  (for initialization of array)
        ('', '[100, "a"] * 3.7', None, True),  # array * float --> ERROR because max array size is limited as 5.
        ('', '[100] * true', None, True),  # array * boolean --> ERROR
        ('', '[100] * false', None, True),  # array * boolean --> ERROR
        ('', '[100] * null', None, False),  # array * null --> null
        ('', '"|" * {"a", 100}', None, True),  # string * block --> ERROR
        ('', '"|" * [100, "a"]', "100|a", False),  # string * array --> string  (Concatenate elements with delimiter)
        ('', '"3a" * "3a"', None, True),  # string * string --> ERROR
        ('', '"3a" * 2', "3a3a", False),  # string * int --> string
        ('', '"3a" * 2.9', "3a3a", False),  # string * float --> string
        ('', '"3a" * true', None, True),  # string * boolean --> ERROR
        ('', '"3a" * false', None, True),  # string * boolean --> ERROR
        ('', '"3a" * null', None, False),  # string * null --> null
        ('', '3 * {"a": 50}', None, True),  # int * block --> ERROR
        ('', '3 * [50]', [50, 50, 50], False),  # int * array --> array  (for initialization of array)
        ('', '2 * "3a"', "3a3a", False),  # int * string --> string
        ('', '2 * 60', 120, False),  # int * int --> int
        ('', '2 * 60.0', 120.0, False),  # int * float --> float
        ('', '2 * 60.7', 121.4, False),  # int * float --> float
        ('', '2 * true', None, True),  # int * boolean --> ERROR
        ('', '2 * false', None, True),  # int * boolean --> ERROR
        ('', '2 * null', None, False),  # int * null --> null
        ('', '3.8 * {"a": 50}', None, True),  # float * block --> ERROR
        ('', '3.8 * [50]', [50, 50, 50], False),  # float * array --> array  (for initialization of array)
        ('', '2.8 * "3a"', "3a3a", False),  # float * string --> string
        ('', '2.8 * 60', 168.0, False),  # float * int --> float
        ('', '2.8 * 60.7', 169.96, False),  # float * float --> float
        ('', '2.8 * true', None, True),  # float * boolean --> ERROR
        ('', '2.8 * false', None, True),  # float * boolean --> ERROR
        ('', '2.8 * null', None, False),  # float * null --> null
        ('', 'true * {"a": 3}', None, True),  # boolean * block --> ERROR
        ('', 'true * [3, 2]', None, True),  # boolean * array --> ERROR
        ('', 'false * [3, 2]', None, True),  # boolean * array --> ERROR
        ('', 'true * "x1"', None, True),  # boolean * string --> ERROR
        ('', 'false * "x1"', None, True),  # boolean * string --> ERROR
        ('', 'true * 20', None, True),  # boolean * int --> ERROR
        ('', 'false * 20', None, True),  # boolean * int --> ERROR
        ('', 'true * 20.5', None, True),  # boolean * float --> ERROR
        ('', 'false * 20.5', None, True),  # boolean * float --> ERROR
        ('', 'true * true', None, True),  # boolean * boolean --> ERROR
        ('', 'true * false', None, True),  # boolean * boolean --> ERROR
        ('', 'false * true', None, True),  # boolean * boolean --> ERROR
        ('', 'false * false', None, True),  # boolean * boolean --> ERROR
        ('', 'null * {"a": 3}', None, False),  # null * block --> ERROR
        ('', 'null * [3, 2]', None, False),  # null * array --> null
        ('', 'null * "a"', None, False),  # null * string --> null
        ('', 'null * 3', None, False),  # null * int --> null
        ('', 'null * 3.8', None, False),  # null * float --> null
        ('', 'null * true', None, False),  # null * boolean --> null
        ('', 'null * false', None, False),  # null * boolean --> null
        ('', 'null * null', None, False),  # null * null --> null
        ('function test() {return(1)}, x = test, y = test', 'x * y', None, True),  # function * function --> ERROR

        # for Evaluator._divide
        ('', '{"a": 2} / {"a": 10, "b": 3}', {"a": 0.2, "b": None}, False),  # block / block --> block
        ('', '{"a": 2} / {"a": 2, "b": 3, "c": 4, "d": 5, "e": 6, "f": 7}', None, True),  # block / block --> ERROR because max array size is limited as 5.
        ('', '{"a": 2} / {"b": 3}', None, True),  # block / block --> ERROR
        ('', '{"a": 2} / [2]', None, True),  # block / array --> ERROR
        ('', '{"a": 2} / "a"', None, True),  # block / string --> ERROR
        ('', '{"a": 2} / 2', None, True),  # block / int --> ERROR
        ('', '{"a": 2.0} / 2.0', None, True),  # block / float --> ERROR
        ('', '{"a": true} / true', None, True),  # block / boolean --> ERROR
        ('', '{"a": true} / null', None, True),  # block / null --> ERROR
        ('', '[3, 2] / [2]', None, True),  # array / array --> ERROR
        ('', '[3, 2] / ","', None, True),  # array / string --> ERROR
        ('', '[3, 2] / 2', None, True),  # array / int --> ERROR
        ('', '[3, 2] / 2.5', None, True),  # array / float --> ERROR
        ('', '[3, 2] / false', None, True),  # array / boolean --> ERROR
        ('', '[3, 2] / true', None, True),  # array / boolean --> ERROR
        ('', '[3, 2] / null', None, True),  # array / null --> ERROR
        ('', '"a,b" / {"a": ","}', None, True),  # string / block --> ERROR
        ('', '"a,b" / [","]', None, True),  # string / array --> ERROR
        ('', '"a,b" / ","', ["a", "b"], False),  # string / string --> array
        ('', '"a,b," / ","', ["a", "b", ""], False),  # string / string --> array
        ('', '"a,b,c,d,e" / ","', ["a", "b", "c", "d", "e"], False),  # string / string --> array
        ('', '"a,b,c,d,e,f" / ","', None, True),  # string / string --> ERROR because max array size is limited as 5.
        ('', '"a,b" / ""', ["a", ",", "b"], False),  # string / string --> array
        ('', '"xxwwwwyy" / "ww"', ['xx', '', 'yy'], False),  # string / string --> array
        ('', '"xxwwwyy" / "ww"', ['xx', 'wyy'], False),  # string / string --> array
        ('', '"abcde" / ""', ["a", "b", "c", "d", "e"], False),  # string / string --> array
        ('', '"abcdef" / ""', None, True),  # string / string --> ERROR because max array size is limited as 5.
        ('', '"a,b" / 2', None, True),  # string / int --> ERROR
        ('', '"a,b" / 2.5', None, True),  # string / float --> ERROR
        ('', '"a,b" / true', None, True),  # string / boolean --> ERROR
        ('', '"a,b" / false', None, True),  # string / boolean --> ERROR
        ('', '"a,b" / null', None, True),  # string / null --> ERROR
        ('', '20 / {"a": 2}', None, True),  # int / block --> ERROR
        ('', '20 / [2, 5]', None, True),  # int / array --> ERROR
        ('', '20 / "0"', None, True),  # int / string --> ERROR
        ('', '20 / 5', 4, False),  # int / int --> int or float or ERROR
        ('', '20 / 8', 2.5, False),  # int / int --> int or float or ERROR
        ('', '20 / 0', None, True),  # int / 0 --> ERROR
        ('', '20 / 0.0', None, True),  # int / 0.0 --> ERROR
        ('', '20 / 2.5', 8, False),  # int / float --> int or float or ERROR
        ('', '20 / 8', 2.5, False),  # int / float --> int or float or ERROR
        ('', '20 / null', None, True),  # int / null --> ERROR
        ('', '3.5 / {"a": 2.5}', None, True),  # float / block --> ERROR
        ('', '3.5 / [1, 2]', None, True),  # float / array --> ERROR
        ('', '3.5 / "."', None, True),  # float / string --> ERROR
        ('', '3.5 / "0.5"', None, True),  # float / string --> ERROR
        ('', '3.5 / 5', 0.7, False),  # float / int --> int or float or ERROR
        ('', '3.0 / 3', 1, False),  # float / int --> int or float or ERROR
        ('', '3.0 / 0', None, True),  # float / 0 --> ERROR
        ('', '3.5 / 0.5', 7, False),  # float / float --> int or float or ERROR
        ('', '0.49 / 0.7', 0.7, False),  # float / float --> int or float or ERROR
        ('', '0.49 / 0.0', None, True),  # float / 0.0 --> ERROR
        ('', '3.5 / true', None, True),  # float / boolean --> ERROR
        ('', '3.5 / false', None, True),  # float / boolean --> ERROR
        ('', '3.5 / null', None, True),  # float / null --> ERROR
        ('', 'true / {"true": true}', None, True),  # boolean / block --> ERROR
        ('', 'true / [true]', None, True),  # boolean / array --> ERROR
        ('', 'false / [true]', None, True),  # boolean / array --> ERROR
        ('', 'true / [false]', None, True),  # boolean / array --> ERROR
        ('', 'false / [false]', None, True),  # boolean / array --> ERROR
        ('', 'true / "true"', None, True),  # boolean / string --> ERROR
        ('', 'false / "false"', None, True),  # boolean / string --> ERROR
        ('', 'true / 1', None, True),  # boolean / int --> ERROR
        ('', 'false / 1', None, True),  # boolean / int --> ERROR
        ('', 'true / 1.5', None, True),  # boolean / float --> ERROR
        ('', 'false / 1.5', None, True),  # boolean / float --> ERROR
        ('', 'true / true', None, True),  # boolean / boolean --> ERROR
        ('', 'false / true', None, True),  # boolean / boolean --> ERROR
        ('', 'true / null', None, True),  # boolean / null --> ERROR
        ('', 'false / null', None, True),  # boolean / null --> ERROR
        ('', 'null / {"a": null}', None, False),  # null / block --> null
        ('', 'null / [null]', None, False),  # null / array --> null
        ('', 'null / [1, 2]', None, False),  # null / array --> null
        ('', 'null / "a"', None, False),  # null / string --> null
        ('', 'null / 2', None, False),  # null / int --> null
        ('', 'null / 0', None, True),  # null / int --> ERROR
        ('', 'null / 8.8', None, False),  # null / float --> null
        ('', 'null / 0.0', None, True),  # null / float --> ERROR
        ('', 'null / false', None, False),  # null / boolean --> null
        ('', 'null / null', None, True),  # null / null --> ERROR
        ('function test() {return(1)}, x = test, y = test', 'x / y', None, True),  # function / function --> ERROR

        # for Evaluator._modulo
        ('', '{"a": 20} % {"a": 6, "b": 3}', {"a": 2, "b": None}, False),  # block % block --> block
        ('', '{"a": 20} % {"a": 2, "b": 3, "c": 4, "d": 5, "e": 6, "f": 7}', None, True),  # block % block --> ERROR because max array size is limited as 5.
        ('', '{a: 20} % {a: 6, b: 3}', {"a": 2, "b": None}, False),  # block % block --> block
        ('', '{"a": 2} % {"b": 3}', None, True),  # block % block --> ERROR
        ('', '{"a": 2} % [2]', None, True),  # block % array --> ERROR
        ('', '{"a": 2} % "a"', None, True),  # block % string --> ERROR
        ('', '{"a": 2} % 2', None, True),  # block % int --> ERROR
        ('', '{"a": 2} % 1.5', None, True),  # block % float --> ERROR
        ('', '{"a": 2} % true', None, True),  # block % boolean --> ERROR
        ('', '{"a": 2} % null', None, True),  # block % null --> ERROR
        ('', '[2, 3] % {"a": 2}', None, True),  # array % block --> ERROR
        ('', '[2, 3] % [2, 3]', None, True),  # array % array --> ERROR
        ('', '[2, 3] % ","', None, True),  # array % string --> ERROR
        ('', '[2, 3] % 2', None, True),  # array % int --> ERROR
        ('', '[2, 3] % 2.5', None, True),  # array % float --> ERROR
        ('', '[2, 3] % true', None, True),  # array % boolean --> ERROR
        ('', '[2, 3] % null', None, True),  # array % null --> ERROR
        ('', '"a, 2" % {"a", 2}', None, True),  # string % block --> ERROR
        ('', '"2, 3" % [2]', None, True),  # string % array --> ERROR
        ('', '"2, 3" % ","', None, True),  # string % string --> ERROR
        ('', '"2, 3" % 2', None, True),  # string % int --> ERROR
        ('', '"2, 3" % 2.0', None, True),  # string % float --> ERROR
        ('', '"2, 3" % true', None, True),  # string % boolean --> ERROR
        ('', '"2, 3" % null', None, True),  # string % null --> ERROR
        ('', '10 % {"a": 2}', None, True),  # int % block --> ERROR
        ('', '10 % [3]', None, True),  # int % array --> ERROR
        ('', '10 % "3"', None, True),  # int % string --> ERROR
        ('', '10 % 3', 1, False),  # int % int --> int or float or ERROR, 10 = 3 x 3 + 1
        ('', '-10 % 3', 2, False),  # int % int --> int or float or ERROR, -10 = 3 x (-4) + 2 (NG: -10 = 3 x (-3) - 1)
        ('', '10 % -3', -2, False),  # int % int --> int or float or ERROR, 10 = -3 x (-4) - 2 (NG: 10 = -3 x (-3) + 1)
        ('', '-10 % -3', -1, False),  # int % int --> int or float or ERROR, -10 = -3 x 3 - 1 (NG: -10 = -3 x 4 + 2)
        ('', '10 % 0', None, True),  # int % 0 --> ERROR
        ('', '10 % 3.0', 1, False),  # int % float --> int or float or ERROR
        ('', '10 % 1.7', 1.5, False),  # int % float --> int or float or ERROR
        ('', '10 % 0.0', None, True),  # int % 0.0 --> ERROR
        ('', '10 % true', None, True),  # int % boolean --> ERROR
        ('', '10 % null', None, True),  # int % null --> ERROR
        ('', '10.5 % {"a": 3.0}', None, True),  # float % block --> ERROR
        ('', '10.5 % [3.0]', None, True),  # float % array --> ERROR
        ('', '10.5 % "a"', None, True),  # float % string --> ERROR
        ('', '10.5 % 3', 1.5, False),  # float % int --> int or float or ERROR
        ('', '10.5 % 0', None, True),  # float % 0 --> ERROR
        ('', '17.5 % 1.5', 1, False),  # float % float --> int or float or ERROR
        ('', '10.5 % 1.7', 0.3, False),  # float % float --> int or float or ERROR
        ('', '10.5 % 0.0', None, True),  # float % 0.0 --> ERROR
        ('', '10.5 % true', None, True),  # float % boolean --> ERROR
        ('', '10.5 % null', None, True),  # float % null --> ERROR
        ('', 'true % {"true": true}', None, True),  # boolean % block --> ERROR
        ('', 'true % [true]', None, True),  # boolean % array --> ERROR
        ('', 'true % "true"', None, True),  # boolean % string --> ERROR
        ('', 'true % 3', None, True),  # boolean % int --> ERROR
        ('', 'true % 1.7', None, True),  # boolean % float --> ERROR
        ('', 'true % true', None, True),  # boolean % boolean --> ERROR
        ('', 'true % null', None, True),  # boolean % null --> ERROR
        ('', 'null % {"a": null}', None, False),  # null % block --> null
        ('', 'null % [null]', None, False),  # null % array --> null
        ('', 'null % "null"', None, False),  # null % string --> null
        ('', 'null % 3', None, False),  # null % int --> null
        ('', 'null % 0', None, True),  # null % int --> ERROR
        ('', 'null % 1.7', None, False),  # null % float --> null
        ('', 'null % 0.0', None, True),  # null % float --> ERROR
        ('', 'null % true', None, False),  # null % boolean --> null
        ('', 'null % null', None, True),  # null % null --> ERROR
        ('function test() {return(1)}, x = test, y = test', 'x % y', None, True),  # function % function --> ERROR

        # for Evaluator._logical_invert
        ('a = {}', 'not a', False, False),  # not block --> boolean (using truthy) (always false)
        ('a = {"a": 3}', 'not a', False, False),  # not block --> boolean (using truthy) (always false)
        ('', 'not {"a": 3}', None, True),  # not {"a": 3} is confused as function "not". --> ERROR
        ('a = []', 'not a', False, False),  # not array --> boolean (using truthy) (always false)
        ('a = [3]', 'not a', False, False),  # not array --> boolean (using truthy) (always false)
        ('', 'not [3]', None, True),  # not [3] is confused as variable "not". --> ERROR
        ('', 'not ""', False, False),  # not string --> boolean (using truthy) (always false)
        ('', 'not 0', True, False),  # not int --> boolean (using truthy)
        ('', 'not 10', False, False),  # not int --> boolean (using truthy)
        ('', 'not 0.0', True, False),  # not float --> boolean (using truthy)
        ('', 'not 5.0', False, False),  # not float --> boolean (using truthy)
        ('', 'not true', False, False),  # not boolean --> boolean
        ('', 'not false', True, False),  # not boolean --> boolean
        ('', 'not null', True, False),  # not null --> boolean (using truthy) (always true)
        ('', 'false not false', None, True),  # "not" is binary expression in grammar.
        ('function test() {return(1)}, x = test', 'not x', False, False),  # not function --> boolean (using truthy)

        # for Evaluator._logical_and
        ('', 'false and false', False, False),
        ('', 'false and true', False, False),
        ('', 'true and false', False, False),
        ('', 'true and true', True, False),
        ('', '{} and false', False, False),  # using truthy
        ('', '{} and true', True, False),  # using truthy
        ('', '{"a": 3} and false', False, False),  # using truthy
        ('', '{"a": 3} and true', True, False),  # using truthy
        ('', '[] and false', False, False),  # using truthy
        ('', '[] and true', True, False),  # using truthy
        ('', '[3] and false', False, False),  # using truthy
        ('', '[3] and true', True, False),  # using truthy
        ('', '"a" and false', False, False),  # using truthy
        ('', '"a" and true', True, False),  # using truthy
        ('', '10 and false', False, False),  # using truthy
        ('', '10 and true', True, False),  # using truthy
        ('', '0 and false', False, False),  # using truthy, 0 is equivalent to false.
        ('', '0 and true', False, False),  # using truthy, 0 is equivalent to false.
        ('', '10.5 and false', False, False),  # using truthy
        ('', '10.5 and true', True, False),  # using truthy
        ('', '0.0 and false', False, False),  # using truthy, 0 is equivalent to false.
        ('', '0.0 and true', False, False),  # using truthy, 0 is equivalent to false.
        ('', 'null and false', False, False),  # using truthy, null is equivalent to false.
        ('', 'null and true', False, False),  # using truthy, null is equivalent to false.
        ('', 'false and {}', False, False),  # using truthy
        ('', 'true and {}', True, False),  # using truthy
        ('', 'false and {"a": 3}', False, False),  # using truthy
        ('', 'true and {"a": 3}', True, False),  # using truthy
        ('', 'false and []', False, False),  # using truthy
        ('', 'true and []', True, False),  # using truthy
        ('', 'false and [3]', False, False),  # using truthy
        ('', 'true and [3]', True, False),  # using truthy
        ('', 'false and "a"', False, False),  # using truthy
        ('', 'true and "a"', True, False),  # using truthy
        ('', 'false and 10', False, False),  # using truthy
        ('', 'true and 10', True, False),  # using truthy
        ('', 'false and 0', False, False),  # using truthy, 0 is equivalent to false.
        ('', 'true and 0', False, False),  # using truthy, 0 is equivalent to false.
        ('', 'false and 10.5', False, False),  # using truthy
        ('', 'true and 10.5', True, False),  # using truthy
        ('', 'false and 0.0', False, False),  # using truthy, 0 is equivalent to false.
        ('', 'true and 0.0', False, False),  # using truthy, 0 is equivalent to false.
        ('', 'false and null', False, False),  # using truthy, null is equivalent to false.
        ('', 'true and null', False, False),  # using truthy, null is equivalent to false.
        ('y = 0; function y10() {y = 10, return(true)}, z = 0; if (false or y10()) {z = 20}', '[y, z]', [10, 20], False),
        ('y = 0; function y10() {y = 10, return(true)}, z = 0; if (true or y10()) {z = 20}', '[y, z]', [0, 20], False),  # Short-circuit evaluation
        ('y = 0; function y10() {y = 10, return(true)}, z = 0; if (false and y10()) {z = 20}', '[y, z]', [0, 0], False),  # Short-circuit evaluation
        ('y = 0; function y10() {y = 10, return(true)}, z = 0; if (true and y10()) {z = 20}', '[y, z]', [10, 20], False),
        ('function test() {return(1)}, x = test, y = test', 'x and y', True, False),  # using truthy

        # for Evaluator._logical_or
        ('', 'false or false', False, False),
        ('', 'false or true', True, False),
        ('', 'true or false', True, False),
        ('', 'true or true', True, False),
        ('', '{} or false', True, False),  # using truthy
        ('', '{} or true', True, False),  # using truthy
        ('', '{"a": 3} or false', True, False),  # using truthy
        ('', '{"a": 3} or true', True, False),  # using truthy
        ('', '[] or false', True, False),  # using truthy
        ('', '[] or true', True, False),  # using truthy
        ('', '[3] or false', True, False),  # using truthy
        ('', '[3] or true', True, False),  # using truthy
        ('', '"a" or false', True, False),  # using truthy
        ('', '"a" or true', True, False),  # using truthy
        ('', '10 or false', True, False),  # using truthy
        ('', '10 or true', True, False),  # using truthy
        ('', '0 or false', False, False),  # using truthy, 0 is equivalent to false.
        ('', '0 or true', True, False),  # using truthy, 0 is equivalent to false.
        ('', '10.5 or false', True, False),  # using truthy
        ('', '10.5 or true', True, False),  # using truthy
        ('', '0.0 or false', False, False),  # using truthy, 0 is equivalent to false.
        ('', '0.0 or true', True, False),  # using truthy, 0 is equivalent to false.
        ('', 'null or false', False, False),  # using truthy, null is equivalent to false.
        ('', 'null or true', True, False),  # using truthy, null is equivalent to false.
        ('', 'false or {}', True, False),  # using truthy
        ('', 'true or {}', True, False),  # using truthy
        ('', 'false or {"a": 3}', True, False),  # using truthy
        ('', 'true or {"a": 3}', True, False),  # using truthy
        ('', 'false or []', True, False),  # using truthy
        ('', 'true or []', True, False),  # using truthy
        ('', 'false or [3]', True, False),  # using truthy
        ('', 'true or [3]', True, False),  # using truthy
        ('', 'false or "a"', True, False),  # using truthy
        ('', 'true or "a"', True, False),  # using truthy
        ('', 'false or 10', True, False),  # using truthy
        ('', 'true or 10', True, False),  # using truthy
        ('', 'false or 0', False, False),  # using truthy, 0 is equivalent to false.
        ('', 'true or 0', True, False),  # using truthy, 0 is equivalent to false.
        ('', 'false or 10.5', True, False),  # using truthy
        ('', 'true or 10.5', True, False),  # using truthy
        ('', 'false or 0.0', False, False),  # using truthy, 0 is equivalent to false.
        ('', 'true or 0.0', True, False),  # using truthy, 0 is equivalent to false.
        ('', 'false or null', False, False),  # using truthy, null is equivalent to false.
        ('', 'true or null', True, False),  # using truthy, null is equivalent to false.
        ('function test() {return(1)}, x = test, y = test', 'x or y', True, False),  # using truthy

        # for Evaluator._is_equal
        ('', '{"a": 1, "b": 2} == {"b": 2, "a": 1}', True, False),
        ('', '{"a": 1, "b": 2} == {"a": 1}', False, False),
        ('', '[1, 2] == [1, 2]', True, False),
        ('', '[1, 2] == [2, 1]', False, False),
        ('', '"a" == "a"', True, False),
        ('', '"a" == "b"', False, False),
        ('', '100 == 100', True, False),
        ('', '100 == 200', False, False),
        ('', '1.5 == 1.5', True, False),
        ('', '1.5 == 1.4', False, False),
        ('', 'true == true', True, False),
        ('', 'true == false', False, False),
        ('', 'null == null', True, False),
        ('a = null', 'null == a', True, False),
        ('', '{"a": 1, "b": 2} == ["a", "b"]', False, False),
        ('', '{"a": 1, "b": 2} == [1, 2]', False, False),
        ('', '{"a": 1, "b": 2} == true', True, False),  # using truthy
        ('', '[1, 2] == true', True, False),  # using truthy
        ('', '[1, 2] == 1', False, False),  # using truthy
        ('', '"a" == true', True, False),  # using truthy
        ('', 'true == "a"', True, False),  # using truthy
        ('', '"a" == 1', False, False),  # using truthy
        ('', '100 == true', True, False),  # using truthy
        ('', 'true == 100', True, False),  # using truthy
        ('', '0 == false', True, False),  # using truthy
        ('', 'false == 0', True, False),  # using truthy
        ('', 'null == false', True, False),  # using truthy
        ('', 'false == null', True, False),  # using truthy
        ('function test() {return(1)}, x = test, y = test', 'x == y', True, False),

        # for Evaluator._is_not_equal
        ('', '{"a": 1, "b": 2} != {"b": 2, "a": 1}', False, False),
        ('', '{"a": 1, "b": 2} != {"a": 1}', True, False),
        ('', '[1, 2] != [1, 2]', False, False),
        ('', '[1, 2] != [2, 1]', True, False),
        ('', '"a" != "a"', False, False),
        ('', '"a" != "b"', True, False),
        ('', '100 != 100', False, False),
        ('', '100 != 200', True, False),
        ('', '1.5 != 1.5', False, False),
        ('', '1.5 != 1.4', True, False),
        ('', 'true != true', False, False),
        ('', 'true != false', True, False),
        ('', 'null != null', False, False),
        ('a = null', 'null != a', False, False),
        ('', '{"a": 1, "b": 2} != ["a", "b"]', True, False),
        ('', '{"a": 1, "b": 2} != [1, 2]', True, False),
        ('', '{"a": 1, "b": 2} != false', True, False),  # using truthy
        ('', '{"a": 1, "b": 2} != true', False, False),  # using truthy
        ('', '[1, 2] != true', False, False),  # using truthy
        ('', '[1, 2] != 1', True, False),  # using truthy
        ('', '"a" != true', False, False),  # using truthy
        ('', 'true != "a"', False, False),  # using truthy
        ('', '"a" != 1', True, False),  # using truthy
        ('', '100 != true', False, False),  # using truthy
        ('', 'true != 100', False, False),  # using truthy
        ('', '0 != false', False, False),  # using truthy
        ('', 'false != 0', False, False),  # using truthy
        ('', 'null != false', False, False),  # using truthy
        ('', 'false != null', False, False),  # using truthy
        ('function test() {return(1)}, x = test, y = test', 'x != y', False, False),

        # for Evaluator._is_less_than
        ('', '3 < 5', True, False),
        ('', '3 < 3', False, False),
        ('', '-3 < 2', True, False),
        ('', '3 < -5', False, False),
        ('', '2.3 < 2.4', True, False),
        ('', '1e4 < 1e3', False, False),
        ('', '1e-4 < 1e-3', True, False),
        ('', '{} < 5', None, True),
        ('', '[] < 5', None, True),
        ('', '"" < 5', None, True),
        ('', '"0" < 5', None, True),
        ('', 'false < 5', None, True),
        ('', 'null < 5', None, True),
        ('function test() {return(1)}, x = test, y = test', 'x < y', None, True),

        # for Evaluator._is_less_than_or_equal
        ('', '3 <= 5', True, False),
        ('', '3 <= 3', True, False),
        ('', '-3 <= 2', True, False),
        ('', '3 <= -5', False, False),
        ('', '2.3 <= 2.3', True, False),
        ('', '2.3 <= 2.4', True, False),
        ('', '-1e+4 <= -1e+4', True, False),
        ('', '1e4 <= 1e3', False, False),
        ('', '1e-4 <= 1e-3', True, False),
        ('', '{} <= 5', None, True),
        ('', '[] <= 5', None, True),
        ('', '"" <= 5', None, True),
        ('', '"0" <= 5', None, True),
        ('', 'false <= 5', None, True),
        ('', 'null <= 5', None, True),
        ('function test() {return(1)}, x = test, y = test', 'x <= y', None, True),

        # for Evaluator._is_greater_than
        ('', '3 > 1', True, False),
        ('', '3 > 5', False, False),
        ('', '3 > 3', False, False),
        ('', '-3 > 2', False, False),
        ('', '3 > -5', True, False),
        ('', '2.3 < 2.4', True, False),
        ('', '1e4 > 1e3', True, False),
        ('', '1e-4 > 1e-3', False, False),
        ('', '{} > 5', None, True),
        ('', '[] > 5', None, True),
        ('', '"" > 5', None, True),
        ('', '"0" > 5', None, True),
        ('', 'false > 5', None, True),
        ('', 'null > 5', None, True),
        ('function test() {return(1)}, x = test, y = test', 'x > y', None, True),

        # for Evaluator._is_greater_than_or_equal
        ('', '3 >= 1', True, False),
        ('', '3 >= 5', False, False),
        ('', '3 >= 3', True, False),
        ('', '-3 >= 2', False, False),
        ('', '3 >= -5', True, False),
        ('', '2.3 < 2.4', True, False),
        ('', '1e3 >= 1e3', True, False),
        ('', '1e4 >= 1e3', True, False),
        ('', '1e-4 >= 1e-3', False, False),
        ('', '{} >= 5', None, True),
        ('', '[] >= 5', None, True),
        ('', '"" >= 5', None, True),
        ('', '"0" >= 5', None, True),
        ('', 'false >= 5', None, True),
        ('', 'null >= 5', None, True),
        ('function test() {return(1)}, x = test, y = test', 'x >= y', None, True),

        # for Evaluator._is_contained
        ('', '"b" in ["a", "b", "c"]', True, False),
        ('', '"d" in ["a", "b", "c"]', False, False),
        ('', '1 in [1, 2, "c"]', True, False),
        ('', '3 in [1, 2, "c"]', False, False),
        ('', 'true in [1, true, "c"]', True, False),
        ('', '[2, 3] in [1, [2,3], "c"]', True, False),
        ('', '{"a": 2, "b": false} in [1, {"b":false, "a":2}, "c"]', True, False),
        ('', '"x" in {"x": 3, "y": 10}', True, False),
        ('', '"z" in {"x": 3, "y": 10}', False, False),
        ('', '{"x": 3} in {"x": 3, "y": 10}', True, False),
        ('', '{"x": 2} in {"x": 3, "y": 10}', False, False),
        ('', '{"x": 3, "y": 10} in {"x": 3, "y": 10}', True, False),
        ('', '{"x": 3, "y": 1} in {"x": 3, "y": 10}', False, False),
        ('', '"dog" in "cat&dog&bird"', True, False),
        ('', '"dogs" in "cat&dog&bird"', False, False),
        ('', '"23" in "123"', True, False),
        ('', '23 in "123"', None, True),  # int in str --> ERROR
        ('', '1 in 5', None, True),  # int in int --> ERROR
        ('', '1.5 in 4.5', None, True),  # float in float --> ERROR
        ('', '[1, 2, "c"] in 1', None, True),  # array in int --> ERROR
        ('', 'true in true', None, True),  # boolean in boolean --> ERROR
        ('', 'null in null', None, True),  # null in null --> ERROR
        ('function test() {return(1)}, x = test, y = test', 'x in y', None, True),
        ('function test() {return(1)}, x = test, y = test', '1 in y', None, True),
        ('function test() {return(1)}, x = test, y = test', 'x in [y]', True, False),
        ('{"foo":3, "bar": 2}', '"foo" in .', True, False),
        ('{"foo":3, "bar": 2}', '"baz" in .', False, False),
    )
)

def test_binary(prepared_expression, target_expression, expected_value,
                is_error):
    """Unit-test for binary expression in Evaluator

    Unit-test for "+", "*", "and", "<=", ...

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
    config = Config(max_array_size=5)

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
