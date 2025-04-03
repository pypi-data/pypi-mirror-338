"""Unit-test for sample codes

Run `python3 -m pytest tests/test_sample_codes.py` in
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

# pylint: disable=E0401

from vivjson.viv import Viv

def test():
    """Unit-test for sample codes."""
    value, error_message = Viv.run("tests/sample_codes.viv")
    assert error_message == ''

    assert "array_2d" in value
    assert value["array_2d"] == [[0, 1, 2], [True, "text", None], [3, 4, 5], [6, 7, 8]]

    assert "array_init" in value
    assert value["array_init"] == [None, None, None, None, None]

    assert "delegate_do" in value
    assert value["delegate_do"] == "1xxx"

    assert "operated_1" in value
    assert value["operated_1"] == 3

    assert "operated_2" in value
    assert value["operated_2"] == [7, 3, 10, 2.5]

    assert "month" in value
    assert value["month"] == "May"

    assert "day_of_week" in value
    assert value["day_of_week"] == "Sat"
