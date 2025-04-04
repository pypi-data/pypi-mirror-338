"""Error for VivJson

- Error.make_lex_error: Report error information and return LexError.
- Error.make_parse_error: Report error information and return
                          ParseError.
- Error.make_evaluate_error: Report error information and return
                             EvaluateError.

Refer to:
- "Crafting Interpreters"
  https://craftinginterpreters.com/
Note that this code is made from scratch. The source code
of the above WEB site is not used.

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
__date__ = '2025-03-22'

from functools import singledispatchmethod
import sys
from .config import Config
from .statement import Literal, Identifier, Keyword, Blank, \
                       Array, Block, Binary, Parameter, \
                       Callee, Call, CalleeRegistry, Loop, \
                       Get, Set, Remove, \
                       Return, Injection, Value
from .tokens import Token

class Error:
    """Error class"""
    TAG = 'Viv'

    class LexError(RuntimeError):
        """Lex-error class of Runtime error"""

    class ParseError(RuntimeError):
        """Parse-error class of Runtime error"""

    class EvaluateError(RuntimeError):
        """Evaluate-error class of Runtime error"""

    @staticmethod
    def make_lex_error(message, medium, line, column, config=None):
        """Make lex-error.

        Report error information and return LexError that is Exception.
        This method does not raise Exception. So caller should raise
        Exception if it is needed.

        Args:
            message (str): Error message
            medium (str or NoneType): The object that has source code.
            line (int): Line number of location where error occurs.
            column (int): Column number of location where error occurs.
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            LexError: Exception for raising.
        """
        report = Error.report('Lexer', message,
                      Error._get_location_text(medium, line, column), config)
        sys.tracebacklimit = 0
        return Error.LexError(report)

    @staticmethod
    def make_parse_error(message, token=None, config=None):
        """Make parse-error.

        Report error information and return ParseError that is
        Exception.
        This method does not raise Exception. So caller should raise
        Exception if it is needed.

        Args:
            message (str): Error message
            token (Token or NoneType, optional): Token.
                                                 None is given when
                                                 cause is not Token.
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            ParseError: Exception for raising.
        """
        report = Error.report('Parser', message, token, config)
        sys.tracebacklimit = 0
        return Error.ParseError(report)

    @staticmethod
    def make_evaluate_error(message, statement=None, config=None,
                            eliminate_tag=False):
        """Make evaluate-error.

        Report error information and return EvaluateError that is
        Exception.
        This method does not raise Exception. So caller should raise
        Exception if it is needed.

        Args:
            message (str): Error message
            statement (Statement or NoneType, optional): Statement
                    where error occurs. It is used to get location.
                    None is given when cause is not Statement.
            config (Config or NoneType, optional): Configuration if
                                                   needed.
            eliminate_tag (bool, optional): True if tag is not needed,
                                            False otherwise.
                                            The default is False

        Returns:
            EvaluateError: Exception for raising.
        """
        location = Error._get_statement_location(statement)
        report = Error.report('Evaluator', message, location, config,
                               eliminate_tag)
        sys.tracebacklimit = 0
        return Error.EvaluateError(report)

    @staticmethod
    def report(tag, message, location=None, config=None,
               eliminate_tag=False):
        """Report an error message.

        Print an error message into stderr according as configuration.

        Args:
            tag (str): Tag, such as "Lexer", "Parser", or "Evaluator".
            message (str): Main message of Error
            location (Token or str or NoneType, optional): The location
                                                           of error
            config (Config or NoneType, optional): Configuration if
                                                   needed.
            eliminate_tag (bool, optional): True if tag is not needed,
                                            False otherwise.
                                            The default is False

        Returns:
            str: Error message
        """
        tag_detail = ''
        if Config.get_enable_tag_detail_alt(config):
            tag_detail = f':{tag}'
        text = message if eliminate_tag \
                    else  f'[{Error.TAG}{tag_detail}] Error: {message}'
        if location is not None:
            if isinstance(location, Token):
                text = f'{text} for {location.to_string()}'
            elif isinstance(location, str):
                text = f'{text} in {location}'
        if Config.get_enable_stderr_alt(config):
            print(text, file=sys.stderr)
        return text

    @staticmethod
    def _get_location_text(medium, line: int, column: int) -> str:
        medium = f'{medium}, ' if isinstance(medium, str) else ''
        return f'({medium}line: {line}, column: {column})'

    @staticmethod
    def _get_token_location(token: Token):
        """Get Token's location in source code."""
        location = None
        if token is not None and token.line_number is not None \
                and token.column_number is not None:
            location = Error._get_location_text(token.medium,
                                                token.line_number,
                                                token.column_number)
        return location

    @singledispatchmethod
    @staticmethod
    def _get_statement_location(_):
        """Get Statement's location in source code."""
        return None

    @staticmethod
    @_get_statement_location.register
    def _(literal: Literal):
        return Error._get_token_location(literal.token)

    @staticmethod
    @_get_statement_location.register
    def _(identifier: Identifier):
        return Error._get_token_location(identifier.name)

    @staticmethod
    @_get_statement_location.register
    def _(keyword: Keyword):
        return Error._get_token_location(keyword.token)

    @staticmethod
    @_get_statement_location.register
    def _(blank: Blank):
        return Error._get_token_location(blank.token)

    @staticmethod
    @_get_statement_location.register
    def _(array: Array):
        if len(array.values) == 0:
            return None
        return Error._get_statement_location(array.values[0])

    @staticmethod
    @_get_statement_location.register
    def _(block: Block):
        if len(block.values) == 0:
            return None
        return Error._get_statement_location(block.values[0])

    @staticmethod
    @_get_statement_location.register
    def _(binary: Binary):
        return Error._get_statement_location(binary.left)

    @staticmethod
    @_get_statement_location.register
    def _(parameter: Parameter):
        if parameter.modifier is not None:
            return Error._get_token_location(parameter.modifier)
        return Error._get_statement_location(parameter.name)

    @staticmethod
    @_get_statement_location.register
    def _(callee: Callee):
        return Error._get_statement_location(callee.name)

    @staticmethod
    @_get_statement_location.register
    def _(callee_registry: CalleeRegistry):
        return Error._get_statement_location(callee_registry.callee)

    @staticmethod
    @_get_statement_location.register
    def _(call: Call):
        return Error._get_statement_location(call.name)

    @staticmethod
    @_get_statement_location.register
    def _(loop: Loop):
        return Error._get_statement_location(loop.call)

    @staticmethod
    @_get_statement_location.register
    def _(get: Get):
        if len(get.members) == 0:
            return None
        return Error._get_statement_location(get.members[0])

    @staticmethod
    @_get_statement_location.register
    def _(s: Set):
        if len(s.members) == 0:
            return None
        return Error._get_statement_location(s.members[0])

    @staticmethod
    @_get_statement_location.register
    def _(remove: Remove):
        return Error._get_token_location(remove.token)

    @staticmethod
    @_get_statement_location.register
    def _(r: Return):
        return Error._get_token_location(r.token)

    @staticmethod
    @_get_statement_location.register
    def _(injection: Injection):
        return injection.location

    @staticmethod
    @_get_statement_location.register
    def _(value: Value):
        return value.location
