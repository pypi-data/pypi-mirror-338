"""Configuration for VivJson

Environment:
- Python 3.9 or later

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

from typing import Optional

class Config:  # pylint: disable=R0902, R0904
    """Config class

    Attributes:
        _enable_stderr (bool): When True is given, error message is
                               outputted into stderr.
                               Otherwise, it is not outputted.
        _enable_tag_detail (bool): When True is given, error message's
                               tag contains either of "Lexer",
                               "Parser", or "Evaluator".
        _enable_only_json (bool): When true is given, the given data is
                                  parsed as JSON.
                                  In other words, script is disabled.
        _infinity (str on NoneType): When string is given, Infinity is
                                     allowed. Then the given string is
                                     used to input/output Infinity
                                     from/to JSON. (Note that it is not
                                     surrounded with quotation mark.)
                                     When None is given and Infinity is
                                     happen, error is occurred.
        _nan (str on NoneType): When string is given, NaN (Not a
                                Number) is allowed. Then the given
                                string is used to input/output NaN
                                from/to JSON. (Note that it is not
                                surrounded with quotation mark.)
                                When None is given and NaN is happen,
                                error is occurred.
        _max_array_size (int): Maximum array/block size
        _max_depth (int): Maximum recursive called times of evaluate
                          method
        _max_loop_times (int): Maximum loop times of "for", "while",
                               and so on
        SPEC_VERSION (str): Version of VivJson's specification
                            as <Major> "." <Minor> "." <Patch>
                            (For example, "1.0.0")
        INTERPRETER_VERSION (str): Version of this interpreter as
                                   <Major> "." <Minor> "." <Patch>
                                   (For example, "1.0.0")
                                   This <Major> "." <Minor> is equal to
                                   <SPEC_VERSION>'s one.
        ENABLE_STDERR_DEFAULT (bool): The default of enabling error
                                      message's stderr output
        ENABLE_TAG_DETAIL_DEFAULT (bool): The default of enabling
                                      detail of error message's tag
        ENABLE_ONLY_JSON_DEFAULT (bool): The default of enabling only
                                         JSON
        INFINITY_DEFAULT (str on NoneType): The default of Infinity
        NAN_DEFAULT (str on NoneType): The default of NaN (Not a
                                       Number)
        MAX_ARRAY_SIZE_DEFAULT (int): The default of maximum array size
        MAX_DEPTH_DEFAULT (int): The default of maximum recursive
                                 called times of evaluate method
        MAX_LOOP_TIMES_DEFAULT (int): The default of maximum loop times
                                      of "for", "while", and so on
    """
    SPEC_VERSION = '1.0.0'
    INTERPRETER_VERSION = '1.0.0'
    ENABLE_STDERR_DEFAULT = False
    ENABLE_TAG_DETAIL_DEFAULT = False
    ENABLE_ONLY_JSON_DEFAULT = False
    INFINITY_DEFAULT = None
    NAN_DEFAULT = None
    MAX_ARRAY_SIZE_DEFAULT = 1000
    MAX_DEPTH_DEFAULT = 200
    MAX_LOOP_TIMES_DEFAULT = 1000

    def __init__(self,  # pylint: disable=R0913
                 enable_stderr=ENABLE_STDERR_DEFAULT,
                 enable_tag_detail=ENABLE_TAG_DETAIL_DEFAULT,
                 enable_only_json=ENABLE_ONLY_JSON_DEFAULT,
                 infinity=INFINITY_DEFAULT,
                 nan=NAN_DEFAULT,
                 max_array_size=MAX_ARRAY_SIZE_DEFAULT,
                 max_depth=MAX_DEPTH_DEFAULT,
                 max_loop_times=MAX_LOOP_TIMES_DEFAULT):
        """Initialize class.

        Args:
            enable_stderr (bool, optional): When True is given, error 
                                    message is outputted into stderr.
                                    Otherwise, it is not outputted.
                                    The default is False.
            enable_tag_detail (bool): When True is given, error
                                    message's tag contains either of
                                    "Lexer", "Parser", or "Evaluator".
            enable_only_json (bool): When true is given, the given data
                                     is parsed as JSON.
                                     In other words, script is
                                     disabled.
            infinity (str on NoneType, optional): When string is given,
                                    Infinity is allowed in JSON. Then
                                    the given string is used to
                                    input/output Infinity from/to JSON.
                                    (Note that it is not surrounded
                                    with quotation mark.)
                                    When None is given and Infinity is
                                    happen, error may be occurred.
                                    The default is None.
            nan (str on NoneType, optional): When string is given,
                                    NaN (Not a Number) is allowed in
                                    JSON. Then the given string is used
                                    to input/output NaN from/to JSON.
                                    (Note that it is not surrounded
                                    with quotation mark.)
                                    When None is given and NaN is
                                    happen, error may be occurred.
                                    The default is False.
            max_array_size (int, optional): Maximum array/block size
            max_depth (int, optional): Maximum recursive called times
                                       of evaluate method
            max_loop_times (int, optional): Maximum loop times of
                                            "for", "while", and so on
        """
        self._enable_stderr = enable_stderr
        self._enable_tag_detail = enable_tag_detail
        self._enable_only_json = enable_only_json
        self._infinity = infinity
        self._nan = nan
        self._max_array_size = max_array_size
        self._max_depth = max_depth
        self._max_loop_times = max_loop_times

    def clone(self):
        """Copy itself.

        Returns:
            Config: Copied Config object
        """
        return Config(self._enable_stderr,
                      self._enable_tag_detail,
                      self._enable_only_json,
                      self._infinity,
                      self._nan,
                      self._max_array_size,
                      self._max_depth,
                      self._max_loop_times)

    def enable_stderr(self, enable=True):
        """Enable that error message outputs into stderr.

        Args:
            enable (bool, optional): When True is given, error message
                                     is outputted into stderr.
                                     Otherwise, it is not outputted.
                                     The argument's default is True.
        """
        self._enable_stderr = enable

    def get_enable_stderr(self) -> bool:
        """Get whether outputting error message into stderr is enable.
        """
        return self._enable_stderr

    @staticmethod
    def get_enable_stderr_alt(config) -> bool:
        """Get whether outputting error message into stderr is enable.

        Args:
            config (Config or NoneType): Instance of configuration.
                                         When it is None, default
                                         value is returned.

        Returns:
            bool: Outputting error message into stderr is enable or not
        """
        return Config.ENABLE_STDERR_DEFAULT if config is None \
               else config.get_enable_stderr()

    def enable_tag_detail(self, enable=True):
        """Enable that detail of error message's tag.

        Args:
            enable (bool, optional): When True is given, error
                                     message's tag contains either of
                                     "Lexer", "Parser", or "Evaluator".
                                     The argument's default is True.
        """
        self._enable_tag_detail = enable

    def get_enable_tag_detail(self) -> bool:
        """Get whether detail of error message's tag is enable or not.
        """
        return self._enable_tag_detail

    @staticmethod
    def get_enable_tag_detail_alt(config) -> bool:
        """Get whether detail of error message's tag is enable or not.

        Args:
            config (Config or NoneType): Instance of configuration.
                                         When it is None, default
                                         value is returned.

        Returns:
            bool: Detail of error message's tag is enable or not
        """
        return Config.ENABLE_TAG_DETAIL_DEFAULT if config is None \
               else config.get_enable_tag_detail()

    def enable_only_json(self, enable=True):
        """Enable that parsing data as only JSON.

        Args:
            enable (bool, optional): When true is given, the given data
                                     is parsed as JSON.
                                     In other words, script is
                                     disabled.
        """
        self._enable_only_json = enable

    def get_enable_only_json(self) -> bool:
        """Get whether parsing data as only JSON is enable or not.
        """
        return self._enable_only_json

    @staticmethod
    def get_enable_only_json_alt(config) -> bool:
        """Get whether parsing data as only JSON is enable or not.

        Args:
            config (Config or NoneType): Instance of configuration.
                                         When it is None, default
                                         value is returned.

        Returns:
            bool: parsing data as only JSON is enable or not
        """
        return Config.ENABLE_ONLY_JSON_DEFAULT if config is None \
               else config.get_enable_only_json()

    def set_infinity(self, infinity: Optional[str]):
        """Set infinity's string.

        When string is given, Infinity is allowed. Then the given
        string is used to input/output Infinity from/to JSON. (Note
        that it is not  surrounded with quotation mark.)
        When None is given and Infinity is happen, error may be
        occurred.

        Args:
            infinity (str or NoneType): Infinity's string or None.
        """
        self._infinity = infinity

    def get_infinity(self) -> Optional[str]:
        """Get infinity's string."""
        return self._infinity

    @staticmethod
    def get_infinity_alt(config) -> Optional[str]:
        """Get infinity's string.

        Args:
            config (Config or NoneType): Instance of configuration.
                                         When it is None, default
                                         value is returned.

        Returns:
            str on NoneType: Infinity's string.
                             When this is None, Infinity is not
                             allowed.
        """
        return Config.INFINITY_DEFAULT if config is None \
               else config.get_infinity()

    def set_nan(self, nan: Optional[str]):
        """Set NaN(Not a Number)'s string.

        When string is given, NaN (Not a Number) is allowed. Then the
        given string is used to input/output NaN from/to JSON. (Note
        that it is not surrounded with quotation mark.)
        When None is given and NaN is happen, error may be occurred.

        Args:
            nan (str or NoneType): NaN(Not a Number)'s string
        """
        self._nan = nan

    def get_nan(self) -> Optional[str]:
        """Get NaN(Not a Number)'s string."""
        return self._nan

    @staticmethod
    def get_nan_alt(config) -> Optional[str]:
        """Get NaN(Not a Number)'s string.

        Args:
            config (Config or NoneType): Instance of configuration.
                                         When it is None, default
                                         value is returned.

        Returns:
            str on NoneType: NaN (Not a Number)'s string.
                             When this is None, NaN is not allowed.
        """
        return Config.NAN_DEFAULT if config is None else config.get_nan()

    def set_max_array_size(self, size: int):
        """Set maximum array/block size."""
        self._max_array_size = size

    def get_max_array_size(self) -> int:
        """Get maximum array/block size."""
        return self._max_array_size

    @staticmethod
    def get_max_array_size_alt(config) -> int:
        """Get maximum array/block size.

        Args:
            config (Config or NoneType): Instance of configuration.
                                         When it is None, default
                                         value is returned.

        Returns:
            int: Maximum array/block size
        """
        return Config.MAX_ARRAY_SIZE_DEFAULT if config is None \
               else config.get_max_array_size()

    def set_max_depth(self, depth: int):
        """Set maximum recursive called times of evaluate method."""
        self._max_depth = depth

    def get_max_depth(self) -> int:
        """Get maximum recursive called times of evaluate method."""
        return self._max_depth

    @staticmethod
    def get_max_depth_alt(config) -> int:
        """Get maximum recursive called times of evaluate method.

        Args:
            config (Config or NoneType): Instance of configuration.
                                         When it is None, default
                                         value is returned.

        Returns:
            int: Maximum recursive called times of evaluate method
        """
        return Config.MAX_DEPTH_DEFAULT if config is None \
               else config.get_max_depth()

    def set_max_loop_times(self, times: int):
        """Set maximum loop times of "for", "while", and so on."""
        self._max_loop_times = times

    def get_max_loop_times(self) -> int:
        """Get maximum loop times of "for", "while", and so on."""
        return self._max_loop_times

    @staticmethod
    def get_max_loop_times_alt(config) -> int:
        """Get maximum loop times of "for", "while", and so on.

        Args:
            config (Config or NoneType): Instance of configuration.
                                         When it is None, default
                                         value is returned.

        Returns:
            int: Maximum loop times of "for", "while", and so on.
        """
        return Config.MAX_LOOP_TIMES_DEFAULT if config is None \
               else config.get_max_loop_times()
