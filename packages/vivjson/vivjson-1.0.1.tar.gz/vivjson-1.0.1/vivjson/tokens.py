"""Token for VivJson

For example,

              GT  NUMBER  ASSIGN  PLUS  NUMBER
               |  |            |   |    |
    while  ( i >  3     )  { i = i +    1     }
    |      | |          |  | |   |            |
IDENTIFIER | IDENTIFIER |  | IDENTIFIER       |
           |            |  |                  |
       LEFT_PARENTHESIS |  LEFT_CURLY_BRACKET |
                        |                     |
          RIGHT_PARENTHESIS            RIGHT_CURLY_BRACKET


Refer to:
- "Let's make a Teeny Tiny compiler"
  https://austinhenley.com/blog/teenytinycompiler1.html
- "Crafting Interpreters"
  https://craftinginterpreters.com/
Note that this code is made from scratch. The source code
of the above WEB sites is not used.

Note:
This file name is "tokens.py" instead of "token.py". Because `pydoc`
does not work correctly for "token.py". Then `pydoc` outputs error
as below.
> ImportError: cannot import name 'EXACT_TOKEN_TYPES' from 'token'

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
__date__ = '2025-03-30'

from enum import Enum

class Token:
    """Token class

    Attributes:
        type (Token.Type): The type of token
        lexeme (str or NoneType): The token's actual text
        medium (str or NoneType): The name of object where the token is
                                  existed. For example, "test.viv",
                                  "1st argument".
        line_number (int or NoneType): Line number where the token is
                                       existed.
        column_number (int or NoneType): Column number where the token
                                         is existed.
        _keywords (dict): Keywords table that is generated from
                          _KEYWORD_TYPES.
        _KEYWORD_TYPES (tuple): Token types of Keyword.
    """
    class Type(Enum):
        """Token types"""
        # 4 arithmetic operators and so on
        PLUS = '+'
        MINUS = '-'
        MULTIPLY = '*'
        DIVIDE = '/'
        MODULO = '%'

        # Specific operator
        IN = 'in'

        # Using various purpose
        DOT = '.'
        LEFT_PARENTHESIS = '('
        RIGHT_PARENTHESIS = ')'
        LEFT_SQUARE_BRACKET = '['
        RIGHT_SQUARE_BRACKET = ']'
        LEFT_CURLY_BRACKET = '{'
        RIGHT_CURLY_BRACKET = '}'

        # Assignments (Substitutes)
        ASSIGN = '='
        SET = ':'
        RESULT = ':='
        PLUS_ASSIGN = '+='
        MINUS_ASSIGN = '-='
        MULTIPLY_ASSIGN = '*='
        DIVIDE_ASSIGN = '/='
        MODULO_ASSIGN = '%='

        # Conditions
        EQ = '=='
        NE = '!='
        LT = '<'
        LE = '<='
        GT = '>'
        GE = '>='

        # Logical operators
        OR = 'or'
        AND = 'and'
        NOT = 'not'

        # Modifiers
        CLASS = 'class'
        FUNCTION = 'function'
        REFERENCE = 'reference'

        # Statements
        BREAK = 'break'
        CONTINUE = 'continue'
        RETURN = 'return'

        # Values
        NUMBER = 'number'
        STRING = 'string'
        NULL = 'null'
        TRUE = 'true'
        FALSE = 'false'

        # Variable/Function name
        IDENTIFIER = 'identifier'

        # Functions
        IF = 'if'
        ELSEIF = 'elseif'
        ELSE = 'else'
        FOR = 'for'
        REMOVE = 'remove'
        INCLUDE = 'include'
        IMPORT = 'import'
        SUPER = 'super'

        # Terminator
        NEW_LINE = 'new_line'
        SEMICOLON = ';'
        COMMA = ','
        EOS = 'eos'

        # Unexpected
        ERROR = 'error'

    _KEYWORD_TYPES = (
        Type.IN, Type.OR, Type.AND, Type.NOT,
        Type.CLASS, Type.FUNCTION, Type.REFERENCE,
        Type.BREAK, Type.CONTINUE, Type.RETURN,
        Type.NULL, Type.TRUE, Type.FALSE,
        Type.IF, Type.ELSEIF, Type.ELSE,
        Type.FOR, Type.REMOVE,
        Type.INCLUDE, Type.IMPORT, Type.SUPER
    )

    def __init__(self, token_type, medium=None,  # pylint: disable=R0913
                 line_number=None, column_number=None, lexeme=None):
        """Initialize class.

        Args:
            token_type (Token.Type): The type of token
            medium (str, optional): The name of object where the token
                                    is existed. For example,
                                    "test.viv", "1st argument".
            line_number (int, optional): Line number where the token
                                         is existed.
            column_number (int, optional): Column number where the
                                           token is existed.
            lexeme (str, optional): The token's actual text. It is so
                                    called "lexeme".
                                    When this is omitted or this is
                                    None, the assigned value of Token
                                    type is used.
        """
        self.type = token_type
        self.medium = medium
        self.line_number = line_number
        self.column_number = column_number
        self.lexeme = lexeme if lexeme is not None else token_type.value

        self._keywords = {}
        for keyword_type in self._KEYWORD_TYPES:
            self._keywords[keyword_type.value] = keyword_type

    def __repr__(self):
        return self.to_string()

    def fix_keyword_type(self):
        """Fix type if this is Keyword.

        Returns:
            bool: True if it is fixed,
                  False otherwise.
        """
        is_fixed = self.lexeme in self._keywords
        if is_fixed:
            self.type = self._keywords[self.lexeme]
        return is_fixed

    def to_string(self, omit_type_name=False):
        """Get as string.

        Args:
            omit_type_name (bool, optional): Type name is omitted when
                                             it is True.
                                             The default is False.

        Returns:
            str: Type name and lexeme
        """
        text = self.lexeme if self.lexeme != '\n' else 'LF'
        text = f'"{text}"' if omit_type_name else f'{self.type.name} ({text})'
        additional = []
        if self.medium is not None:
            additional.append(self.medium)
        if self.line_number is not None:
            additional.append(f'line: {self.line_number}')
        if self.column_number is not None:
            additional.append(f'column: {self.column_number}')
        if len(additional) > 0:
            text +=  f' in ({", ".join(additional)})'
        return text
