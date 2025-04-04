"""Unit-test for order of operations in Evaluator

Unit-test for +, -, *, /, and, or, ...

Run `python3 -m pytest tests/test_evaluator_order.py` in
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
__date__ = '2025-03-20'

# pylint: disable=C0301, E0401, R0801

import pytest
from vivjson.viv import Viv
from vivjson.config import Config

@pytest.mark.parametrize(
    'prepared_expression, target_expression, expected_value, is_error', (
        ('', '1 + 2 * 5', 11, False),
        ('', '(1 + 2) * 5', 15, False),
        ('', '2 * 3 + 8', 14, False),
        ('', '3 / 5 + 10', 10.6, False),
        ('', '3 / (5 + 3 + 3 + 3 + 1)', 0.2, False),
        ('', '12 % 5 + 1', 3, False),
        ('', '12 % (5 + 1)', 0, False),
        ('', '3 / 5 * 3', 1.8, False),
        ('', '3 / (5 * 3)', 0.2, False),
        ('', '3 / (4 + 5 + 6)', 0.2, False),
        ('', '6 / ((4 + 5 + 6))', 0.4, False),
        ('', '(6 / ((4 + 5 + 6)))', 0.4, False),
        ('', '1 + (-6 / (4 + 5 + 6))', 0.6, False),
        ('', '-1 / 10', -0.1, False),
        ('', '3 +-1 / 10', 2.9, False),
        ('', '3 /-1', -3, False),
        ('', '("a,b" + "c") / ","', ["a", "bc"], False),
        ('', '"a,b" + "c" / ","', ["a,b", "c"], False),
        ('', '3 + [] + true', [3, True], False),
        ('', '3 + ["x"] + true', [3, "x", True], False),
        ('', 'false or true and true or false', True, False),
        ('', 'false or not false', True, False),
        ('', 'not false or false', True, False),
        ('', 'not true and true', False, False),
        ('', 'not(true and true)', False, False),
        ('', 'not (3 != 3)', True, False),
        ('', 'not (true)', False, False),
        ('', '(true)', True, False),
        ('', '3 > 2 and 0 > -1', True, False),
        ('', '3 > (2 and 0) > -1', None, True),  # 3 > false > -1 is invalid.
        ('', '3 > 2 and 2 > -1', True, False),
        ('a = 5; a += 3 * 2', 'a', 11, False),
        ('', '"a" and "b" == "c"', False, False),  # --> true and false --> false
        ('', '("a" and "b") == "c"', True, False),  # --> true == true --> true
    )
)

def test_order(prepared_expression, target_expression, expected_value,
               is_error):
    """Unit-test for order of operations in Evaluator

    Unit-test for +, -, *, /, and, or, ...

    Args:
        prepared_expression (str): When the another expression,
                                 such as assignment, is needed before
                                 test, it is given here.
                                 Maybe this is '' mostly.
        target_expression (str): "return" method's argument as targeted
                                 expression.
        expected_value (Any): The expected value as Python's value
        is_error (bool): True if occurring error is expected,
                         False otherwise.
    """
    config = Config(max_depth=10)

    text = f'{prepared_expression}; return({target_expression})'
    value, error_message = Viv.run(text, config)

    assert (error_message != '') == is_error

    if isinstance(value, float):
        value = round(value, 10)
    assert value == expected_value

    if error_message == '' \
            and not isinstance(expected_value, bool) \
            and isinstance(expected_value, (int, float)):
        assert type(value) == type(expected_value)  # pylint: disable=C0123
