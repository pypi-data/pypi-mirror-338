"""Parser for VivJson

- Parser: Constructor. Its argument is source code as string.
- Parser#parse: Parse source code and get statements.

<program> ::= [ "{" [ <nl>+ ] ]
    [ <statement> { <end> <statement> } [ <end> ] ]
    [ [ <nl>+ ] "}" ]
<block> ::= "{" [ <nl>+ ]
    [ <statement> { <end> <statement> } [ <end> ] ]
    [ <nl>+ ] "}"
<statement> ::= "break" | "continue" | <return> | <remove>
    | <expression> | <call_if> | <call_for>
    | <call_primitive> | <call_extended> | <declaration>
<return> ::= "return" [ <nl>+ ] [ "(" [ <nl>+ ] <or> [ <nl>+ ] ")" ]
<remove> ::= "remove" [ <nl>+ ] "(" [ <nl>+ ] <element> [ <nl>+ ] ")"
<declaration> ::= <callee>
<callee> ::= <modifier> [ <nl>+ ] <identifier> [ <nl>+ ]
    [ "(" [ <nl> ] [ <parameter> { <end> <parameter> } ] [ <nl> ] ")" ]
    [ <nl>+ ] <block>
<call_extended> ::= <element> [ <nl>+ ]
    [ "(" [ <nl> ] [ <argument> { <end> <argument> } ] [ <nl> ]
    [ <block> [ <nl> ] ] ")" ] [ <nl>+ ] [ <block> ]
<call_primitive> ::= <element> [ <nl>+ ]
    "(" [ <nl> ] [ <argument> { <end> <argument> } ] [ <nl> ] ")"
<call_for> ::= "for" [ <nl>+ ] "(" [ <nl> ]
    ( [ <argument_for> ] [ <end> ] [ <or> ] [ <end> ]
      [ <argument_for> ] [ <end> ] [ <block> ] )
    [ <nl> ] ")" [ <nl>+ ] [ <block> ]
<call_if> ::= "if" [ <nl>+ ] "(" [ <nl>+ ] <argument>
      [ <end> [ <nl>+ ] <block> ] [ <nl> ] ")" [ <nl>+ ] [ <block> ]
    { [ <nl>+ ] "elseif" [ <nl>+ ] "(" [ <nl>+ ] <argument>
      [ <end> [ <nl>+ ] <block> ] [ <nl> ] ")" [ <nl>+ ] [ <block> ] }
    [ [ <nl>+ ] "else" [ <nl>+ ] [ "("
      [ [ <nl>+ ] <block> ] [ <nl> ] ")" ] [ <nl>+ ] [ <block> ] ]
<parameter> ::= [ <modifier> [ <nl>+ ] ] <identifier>
<argument> ::= <or>
<argument_for> ::= <assignment> | <call_primitive> | <call_extended>
<expression> ::= <assignment> | <result>
<result> ::= ":=" [ <nl>+ ] <or>
<assignment> ::= <element> [ <nl>+ ]
    ( "=" | ":" | "+=" | "-=" | "*=" | "/=" | "%=" ) [ <nl>+ ] <or>
<group> :: = "(" [ <nl>+ ] <or> [ <nl>+ ] ")"
<or> ::= <and> { [ <nl>+ ] "or" [ <nl>+ ] <and> }
<and> ::= <equality> { [ <nl>+ ] "and" [ <nl>+ ] <equality> }
<equality> ::= <comparison>
    { [ <nl>+ ] ( "==" | "!=" | "in" ) [ <nl>+ ] <comparison> }
<comparison> ::= <term>
    { [ <nl>+ ] ( "<" | "<=" | ">" | ">=" ) [ <nl>+ ] <term> }
<term> ::= <factor> { [ <nl>+ ] ( "+" | "-" ) [ <nl>+ ] <factor> }
<factor> ::= <thing>
    { [ <nl>+ ] ( "*" | "/" | "%" ) [ <nl>+ ] <thing> }
<thing> ::= <unary> | <array> | <block>
<unary> ::= [ "+" | "-" | "not" ] ( <primary> | <element>
    | <call_extended> | <call_if> | <call_for> )
<element> ::=
    ( ( <identifier> | <call_primitive> )
      {
        ( [ <nl>+ ] "." [ <nl>+ ]
            ( <identifier> | <call_primitive> |
              ( [ "+" | "-" ] <digit>+ ) ) )
        | ( "[" [ <nl>+ ] <term> [ <nl>+ ] "]" )
      }
    )
<array> :: = "[" [ <nl> ] 
      [ <argument> { <end> <argument> } [ <end> ] ] [ <nl> ]
    "]"
<primary> ::= <number> | <string> | <boolean> | "null" | <group>
<modifier> ::= "function" | "reference"
<identifier> ::= ( "_" | <alphabet> ) { "_" | <alphabet> | <digit> }
<boolean> ::= "true" | "false"
<number> ::= <digit>+ [ "." <digit>+ ]
    [ ( "e" | "E" ) ( "+" | "-" ) <digit>+ ]
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<alphabet> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H"
    | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q"
    | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
    | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h"
    | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q"
    | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
<end> ::= <nl> | ";" | ","
<nl> ::= "\n"

<string> is any characters as UTF-8. It is surrounded with "" or ''.

[]: 0 or 1 time (? is not used here. But it has same meaning.)
{}: 0 or more times (* is not used here. But it has same meaning.)
+: 1 or more times
(): group
|: or

"." is allowed as the right-hand sided operand of "in".

Refer to:
- "Let's make a Teeny Tiny compiler"
  https://austinhenley.com/blog/teenytinycompiler2.html
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
__date__ = '2025-04-04'

# pylint: disable=C0302, R0903

from .config import Config
from .error import Error
from .lexer import Lexer
from .statement import Literal, Identifier, Keyword, Blank, \
                       Array, Block, Binary, Parameter, \
                       Callee, Call, Get, Set, Remove, Return
from .tokens import Token

class Parser:  # pylint: disable=R0902
    """Parser class

    Attributes:
        _config (Config or NoneType): Configuration
        _is_enable_only_json (bool): When true is given, the given data
                                     is parsed as JSON.
                                     In other words, script is
                                     disabled.
        _lexer (Lexer): An instance of Lexer
        _make_statement_methods (tuple): Methods of making statement.
        _make_unary_methods (tuple): Methods of making unary.
        _make_for_argument_methods (tuple): Methods of making for-loop
                                            argument.
        _tokens (list): Tokens of the current statement.
        _index (int): The current index of the above list "_tokens".
        _is_implicit_assign (bool): When the given source code is not
                                    JSON object (a.k.a. map, hash,
                                    dictionary), this is True.
                                    The default is False.
    """
    def __init__(self, source_code, medium=None, config=None):
        """Initialize class.

        Args:
            source_code (str): Source code as text
            medium (str, optional): The object that has source code.
                                    It is used to report error.
            config (Config, optional): Configuration if needed.
        """
        self._config = config
        self._is_enable_only_json = Config.get_enable_only_json_alt(config)
        self._lexer = Lexer(source_code, medium, config)

        self._make_statement_methods = (
            self._make_return,
            self._make_remove,
            self._make_expression,
            self._make_call_if,
            self._make_call_for,
            self._make_call_extended,
            self._make_call_primitive,
            self._make_declaration
        )
        self._make_unary_methods = (
            self._make_call_for,
            self._make_call_if,
            self._make_call_extended,
            self._make_element,
            self._make_primary
        )
        self._make_for_argument_methods = (
            self._make_block,
            self._make_argument_for,
            self._make_or
        )

        # Initialize tokens.
        self._tokens = []
        self._index = 0
        self._is_implicit_assign = False

    def parse(self):
        """Parse source code and get statements that construct it.

        - Parse VivJson and JSON object (with/without bracket).
        - Parse directly represented value of JSON.

        Returns:
            list[Statement]: <program>

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        # Parse VivJson and JSON object (with/without bracket).
        statements = self._make_program()
        if isinstance(statements, Block):
            return statements.values

        # Parse directly represented value of JSON.
        # It will be an assignment of implicit variable '_'
        return self._parse_directly_represented()

    def _parse_directly_represented(self):
        """Parse directly represented value of JSON.
   
        Target value is number, string, boolean, array, or null.
        The given value is assigned into a implicit variable '_'.
        When some values are given, the value of implicit variable '_'
        is represented as array.
        For example,
          - 3 --> _ = 3
          - [2, 1]; 3 --> _ = [[2, 1], 3]

        Returns:
            list[Statement]: <program>

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        self._is_implicit_assign = True

        arguments = []
        while self._get_token_type() != Token.Type.EOS: # pylint: disable=R1702
            while self._skip_end() is not None:  # Skip <end>+
                pass
            if self._get_token_type() == Token.Type.EOS:
                break

            if self._is_enable_only_json:
                argument = self._make_thing()
                if argument is not None:
                    arguments.append(argument)
                    continue
            else:
                argument = self._make_argument()
                if argument is not None:
                    if isinstance(argument, Get):
                        if len(argument.members) == 1:
                            statement = argument.members[0]
                            if isinstance(statement, Identifier):
                                identifier = statement.name
                                if not self._is_infinity_or_nan(identifier):
                                    string = Token(Token.Type.STRING,
                                                identifier.medium,
                                                identifier.line_number,
                                                identifier.column_number,
                                                identifier.lexeme)
                                    arguments.append(Literal(string))
                                    continue

                    arguments.append(argument)
                    continue

            token_info = self._get_token().to_string(omit_type_name=True)
            self._abort(f'{token_info} is invalid statement/value.')
        if len(arguments) == 0:
            self._abort('No effective statement/value')

        identifier = Identifier(Token(Token.Type.IDENTIFIER, lexeme='_'))
        value = Array(arguments) if len(arguments) > 1 else arguments[0]
        return [Set([identifier], Token(Token.Type.SET), value)]

    def _make_program(self):
        """Make <program>.

        Parse <program> into <statement>.

        <program> ::= [ "{" [ <nl>+ ] ]
            [ <statement> { <end> <statement> } [ <end> ] ]
            [ [ <nl>+ ] "}" ]

        Returns:
            Block or NoneType: <program> as Block if it is obtained,
                               None otherwise.
                               Block is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_block(is_bracket_essential=False, is_consumed=True)

    def _make_block(self, is_bracket_essential=True, is_consumed=False,
                    function_type=Block.ANONYMOUS_FUNCTION):
        """Make <block>.

        <block> ::= "{" [ <nl>+ ]
            [ <statement> { <end> <statement> } [ <end> ] ]
            [ <nl>+ ] "}"

        Args:
            is_bracket_essential (bool, optional): True if left/right
                                    curly brackets are essential.
                                    The default is True.
            is_consumed (bool, optional): When this is True and
                    a statement is constructed, its token are consumed.
                    The default is False.
            function_type (str, optional): Function type of Block
                                  - Block.ANONYMOUS_FUNCTION (default)
                                  - Block.PURE_FUNCTION
                                  - Block.LIMITED_FUNCTION

        Returns:
            Block or NoneType: <block> as Block if it is obtained,
                               None otherwise.
                               Block is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        end_of_block = Token.Type.EOS
        left_bracket = self._match(Token.Type.LEFT_CURLY_BRACKET)  # "{"
        if left_bracket is None:
            if is_bracket_essential:
                return None
        else:
            self._go_to_next_token()
            self._skip_new_lines()  # [ <nl>+ ]
            end_of_block = Token.Type.RIGHT_CURLY_BRACKET  # "}"

        statements = []
        while self._get_token_type() != end_of_block:
            count = len(statements)

            statement = self._make_assignment() if self._is_enable_only_json \
                        else self._make_statement()
            if statement is not None:
                statements.append(statement)

            # <end>s are translated to blank lines.
            # <nl>+ in front of "}" are treated here. Because <end>
            # includes <nl>.
            is_just_behind = statement is not None
            while (token := self._skip_end()) is not None:
                if not is_just_behind:
                    statements.append(Blank(token))
                is_just_behind = False

            # Abort when the effective statement is not found here.
            # However, when the effective statement is completely nothing,
            # we try to assign to implicit variable.
            if count == len(statements):
                if count == 0 and is_consumed \
                        and not self._is_implicit_assign:
                    return None
                token_info = self._get_token().to_string(omit_type_name=True)
                self._abort(f'{token_info} is unexpected.')

            if is_consumed:
                self._consume_token() # Consume Tokens of the above statement.

        if end_of_block == Token.Type.RIGHT_CURLY_BRACKET:
            self._go_to_next_token()

        return Block(statements, function_type)

    def _make_statement(self):
        """Make <statement>.

        <statement> ::= "break" | "continue" | <return> | <remove>
            | <expression> | <call_if> | <call_for>
            | <call_primitive> | <call_extended> | <declaration>

        Returns:
            Statement or NoneType: <statement> if it is obtained,
                                   None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        token = self._match(Token.Type.BREAK, Token.Type.CONTINUE)
        if token is not None:
            self._go_to_next_token()
            return Keyword(token)

        for method in self._make_statement_methods:
            statement = method()
            if statement is not None:
                return statement
        return None

    def _make_return(self):
        """Make <return>.

        <return> ::=
            "return" [ <nl>+ ] [ "(" [ <nl>+ ] <or> [ <nl>+ ] ")" ]

        Returns:
            Return or NoneType: <return> as Return if it is
                                obtained, None otherwise.
                                Return is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        token = self._match(Token.Type.RETURN)
        if token is None:
            return None
        self._go_to_next_token()

        maybe_restored_index = self._index  # #1

        self._skip_new_lines()  # [ <nl>+ ]

        parenthesis = self._match(Token.Type.LEFT_PARENTHESIS)  # "("
        if parenthesis is None:
            self._index = maybe_restored_index  # Restore #1
            return Return(token, None)
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        value = self._make_or()
        if value is None:
            token_info = parenthesis.to_string(omit_type_name=True)
            self._abort(f'No returned value after {token_info}')

        self._skip_new_lines()  # [ <nl>+ ]

        parenthesis = self._match(Token.Type.RIGHT_PARENTHESIS)  # ")"
        if parenthesis is None:
            token_info = self._get_token().to_string(omit_type_name=True)
            self._abort(f'{token_info} is unexpected.')
        self._go_to_next_token()

        return Return(token, value)

    def _make_remove(self):
        """Make <remove>.

        <remove> ::=
            "remove" [ <nl>+ ] "(" [ <nl>+ ] <element> [ <nl>+ ] ")"

        Returns:
            Remove or NoneType: <remove> as Remove if it is obtained,
                                None otherwise.
                                Remove is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        token = self._match(Token.Type.REMOVE)
        if token is None:
            return None
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        parenthesis = self._match(Token.Type.LEFT_PARENTHESIS)  # "("
        if parenthesis is None:
            token_info = self._get_token().to_string(omit_type_name=True)
            self._abort(f'{token_info} is unexpected.')
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        element = \
            self._make_element(except_call_primitive=True)  # <element>
        if element is None:
            token_info = parenthesis.to_string(omit_type_name=True)
            self._abort(f'No variable after {token_info}')

        self._skip_new_lines()  # [ <nl>+ ]

        parenthesis = self._match(Token.Type.RIGHT_PARENTHESIS)  # ")"
        if parenthesis is None:
            token_info = self._get_token().to_string(omit_type_name=True)
            self._abort(f'{token_info} is unexpected.')
        self._go_to_next_token()

        return Remove(token, element.members)

    def _make_declaration(self):
        """Make <declaration>.

        <declaration> ::= <callee>

        Returns:
            Callee or NoneType: <declaration> as Callee if it is
                                obtained, None otherwise.
                                Callee is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_callee()

    def _make_callee(self):
        """Make <callee>.

        <callee> ::= <modifier> [ <nl>+ ] <identifier> [ <nl>+ ]
            [ "(" [ <nl> ] [ <parameter> { <end> <parameter> } ]
            [ <nl> ] ")" ] [ <nl>+ ] <block>

        Returns:
            Callee or NoneType: <callee> as Callee if it is
                                obtained, None otherwise.
                                Callee is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        maybe_restored_index = self._index  # #1

        # <modifier> [ <nl>+ ] <identifier>
        statement = self._make_parameter(is_modifier_essential=True)
        if statement is None:
            return None

        self._skip_new_lines()  # [ <nl>+ ]

        parameters = self._make_array(Token.Type.LEFT_PARENTHESIS,
                                      Token.Type.RIGHT_PARENTHESIS,
                                      is_parameter=True)
        if parameters is None:
            parameters = Array([])

        self._skip_new_lines()  # [ <nl>+ ]

        block = self._make_block(function_type=Block.PURE_FUNCTION)
        if block is None:
            self._index = maybe_restored_index  # Restore #1
            return None
        parameters.values.append(block)  # It is permitted though frozen=True.

        return Callee(statement, parameters)

    def _make_call_extended(self):
        """Make <call_extended>.

        Returns:
            Call or NoneType: <call_extended> as Call if it is
                              obtained, None otherwise.
                              Call is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_call(is_extended=True)

    def _make_call_primitive(self):
        """Make <call_primitive>.

        Returns:
            Call or NoneType: <call_primitive> as Call if it is
                              obtained, None otherwise.
                              Call is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_call()

    def _make_call(self,  # pylint: disable=R0911
                   is_extended=False, is_keyword=False,
                   function_type=Block.ANONYMOUS_FUNCTION):
        """Make <call_primitive> or <call_extended>.

        <call_primitive> ::= <element> [ <nl>+ ]
            "(" [ <nl> ] [ <argument> { <end> <argument> } ]
                [ <nl> ] ")"

        <call_extended> ::= <element> [ <nl>+ ]
            [ "(" [ <nl> ] [ <argument> { <end> <argument> } ]
                  [ <nl> ] [ <block> [ <nl> ] ] ")" ]
            [ <nl>+ ] [ <block> ]

        Args:
            is_extended (bool, optional): True for <call_extended>,
                                          False for <call_primitive>.
                                          The default is False.
            is_keyword (bool, optional): True if function name's token
                                         type is Keyword,
                                         False otherwise.
                                         The default is False.
            function_type (str, optional): Function type of Block
                                  - Block.ANONYMOUS_FUNCTION (default)
                                  - Block.PURE_FUNCTION
                                  - Block.LIMITED_FUNCTION

        Returns:
            Call or NoneType: <call_primitive> as Call or
                              <call_extended> as Call if it is
                              obtained, None otherwise.
                              Call is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        maybe_restored_index = self._index  # #1
        element = None
        if is_keyword:
            element = Identifier(self._get_token())
            self._go_to_next_token()
        else:
            element = \
                self._make_element(except_call_primitive=True)  # <element>
            if element is None:
                return None

        self._skip_new_lines()  # [ <nl>+ ]

        arguments = self._make_array(Token.Type.LEFT_PARENTHESIS,
                                     Token.Type.RIGHT_PARENTHESIS)

        # <call_primitive>
        if not is_extended:
            if arguments is None:
                self._index = maybe_restored_index  # Restore #1
                return None
            return Call(element, arguments)

        # <call_extended>
        self._skip_new_lines()  # [ <nl>+ ]
        block = self._make_block(function_type=function_type)
        if block is None:
            if not isinstance(arguments, Array) \
                    or len(arguments.values) == 0 \
                    or not isinstance(arguments.values[-1], Block):
                self._index = maybe_restored_index  # Restore #1
                return None
            arguments.values[-1] = \
                Block(arguments.values[-1].values, function_type)
            return Call(element, arguments)
        if isinstance(arguments, Array):
            arguments.values.append(block)  # It is permitted though
                                            # frozen=True.
            return Call(element, arguments)
        return Call(element, Array([block]))

    def _make_call_for(self):  # pylint: disable=R0912, R0915
        """Make <call_for>.

        <call_for> ::= "for" [ <nl>+ ] "(" [ <nl> ]
            ( [ <argument_for> ] [ <end> ] [ <or> ] [ <end> ]
              [<argument_for> ] [ <end> ] [ <block> ] )
            [ <nl> ] ")" [ <nl>+ ] [ <block> ]

        Returns:
            Call or NoneType: <call_for> as Call if it is obtained,
                              None otherwise.
                              Call is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        call_for = self._match(Token.Type.FOR)  # "for"
        if call_for is None:
            return None
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        bracket = self._match(Token.Type.LEFT_PARENTHESIS)  # "("
        if bracket is None:
            token_info = call_for.to_string(omit_type_name=True)
            self._abort(f'There is no parenthesis after {token_info}.')
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        arguments = []
        flag = 0

        for _ in range(5):
            statement = None
            for method in self._make_for_argument_methods:
                statement = method()
                if statement is not None:
                    arguments.append(statement)
                    break
            end = self._skip_end()  # <end>
            if statement is None:
                if end is not None:
                    arguments.append(Blank(end))
                else:
                    bracket = self._match(Token.Type.RIGHT_PARENTHESIS)  # ")"
                    if bracket is not None:
                        self._go_to_next_token()
                        arguments.append(None)
                        flag |= 1
            elif isinstance(statement, Block):
                flag |= 2
            if flag == 3:
                break

        if len(arguments) < 2:
            token_info = call_for.to_string(omit_type_name=True)
            self._abort(f'There is no operation of {token_info}.' \
                        if len(arguments) < 1 or arguments[0] is None else \
                        f'There is no right parenthesis of {token_info}.')

        block = arguments.pop()
        parenthesis = arguments.pop()
        if block is None and isinstance(parenthesis, Block):
            block = parenthesis
        elif not isinstance(block, Block) or parenthesis is not None:
            token_info = call_for.to_string(omit_type_name=True)
            self._abort(f'Invalid argument in {token_info}')

        length = len(arguments)  # Number of arguments that does not contain
                                 # operations (block).
        if length == 0:  # for () { operation }
            blank = Blank(Token(Token.Type.SEMICOLON))
            arguments = [
                blank,
                Literal(Token(Token.Type.TRUE)),
                blank,
                block
            ]
        elif length == 1:
            if isinstance(arguments[0], Binary) \
                    and arguments[0].operator.type == Token.Type.IN:
                # for (variable in list) { operation }
                variable = arguments[0].left
                if isinstance(variable, Get) and len(variable.members) == 1:
                    variable = variable.members[0]
                if not isinstance(variable, Identifier):
                    token_info = call_for.to_string(omit_type_name=True)
                    self._abort(f'Invalid argument in {token_info}')
                arguments = [
                    Binary(variable, arguments[0].operator,
                           arguments[0].right),
                    block
                ]
            else:  # for (initial) { operation }
                arguments = [
                    arguments[0],
                    Literal(Token(Token.Type.TRUE)),
                    Blank(Token(Token.Type.SEMICOLON)),
                    block
                ]
        elif length == 2:  # for (initial; condition) { operation }
            arguments = [
                arguments[0],
                arguments[1] if not isinstance(arguments[1], Blank) \
                    else Literal(Token(Token.Type.TRUE)),
                Blank(Token(Token.Type.SEMICOLON)),
                block
            ]
        elif length == 3:  # for (initial; condition; update) { operation }
            if isinstance(arguments[1], Blank):
                arguments[1] = Literal(Token(Token.Type.TRUE))
            arguments.append(block)
        else:
            token_info = call_for.to_string(omit_type_name=True)
            self._abort(f'Invalid argument in {token_info}')

        return Call(Identifier(call_for), Array(arguments))

    def _make_call_if(self):
        """Make <call_if>.

        <call_if> ::= "if" [ <nl>+ ] "(" [ <nl>+ ] <argument>
                         [ <end> [ <nl>+ ] <block> ] [ <nl> ] ")"
            [ <nl>+ ][ <block> ]
        { [ <nl>+ ] "elseif" [ <nl>+ ] "(" [ <nl>+ ] <argument>
                         [ <end> [ <nl>+ ] <block> ] [ <nl> ] ")"
            [ <nl>+ ][ <block> ] }
        [ [ <nl>+ ] "else" [ <nl>+ ] [ "("
                         [ [ <nl>+ ] <block> ] [ <nl> ] ")" ]
            [ <nl>+ ] [ <block> ] ]

        Returns:
            Call or NoneType: <call_if> as Call if it is obtained,
                              None otherwise.
                              Call is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        # if
        token = self._match(Token.Type.IF)
        if token is None:
            return None
        condition, block = \
            self._make_call_condition_and_operations(Token.Type.IF)
        if condition is None or block is None:
            return None
        arguments = [condition, block]

        # elseif
        while True:
            self._skip_new_lines()  # [ <nl>+ ]
            condition, block = \
                self._make_call_condition_and_operations(Token.Type.ELSEIF)
            if condition is None or block is None:
                break
            arguments.append(condition)
            arguments.append(block)

        # else
        self._skip_new_lines()  # [ <nl>+ ]
        condition, block = \
            self._make_call_condition_and_operations(Token.Type.ELSE)
        if block is not None:
            arguments.append(Literal(Token(Token.Type.TRUE)))
            arguments.append(block)

        return Call(Identifier(token), Array(arguments))

    def _make_call_condition_and_operations(self, name: Token.Type):
        """Make [(condition)] {operations}.

        - if/elseif (condition) {operations}
        - else {operations}

        Args:
            name (Token.Type): Function name as Token.Type
                               - Token.Type.IF
                               - Token.Type.ELSEIF
                               - Token.Type.ELSE

        Returns:
            Statement or NoneType, Block or NoneType: Condition and
                            Operations if they are obtained.
                            None and None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        token = self._match(name)
        if token is None:
            return None, None

        length = 1 if name == Token.Type.ELSE else 2

        call = self._make_call(is_extended=True, is_keyword=True,
                               function_type= Block.LIMITED_FUNCTION)
        # pylint: disable=E1101
        if not isinstance(call, Call) \
                or not isinstance(call.name, Identifier) \
                or call.name.name.type != name \
                or len(call.arguments.values) < length \
                or not isinstance(call.arguments.values[-1], Block):
            token_info = token.to_string(omit_type_name=True)
            self._abort(f'{token_info} is invalid.')

        arguments = []
        for statement in call.arguments.values:
            if isinstance(statement, Blank):
                continue

            if len(arguments) < length:
                arguments.append(statement)
            else:
                arguments = []  # It indicates error.
                break

        if len(arguments) != length or not isinstance(arguments[-1], Block):
            token_info = token.to_string(omit_type_name=True)
            self._abort(f'{token_info} is invalid.')
        if length == 1:
            return None, arguments[0]
        return arguments[0], arguments[1]

    def _make_parameter(self, is_modifier_essential=False):
        """Make <parameter>.

        <parameter> ::= [ <modifier> [ <nl>+ ] ] <identifier>
        <modifier> ::= "function" | "reference"

        Args:
            is_modifier_essential (bool, optional): True if <modifier>
                                                    is essential.

        Returns:
            Parameter or NoneType: <parameter> as Parameter if it is
                                    obtained, None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        maybe_restored_index = self._index  # #1
        modifier = self._match( # Token.Type.CLASS,
                               Token.Type.FUNCTION,
                               Token.Type.REFERENCE)
        if modifier is None:
            if is_modifier_essential:
                return None
        else:
            self._go_to_next_token()
            self._skip_new_lines()  # [ <nl>+ ]

        identifier = self._match(Token.Type.IDENTIFIER)
        if identifier is None:
            if modifier is not None:
                token_info = modifier.to_string(omit_type_name=True)
                self._abort(f'Unexpected statement after {token_info}')
            self._index = maybe_restored_index  # Restore #1
            return None
        self._go_to_next_token()

        return Parameter(modifier, Identifier(identifier))

    def _make_argument(self):
        """Make <argument>.

        <argument> ::= <or>

        Returns:
            Statement or NoneType: <or> if it is obtained,
                                   None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_or()

    def _make_argument_for(self):
        """Make <argument_for>.

        <argument_for> ::= <assignment> | <call_primitive>
            | <call_extended>

        Returns:
            Statement or NoneType: <argument_for> if it is obtained,
                                   None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        statement = self._make_assignment()
        if statement is None:
            statement = self._make_call_primitive()
            if statement is None:
                statement = self._make_call_extended()
        return statement

    def _make_expression(self):
        """Make <expression>.

        <expression> ::= <assignment> | <result>

        Returns:
            Statement or NoneType: <expression> if it is obtained,
                                   None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        statement = self._make_assignment()
        if statement is None:
            statement = self._make_result()
        return statement

    def _make_assignment(self):
        """Make <assignment>.

        <assignment> ::= <element> [ <nl>+ ]
            ( "=" | ":" | "+=" | "-=" | "*=" | "/=" | "%=" ) [ <nl>+ ]
            <or>

        Returns:
            Set or NoneType: <assignment> if it is obtained,
                             None otherwise.
                             Set is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        maybe_restored_index = self._index  # #1

        element = None
        if not self._is_enable_only_json:
            element = self._make_element()
            if element is not None:
                # _make_element method returns an instance of Get data
                # class.
                # But this method makes an instance of Set data class.
                # Therefore, it is extracted.
                element = element.members

        if element is None:
            # Allow string that is surrounded with quotation marks,
            # such as {'key': 100}.
            token = self._match(Token.Type.IDENTIFIER, Token.Type.STRING) \
                    if self._is_enable_only_json \
                    else self._match(Token.Type.STRING)
            if token is None:
                return None
            token.type = Token.Type.IDENTIFIER
            element = [Identifier(token)]
            self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        operator = self._match(Token.Type.SET) if self._is_enable_only_json \
                   else self._match(
                    Token.Type.ASSIGN, Token.Type.SET,
                    Token.Type.PLUS_ASSIGN, Token.Type.MINUS_ASSIGN,
                    Token.Type.MULTIPLY_ASSIGN, Token.Type.DIVIDE_ASSIGN,
                    Token.Type.MODULO_ASSIGN)
        if operator is None:
            self._index = maybe_restored_index  # Restore #1
            return None
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        argument = self._make_thing() if self._is_enable_only_json \
                   else self._make_or()  # <thing> or <or>
        if argument is None:
            self._index = maybe_restored_index  # Restore #1
            return None

        return Set(element, operator, argument)

    def _make_result(self):
        """Make <result>.

        <result> ::= ":=" [ <nl>+ ] <or>

        Returns:
            Set or NoneType: <result> as Set if it is obtained,
                             None otherwise.
                             Set is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        maybe_restored_index = self._index  # #1
        operator = self._match(Token.Type.RESULT)  # ":="
        if operator is None:
            return None
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        argument = self._make_or()  # <or>
        if argument is None:
            self._index = maybe_restored_index  # Restore #1
            return None

        return Set([], operator, argument)

    def _make_group(self):
        """Make <group>.

        <group> :: = "(" [ <nl>+ ] <or> [ <nl>+ ] ")"

        Returns:
            Statement or NoneType: <or> or <group> if it is obtained,
                                   None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        maybe_restored_index = self._index  # #1
        token = self._match(Token.Type.LEFT_PARENTHESIS)  # "("
        if token is None:
            return None
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        statement = self._make_or()  # <or>
        if statement is None:
            token_info = token.to_string(omit_type_name=True)
            self._abort(f'Bad statement after {token_info}')

        self._skip_new_lines()  # [ <nl>+ ]

        token = self._match(Token.Type.RIGHT_PARENTHESIS)  # ")"
        if token is None:
            self._index = maybe_restored_index  # Restore #1
            return None
        self._go_to_next_token()

        return statement

    def _make_or(self):
        """Make <or>.

        <or> ::= <and> { [ <nl>+ ] "or" [ <nl>+ ] <and> }

        Returns:
            Statement or NoneType: <and> or <or> if it is obtained,
                                   None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_binary(Token.Type.OR, self._make_and)

    def _make_and(self):
        """Make <and>.

        <and> ::= <equality> { [ <nl>+ ] "and" [ <nl>+ ] <equality> }

        Returns:
            Statement or NoneType: <equality> or <and> if it is
                                   obtained, None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_binary(Token.Type.AND, self._make_equality)

    def _make_equality(self):
        """Make <equality>.

        <equality> ::= <comparison>
            { [ <nl>+ ] ( "==" | "!=" | "in" ) [ <nl>+ ] <comparison> }

        Returns:
            Statement or NoneType: <comparison> or <equality> if it is
                                   obtained, None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_binary(
                    (Token.Type.EQ, Token.Type.NE, Token.Type.IN),
                    self._make_comparison)

    def _make_comparison(self):
        """Make <comparison>.

        <comparison> ::= <term>
            { [ <nl>+ ] ( "<" | "<=" | ">" | ">=" ) [ <nl>+ ] <term> }

        Returns:
            Statement or NoneType: <term> or <comparison> as Binary
                                   if it is obtained, None
                                   otherwise.
                                   Binary is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_binary(
            (Token.Type.LT, Token.Type.LE, Token.Type.GT, Token.Type.GE),
            self._make_term)

    def _make_term(self):
        """Make <term>.

        <term> ::=
            <factor> { [ <nl>+ ] ( "+" | "-" ) [ <nl>+ ] <factor> }

        Returns:
            Statement or NoneType: <factor> or <term> as Binary if it
                                   is obtained, None otherwise.
                                   Binary is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_binary((Token.Type.PLUS, Token.Type.MINUS),
                                 self._make_factor)

    def _make_factor(self):
        """Make <factor>.

        <factor> ::=
            <thing> { [ <nl>+ ] ( "*" | "/" | "%" ) [ <nl>+ ] <thing> }

        Returns:
            Statement or NoneType: <thing> or <factor> as Binary if it
                                   is obtained, None otherwise.
                                   Binary is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        return self._make_binary(
            (Token.Type.MULTIPLY, Token.Type.DIVIDE, Token.Type.MODULO),
            self._make_thing)

    def _make_thing(self):
        """Make <thing>.

        <thing> ::= <unary> | <array> | <block>

        Returns:
            Statement or NoneType: <unary> or <array> or <block> if it
                                   is obtained, None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        statement = self._make_unary()
        if statement is None:
            statement = self._make_array()
            if statement is None:
                statement = self._make_block()
        return statement

    def _make_binary(self, operator_tokens, *method_for_making_statement):
        """Make binary.

        binary ::= <statement> 
            { [ <nl>+ ] <operator> [ <nl>+ ] <statement> }

        Args:
            operator_tokens (tuple): Tokens of operator
            method_for_making_statement (function): Method for making
                    sub class of Statement.
                    When 2 methods are given, 1st method is used for
                    left side and other is used for right side.
                    When only 1 method is given, it is used for both
                    sides.

        Returns:
            Statement or NoneType: <statement> or Binary if it is
                                   obtained, None otherwise.
                                   Binary is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        statement = method_for_making_statement[0]()  # <statement>
        if statement is None:
            return None

        while True:  # {}
            maybe_restored_index = self._index  # #1

            self._skip_new_lines()  # [ <nl>+ ]

            operator = self._match(operator_tokens)  # <operator>
            if operator is None:
                break
            self._go_to_next_token()

            self._skip_new_lines()  # [ <nl>+ ]

            right = method_for_making_statement[-1]()  # <statement>
            if right is None:
                if operator.type == Token.Type.IN:
                    dot = self._match(Token.Type.DOT)
                    if dot is not None:
                        dot.type = Token.Type.IDENTIFIER
                        right = Identifier(dot)
                        self._go_to_next_token()
                if right is None:
                    token_info = operator.to_string(omit_type_name=True)
                    self._abort(f'Bad statement after {token_info}')

            statement = Binary(statement, operator, right)

        self._index = maybe_restored_index  # Restore #1
        return statement

    def _make_unary(self):
        """Make <unary>.

        <unary> ::= [ "+" | "-" | "not" ] ( <primary> | <element>
            | <call_extended> | <call_if> | <call_for> )

        Returns:
            Statement or NoneType: <primary>, <element>,
                                   <call_extended>, <call_if>,
                                   <call_for>, or <unary> if it is
                                   obtained,
                                   None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        maybe_restored_index = self._index  # #1
        prefix = self._match(Token.Type.PLUS, Token.Type.MINUS) \
                 if self._is_enable_only_json \
                 else self._match(Token.Type.PLUS, Token.Type.MINUS,
                                  Token.Type.NOT)
        if prefix is not None:
            self._go_to_next_token()

        statement = None
        if self._is_enable_only_json:
            statement = self._make_primary()
        else:
            for method in self._make_unary_methods:
                statement = method()
                if statement is not None:
                    break
        if statement is None:
            self._index = maybe_restored_index  # Restore #1
            return None

        if prefix is None or prefix.type == Token.Type.PLUS:
            return statement
        if prefix.type == Token.Type.MINUS:
            return Binary(Literal(Token(Token.Type.NUMBER,
                                        medium=prefix.medium,
                                        line_number=prefix.line_number,
                                        column_number=prefix.column_number,
                                        lexeme='-1')),
                          Token(Token.Type.MULTIPLY), statement)
        return Binary(Literal(Token(Token.Type.NULL)), prefix, statement)

    def _make_element(self, except_call_primitive=False):
        """Make <element>.

        <element> ::=
        ( ( <identifier> | <call_primitive> )
          {
            ( [ <nl>+ ] "." [ <nl>+ ]
                ( <identifier> | <call_primitive> | <digit>+ ) )
            | ( "[" [ <nl>+ ] <unary> [ <nl>+ ] "]" )
          }
        )

        Args:
            except_call_primitive (bool, optional): True if
                                    <call_primitive> is not allowed.
                                    The default is False.

        Returns:
            Get or NoneType: <element> as Get if it is obtained,
                             None otherwise.
                             Get is sub class of Statement

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        # <identifier> | <call_primitive>
        member = None if except_call_primitive \
                    else self._make_call_primitive()  # <call_primitive>
        if member is None:
            token = self._match(Token.Type.IDENTIFIER)
            if token is None:
                return None
            member = Identifier(token)  # <identifier>
            self._go_to_next_token()

        members = [member]

        while True:  # {}
            maybe_restored_index = self._index  # #1

            # "[" [ <nl>+ ] <term> [ <nl>+ ] "]"
            member = self._make_member_with_bracket()
            if member is not None:
                members.append(member)
                continue

            # [ <nl>+ ] "." [ <nl>+ ]
            # ( <identifier> | <call_primitive> | ( [ "+" | "-" ] <digit>+ ) )
            member = self._make_member_with_dot()
            if member is not None:
                members.append(member[0])
                if member[1] is not None:
                    members.append(member[1])
                continue

            self._index = maybe_restored_index  # Restore #1
            break

        return Get(members)

    def _make_member_with_bracket(self):
        """Make bracket member, such as *[a], *[3].

        "[" [ <nl>+ ] <term> [ <nl>+ ] "]"

        Returns:
            Statement or NoneType: <unary> if it is obtained,
                                   None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        bracket = self._match(Token.Type.LEFT_SQUARE_BRACKET)  # "["
        if bracket is None:
            return None
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        member = self._make_term()  # <term>
        if member is None:
            token_info = bracket.to_string(omit_type_name=True)
            self._abort(f'Unexpected statement after {token_info}.')

        self._skip_new_lines()  # [ <nl>+ ]

        bracket = self._match(Token.Type.RIGHT_SQUARE_BRACKET)  # "]"
        if bracket is None:
            token_info = self._get_token().to_string(omit_type_name=True)
            self._abort(f'{token_info} is unexpected.')
        self._go_to_next_token()
        return member

    def _make_member_with_dot(self):
        """Make dot member, such as *.a, *.3, *.func().

        [ <nl>+ ] "." [ <nl>+ ]
        ( <identifier> | <call_primitive> |
            ( [ "+" | "-" ] <digit>+ )
        )

        The returned value is a list that has 2 statements.
        However 2nd statement is null mostly. 2nd statement becomes
        valid statement if it seems that they are floating-point
        number.
        There are some example in the following table. To tell the
        truth, in the last item "f.0.2", 0.2 is entered in a Token
        that is created by Lexer. Thus, this parsing is needed.

        | Target value                 | Expression | 1st | 2nd  |
        |------------------------------|------------|-----|------|
        | {"a": {"x": 3}}              | a.x        | "x" | null |
        | {"b": [7, 8, 9]}             | b.0        |  0  | null |
        | {"c": [10, [50, 70]]}        | c.1.0      |  1  |  0   |
        | {"d": {"2": {"6": 100}}}     | d.2.6      |  2  |  6   |
        | {"e": {"3": [1000, 2000]}}   | e.3.1      |  3  |  1   |
        | {"f": [{"2": 10000}, 20000]} | f.0.2      |  0  |  2   |

        Returns:
            list[Statement] or NoneType: <identifier>,
                                         <call_primitive>, or
                                         <digit>+ if it is obtained,
                                         None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        self._skip_new_lines()  # [ <nl>+ ]

        dot = self._match(Token.Type.DOT)
        if dot is None:
            return None
        self._go_to_next_token()

        self._skip_new_lines()  # [ <nl>+ ]

        member = self._make_call_primitive()  # <call_primitive>
        additional_member = None
        if member is None:
            token = self._match(Token.Type.IDENTIFIER, Token.Type.STRING)
            if token is not None:
                # Literal data class is used instead of Identifier data class.
                # It prevents this member from evaluation as variable.
                token.type = Token.Type.STRING
                member = Literal(token)  # <identifier>
            else:
                prefix = self._match(Token.Type.PLUS, Token.Type.MINUS)
                if prefix is not None:
                    self._go_to_next_token()
                token = self._match(Token.Type.NUMBER)
                if token is None:
                    token_info = dot.to_string(omit_type_name=True)
                    self._abort(f'Unexpected member after {token_info}')
                if '.' not in token.lexeme:
                    member = Literal(token)  # <digit>+
                else:
                    numbers = token.lexeme.split('.', maxsplit=2)
                    # The range of len(numbers) may be 0-3. But it must be 2.
                    if len(numbers) != 2 or not numbers[1].isdigit():
                        token_info = token.to_string(omit_type_name=True)
                        self._abort(f'Unexpected member after {token_info}')
                    for index, number in enumerate(numbers):
                        numbers[index] = Literal(
                                Token(Token.Type.NUMBER, medium=token.medium,
                                      line_number=token.line_number,
                                      column_number=token.column_number,
                                      lexeme=number))
                    member = numbers[0]
                    additional_member = numbers[1]
                if prefix is not None and prefix.type == Token.Type.MINUS:
                    member = Binary(
                              Literal(Token(Token.Type.NUMBER,
                                           medium=prefix.medium,
                                           line_number=prefix.line_number,
                                           column_number=prefix.column_number,
                                           lexeme='-1')),
                              Token(Token.Type.MULTIPLY), member)
            self._go_to_next_token()
        return [member, additional_member]

    def _make_array(self,
                    left_bracket=Token.Type.LEFT_SQUARE_BRACKET,
                    right_bracket=Token.Type.RIGHT_SQUARE_BRACKET,
                    is_parameter=False):
        """Make <array>.

        Normally, <array> :: = "[" [ <nl> ] [ <argument>
        { <end> <argument> } [ <end> ] ] [ <nl> ] "]" is made.

        "(" and ")" can be used instead of "[" and "]" for caller.
        <parameter> can be used instead of <argument> for callee.

        Args:
            left_bracket (Toke.Type, optional): The left side of
                                                surrounding array.
                                                The default is "[".
            right_bracket (Toke.Type, optional): The right side of
                                                 surrounding array.
                                                 The default is "]".
            is_parameter (bool, optional): True for using <parameter>
                                           instead of <argument>,
                                           False otherwise.
                                           The default is False.

        Returns:
            Array or NoneType: <array> as Array if it is obtained,
                               None otherwise.
                               Array is sub class of Statement.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        bracket = self._match(left_bracket)
        if bracket is None:
            return None
        self._go_to_next_token()

        self._skip_new_line()  # [ <nl> ]

        values = []
        while self._get_token_type() != right_bracket:
            value = self._make_argument() if not is_parameter \
                        else self._make_parameter()
            if value is not None:
                values.append(value)

            end = self._skip_end()
            if value is None:
                if end is None:
                    # There is no right bracket, no value, no ";",
                    # no ",", and no new line code. It is invalid.
                    token_info = \
                        self._get_token().to_string(omit_type_name=True)
                    self._abort(f'{token_info} is unexpected.')

                if end.type == Token.Type.NEW_LINE:
                    # Blank line is ignored.
                    continue

                # There is no value though delimiter is existed.
                # However it is permitted for "for (;;)",
                # for (; i < 10; i += 1), and so on.
                # In other words, it is not permitted for parameter of
                # function definition and array.
                if is_parameter:  # Parameter of function definition
                    token_info = end.to_string(omit_type_name=True)
                    self._abort(
                        f'{token_info} is found without parameter.')
                if left_bracket == Token.Type.LEFT_SQUARE_BRACKET:  # array
                    token_info = end.to_string(omit_type_name=True)
                    self._abort(f'{token_info} is found without value.')

        self._go_to_next_token()

        return Array(values)

    def _make_primary(self):
        """Make <primary>.

        <primary> ::= <number> | <string> | <boolean> | "null"
            | <group>

        Returns:
            Statement or NoneType: <primary> if it is obtained,
                                   None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        token = self._match(Token.Type.NUMBER, Token.Type.STRING,
                            Token.Type.TRUE, Token.Type.FALSE,
                            Token.Type.NULL)

        if token is None:
            token = self._match(Token.Type.IDENTIFIER)
            if token is not None:
                if self._is_infinity_or_nan(token):
                    self._go_to_next_token()
                    return Identifier(token)
                if self._is_implicit_assign:
                    token.type = Token.Type.STRING
                else:
                    token = None

        if token is not None:
            self._go_to_next_token()
            return Literal(token)

        if self._is_enable_only_json:
            return None

        return self._make_group()

    def _is_infinity_or_nan(self, token: Token) -> bool:
        """Detect whether the given token is Infinity/NaN or not.

        Args:
            token (Token): Token

        Returns:
            bool: True if the given token is Infinity/NaN,
                  False otherwise
        """
        identifiers = [Config.get_infinity_alt(self._config),
                       Config.get_nan_alt(self._config)]
        for identifier in identifiers:
            if identifier is not None and identifier == token.lexeme:
                return True
        return False

    def _match(self, *token_types):
        """Get token if the given types have the current token type.

        Example:
        - self._match(Token.Type.NUMBER)
        - self._match(Token.Type.NUMBER, Token.Type.STRING)
        - self._match((Token.Type.NUMBER, Token.Type.STRING))
        - self._match([Token.Type.NUMBER, Token.Type.STRING])

        Args:
            token_types (tuple or list or Token.Type): Token types.

        Returns:
            Token or NoneType: Token if the current token type is
                    existed in the given types, None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: It is happen when parsing is failed.
        """
        token = self._get_token()
        if len(token_types) > 1:  # multiple parameters
            if token.type not in token_types:
                token = None
        elif isinstance(token_types[0], (list, tuple)):
            if token.type not in token_types[0]:
                token = None
        elif isinstance(token_types[0], Token.Type):
            if token.type != token_types[0]:
                token = None
        else:
            self._abort("Interpreter side error in Parser#_match")
        return token

    def _go_to_next_token(self):
        """Process a next token.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: The out of range is happen.
        """
        self._index += 1
        self._get_token()

    def _get_token_type(self):
        """Get current Token type.

        Returns:
            Token.Type: The current Token type

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: The out of range is happen.
        """
        return self._get_token().type

    def _get_token(self):
        """Get current Token.

        Returns:
            Token: The current Token

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: The out of range is happen.
        """
        if self._index > len(self._tokens):
            self._abort("Interpreter side error in Parser#_get_token")

        if self._index == len(self._tokens):
            self._tokens.append(self._lexer.get_token())
        return self._tokens[self._index]

    def _consume_token(self):
        """Consume the current token.

        For example, the current token is "abc" and it is consumed.
        self._index points the head of next token.

                                    self._index
                                    |
                        0   1   2   3   4   5   6
                      +---+---+---+---+---+---+---+
        self._tokens: | a | b | c | d | e | f | g |
                      +---+---+---+---+---+---+---+

                             |
                             V

                        self._index
                        |
                        0   1   2   3
                      +---+---+---+---+
        self._tokens: | d | e | f | g |
                      +---+---+---+---+
        """
        if self._index > len(self._tokens):
            self._abort("Interpreter side error in Parser#_consume_token")

        # Remove from 0 to (self._index - 1).
        del self._tokens[0:self._index]
        self._index = 0

    def _skip_new_line(self):
        """Skip <nl>.

        Skip new line code from the current position.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: The out of range is happen.
        """
        if self._get_token_type() == Token.Type.NEW_LINE:
            self._go_to_next_token()

    def _skip_new_lines(self):
        """Skip <nl>+.

        Skip new line codes from the current position.
        As a result, there is other letter in the current position.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: The out of range is happen.
        """
        while self._get_token_type() == Token.Type.NEW_LINE:
            self._go_to_next_token()

    def _skip_end(self):
        """Skip <end>.

        Skip the following tokens from the current position.
        - ";" "\n"
        - "," "\n"
        - "\n"

        Returns:
            Token or NoneType: The skipped <end> Token if <end> is
                               skipped, None otherwise.

        Raises:
            LexError: It is happen when unknown token is found.
            ParseError: The out of range is happen.
        """
        is_end = False

        token = self._get_token()
        if token.type in (Token.Type.SEMICOLON, Token.Type.COMMA):
            is_end = True
            self._go_to_next_token()

        if self._get_token_type() == Token.Type.NEW_LINE:
            is_end = True
            self._go_to_next_token()

        return token if is_end else None

    def _abort(self, message):
        """Abort Parser.

        Print an error message and raise Exception.

        Args:
            message (str): Error message

        Raises:
            ParseError: This exception always happen when this method
                        is called.
        """
        raise Error.make_parse_error(message, config=self._config)
