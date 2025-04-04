"""Lexer for VivJson

- Lexer: Constructor. Its argument is source code as string.
- Lexer#get_token: Extract a token from the current position of source
                   code.

For example, the given source code is extracted as below.

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
__date__ = '2025-03-20'

# pylint: disable=R0902, R0903

import re
from .error import Error
from .tokens import Token

class Lexer:
    """Lexer class

    Attributes:
        _medium (str or NoneType): The name of object that has source
                                   code. It is used to report error.
                                   For example, "test.viv",
                                   "1st argument".
        _config (Config or NoneType): Configuration
        _maybe_get_token_methods (tuple): Methods of getting
                                          the particular token.
        _source_code (str): Source code as text. It is given from
                            caller.
        _current_letter (str): A current letter in the text.
        _current_position (int): The current position in the text.
        _token_head_position (int): The position of the current
                                    token's head in the text.
        _line_number (int): Line number in the text. It is
                            saved into Token and is used for
                            error information.
        _line_head_position (int): The position of the current
                                   line's head in the text.
                                   It is used to calculate column
                                   number that is saved into Token.
                                   The column number is used for
                                   error information.
        _previous_token (Token or NoneType): Previous token.
                                             None if first parsing.
        _hex_pattern (re.Pattern): Compiled pattern of Hex-digit.
        _EOS (str): A marker for end of string.
                    It indicates that all letters are consumed.
        _ONE_LETTER_OPERATORS (tuple): Token types of
                                       1 letter's operations
        _TWO_LETTERS_OPERATORS (tuple): 2 dimensional tuple of
                                        Token type.
                                        1st value is Token type of
                                        2 letter's operation.
                                        2nd value is Token type of
                                        first one letter.
        _TERMINATORS (dict): Token types of terminator.
        _WHITE_SPACES (str): White spaces that should be skipped.
        _REPLACED_LETTERS (dict): The escaped letter and real letter.
    """
    _EOS = '\0'
    _ONE_LETTER_OPERATORS = (
        Token.Type.DOT,
        Token.Type.LEFT_PARENTHESIS,
        Token.Type.RIGHT_PARENTHESIS,
        Token.Type.LEFT_SQUARE_BRACKET,
        Token.Type.RIGHT_SQUARE_BRACKET,
        Token.Type.LEFT_CURLY_BRACKET,
        Token.Type.RIGHT_CURLY_BRACKET
    )
    _TWO_LETTERS_OPERATORS = (
        # (for 2 letters, for first 1 letter)
        (Token.Type.EQ, Token.Type.ASSIGN),  # ==, =
        (Token.Type.LE, Token.Type.LT),  # <=, <
        (Token.Type.GE, Token.Type.GT),  # >=, >
        (Token.Type.NE, Token.Type.ERROR),  # !=, (unexpected)
        (Token.Type.PLUS_ASSIGN, Token.Type.PLUS),  # +=, +
        (Token.Type.MINUS_ASSIGN, Token.Type.MINUS),  # -=, -
        (Token.Type.MULTIPLY_ASSIGN, Token.Type.MULTIPLY),  # *=, *
        (Token.Type.DIVIDE_ASSIGN, Token.Type.DIVIDE),  # /=, /
        (Token.Type.MODULO_ASSIGN, Token.Type.MODULO),  # %=, %
        (Token.Type.RESULT, Token.Type.SET)  # :=, :
    )
    _TERMINATORS = {
        '\n': Token.Type.NEW_LINE,
        ';': Token.Type.SEMICOLON,
        ',': Token.Type.COMMA,
        _EOS: Token.Type.EOS
    }
    _WHITE_SPACES = ' \t\r'  # Space, Tab, and Carriage Return
    _REPLACED_LETTERS = {'b': chr(0x08), 'f': chr(0x0C), 'n': chr(0x0A),
                         'r': chr(0x0D), 't': chr(0x09)}

    def __init__(self, source_code, medium=None, config=None):
        """Initialize class.

        Args:
            source_code (str): Source code as text
            medium (str, optional): The name of object that has source
                                    code. It is used to report error.
                                    For example, "test.viv",
                                    "1st argument".
            config (Config or NoneType): Configuration if needed.
        """
        self._medium = medium
        self._config = config
        self._maybe_get_token_methods = (
            self._maybe_get_1_letter_operation,
            self._maybe_get_2_letters_operation,
            self._maybe_get_string,
            self._maybe_get_number,
            self._maybe_get_identifier_or_keyword,
            self._maybe_get_terminator
        )

        self._source_code = source_code + '\n'  # Add for convenient reason

        self._current_letter = ''
        self._current_position = -1  # It becomes 0 in the following function.
        self._go_to_next_letter()
        self._token_head_position = self._current_position

        self._line_number = 0  # It becomes 1 in the following function.
        self._record_new_line()

        self._previous_token = None

        self._hex_pattern = re.compile(r'[\dA-Fa-f]+')

    def get_token(self):
        """Get the current token.

        Returns:
            Token: The current token.

        Raises:
            LexError: When unknown token is found, it is happen.
        """
        while self._skip_white_space() or self._skip_comment():
            pass

        self._token_head_position = self._current_position
        token = None

        for method in self._maybe_get_token_methods:
            token = method()       # None is returned when this method
            if token is not None:  # can't treat the current lexeme.
                break

        # Error if all methods can't treat the current lexeme.
        if token is None or token.type == Token.Type.ERROR:
            self._abort('Unknown token')

        self._previous_token = token
        return token

    def _record_new_line(self):
        """Record about new line."""
        self._line_number += 1
        self._line_head_position = self._current_position

    def _get_column_number(self):
        """Calculate column number.

        Returns:
            int: The column number. Its minimum value is 1.
        """
        return self._token_head_position - self._line_head_position + 1

    def _go_to(self, offset):
        """Seek and get a letter.

        The current position is moved to the given offset.
        Then the current letter is updated. It becomes EOS marker
        when the position is larger than source code's size. In
        other words, it indicates that all letters are consumed.

        Args:
            offset (int): The offset of position in the text.
        """
        self._current_position = \
            max(self._current_position + offset, 0)  # >= 0
        self._current_letter = self._get_letter()

    def _go_to_next_letter(self):
        """Process a next letter.

        The current position is moved to next letter.
        Then the current letter is updated. It becomes EOS marker
        when all letters are consumed.
        """
        self._go_to(1)

    def _peek_next_letter(self):
        """Peek a next letter.

        A next letter is returned without increment of current
        position.

        Returns:
            str: A next letter
                 EOS if the given position is passed through
                 end of text.
        """
        return self._get_letter(1)

    def _get_letter(self, offset=0):
        """Get a letter of the given offset.

        Args:
            offset (int, optional): The offset of position in the text.
                                    It must be positive number.
                                    The default is 0.

        Returns:
            str: A letter of the given offset.
                 EOS if the given position is out of range.
        """
        position = self._current_position + offset
        return self._source_code[position] \
                if position < len(self._source_code) \
                else self._EOS

    def _maybe_get_1_letter_operation(self):
        """Try to get a token of 1 letter's operation.

        Returns:
            Token or NoneType: A token of 1 letter's operation
                               if it is existed in the current
                               position.
                               Otherwise, None is returned.

        Note:
            When Token is returned, the current position & letter
            are progressed. Otherwise, they are kept.
        """
        token = None
        for token_type in self._ONE_LETTER_OPERATORS:
            if self._current_letter == token_type.value:
                token = self._make_token(token_type)
                self._go_to_next_letter()
                break
        return token

    def _maybe_get_2_letters_operation(self):
        """Try to get a token of two letters operation.

        Returns:
            Token or NoneType: A token of "==", "=", "<=", "<",
                               ">=", ">", or "!=" if it is existed
                               in the current position.
                               Otherwise, None is returned.

        Raises:
            LexError: When only "!" is found, it is happen.

        Note:
            When Token is returned, the current position & letter
            are progressed. Otherwise, they are kept.
        """
        token = None
        for token_types in self._TWO_LETTERS_OPERATORS:
            operator = token_types[0].value
            if self._current_letter == operator[0]:
                length = 1
                if self._peek_next_letter() == operator[1]:
                    length = 2
                token_type = token_types[2 - length]
                operator = operator[0:length]
                if token_type == Token.Type.ERROR:
                    self._abort(f'Operation "{operator}" is not allowed here')
                token = self._make_token(token_type, operator)
                self._go_to(length)
                break
        return token

    def _maybe_get_string(self):
        """Try to get a token of string.

        string is any characters as UTF-8. It is surrounded with
        "" or ''.

        Returns:
            Token or NoneType: A token of string if it is existed
                               in the current position.
                               Otherwise, None is returned.

        Raises:
            LexError: When the end of quotation mark is missing,
                      it is happen.

        Note:
            When Token is returned, the current position & letter
            are progressed. Otherwise, they are kept.
        """
        # Need a quotation mark for start.
        if self._current_letter not in ('"', "'"):
            return None
        surround_mark = self._current_letter

        # Remove the above quotation mark.
        self._go_to_next_letter()
        lexeme = ''

        # Loop until reaching a quotation mark or end of string.
        while self._current_letter not in (surround_mark, '\n', self._EOS):
            # Escape sequence
            if self._current_letter == '\\':
                next_letter = self._peek_next_letter()
                # 4 hexdigits unicode
                if next_letter == 'u':
                    # No problem even if the following indexes are
                    # out of range.
                    hexdigits = self._source_code[self._current_position+2:
                                                  self._current_position+6]
                    if len(hexdigits) != 4:
                        self._abort("4 hexdigits unicode is invalid.")
                    re_obj = self._hex_pattern.fullmatch(hexdigits)
                    if re_obj is None:
                        self._abort("4 hexdigits unicode is invalid.")
                    letter = self._source_code[self._current_position:
                                               self._current_position+6]
                    lexeme += letter.encode().decode('unicode_escape')
                    self._go_to(6)
                    continue

                # Quotation mark, Reverse solidus, Solidus
                if next_letter in ('"', "'", '\\', '/'):
                    lexeme += next_letter
                    self._go_to(2)
                    continue

                # BS, Form-feed, LF, CR, Tab
                if next_letter in self._REPLACED_LETTERS:
                    lexeme += self._REPLACED_LETTERS[next_letter]
                    self._go_to(2)
                    continue

            lexeme += self._current_letter
            # Progress
            self._go_to_next_letter()

        if self._current_letter != surround_mark:
            self._abort('Missing the end of quotation mark')

        # Remove the quotation mark.
        self._go_to_next_letter()

        return self._make_token(Token.Type.STRING, lexeme)

    def _maybe_get_number(self):
        """Try to get a token of number.

        Get a token of number as the following format.
        As you can see, the head of sign (+/-) is not given in order to
        parse later.
        For example, 2, 5.7, 100.5e30, 0.8e+2, 4E-100.

        When previous token is "." and "." exists after number, this
        number is treated as int. To tell the truth, this judgement is
        too much as role of Lexer. But it is needed here.

        <number> ::= <digit>+ [ "." <digit>+ ]
            [ ( "e" | "E" ) [ "+" | "-" ] <digit>+ ]
        <digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8"
            | "9"

        Returns:
            Token or NoneType: A token of number if it is existed
                               in the current position.
                               Otherwise, None is returned.

        Raises:
            LexError: When there is no digit after decimal point,
                      it is happen.

        Note:
            When Token is returned, the current position & letter
            are progressed. Otherwise, they are kept.
        """
        start_position = self._current_position

        is_skipped = self._skip_digit()  # Check and proceed for 0-9.
        if not is_skipped:
            return None

        token_type = Token.Type.NUMBER

        if self._current_letter == '.':  # Check a decimal point.
            # For access of array/block's member with "." operator.
            # For example, the above skipped digits are 10 and the
            # current letter is 2nd dot in "foo.10.3".
            # Avoid to confuse as floating-number.
            if self._previous_token is not None \
                    and self._previous_token.type == Token.Type.DOT:
                lexeme = self._source_code[start_position:
                                           self._current_position]
                return self._make_token(token_type, lexeme)
            # Is there number after dot (decimal point)?
            if self._peek_next_letter().isdigit():
                # For floating-point number
                # For example, the above skipped digits are 10,
                # the current letter is dot, and peeked letter
                # is 3 in "10.35".
                self._go_to_next_letter()  # Skip a decimal point.
                is_skipped = self._skip_digit()  # Check and proceed for 0-9.
                if not is_skipped:
                    self._abort(
                        'Interpreter side error in Lexer#_maybe_get_number')
            else:
                # For access of array/block's member with "." operator.
                # Check the following token may be identifier.
                # Note that white spaces (includes line-break) around dot
                # are permitted, such as "foo.3. bar".
                offset = 1
                while (letter := self._get_letter(offset)) != self._EOS:
                    if letter == '_' or letter.isalpha():
                        lexeme = self._source_code[start_position:
                                                   self._current_position]
                        return self._make_token(token_type, lexeme)
                    if letter != '\n' and letter not in self._WHITE_SPACES:
                        break
                    offset += 1
                self._abort('There is no digit after decimal point')

        if self._current_letter in ('e', 'E'):  # Check a exponential mark.
            self._go_to_next_letter()  # Skip a exponential mark.
            if self._current_letter in ('+', '-'):  # Check a sign.
                self._go_to_next_letter()  # Skip a sign.
            is_skipped = self._skip_digit()  # Check and proceed for 0-9.
            if not is_skipped:
                self._abort('There is no digit after exponential mark')

        # When this line is reached, the current position goes over
        # number. In other words, the current letter is not number.
        lexeme = self._source_code[start_position:self._current_position]

        return self._make_token(token_type, lexeme)

    def _maybe_get_identifier_or_keyword(self):
        """Try to get a token of identifier/keyword.

        | Category          | 1st letter | The following letters |
        |-------------------|------------|-----------------------|
        | Alphabet [a-zA-Z] | Valid      | Valid                 |
        | Digit [0-9]       | Invalid    | Valid                 |
        | Under score "_"   | Valid      | Valid                 |
        | Others            | Invalid    | Invalid               |

        Returns:
            Token or NoneType: A token of identifier/keyword if it is
                               existed in the current position.
                               Otherwise, None is returned.

        Note:
            When Token is returned, the current position & letter
            are progressed. Otherwise, they are kept.
        """
        start_position = self._current_position
        is_processed = False
        while self._current_letter.isalpha() or self._current_letter == '_' \
                or (is_processed and self._current_letter.isdigit()):
            self._go_to_next_letter()
            is_processed = True

        if not is_processed:
            return None

        # When this line is reached, the current position goes over
        # the identifier. In other words, the current letter is not
        # identifier.
        lexeme = self._source_code[start_position:self._current_position]

        token = self._make_token(Token.Type.IDENTIFIER, lexeme)
        token.fix_keyword_type()
        return token

    def _maybe_get_terminator(self):
        """Try to get a token of terminator.

        Returns:
            Token or NoneType: A token of terminator if it is
                               existed in the current position.
                               Otherwise, None is returned.

        Note:
            When Token is returned, the current position & letter
            are progressed. Otherwise, they are kept.
        """
        if self._current_letter not in self._TERMINATORS:
            return None

        token_type = self._TERMINATORS[self._current_letter]
        token = self._make_token(token_type, self._current_letter)
        current_letter = self._current_letter
        self._go_to_next_letter()
        if current_letter == '\n':
            self._record_new_line()
        return token

    def _make_token(self, token_type, lexeme=None):
        """Make a token.

        Args:
            token_type (Token.Type): The type of token
            lexeme (str, optional): The token's actual text. It is so
                                    called "lexeme".
                                    When this is omitted or this is
                                    None, the assigned value of Token
                                    type is used instead it.

        Returns:
            Token: A token.
        """
        return Token(token_type, self._medium,
                     self._line_number, self._get_column_number(),
                     lexeme)

    def _skip_digit(self):
        """Skip digit.

        Returns:
            bool: True if digit is skipped,
                  False otherwise.
        """
        is_skipped = False
        while self._current_letter.isdigit():
            is_skipped = True
            self._go_to_next_letter()
        return is_skipped

    def _skip_white_space(self):
        """Skip white space.

        Skip whitespace except newlines, which we will use to indicate
        the end of a statement.

        Returns:
            bool: True if white spaces are skipped, False otherwise.
        """
        is_skipped = False
        while self._WHITE_SPACES.find(self._current_letter) != -1:
            self._go_to_next_letter()
            is_skipped = True
        return is_skipped

    def _skip_comment(self):
        """Skip comment in the code.

        The following comment is skipped.
        - It is constructed from "#" to the end of line.
        - It is constructed from "//" to the end of line.
        - It is constructed from "/*" to "*/". It can be over multi-line.

        Returns:
            bool: True if comment is skipped, False otherwise.

        Raises:
            LexError: When the end of "*/" is missing, it is happen.
        """
        if (self._current_letter == '/' and self._peek_next_letter() == '/') \
                or self._current_letter == '#':
            while self._current_letter != '\n':
                self._go_to_next_letter()
            return True

        if self._current_letter != '/' or self._peek_next_letter() != '*':
            return False
        self._go_to(2)
        while (self._current_letter != '*' \
               or self._peek_next_letter() != '/'):
            if self._current_letter == self._EOS:
                self._abort('Missing the the end of "*/"')
            current_letter = self._current_letter
            self._go_to_next_letter()
            if current_letter == '\n':
                self._record_new_line()
        self._go_to(2)
        return True

    def _abort(self, message):
        """Abort Lexer.

        Print an error message and raise Exception.

        Args:
            message (str): Error message

        Raises:
            LexError: This exception always happen when this method
                      is called.
        """
        raise Error.make_lex_error(message, self._medium, self._line_number,
                                   self._get_column_number(), self._config)
