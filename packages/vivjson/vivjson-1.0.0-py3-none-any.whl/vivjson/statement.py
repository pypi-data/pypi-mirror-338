"""Statement for VivJson

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
__date__ = '2025-03-29'

from dataclasses import dataclass
from typing import Optional, TypeVar, Any
from .tokens import Token

@dataclass(frozen=True)
class Statement:
    """Statement data class

    Abstract class.
    """
    def __repr__(self):
        return ''

LITERAL = TypeVar("LITERAL", str, int, float, bool, None)

@dataclass(frozen=True)
class Literal(Statement):
    """Literal data class"""
    token: Token

    def __repr__(self):
        if self.token.type in (Token.Type.NULL,
                               Token.Type.TRUE, Token.Type.FALSE):
            return self.token.type.value
        mark = '"' if self.token.type == Token.Type.STRING else ''
        return f'{mark}{self.token.lexeme}{mark}'

@dataclass(frozen=True)
class Identifier(Statement):
    """Identifier data class

    It is used as name of variable, function, and class.
    """
    name: Token

    def __repr__(self):
        return self.name.lexeme

@dataclass(frozen=True)
class Keyword(Statement):
    """Keyword data class

    return, break, and so on
    """
    token: Token

    def __repr__(self):
        return self.token.lexeme

@dataclass(frozen=True)
class Blank(Statement):
    """Blank data class"""
    token: Token

    BLANK = '(blank)'

    def __repr__(self):
        return self.BLANK

@dataclass(frozen=True)
class Array(Statement):
    """Array data class"""
    values: list[Statement]

    def __repr__(self):
        return f'[{", ".join(map(str, self.values))}]'

@dataclass(frozen=True)
class Block(Statement):
    """Block data class

    For example,
    - anonymous: x = {a: 3, b: 2}
    - pure: function test() {return(10)}
    - limited: if (i > 10) {x="+"} else {x="-"}

    In VivJson, any block is function.
    The type of the outermost block (that is given from file/text) is
    decided as anonymous function or class constructor by calling the
    particular method.
    """
    values: list[Statement]
    type: str

    CLASS_CONSTRUCTOR = 'Block_class'
    ANONYMOUS_FUNCTION = 'Block_anonymous'
    PURE_FUNCTION = 'Block_pure'
    LIMITED_FUNCTION = 'Block_limited'

    def __repr__(self):
        return f'{{{", ".join(map(str, self.values))}}}'

@dataclass(frozen=True)
class Binary(Statement):
    """Binary data class

    For example, 3 * 2 are stored into left, operator, and right.
    """
    left: Statement
    operator: Token
    right: Statement

    def __repr__(self):
        return f'({self.left} {self.operator.lexeme} {self.right})' \
            if self.operator.type != Token.Type.NOT else f'(not {self.right})'

@dataclass(frozen=True)
class Parameter(Statement):
    """Parameter data class

    This is used to assist the definition of function entity.
    The example is shown as below. There are 3 Parameters.

    (1) modifier + name   (3) modifier + name
         |                     |
         |    (2) only name    |
         |          |          |
         V          V          v
    _____________ ____  ______________
    function test(data, function block) {
        :
        :
    }

    - "modifier" is essential at (1).
    - "modifier" is optional at (2) and (3).
    """
    modifier: Optional[Token]
    name: Identifier

    def __repr__(self):
        modifier = f'{self.modifier.lexeme} ' \
                    if self.modifier is not None else ''
        return modifier + self.name.name.lexeme

@dataclass(frozen=True)
class Callee(Statement):
    """Callee data class

    This is used to define function entity.
    The example is shown as below.

        name   parameters[0]   parameters[1]
         |         |             |
         V         V             v
    _____________ ____  ______________
    function test(data, function block) {
        :
        :
    }

    In "name", its "modifier" of Parameter is essential.
    In "parameters", its "modifier" of Parameter is optional.
    """
    name: Parameter
    parameters: Array

    def __repr__(self):
        return f'{self.name}({", ".join(map(str, self.parameters.values))})'

@dataclass(frozen=True)
class CalleeRegistry(Statement):
    """Callee Registry data class

    This is made in Evaluator. This is not used in Parser.

    Member "environment" is Environment instance or None.
    The former (Environment instance) is set if callee is Closure.

    Member "is_reference" is True if this is not the definition of
    function.

    For example, "enclosure", "z1", and "z2" are registered as this
    data class.
    "environment" of "enclosure" is None.
    On the other hand, "environment" of "z1" and "z2" is Environment
    instance.
    "is_reference" of "enclosure" is False. "is_reference" of "z1" and
    "z2" is True.

    function enclosure(a) {
        x = a
        function closure(y) {
            return(x + y)
        }
        return(closure)
    }
    z1 = enclosure(100)
    z2 = enclosure(200)
    print(z1(5))  # 105
    print(z2(10))  # 210

    By the way, this data class is used even if assignment is simple.
    The following "y" is also this instance.
    "environment" of "x2" and "y" is None.
    "is_reference" of "x2" is False. "is_reference" of "y" is True.

    function x2(a) {
        return(a * 2)
    }
    y = x2

    "is_reference" decides whether the variable is remained or not
    after evaluating block.
    In the following sample, member of "k" will be only "y" after
    evaluation. Because the definition of function is not remained
    as result. Although value of "x2" and "y" is this instance,
    since "is_reference" of "y" is True, only "y" will be remained.

    k = {
        function x2(a) {
            return(a * 2)
        }
        y = x2
    }

    Similarly, the following "table" can keep its members.

    function add(a, b) {
        return(a + b)
    }
    function sub(a, b) {
        return(a - b)
    }
    table = {
        "+": add,
        "-": sub
    }
    """
    callee: Callee
    environment: Any
    is_reference: bool

    def __repr__(self):
        return str(self.callee)

@dataclass(frozen=True)
class Call(Statement):
    """Call data class

    This is used to call function, such as len("abc").
    """
    name: Statement
    arguments: Array

    def __repr__(self):
        return f'{self.name}({", ".join(map(str, self.arguments.values))})'

@dataclass(frozen=True)
class Loop(Statement):
    """Loop data class

    "call" is not used for actual control. It may be used to print
    function name.
    "statements" is main operation.
    "initial" proposes whether loop should be done or not before loop.
    "continuous" proposes whether loop should be done or not after 1st
    loop.
    "initial" and "continuous" are a list of Statement. The judgement
    is decided with the last Statement.
    "each" and "iterator" is used for "for (i in [1, 2, 3]) {...}"
    style. "each" is variable as Identifier. "iterator" is list or
    dict.

    For example, for (i = 0; i < 10; i += 1) { print(i) }
    "initial" is [i = 0; i < 10].
    "continuous" is [i += 1; i < 10].
    "statements" is [print(i)].
    "each" is None.
    "iterator" is None.

    For example, for (i in [1, 2, 3]) { print(i) }
    "initial" is [true].
    "continuous" is [true].
    "statements" is [print(i)].
    "each" is i.
    "iterator" is [1, 2, 3].

    For example, for (i in {"a": 1, "b": 2, "c": 3}) { print(i) }
    "initial" is [true].
    "continuous" is [true].
    "statements" is [print(i)].
    "each" is i.
    "iterator" is {"a": 1, "b": 2, "c": 3}.
    """
    call: Call
    initial: list[Statement]
    continuous: list[Statement]
    statements: list[Statement]
    each: Optional[Identifier]
    iterator: Optional[list]

    def __repr__(self):
        if isinstance(self.each, Identifier) and self.iterator is not None:
            text = ", ".join(map(str, self.statements))
            return f'{self.call.name}({self.each} in {self.iterator}) ' \
                   f'{{{text}}}'
        texts = []
        for statements in [self.initial, self.continuous, self.statements]:
            text = ", ".join(map(str, statements))
            texts.append(f'{{{text}}}')
        return f'{self.call.name}(init={texts[0]}, continue={texts[1]}) ' \
               f'{texts[2]}'

@dataclass(frozen=True)
class Get(Statement):
    """Get data class

    For example, x["y"]["z"] is represented as ["x", "y", "z"].
    Similarly, x.y.z is represented.
    """
    members: list[Statement]

    def __repr__(self):
        variable = ''
        for member in self.members:
            variable = str(member) if variable == '' \
                        else f'{variable}[{member}]'
        return variable

@dataclass(frozen=True)
class Set(Statement):
    """Set data class

    For example, x["y"]["z"] = 3 is represented as below.
      - members: ["x", "y", "z"]
      - operator: =
      - value: 3
    Similarly, x.y.z = 3 is represented.
    """
    members: list[Statement]
    operator: Token
    value: Statement

    def __repr__(self):
        variable = ''
        for member in self.members:
            variable = str(member) if variable == '' \
                        else f'{variable}[{member}]'
        space = '' if self.operator.type == Token.Type.SET else ' '
        return f'{variable}{space}{self.operator.lexeme} {self.value}'

@dataclass(frozen=True)
class Remove(Statement):
    """Remove data class

    For example, remove(x["y"]["z"]), remove(x.y.z)
    """
    token: Token
    members: list[Statement]

    def __repr__(self):
        variable = ''
        for member in self.members:
            variable = str(member) if variable == '' \
                        else f'{variable}[{member}]'
        return f'remove({variable})'

@dataclass(frozen=True)
class Return(Statement):
    """Return data class

    "return" [ "(" value ")" ]
    """
    token: Token
    value: Optional[Statement]

    def __repr__(self):
        if self.value is None:
            return 'return'
        value = str(self.value)
        if value[0] == '(' and value[-1] == ')':
            value = value[1:-1]
        return f'return({value})'

# tuple is disallowed.
# When tuple has simple structure, such as 1 dimensional tuple,
# converting to list is possible. However complex structure is
# given, it is so difficult. So it is not allowed.
HOSTVALUE = \
    TypeVar("HOSTVALUE", None, bool, int, float, str, list, dict)

@dataclass(frozen=True)
class Injection(Statement):
    """Injection data class

    Set host language's variable.
    """
    variable: str
    value: HOSTVALUE
    location: Optional[str]  # for reporting Error, ex) "2nd argument"

    def __repr__(self):
        value = self.value
        if value is None:
            value = 'null'
        elif value is True:
            value = 'true'
        elif value is False:
            value = 'false'
        return f'{self.variable}: {value}'

@dataclass(frozen=True)
class Value(Statement):
    """Value data class

    Set host language's value.
    """
    value: HOSTVALUE
    location: Optional[str]  # for reporting Error, ex) "2nd argument"

    def __repr__(self):
        value = self.value
        if value is None:
            value = 'null'
        elif value is True:
            value = 'true'
        elif value is False:
            value = 'false'
        return str(value)
