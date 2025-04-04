"""Unit-test for Config

Unit-test for getter/setter in Config

Run `python3 -m pytest tests/test_config.py` in parent directory.

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
__date__ = '2025-03-25'

# pylint: disable=C0121, E0401

from vivjson.config import Config

def test_config():  # pylint: disable=R0915
    """Unit-test for Config

    Unit-test for getter/setter in Config
    """
    assert Config.get_enable_stderr_alt(None) == Config.ENABLE_STDERR_DEFAULT
    assert Config.get_enable_tag_detail_alt(None) == Config.ENABLE_TAG_DETAIL_DEFAULT
    assert Config.get_enable_only_json_alt(None) == Config.ENABLE_ONLY_JSON_DEFAULT
    assert Config.get_infinity_alt(None) == Config.INFINITY_DEFAULT
    assert Config.get_nan_alt(None) == Config.NAN_DEFAULT
    assert Config.get_max_array_size_alt(None) == Config.MAX_ARRAY_SIZE_DEFAULT
    assert Config.get_max_depth_alt(None) == Config.MAX_DEPTH_DEFAULT
    assert Config.get_max_loop_times_alt(None) == Config.MAX_LOOP_TIMES_DEFAULT

    config = Config()

    assert config.get_enable_stderr() == Config.ENABLE_STDERR_DEFAULT
    assert Config.get_enable_stderr_alt(config) == Config.ENABLE_STDERR_DEFAULT
    assert config.get_enable_tag_detail() == Config.ENABLE_TAG_DETAIL_DEFAULT
    assert Config.get_enable_tag_detail_alt(config) == Config.ENABLE_TAG_DETAIL_DEFAULT
    assert config.get_enable_only_json() == Config.ENABLE_ONLY_JSON_DEFAULT
    assert Config.get_enable_only_json_alt(config) == Config.ENABLE_ONLY_JSON_DEFAULT
    assert config.get_infinity() == Config.INFINITY_DEFAULT
    assert Config.get_infinity_alt(config) == Config.INFINITY_DEFAULT
    assert config.get_nan() == Config.NAN_DEFAULT
    assert Config.get_nan_alt(config) == Config.NAN_DEFAULT
    assert config.get_max_array_size() == Config.MAX_ARRAY_SIZE_DEFAULT
    assert Config.get_max_array_size_alt(config) == Config.MAX_ARRAY_SIZE_DEFAULT
    assert config.get_max_depth() == Config.MAX_DEPTH_DEFAULT
    assert Config.get_max_depth_alt(config) == Config.MAX_DEPTH_DEFAULT
    assert config.get_max_loop_times() == Config.MAX_LOOP_TIMES_DEFAULT
    assert Config.get_max_loop_times_alt(config) == Config.MAX_LOOP_TIMES_DEFAULT

    config = Config(
        enable_stderr=True,
        enable_tag_detail=True,
        enable_only_json=True,
        infinity='Infinity',
        nan='NaN',
        max_array_size=3,
        max_depth=2,
        max_loop_times=1
    )

    assert config.get_enable_stderr() == True
    assert Config.get_enable_stderr_alt(config) == True
    assert Config.get_enable_stderr_alt(None) == Config.ENABLE_STDERR_DEFAULT
    assert config.get_enable_tag_detail() == True
    assert Config.get_enable_tag_detail_alt(config) == True
    assert Config.get_enable_tag_detail_alt(None) == Config.ENABLE_TAG_DETAIL_DEFAULT
    assert config.get_enable_only_json() == True
    assert Config.get_enable_only_json_alt(config) == True
    assert Config.get_enable_only_json_alt(None) == Config.ENABLE_ONLY_JSON_DEFAULT
    assert config.get_infinity() == 'Infinity'
    assert Config.get_infinity_alt(config) == 'Infinity'
    assert Config.get_infinity_alt(None) == Config.INFINITY_DEFAULT
    assert config.get_nan() == 'NaN'
    assert Config.get_nan_alt(config) == 'NaN'
    assert Config.get_nan_alt(None) == Config.NAN_DEFAULT
    assert config.get_max_array_size() == 3
    assert Config.get_max_array_size_alt(config) == 3
    assert Config.get_max_array_size_alt(None) == Config.MAX_ARRAY_SIZE_DEFAULT
    assert config.get_max_depth() == 2
    assert Config.get_max_depth_alt(config) == 2
    assert Config.get_max_depth_alt(None) == Config.MAX_DEPTH_DEFAULT
    assert config.get_max_loop_times() == 1
    assert Config.get_max_loop_times_alt(config) == 1
    assert Config.get_max_loop_times_alt(None) == Config.MAX_LOOP_TIMES_DEFAULT

    config = Config()

    assert config.get_enable_stderr() == Config.ENABLE_STDERR_DEFAULT
    assert Config.get_enable_stderr_alt(config) == Config.ENABLE_STDERR_DEFAULT
    assert Config.get_enable_stderr_alt(None) == Config.ENABLE_STDERR_DEFAULT
    config.enable_stderr()
    assert config.get_enable_stderr() == True
    assert Config.get_enable_stderr_alt(config) == True
    assert Config.get_enable_stderr_alt(None) == Config.ENABLE_STDERR_DEFAULT
    config.enable_stderr(False)
    assert config.get_enable_stderr() == False
    assert Config.get_enable_stderr_alt(config) == False
    assert Config.get_enable_stderr_alt(None) == Config.ENABLE_STDERR_DEFAULT
    config.enable_stderr(True)
    assert config.get_enable_stderr() == True
    assert Config.get_enable_stderr_alt(config) == True
    assert Config.get_enable_stderr_alt(None) == Config.ENABLE_STDERR_DEFAULT

    assert config.get_enable_tag_detail() == Config.ENABLE_TAG_DETAIL_DEFAULT
    assert Config.get_enable_tag_detail_alt(config) == Config.ENABLE_TAG_DETAIL_DEFAULT
    assert Config.get_enable_tag_detail_alt(None) == Config.ENABLE_TAG_DETAIL_DEFAULT
    config.enable_tag_detail()
    assert config.get_enable_tag_detail() == True
    assert Config.get_enable_tag_detail_alt(config) == True
    assert Config.get_enable_tag_detail_alt(None) == Config.ENABLE_TAG_DETAIL_DEFAULT
    config.enable_tag_detail(False)
    assert config.get_enable_tag_detail() == False
    assert Config.get_enable_tag_detail_alt(config) == False
    assert Config.get_enable_tag_detail_alt(None) == Config.ENABLE_TAG_DETAIL_DEFAULT
    config.enable_tag_detail(True)
    assert config.get_enable_tag_detail() == True
    assert Config.get_enable_tag_detail_alt(config) == True
    assert Config.get_enable_tag_detail_alt(None) == Config.ENABLE_TAG_DETAIL_DEFAULT

    assert config.get_enable_only_json() == Config.ENABLE_ONLY_JSON_DEFAULT
    assert Config.get_enable_only_json_alt(config) == Config.ENABLE_ONLY_JSON_DEFAULT
    assert Config.get_enable_only_json_alt(None) == Config.ENABLE_ONLY_JSON_DEFAULT
    config.enable_only_json()
    assert config.get_enable_only_json() == True
    assert Config.get_enable_only_json_alt(config) == True
    assert Config.get_enable_only_json_alt(None) == Config.ENABLE_ONLY_JSON_DEFAULT
    config.enable_only_json(False)
    assert config.get_enable_only_json() == False
    assert Config.get_enable_only_json_alt(config) == False
    assert Config.get_enable_only_json_alt(None) == Config.ENABLE_ONLY_JSON_DEFAULT
    config.enable_only_json(True)
    assert config.get_enable_only_json() == True
    assert Config.get_enable_only_json_alt(config) == True
    assert Config.get_enable_only_json_alt(None) == Config.ENABLE_ONLY_JSON_DEFAULT

    assert config.get_infinity() == Config.INFINITY_DEFAULT
    assert Config.get_infinity_alt(config) == Config.INFINITY_DEFAULT
    assert Config.get_infinity_alt(None) == Config.INFINITY_DEFAULT
    config.set_infinity('abc')
    assert config.get_infinity() == 'abc'
    assert Config.get_infinity_alt(config) == 'abc'
    assert Config.get_infinity_alt(None) == Config.INFINITY_DEFAULT
    config.set_infinity(None)
    assert config.get_infinity() is None
    assert Config.get_infinity_alt(config) is None
    assert Config.get_infinity_alt(None) == Config.INFINITY_DEFAULT

    assert config.get_nan() == Config.NAN_DEFAULT
    assert Config.get_nan_alt(config) == Config.NAN_DEFAULT
    assert Config.get_nan_alt(None) == Config.NAN_DEFAULT
    config.set_nan('Xyz')
    assert config.get_nan() == 'Xyz'
    assert Config.get_nan_alt(config) == 'Xyz'
    assert Config.get_nan_alt(None) == Config.NAN_DEFAULT
    config.set_nan(None)
    assert config.get_nan() is None
    assert Config.get_nan_alt(config) is None
    assert Config.get_nan_alt(None) == Config.NAN_DEFAULT

    assert config.get_max_array_size() == Config.MAX_ARRAY_SIZE_DEFAULT
    assert Config.get_max_array_size_alt(config) == Config.MAX_ARRAY_SIZE_DEFAULT
    assert Config.get_max_array_size_alt(None) == Config.MAX_ARRAY_SIZE_DEFAULT
    config.set_max_array_size(20)
    assert config.get_max_array_size() == 20
    assert Config.get_max_array_size_alt(config) == 20
    assert Config.get_max_array_size_alt(None) == Config.MAX_ARRAY_SIZE_DEFAULT

    assert config.get_max_depth() == Config.MAX_DEPTH_DEFAULT
    assert Config.get_max_depth_alt(config) == Config.MAX_DEPTH_DEFAULT
    assert Config.get_max_depth_alt(None) == Config.MAX_DEPTH_DEFAULT
    config.set_max_depth(8)
    assert config.get_max_depth() == 8
    assert Config.get_max_depth_alt(config) == 8
    assert Config.get_max_depth_alt(None) == Config.MAX_DEPTH_DEFAULT

    assert config.get_max_loop_times() == Config.MAX_LOOP_TIMES_DEFAULT
    assert Config.get_max_loop_times_alt(config) == Config.MAX_LOOP_TIMES_DEFAULT
    assert Config.get_max_loop_times_alt(None) == Config.MAX_LOOP_TIMES_DEFAULT
    config.set_max_loop_times(15)
    assert config.get_max_loop_times() == 15
    assert Config.get_max_loop_times_alt(config) == 15
    assert Config.get_max_loop_times_alt(None) == Config.MAX_LOOP_TIMES_DEFAULT
