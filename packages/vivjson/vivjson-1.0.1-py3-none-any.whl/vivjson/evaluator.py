"""Evaluator for VivJson

- Evaluator: Constructor.
- Evaluator#evaluate: Evaluate the given statements.

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
__date__ = '2025-03-30'

# pylint: disable=C0302

from copy import deepcopy
from functools import singledispatchmethod
from math import isinf, isnan
from .config import Config
from .error import Error
from .environment import Environment
from .statement import Literal, Identifier, Keyword, Blank, \
                       Array, Block, Binary, Parameter, \
                       Callee, CalleeRegistry, Call, Loop, \
                       Get, Set, Remove, \
                       Return, Injection, Value, LITERAL
from .standard import Standard
from .tokens import Token

class Evaluator:  # pylint: disable=R0902
    """Evaluator class

    Evaluate statement.

    Attributes:
        _config (Config or NoneType): Configuration
        _environment (Environment): Environment instance that is used
                                    to read/write variable.
        _binary_operations (dict): Token type -> method
        _assign_operations (dict): Token type -> method
        _stack (list[dict]): Stack of evaluated statement.
                             There are two purposes.
                               - Keep limit of the recursive called
                                 times.
                               - Avoid software runaway.
                             The each element is a dict that have
                             2 strings.
                               - "name": Block type or the class name
                                 of evaluated statement.
                               - "detail": The detail of evaluated
                                 statement.
        _max_array_size (int): Maximum array/block size
        _max_depth (int): Maximum recursive called times of evaluate
                          method
        _max_loop_times (int): Maximum loop times of "for", "while",
                               and so on.
        _REPLACED_LETTERS (dict): The escaped letter and real letter.
    """
    _REPLACED_LETTERS = {chr(0x08): 'b', chr(0x0C): 'f', chr(0x0A): 'n',
                         chr(0x0D): 'r', chr(0x09): 't',
                         '"': '"', '\\': '\\'}

    def __init__(self, config=None):
        """Initialize class.

        Args:
            config (Config or NoneType): Configuration if needed.
        """
        self._config = config
        self._environment = Environment()
        infinity = Config.get_infinity_alt(config)
        if isinstance(infinity, str):
            self._environment.set(infinity, float('inf'))
        nan = Config.get_nan_alt(config)
        if isinstance(nan, str):
            self._environment.set(nan, float('nan'))
        self._binary_operations = {
            Token.Type.PLUS: Evaluator._add,
            Token.Type.MINUS: Evaluator._subtract,
            Token.Type.MULTIPLY: Evaluator._multiply,
            Token.Type.DIVIDE: Evaluator._divide,
            Token.Type.MODULO: Evaluator._modulo,
            Token.Type.NOT: Evaluator._logical_invert,
            Token.Type.AND: Evaluator._logical_and,
            Token.Type.OR: Evaluator._logical_or,
            Token.Type.EQ: Evaluator._is_equal,
            Token.Type.NE: Evaluator._is_not_equal,
            Token.Type.LT: Evaluator._is_less_than,
            Token.Type.LE: Evaluator._is_less_than_or_equal,
            Token.Type.GT: Evaluator._is_greater_than,
            Token.Type.GE: Evaluator._is_greater_than_or_equal,
            Token.Type.IN: Evaluator._is_contained
        }
        self._assign_operations = {
            Token.Type.PLUS_ASSIGN: Evaluator._add,
            Token.Type.MINUS_ASSIGN: Evaluator._subtract,
            Token.Type.MULTIPLY_ASSIGN: Evaluator._multiply,
            Token.Type.DIVIDE_ASSIGN: Evaluator._divide,
            Token.Type.MODULO_ASSIGN: Evaluator._modulo
        }
        self._stack = []
        self._max_array_size = Config.get_max_array_size_alt(config)
        self._max_depth = Config.get_max_depth_alt(config)
        self._max_loop_times = Config.get_max_loop_times_alt(config)

    def get(self, name):
        """Get a variable's value.

        Args:
            name (str): Variable name

        Returns:
            Any: Its value
                 Environment.UNDEFINED is returned if the given name's
                 variable is not existed.

        Raises:
            EvaluateError: It is happen if the given name isn't string.
        """
        if not isinstance(name, str):
            self._abort(f'"{name}" is not string in Evaluator#get.')
        return self._environment.get(name, only_this_scope=True)

    def set(self, name, value):
        """Set a variable.

        Args:
            name (str): Variable name
            value (Any): Its value

        Raises:
            EvaluateError: It is happen if the given name isn't string.
        """
        if not isinstance(name, str):
            self._abort(f'"{name}" is not string in Evaluator#set.')
        self._environment.set(name, value, only_this_scope=True)

    def rewind_after_abort(self):
        """Rewinds stack and environment after abort.

        Fix as below. This is clean up for abort (exception).
        When Viv.run_method is failed, instance has unnecessary
        information. It may be happen unusual behavior in the next
        running via its instance. So clean up is needed.

        - Reset stack of evaluated statement "{@link #stack}".
        - Rewind environment "{@link #environment}" to first hierarchy.

        Note that it is assumed that the first call of evaluate method
        is evaluate(self, block: Block).

        For example,

          - The newest Environment #1  : The present position
              - enclosing = #2                |
          - Environment #2                    |
              - enclosing = #3                V
          - Environment #3             : Rewind to this position.
            (This is made by Block statement of making Instance.)
              - enclosing = #4
              - Instance's member variable is available.
              - Instance's method is available.
          - Root Environment #4
              - enclosing = null
        """
        # Reset stack of evaluated statement.
        self._stack = []
        # Rewind environment.
        while (enclosing := self._environment.get_enclosing()) is not None \
              and enclosing.get_enclosing() is not None:
            self._environment = enclosing

    @singledispatchmethod
    def evaluate(self, statement):
        """Evaluate statement.

        This should not be called. Sub-class, such as Identifier,
        should be called.

        Args:
            statement (Statement): The evaluated statement

        Raises:
            EvaluateError: This exception always happen when this
                           method is called.
        """
        self._abort(f'Cannot evaluate "{statement}"', statement)

    @evaluate.register
    def _(self, literal: Literal) -> LITERAL:
        """Evaluate literal.

        Args:
            literal (Literal): The evaluated literal statement

        Returns:
            float or int or str or bool or NoneType: the literal value
                                                as evaluated result.

        Raises:
            EvaluateError: It is happen if the given number is invalid.
        """
        self._enter_evaluate(literal)
        value = None
        if literal.token.type == Token.Type.NUMBER:
            try:
                value = float(literal.token.lexeme) \
                        if '.' in literal.token.lexeme \
                            or 'e' in literal.token.lexeme \
                            or 'E' in literal.token.lexeme \
                        else int(literal.token.lexeme)
            except (ValueError, OverflowError):
                self._abort(f'Invalid number "{literal}"', literal)
        elif literal.token.type == Token.Type.STRING:
            value = literal.token.lexeme
        elif literal.token.type == Token.Type.TRUE:
            value = True
        elif literal.token.type == Token.Type.FALSE:
            value = False
        self._leave_evaluate(literal)
        return value

    @evaluate.register
    def _(self, identifier: Identifier):
        """Evaluate identifier.

        Args:
            identifier (Identifier): The evaluated identifier statement

        Returns:
            Any: variable's value is returned mostly.
                 Identifier statement is returned if the given
                 identifier is Standard method name.
                 null if variable is undefined.

        Raises:
            EvaluateError: It is happen if the unexpected token is
                           included.
        """
        self._enter_evaluate(identifier)
        is_std_method = \
            Standard.get_method(identifier.name.lexeme) is not None

        if identifier.name.type != Token.Type.IDENTIFIER \
                and not is_std_method:
            self._abort(f'Cannot evaluate "{identifier}"', identifier)

        value = self._environment.get(None if identifier.name.lexeme == '.'
                                      else identifier.name.lexeme)
        if isinstance(value, Get):        # When it is alias,
            value = self.evaluate(value)  # read original variable's value.
        if value == Environment.UNDEFINED:
            if is_std_method:
                value = identifier
            else:
                value = None  # The undefined variable's value is null.
        self._leave_evaluate(identifier)
        return value

    @evaluate.register
    def _(self, keyword: Keyword):
        """Evaluate keyword.

        This should not be called.
        Keyword statement is used in Block/Loop statement. Because
        Keyword statement is "break" or "continue".
        So This is not used by evaluate method directly.

        Args:
            keyword (Keyword): The evaluated keyword statement

        Raises:
            EvaluateError: This exception always happen when this
                           method is called.
        """
        self._abort(f'Cannot evaluate "{keyword}"', keyword)

    @evaluate.register
    def _(self, _: Blank):
        """Evaluate blank.

        Args:
            _ (Blank): The evaluated blank statement

        Returns:
            NoneType: None is always returned.
        """
        return None

    @evaluate.register
    def _(self, array: Array) -> list:
        """Evaluate array.

        Args:
            array (Array): The evaluated array statement

        Returns:
            list: The evaluated result

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        self._enter_evaluate(array)
        if len(array.values) > self._max_array_size:
            self._abort('Array size is too large.', array)
        values = list(map(self.evaluate, array.values))
        self._leave_evaluate(array)
        return values

    @evaluate.register
    def _(self, block: Block) -> dict:
        """Evaluate block.

        Args:
            block (Block): The evaluated block statement

        Returns:
            Any: A dict as the evaluated block is returned mostly.
            However various value may be returned by ":=" and
            "return()".

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        self._enter_evaluate(block)

        # self._print_stack()

        previous_environment = self._environment
        self._environment = Environment(previous_environment)  # Add scope
        # When "return" statement is executed later, it should be recorded.
        # The certain variable is need in order to recording.
        # It is created at starting constructor or anonymous/pure function.
        is_recording = block.type in (Block.CLASS_CONSTRUCTOR,
                                Block.ANONYMOUS_FUNCTION, Block.PURE_FUNCTION)
        if is_recording:
            self._environment.set(Environment.FUNCTION_RETURN_NAME,
                                  Environment.UNDEFINED, only_this_scope=True)

        for value in block.values:
            reason = self._set_reason_going_back(value)
            if reason is not None:
                break

            self.evaluate(value)

            # Finish if break/continue/return happen in the above evaluation.
            reason = self._get_reason_going_back()
            if reason is not None:
                break

        result = Environment.UNDEFINED
        if is_recording:
            value = self._environment.get(Environment.FUNCTION_RETURN_NAME,
                                          only_this_scope=True)
            if value != Environment.FUNCTION_RETURN_NAME:
                result = value
        if result == Environment.UNDEFINED:
            result = self._environment.get()

        if block.type != Block.CLASS_CONSTRUCTOR:
            self._environment = previous_environment  # Restore scope
        self._leave_evaluate(block)
        return result

    @evaluate.register
    def _(self, binary: Binary):
        """Evaluate binary.

        For example, 3 + 2 is evaluated.
        Note that short-circuit evaluation (minimal evaluation) is happen
        for <and> or <or>.

        Args:
            binary (Binary): The evaluated binary statement

        Returns:
            Any: The result of binary operation if it is success, None
                 otherwise.

        Raises:
            EvaluateError: It is happen by some reason.
                           - The operator/operand is invalid.
                           - Array size reaches limit.
                           - Divide by 0.
        """
        self._enter_evaluate(binary)

        op_type = binary.operator.type
        if op_type not in self._binary_operations:
            self._abort(f'Cannot evaluate "{binary}"', binary)

        left = self.evaluate(binary.left)

        value = None
        # 1. Short-circuit evaluation (minimal evaluation) for <and>
        # 2. Short-circuit evaluation (minimal evaluation) for <or>
        # 3. Other evaluation
        if op_type == Token.Type.AND and not Evaluator.is_truthy(left):
            value = False
        elif op_type == Token.Type.OR and Evaluator.is_truthy(left):
            value = True
        else:
            method = self._binary_operations[op_type]
            right = self.evaluate(binary.right)
            try:
                value = method(left, right, self._config)
            except Error.EvaluateError:
                self._abort(f'Cannot evaluate "{binary}"', binary)

        self._leave_evaluate(binary)
        return value

    @evaluate.register
    def _(self, parameter: Parameter):
        """Evaluate parameter.

        This should not be called.
        Parameter statement is used in Call statement. Because
        Parameter statement is "class" or "function".
        So This is not used by evaluate method directly.

        Args:
            parameter (Parameter): the evaluated parameter statement

        Raises:
            EvaluateError: This exception always happen when this
                           method is called.
        """
        self._abort(f'Cannot evaluate "{parameter}"', parameter)

    @evaluate.register
    def _(self, callee: Callee):  # pylint: disable=R1711
        """Evaluate callee.

        Callee statement is the definition (entity) of function.
        For example, "function test() {print(10)}" is represented with
        Callee statement.
        This is wrapped with CalleeRegistry statement. And it is stored
        into Environment in order to register function.

        Args:
            callee (Callee): The evaluated callee statement

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        self._enter_evaluate(callee)
        self._environment.set(callee.name.name.name.lexeme,
                CalleeRegistry(callee, None, False))  # definition of function
        self._leave_evaluate(callee)
        return None

    @evaluate.register
    def _(self, callee_registry: CalleeRegistry):
        """Evaluate callee registry.

        This should not be called.
        CalleeRegistry statement is used to register function. This is
        not used by evaluate method directly.

        Args:
            callee_registry (CalleeRegistry): the evaluated 
                                              CalleeRegistry statement

        Raises:
            EvaluateError: This exception always happen when this
                           method is called.
        """
        self._abort(f'Cannot evaluate "{callee_registry}"', callee_registry)

    @evaluate.register
    def _(self, call: Call):
        """Evaluate call.

        Function call is done.

        Args:
            call (Call): The evaluated call statement

        Returns:
            Any: The returned value of function

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        self._enter_evaluate(call)

        if not isinstance(call.name, (Identifier, Get)):
            self._abort(f'Cannot call for {call}', call)

        result = None
        try:
            # User defined function
            result, is_done = self._call_function(call)
            if not is_done:
                # Standard library's method
                name = call.name
                value = self.evaluate(name)
                if isinstance(value, Identifier):
                    name = value.name.lexeme
                else:
                    if isinstance(name, Get):
                        if len(name.members) == 1:
                            name = name.members[0]
                    if isinstance(name, Identifier):
                        name = name.name.lexeme
                if not isinstance(name, str):
                    self._abort(f'Cannot call for {call}', call)
                method = Standard.get_method(name)
                if method is None:
                    self._abort(f'Cannot call for {call}', call)
                result = method(self, call, self._config)
        except Error.EvaluateError as e:
            message = str(e)
            is_baton = message != ''
            statement_for_location = None
            if not is_baton:
                message = f'{call} is failed'
                statement_for_location = call
            self._abort(message, statement_for_location,
                        eliminate_tag=is_baton)

        self._leave_evaluate(call)
        return result

    @evaluate.register
    def _(self, loop: Loop):  # pylint: disable=R0912
        """Evaluate loop.

        Args:
            loop (Loop): The evaluated loop statement

        Returns:
            Any: The returned value of Loop.
                 Loop has Block. Block is the function.
                 The function returns value.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        self._enter_evaluate(loop)

        # Make sure that initial/continuous condition is given as list.
        if not isinstance(loop.initial, list) \
                or not isinstance(loop.continuous, list):
            self._abort(f'Loop condition of {loop.call} is invalid',
                        loop.call)
        # Make sure that correct iterator is given.
        iterator = None
        if loop.each is not None or loop.iterator is not None:
            if not isinstance(loop.each, Identifier) \
                    or not isinstance(loop.iterator, (list, dict)):
                self._abort(f'Iterator of {loop.call} is invalid', loop.call)
            # Deep copy is needed instead of Shallow copy.
            # Shallow copied value may be broken. For example, the value of
            # "list" is broken as below.
            # list=[{"x":3,"y":5}];for(a in list){a.x=2} --> [{"x":2, "y":5}]
            # list={"x":{"y":5}};for(a in list){a[1]["y"]=1} --> {"x":{"y":1}}
            iterator = deepcopy(loop.iterator)
            if isinstance(iterator, dict):
                iterator = list(iterator.items())

        # Add new environment
        previous_environment = self._environment
        self._environment = Environment(previous_environment)  # Add scope
        self._environment.set(Environment.BREAK_NAME,
                              Environment.UNDEFINED, only_this_scope=True)

        is_satisfied = True
        for loop_times in range(self._max_loop_times):
            statements = loop.initial if loop_times == 0 else loop.continuous
            for statement in statements:
                is_satisfied = self.evaluate(statement)
            is_satisfied = Evaluator.is_truthy(is_satisfied)
            if not is_satisfied:
                break

            self._environment.set(Environment.CONTINUE_NAME,
                                  Environment.UNDEFINED, only_this_scope=True)

            if iterator is not None:
                if len(iterator) == 0:
                    is_satisfied = False
                    break
                datum = iterator.pop(0)
                if isinstance(datum, tuple):
                    datum = list(datum)
                self._environment.set(loop.each.name.lexeme, datum,
                                      only_this_scope=True)

            reason = None
            for statement in loop.statements:
                reason = self._set_reason_going_back(statement)
                if reason is not None:
                    break

                self.evaluate(statement)

                # Terminate current loop if break/continue/return happen
                # in the above evaluation.
                reason = self._get_reason_going_back()
                if reason is not None:
                    break

            if reason in (Environment.BREAK_NAME,
                          Environment.FUNCTION_RETURN_NAME):
                is_satisfied = False
                break

        if is_satisfied:
            self._abort(f'Loop times reach maximum ({self._max_loop_times})',
                        loop.call)

        result = self._environment.get()

        # Discard current environment
        self._environment = previous_environment  # Restore scope

        self._leave_evaluate(loop)
        return result

    @evaluate.register
    def _(self, get: Get):  # pylint: disable=R0912
        """Evaluate get.

        This (Statement "Get") is familiar with Statement "Identifier".
        If variable is simple, such as foo, its value is given by
        evaluating Statement "Identifier" of foo.
        This (Statement "Get") is used to obtain the value of array and
        block, such as foo[2] and bar.baz.

        Args:
            get (Get): The evaluated get statement

        Returns:
            Any: variable's value

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        self._enter_evaluate(get)
        if len(get.members) == 0:
            self._abort(f'Cannot get {get}', get)
        variable = Environment.UNDEFINED
        for member in get.members:
            if variable is None:  # The undefined variable
                break
            member = self.evaluate(member)
            if variable == Environment.UNDEFINED:
                variable = member
                continue
            if isinstance(variable, (list, dict)):
                if isinstance(member, bool):  # Avoid boolean
                                    # Note that isinstance(True, int) is True.
                    self._abort(f'Cannot get {get}', get)
                if isinstance(member, float):
                    if member % 1 != 0:
                        self._abort(f'Cannot get {get}', get)
                    member = int(member)
                # for foo[bar] or foo.bar as array
                if isinstance(member, int) and isinstance(variable, list):
                    length = len(variable)
                    if member < 0:  # Backward access
                        member += length
                    if 0 <= member < length:
                        variable = variable[member]
                        continue
                    # null because out of range
                    variable = None
                    break
                # for foo[bar] of foo.bar as block
                if isinstance(variable, dict):
                    if isinstance(member, int):
                        member = str(member)
                    if isinstance(member, str) and member in variable:
                        variable = variable[member]
                        continue
                    # null because member is not found.
                    variable = None
                    break
            self._abort(f'Cannot get {get}', get)
        self._leave_evaluate(get)
        return None if variable == Environment.UNDEFINED else variable

    @evaluate.register
    def _(self, s: Set):  # pylint: disable=R0912
        """Evaluate set.

        For assignment, various situations are available as below.

        1. Simple assignment: x = 3
        2. Assignment for alias:
                function test(a) { a = 3, ... } --> _[0] = 3
        3. Assignment for block's member:
                a = {b: [2, 3]}, a.b[1] = 10 --> a = {b: [2, 10]}
        4. Removing: It is done with Remove statement.

        "Set" statement has parts of the above variable.
        For example, x["y"]["z"] is represented as ["x", "y", "z"].

        Variable may be alias.
        For example, x is alias of _[0] and x["y"]["z"] is given,
        _[0]["y"]["z"] is evaluated.

        Args:
            s (Set): The evaluated set statement

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        self._enter_evaluate(s)
        value = self.evaluate(s.value)
        if isinstance(value, (dict, list)):
            value = deepcopy(value)

        # The returned value of ":="
        if s.operator.type == Token.Type.RESULT:
            self._environment.set(None, value)  # None indicates
                                                # the returned value.
            self._leave_evaluate(s)
            return None  # None is meaningless.

        is_local = s.operator.type == Token.Type.SET  # ":" makes local.

        if len(s.members) == 0:
            self._abort(f'Cannot assign {s}', s)

        # Get the head. For example, "x" of x["y"]["z"]
        member = s.members[0]
        if not isinstance(member, Identifier):
            member = self.evaluate(member)
            if not isinstance(member, Identifier):
                self._abort(f'Cannot assign {s}', s)

        # Avoid system variable.
        name = member.name.lexeme
        if len(name) >= 6 and name[0:3] == '___' and name[-3:] == '___':
            self._abort(f'Cannot assign {s} '
                        "because variable's prefix/suffix is '___'", s)

        members = []
        maybe_alias = self._environment.get(name)
        if isinstance(maybe_alias, Get):  # for alias
            # For example, maybe_alias = ["_", 1]
            #              "_" is Identifier and 1 is Literal
            if len(maybe_alias.members) <= 1 \
                    or not isinstance(maybe_alias.members[0], Identifier):
                self._abort(f'Cannot assign {s}', s)
            name = maybe_alias.members[0].name.lexeme  # It is '_'.
            # Get the following member. For example, ["y"]["z"] of x["y"]["z"]
            members = s.members.copy()
            members.pop(0)
            # Conjoin.
            # For example, ["_", 1, "y", "z"]
            for index, member in enumerate(maybe_alias.members):
                members.insert(index, member)
        else:  # except alias
            if len(s.members) == 1:  # for simple variable, such as i, num.
                if s.operator.type in self._assign_operations:  # +=, -=, ...
                    method = self._assign_operations[s.operator.type]
                    original_value = self._environment.get(name, is_local)
                    try:
                        value = method(original_value, value, self._config)
                    except Error.EvaluateError:
                        self._abort(f'Cannot evaluate "{s}"', s)
                if s.operator.type == Token.Type.REMOVE:
                    self._environment.remove(name)
                else:
                    if isinstance(value, CalleeRegistry):
                        value = CalleeRegistry(value.callee,
                                               value.environment,
                                               True)  # Reference
                    self._environment.set(name, value, is_local)
                self._leave_evaluate(s)
                return None  # None is meaningless.
            members = s.members.copy()
        members[0] = Literal(Token(Token.Type.STRING, lexeme=name))
        variable = {name: self._environment.get(name, is_local)}
        self._set_member(variable, members, value, s.operator.type)
        self._environment.set(name, variable[name], is_local)

        self._leave_evaluate(s)
        return None  # None is meaningless.

    @evaluate.register
    def _(self, remove: Remove):  # pylint: disable=R1711
        """Evaluate remove.

        Args:
            remove (Remove): The evaluated remove statement

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        self._enter_evaluate(remove)

        s = Set(remove.members, remove.token, Literal(Token(Token.Type.NULL)))
        try:
            self.evaluate(s)
        except Error.EvaluateError as e:
            message = str(e)
            is_baton = message != ''
            statement_for_location = None
            if not is_baton:
                message = f'{remove} is failed'
                statement_for_location = remove
            else:
                message = message.replace('assign', 'remove')
            self._abort(message, statement_for_location,
                        eliminate_tag=is_baton)

        self._leave_evaluate(remove)
        return None  # None is meaningless.

    @evaluate.register
    def _(self, r: Return):
        """Evaluate return.

        This should not be called.
        Return statement is used in Block/Loop statement. This is
        not used by evaluate method directly.

        Args:
            r (Return): The evaluated Return statement

        Raises:
            EvaluateError: This exception always happen when this
                           method is called.
        """
        self._abort(f'Cannot evaluate "{r}"', r)

    @evaluate.register
    def _(self, injection: Injection):  # pylint: disable=R1711
        """Evaluate injection.

        The following values are accepted.
        - null
        - Boolean
        - Number (Byte, Short, Integer, Long, Float, Double)
        - String
        - ArrayList<@Nullable Object>
        - HashMap<String, @Nullable Object>

        Args:
            injection (Injection): The evaluated injection statement

        Raises:
            EvaluateError: It is happen if the prefix/suffix of
                           variable name is "___" or value is
                           illegal.
        """
        self._enter_evaluate(injection)
        if injection.value is not None and not isinstance(injection.value,
                                        (bool, int, float, str, list, dict)):
            self._abort(f'Cannot use a value of "{injection}"', injection)
        if len(injection.variable) >= 6 and injection.variable[0:3] == '___' \
                and injection.variable[-3:] == '___':
            self._abort(f'Cannot use a value of "{injection}" because '
                        "variable's prefix/suffix is '___'", injection)
        self._environment.set(injection.variable, injection.value)
        self._leave_evaluate(injection)
        return None  # None is meaningless.

    @evaluate.register
    def _(self, value: Value):
        """Evaluate value.

        The following values are accepted.
        - null
        - Boolean
        - Number (Byte, Short, Integer, Long, Float, Double)
        - String
        - ArrayList<@Nullable Object>
        - HashMap<String, @Nullable Object>

        Args:
            value (Value): The evaluated value statement

        Raises:
            EvaluateError: It is happen if value is illegal.
        """
        self._enter_evaluate(Value)
        if value.value is not None and not isinstance(value.value,
                                        (bool, int, float, str, list, dict)):
            self._abort(f'Cannot use a value of "{value}"', value)
        self._leave_evaluate(Value)
        return value.value

    def _enter_evaluate(self, statement):
        """Record to enter new evaluation.

        Args:
            statement (Statement or NoneType): Data class of new
                                               evaluation

        Raises:
            EvaluateError: It is happen if the recursive call times
                           reach limit.
        """
        if len(self._stack) >= self._max_depth:
            self._abort('Recursive call times reach '
                        f'maximum ({self._max_depth}).')
        evaluated = {
            'name': statement.type if isinstance(statement, Block) \
                    else statement.__class__.__name__,
            'detail': str(statement)
        }
        self._stack.append(evaluated)

    def _leave_evaluate(self, statement):
        """Record to leave current evaluation.

        Args:
            statement (Statement or NoneType): Data class of current
                                               evaluation

        Raises:
            EvaluateError: It is happen if the order of
                           evaluating/leaving is invalid
                           or recorded data is invalid.
        """
        evaluated = None
        try:
            evaluated = self._stack.pop()
        except IndexError:
            pass
        name = statement.type if isinstance(statement, Block) \
               else statement.__class__.__name__
        if not isinstance(evaluated, dict) or "name" not in evaluated \
                or evaluated['name'] != name:
            self._abort('Interpreter side error in Evaluator#_leave_evaluate')

    def _print_stack(self):
        """Print stack

        Raises:
            EvaluateError: it is happen if recorded data is invalid.
        """
        for index, evaluated in enumerate(self._stack):
            if not isinstance(evaluated, dict) or "name" not in evaluated \
                    or "detail" not in evaluated:
                self._abort('Interpreter side error '
                            'in Evaluator#_print_stack')
            print(f'> {index}: {evaluated["name"]} ({evaluated["detail"]})')

    def _get_reason_going_back(self):
        """Get reason of going back until function/loop statement.

        Returns:
            str or NoneType: Reason if going back is needed,
                             None otherwise.
                             Reason is which one:
                             - Environment.BREAK_NAME
                             - Environment.CONTINUE_NAME
                             - Environment.FUNCTION_RETURN_NAME
        """
        for name in (Environment.FUNCTION_RETURN_NAME,
                     Environment.BREAK_NAME, Environment.CONTINUE_NAME):
            value = self._environment.get(name)
            if value != Environment.UNDEFINED:
                return name
        return None

    def _set_reason_going_back(self, statement):
        """Set reason of going back until function/loop statement.

        Args:
            statement: Statement that may be return/break/continue.

        Returns:
            str or NoneType: Reason if going back is needed,
                             None otherwise.
                             Reason is which one:
                             - Environment.BREAK_NAME
                             - Environment.CONTINUE_NAME
                             - Environment.FUNCTION_RETURN_NAME

        Raises:
            EvaluateError: It is happen if the returned value is
                           invalid or break/continue is used without
                           loop.
        """
        # for "return"
        if isinstance(statement, Return):
            reason = Environment.FUNCTION_RETURN_NAME
            value = reason
            if statement.value is not None:
                # When function object is returned, the persistent
                # environment is given for closure.
                value = self.evaluate(statement.value)
                if isinstance(value, CalleeRegistry):
                    value = CalleeRegistry(value.callee,
                                           self._environment,  # Closure
                                           True)  # Reference
            self._environment.set(reason, value)
            return reason

        # for "break"/"continue"
        reason = None
        if isinstance(statement, Keyword):
            if statement.token.type == Token.Type.BREAK:
                reason = Environment.BREAK_NAME
            elif statement.token.type == Token.Type.CONTINUE:
                reason = Environment.CONTINUE_NAME
        if reason is None:
            return None
        # "break"/"continue" is allowed for Loop.
        # So we find Loop. However function is found, finding is terminated.
        found = False
        for evaluated in reversed(self._stack):
            if not isinstance(evaluated, dict) or 'name' not in evaluated:
                break
            if evaluated['name'] == 'Loop':
                found = True
                break
            if evaluated['name'] in (Block.CLASS_CONSTRUCTOR,
                            Block.ANONYMOUS_FUNCTION, Block.PURE_FUNCTION):
                break
        if not found:
            self._abort(f'{statement.token.lexeme} is found without loop',
                        statement)
        self._environment.set(reason, True)
        return reason

    def _call_function(self, call: Call):  # pylint: disable=R0912, R0914
        """Call a function.

        Args:
            call (Call): The information that contains function name,
                         arguments, and so on.

        Returns:
            Any, bool: 2 values are returned.
                       1st value: The result of function.
                       2nd value: True if processing is done.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        # Get function entity.
        statement = call.name
        if isinstance(statement, Identifier):
            statement = self._environment.get(statement.name.lexeme)
        if isinstance(statement, Get):  # for alias of argument or
                                        # variable that is assigned function
            statement = self.evaluate(statement)
        if isinstance(statement, Block):  # for anonymous function
            return self.evaluate(statement), True
        if not isinstance(statement, CalleeRegistry):
            return None, False
        callee = statement.callee
        environment = statement.environment

        # Check its modifier.
        modifier = callee.name.modifier
        if modifier is None \
                or modifier.type != Token.Type.FUNCTION:
            return None, False

        # Get parameter's definition and function's statements of Callee.
        # They are contained within an Array.
        # For example, there are 2 parameters: This array is
        # [1st parameter, 2nd parameter, A block of statements].
        parameter_length = len(callee.parameters.values)
        if parameter_length < 1:  # One parameter of block is needed at least
            raise Error.EvaluateError()
        parameter_length -= 1  # Number of actual parameters except block
        statements = callee.parameters.values[-1]  # Block
        if not isinstance(statements, Block):
            raise Error.EvaluateError()

        # Add scope for pure function.
        # Reuse environment for closure.
        previous_environment = self._environment
        self._environment = environment if environment is not None \
                            else Environment(previous_environment)

        # Make implicit variable from arguments.
        implicit = []
        for index, value in enumerate(call.arguments.values):
            is_function = False
            is_reference = False
            if index < len(callee.parameters.values):
                parameter = callee.parameters.values[index]
                if isinstance(parameter, Parameter) \
                        and isinstance(parameter.modifier, Token):
                    is_function = \
                        parameter.modifier.type == Token.Type.FUNCTION
                    is_reference = \
                        parameter.modifier.type == Token.Type.REFERENCE
            if not is_function:
                value = self.evaluate(value)
            if not is_reference and isinstance(value, (list, dict)):
                value = deepcopy(value)
            elif isinstance(value, tuple):  # just in case
                value = list(value)
            implicit.append(value)
        self._environment.set('_', implicit, only_this_scope=True)

        # Set parameter as alias of implicit variable.
        for i in range(parameter_length):
            if not isinstance(callee.parameters.values[i], Parameter):
                raise Error.EvaluateError()
            name = callee.parameters.values[i].name.name  # Token
            if name.type != Token.Type.IDENTIFIER:
                raise Error.EvaluateError()
            value = Get([
                Identifier(Token(Token.Type.IDENTIFIER, lexeme='_')),
                Literal(Token(Token.Type.NUMBER, lexeme=str(i)))
            ]) if i < len(implicit) \
            else None
            self._environment.set(name.lexeme, value, only_this_scope=True)

        # Evaluate
        result = self.evaluate(statements)

        self._environment = previous_environment  # Restore scope

        return result, True

    def _set_member(self, target, members, value, operator
                   ):  # pylint: disable=R0912, R0915
        """Set/Modify/Remove a member within variable.

        For example, a.c.1 = 20 is set in
                     {"a": {"b": true, "c": [false, 100]}} .

        1. Caller has members and value.
           - Members: ["a", "c", 1]
           - Value: 20

        2. Caller gets original whole value of "a" from Environment.
           - Original whole value: {"b": true, "c": [false, 100]}

        3. Caller makes block that corresponds to members ["a","c",1].
           That is, it is made that key-value pairs of "a" and its
           value.
           - Block: {"a": {"b": true, "c": [false, 100]}}

        4. Caller call this method.
           - target: {"a": {"b": true, "c": [false, 100]}}

           This method is called as below.
           1st call is done by the above 4th step.
           2nd-4th call is done itself recursively.
           | #   | target                                | members       |
           |-----|---------------------------------------|---------------|
           | 1st | {"a": {"b": true, "c": [false, 100]}} | ["a", "c", 1] |
           | 2nd | {"b": true, "c": [false, 100]}        | ["c", 1]      |
           | 3rd | [false, 100]                          | [1]           |
           | 4th | 100                                   | []            |

           | #   | Returned value                       |
           |-----|--------------------------------------|
           | 4th | 20                                   |
           | 3rd | [false, 20]                          |
           | 2nd | {"b": true, "c": [false, 20]}        |
           | 1st | {"a": {"b": true, "c": [false, 20]}} |

        5. Caller gets the new value of "a" from the returned value:
           {"b": true, "c": [false, 20]}

        6. Caller put it into Environment.

        Args:
            target (Any): Target variable or value.
                          When this method is called from outside,
                          it must be dict.
                          When this method is called from itself
                          recursively, it is dict or list except
                          last call.
                          It must be a value of the latest member
                          at last call.
            members (list[Statement]): Members of the above target
            value (Any): The latest member's value
            operator (Token.Type) Operator's token type

        Returns:
            Any: Variable or Value

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        self._enter_evaluate(None)

        if not isinstance(target, (dict, list)) or len(members) == 0:
            if len(members) > 0:
                self._abort(f'Cannot assign for "{members[0]}"', members[0])
            if operator in self._assign_operations:
                method = self._assign_operations[operator]
                # The following method (_add, _subtract, and so on) may be
                # raise EvaluateError without error-message.
                # However, in present, error position is unknown.
                # This is resolved in the previous recursive caller.
                value = method(target, value, self._config)
            if operator == Token.Type.REMOVE:
                value = Environment.UNDEFINED  # #1
            if isinstance(value, CalleeRegistry):
                value = CalleeRegistry(value.callee,
                                       value.environment,
                                       True)  # Reference
            self._leave_evaluate(None)
            return value

        member = members.pop(0)
        evaluated_member = self.evaluate(member)

        if isinstance(evaluated_member, bool):  # Avoid boolean
                                    # Note that isinstance(True, int) is True.
            self._abort(f'Boolean "{member}" is not suitable', member)

        if isinstance(evaluated_member, float):
            if evaluated_member % 1 != 0:
                self._abort(f'Floating-point number "{member}" is invalid',
                            member)
            evaluated_member = int(evaluated_member)
        if isinstance(evaluated_member, int) and isinstance(target, list):
            length = len(target)
            if evaluated_member < 0:  # Backward access
                evaluated_member += length
            if evaluated_member < 0 or evaluated_member >= length:
                self._abort(f'Index "{evaluated_member}" is out of range',
                            member)
            try:
                value = self._set_member(target[evaluated_member],
                                        members, value, operator)
            except Error.EvaluateError:
                self._abort(f'Cannot evaluate "{member}"', member)
            if value == Environment.UNDEFINED:  # #1
                del target[evaluated_member]
            else:
                target[evaluated_member] = value
            self._leave_evaluate(None)
            return target

        if not isinstance(target, dict):
            self._abort(f'Invalid access for {member}', member)
        if isinstance(evaluated_member, int):
            evaluated_member = str(evaluated_member)
        if not isinstance(evaluated_member, str):
            self._abort(f'Cannot assign for "{member}"', member)
        if evaluated_member not in target:
            if len(members) > 0:
                self._abort(f'Cannot assign for "{members[0]}"',
                            members[0])
            if operator != Token.Type.REMOVE:
                target[evaluated_member] = value
        else:
            try:
                value = self._set_member(target[evaluated_member],
                                        members, value, operator)
            except Error.EvaluateError:
                self._abort(f'Cannot evaluate "{member}"', member)
            if value == Environment.UNDEFINED:  # #1
                del target[evaluated_member]
            else:
                target[evaluated_member] = value
        self._leave_evaluate(None)
        return target

    def _abort(self, message, statement=None, eliminate_tag=False):
        """Abort Evaluator.

        Print an error message and raise Exception.

        Args:
            message (str): Error message
            statement (Statement or NoneType, optional): Statement
                    where error occurs. It is used to get location.
                    None is given when cause is not Statement.
            eliminate_tag (bool, optional): True if tag is not needed,
                                            False otherwise.
                                            The default is False

        Raises:
            EvaluateError: This exception always happen when this method
                           is called.
        """
        raise Error.make_evaluate_error(message, statement, self._config,
                                        eliminate_tag)

    @staticmethod
    def _add(left, right, config=None):  # pylint: disable=R0911, R0912
        """Add

        | left \\ right | block | array | string | int     | float   | boolean | null    |
        |---------------|-------|-------|--------|---------|---------|---------|---------|
        | block         | block | array | ERROR  | ERROR   | ERROR   | ERROR   | block   |
        | array         | array | array | array  | array   | array   | array   | array   |
        | string        | ERROR | array | string | string  | string  | string  | string  |
        | int           | ERROR | array | string | int     | float   | boolean | int     |
        | float         | ERROR | array | string | float   | float   | boolean | float   |
        | boolean       | ERROR | array | string | boolean | boolean | boolean | boolean |
        | null          | block | array | string | int     | float   | boolean | null    |

        For example, {"a": 3, "b": 100} + {"0": "x"}
                                       --> {"a": 3, "b": 100, "0": "x"}
                     {"a": 3, "b": 100} + {"a": -5}
                                       --> {"a": -2, "b": 100}
                     {"a": 3} + [3, "a"] --> [{"a": 3}, 3, "a"]
                     [3, "a"] + {"a": 3} --> [3, "a", {"a": 3}]
                     {"a": 3} + "a" --> ERROR
                     [3, "a"] + true --> [3, "a", true]
                     true + [3, "a"] --> [true, 3, "a"]
                     [3, "a"] + [true, false] --> [3, "a", [true, false]]
                     3 + null --> 3
                     3 + "a" --> "3a"
                     3 + false --> true  # 3 is equivalent to true.
                                 # Then true + false --> true or false.
                     3 + 2 --> 5

        Raises:
            EvaluateError: It is happen if the operator/operand is
                           invalid or array/block size reaches limit.
        """
        max_array_size = Config.get_max_array_size_alt(config)
        # Result is array.
        is_left_array = isinstance(left, list)
        is_right_array = isinstance(right, list)
        if is_left_array:
            if len(left) + 1 > max_array_size:
                raise Error.EvaluateError()
            new_array = left.copy()
            new_array.append(right)
            return new_array
        if is_right_array:
            if 1 + len(right) > max_array_size:
                raise Error.EvaluateError()
            new_array = right.copy()
            new_array.insert(0, left)
            return new_array
        # Result is another operand.
        if left is None:
            return right
        if right is None:
            return left
        # Result is block.
        is_left_block = isinstance(left, dict)
        is_right_block = isinstance(right, dict)
        if is_left_block and is_right_block:
            length = len(left)
            new_block = left.copy()
            for right_name, right_value in right.items():
                if right_name in new_block:
                    new_block[right_name] = \
                            Evaluator._add(new_block[right_name], right_value,
                                           config)
                else:
                    length += 1
                    if length > max_array_size:
                        raise Error.EvaluateError()
                    new_block[right_name] = right_value
            return new_block
        if is_left_block or is_right_block:
            raise Error.EvaluateError()
        # Result is string.
        if isinstance(left, str):
            return f'{left}{Evaluator.make_str(right, config=config)}'
        if isinstance(right, str):
            return f'{Evaluator.make_str(left, config=config)}{right}'
        # Result is boolean.
        if isinstance(left, bool) or isinstance(right, bool):
            return Evaluator.is_truthy(left) or Evaluator.is_truthy(right)
        # Result is int or float.
        if Evaluator._is_numbers(left, right):
            return left + right
        raise Error.EvaluateError()

    @staticmethod
    def _subtract(left, right,  # pylint: disable=R0911, R0912, R0914
                  config=None):
        """Subtract

        | left \\ right | block | array  | string | int   | float | boolean | null    |
        |---------------|-------|--------|--------|-------|-------|---------|---------|
        | block         | block | #      | block  | ERROR | ERROR | ERROR   | block   |
        | array         | array | array  | array  | array | array | array   | array   |
        | string        | ERROR | *      | string | ERROR | ERROR | ERROR   | string  |
        | int           | ERROR | ERROR  | ERROR  | int   | float | ERROR   | int     |
        | float         | ERROR | ERROR  | ERROR  | float | float | ERROR   | float   |
        | boolean       | ERROR | ERROR  | ERROR  | ERROR | ERROR | ERROR   | boolean |
        | null          | ERROR | ERROR  | ERROR  | ERROR | ERROR | ERROR   | null    |

        # is block or ERROR
        * is string or ERROR

        For example, {"a": 10, "b": 20, "c": 30} - {"b": 5, "c": 10}
                                    --> {"a": 10, "b": 15, "c": 20}
                     {"a": 10, "b": 20} - {"b": 5, "c": 10}
                                    --> {"a": 10, "b": 15, "c": -10}
                     {"a": 10, "b": 20, "c": 30} - ["b", "c"]
                                    --> {"a": 10}
                     {"a": 10, "b": 20, "c": 30} - ["b", "c", 3]
                                    --> ERROR because there is number in array
                     {"a": 10, "b": 20, "c": 30} - "b"
                                    --> {"a": 10, "c": 30}
                     {"a": 10, "b": 20, "c": 30} - "d"
                                    --> {"a": 10, "b": 20, "c": 30}
                     [3, "a", "a"] - "a" --> [3]
                     [3, [100, true]] - [100, true] --> [3]
                     [3, {"a": null}] - {"a": null} --> [3]
                     [3, false, "a"] - true --> [3, false, "a"]
                     "large-dog&small-dog&2cat" - "dog"
                                    --> "large-&small-&2cat"
                     "large-dog&small-dog&2cat" - ["large-", "small-"]
                                    --> "dog&dog&2cat"
                     "large-dog&small-dog&2cat" - 2
                                    --> ERROR
                     "large-dog&small-dog&2cat" - ["large-", 2]
                                    --> ERROR
                     {"a": null} - null --> {"a": null}
                     100 - null --> 100
                     true - null --> true
                     null - "a" --> ERROR

        Raises:
            EvaluateError: It is happen if the operator/operand is
                           invalid or array/block size reaches limit.
        """
        if left is None and right is not None:
            raise Error.EvaluateError()
        # Result is array.
        is_left_array = isinstance(left, list)
        is_right_array = isinstance(right, list)
        if is_left_array:
            new_array = left.copy()
            Evaluator._remove_element_from_array(new_array, right)
            return new_array
        # Result is another operand.
        if right is None:
            return left
        # Result is block.
        is_left_block = isinstance(left, dict)
        is_right_block = isinstance(right, dict)
        if is_left_block:
            if is_right_block:
                max_array_size = Config.get_max_array_size_alt(config)
                new_block = left.copy()
                length = len(new_block)
                for right_name, right_value in right.items():
                    if right_name in new_block:
                        new_block[right_name] = \
                                Evaluator._subtract(new_block[right_name],
                                                    right_value, config)
                    else:
                        length += 1
                        if length > max_array_size:
                            raise Error.EvaluateError()
                        new_block[right_name] = \
                                Evaluator._multiply(-1, right_value, config)
                return new_block
            if is_right_array:
                new_block = left.copy()
                for name in right:
                    if not isinstance(name, str):
                        raise Error.EvaluateError()
                    if name in new_block:
                        del new_block[name]
                return new_block
            if isinstance(right, str):
                if right not in left:
                    return left
                new_block = left.copy()
                del new_block[right]
                return new_block
        elif is_right_block:
            raise Error.EvaluateError()
        # Result is string.
        if isinstance(left, str):
            elements = right if is_right_array else [right]
            for element in elements:
                if not isinstance(element, str):
                    raise Error.EvaluateError()
                left = left.replace(element, '')
            return left
        # Result is int or float.
        if Evaluator._is_numbers(left, right):
            return left - right
        raise Error.EvaluateError()

    @staticmethod
    def _multiply(left, right, config=None):  # pylint: disable=R0911, R0912
        """Multiply

        | left \\ right | block | array  | string | int    | float  | boolean | null |
        |---------------|-------|--------|--------|--------|--------|---------|------|
        | block         | block | ERROR  | ERROR  | ERROR  | ERROR  | ERROR   | null |
        | array         | ERROR | ERROR  | string | array  | array  | ERROR   | null |
        | string        | ERROR | string | ERROR  | string | string | ERROR   | null |
        | int           | ERROR | array  | string | int    | float  | ERROR   | null |
        | float         | ERROR | array  | string | float  | float  | ERROR   | null |
        | boolean       | ERROR | ERROR  | ERROR  | ERROR  | ERROR  | ERROR   | null |
        | null          | null  | null   | null   | null   | null   | null    | null |

        For example, {"a": 2} * {"a": 10, "b": 3} --> {"a": 20, "b": null}
                     {"a": 2} * {"b": 3} --> {"a": null, "b": null}
                     [3, "a"] * 2 --> [3, "a", 3, "a"]
                     [3, "a"] * "|" --> '3|a'
                     [3, "a"] * true -> ERROR
                     false * [3, "a"] --> ERROR
                     "3a" * 2  --> "3a3a"
                     100 * null --> null
                     [3, "a"] * [1, 2] --> ERROR

        Raises:
            EvaluateError: It is happen if the operator/operand is
                           invalid or array/block size reaches limit.
        """
        # Result is null.
        if left is None or right is None:
            return None
        # For boolean
        if isinstance(left, bool) or isinstance(right, bool):
            raise Error.EvaluateError()
        # Result is block.
        max_array_size = Config.get_max_array_size_alt(config)
        if isinstance(left, dict) and isinstance(right, dict):
            new_block = {}
            either = []
            for name in left.keys():
                if name not in right:
                    either.append(name)
                    continue
                new_block[name] = \
                        Evaluator._multiply(left[name], right[name], config)
            for name in right.keys():
                if name not in left:
                    either.append(name)
            if len(new_block) + len(either) > max_array_size:
                raise Error.EvaluateError()
            for name in either:
                new_block[name] = None
            return new_block
        # Result is string x n.
        if isinstance(left, str) and Evaluator._is_number(right):
            return left * int(right)
        if isinstance(right, str) and Evaluator._is_number(left):
            return right * int(left)
        # Result is array (elements x n).
        if isinstance(left, list) and Evaluator._is_number(right) \
                and len(left) * int(right) <= max_array_size:
            return left * int(right)
        if isinstance(right, list) and Evaluator._is_number(left) \
                and len(right) * int(left) <= max_array_size:
            return right * int(left)
        # Result is string.
        if isinstance(left, list) and isinstance(right, str):
            return right.join(Evaluator._make_str_array(left, config=config))
        if isinstance(left, str) and isinstance(right, list):
            return left.join(Evaluator._make_str_array(right, config=config))
        # Result is int/float.
        if Evaluator._is_numbers(left, right):
            return left * right
        raise Error.EvaluateError()

    @staticmethod
    def _divide(left, right, config=None):  # pylint: disable=R0912
        """Divide

        | left \\ right | block | array | string | int   | float | boolean | null  |
        |---------------|-------|-------|--------|-------|-------|---------|-------|
        | block         | #     | ERROR | ERROR  | ERROR | ERROR | ERROR   | ERROR |
        | array         | ERROR | ERROR | ERROR  | ERROR | ERROR | ERROR   | ERROR |
        | string        | ERROR | ERROR | array  | ERROR | ERROR | ERROR   | ERROR |
        | int           | ERROR | ERROR | ERROR  | *     | *     | ERROR   | ERROR |
        | float         | ERROR | ERROR | ERROR  | *     | *     | ERROR   | ERROR |
        | boolean       | ERROR | ERROR | ERROR  | ERROR | ERROR | ERROR   | ERROR |
        | null          | null  | null  | null   | x     | x     | null    | ERROR |

        # is block or ERROR
        * is int or float or ERROR
        x is null or ERROR

        For example, {"a": 2} / {"a": 10, "b": 3} --> {"a": 0.2, "b": null}
                     {"a": 2} / {"b": 3} --> ERROR
                     "a,b,c" / "," --> ["a", "b", "c"]
                     "a,b,c," / "," --> ["a", "b", "c", ""]
                     "a,b,c" / "" --> ["a", ",", "b", ",", "c"]
                     3 / 2 --> 1.5
                     3 / 0 --> ERROR
                     3 / null --> ERROR
                     null / 3 --> null
                     null / 0 --> ERROR

        Raises:
            EvaluateError: It is happen if the operator/operand is
                           invalid or array/block size reaches limit.
        """
        # Result is ERROR.
        if right is None \
                or (Evaluator._is_number(right) and right == 0):
            raise Error.EvaluateError()
        # Result is null.
        if left is None:
            return None
        # Result is block.
        max_array_size = Config.get_max_array_size_alt(config)
        if isinstance(left, dict) and isinstance(right, dict):
            new_block = {}
            for name in left.keys():
                if name not in right:
                    raise Error.EvaluateError()
                new_block[name] = \
                        Evaluator._divide(left[name], right[name], config)
            length = len(new_block)
            for name in right.keys():
                if name not in left:
                    length += 1
                    if length > max_array_size:
                        raise Error.EvaluateError()
                    new_block[name] = None
            return new_block
        # Result is array of string.
        if isinstance(left, str) and isinstance(right, str):
            if right == "":
                if len(left) > max_array_size:
                    raise Error.EvaluateError()
                array = []
                for letter in left:
                    array.append(letter)
            else:
                delimiter_length = len(right)
                count = 1
                index = -delimiter_length
                while index < len(left):
                    try:
                        index = left.index(right, index + delimiter_length)
                    except ValueError:
                        break
                    count += 1
                if count > max_array_size:
                    raise Error.EvaluateError()
                array = left.split(right)
            return array
        # Result is int or float.
        if Evaluator._is_numbers(left, right):
            result = left / right
            if result % 1 == 0:
                result = int(result)
            return result
        raise Error.EvaluateError()

    @staticmethod
    def _modulo(left, right, config=None):
        """Modulo

        | left \\ right | block | array | string | int  | float | boolean | null  |
        |---------------|-------|-------|--------|------|-------|---------|-------|
        | block         | #     | ERROR | ERROR  | ERROR| ERROR | ERROR   | ERROR |
        | array         | ERROR | ERROR | ERROR  | ERROR| ERROR | ERROR   | ERROR |
        | string        | ERROR | ERROR | ERROR  | ERROR| ERROR | ERROR   | ERROR |
        | int           | ERROR | ERROR | ERROR  | *    | *     | ERROR   | ERROR |
        | float         | ERROR | ERROR | ERROR  | *    | *     | ERROR   | ERROR |
        | boolean       | ERROR | ERROR | ERROR  | ERROR| ERROR | ERROR   | ERROR |
        | null          | null  | null  | null   | x    | x     | null    | ERROR |

        # is block or ERROR
        * is int or float or ERROR
        x is null or ERROR

        For example, {"a": 20} % {"a": 6, "b": 3} --> {"a": 2, "b": null}
                     {"a": 2} % {"b": 3} --> ERROR
                     15 % 6 --> 3
                     15 % 0 --> ERROR
                     null % 2 --> null
                     null / 0 --> ERROR
                     5 % null --> ERROR

        Raises:
            EvaluateError: It is happen if the operator/operand is
                           invalid.
        """
        # Result is ERROR.
        if right is None \
                or (Evaluator._is_number(right) and right == 0):
            raise Error.EvaluateError()
        # Result is null.
        if left is None:
            return None
        # Result is block.
        max_array_size = Config.get_max_array_size_alt(config)
        if isinstance(left, dict) and isinstance(right, dict):
            new_block = {}
            for name in left.keys():
                if name not in right:
                    raise Error.EvaluateError()
                new_block[name] = \
                        Evaluator._modulo(left[name], right[name], config)
            length = len(new_block)
            for name in right.keys():
                if name not in left:
                    length += 1
                    if length > max_array_size:
                        raise Error.EvaluateError()
                    new_block[name] = None
            return new_block
        # Result is int or float.
        if Evaluator._is_numbers(left, right):
            result = left % right
            if result % 1 == 0:
                result = int(result)
            return result
        raise Error.EvaluateError()

    @staticmethod
    def _logical_invert(left, right,
                        config=None) -> bool:  # pylint: disable=W0613
        """Invert for "not" operator.

        not true --> false
        not false --> true
        not 0 --> true
        not 10 --> false
        not null --> true
        not "" --> false

        Note that not {"a": 3} is confused as function "not" in Parser.
        So error occurs.
        On the other hand, a = {"a": 3}; return(not a) can be evaluated
        as false.

        Note that not [3] is confused as variable "not" in Parser.
        So error occurs.
        On the other hand, a = [3]; return(not a) can be evaluated
        as false.

        Raises:
            EvaluateError: It is happen if left-hand sided operand is
                           not None.
        """
        if left is None:  # Check just in case even if it is None by Parser.
            return not Evaluator.is_truthy(right)
        raise Error.EvaluateError()

    @staticmethod
    def _logical_and(left, right,
                     config=None) -> bool:  # pylint: disable=W0613
        """Evaluate for "and" operator.

        false and false --> false
        false and true --> false
        true and false --> false
        true and true --> true
        0 and true --> false
        10.5 and true --> true
        "a" and true --> true
        null and true --> false
        true and {"a": 3} --> true
        true and {} --> true
        true and [3] --> true
        true and [] --> true
        """
        return Evaluator.is_truthy(left) and Evaluator.is_truthy(right)

    @staticmethod
    def _logical_or(left, right,
                    config=None) -> bool:  # pylint: disable=W0613
        """Evaluate for "or" operator.

        false or false --> false
        false or true --> true
        true or false --> true
        true or true --> true
        1 or false --> true
        "a" or false --> true
        null or false --> false
        false or {} --> true
        false or {"a": 3} --> true
        false or [] --> true
        false or [3] --> true
        """
        return Evaluator.is_truthy(left) or Evaluator.is_truthy(right)

    @staticmethod
    def _is_equal(left, right, config=None) -> bool:  # pylint: disable=W0613
        """Judge for "==" operator.

        "a" == "a" --> true
        [1, 2] == [1, 2] --> true
        [1, 2] == [2, 1] --> false
        {"a": 1, "b": 2} == {"b": 2, "a": 1} --> true
        {"a": 1, "b": 2} == {"a": 1} --> false
        {"a": 1, "b": 2} == [1, 2] --> false
        {"a": 1, "b": 2} == true --> true (using truthy)
        """
        if Evaluator._is_same_both_type(left, right):
            return left == right
        if isinstance(left, bool) or isinstance(right, bool):
            return Evaluator.is_truthy(left) == Evaluator.is_truthy(right)
        return False

    @staticmethod
    def _is_not_equal(left, right, config=None) -> bool:
        """Judge for "!=" operator."""
        return not Evaluator._is_equal(left, right, config)

    @staticmethod
    def _is_less_than(left, right,
                      config=None) -> bool:  # pylint: disable=W0613
        """Judge for "<" operator.

        Raises:
            EvaluateError: It is happen if the given values are not
                           number.
        """
        Evaluator._make_sure_numbers(left, right)
        return left < right

    @staticmethod
    def _is_less_than_or_equal(left, right,
                               config=None) -> bool:  # pylint: disable=W0613
        """Judge for "<=" operator.

        Raises:
            EvaluateError: It is happen if the given values are not
                           number.
        """
        Evaluator._make_sure_numbers(left, right)
        return left <= right

    @staticmethod
    def _is_greater_than(left, right,
                         config=None) -> bool:  # pylint: disable=W0613
        """Judge for ">" operator.

        Raises:
            EvaluateError: It is happen if the given values are not
                           number.
        """
        Evaluator._make_sure_numbers(left, right)
        return left > right

    @staticmethod
    def _is_greater_than_or_equal(left, right,
                                  config=None) -> bool:  # pylint: disable=W0613
        """Judge for ">=" operator.

        Raises:
            EvaluateError: It is happen if the given values are not
                           number.
        """
        Evaluator._make_sure_numbers(left, right)
        return left >= right

    @staticmethod
    def _is_contained(left, right,
                      config=None) -> bool:  # pylint: disable=W0613
        """Judge for "in" operator.

        "b" in ["a", "b", "c"] --> true
        "d" in ["a", "b", "c"] --> false
        1 in [1, 2, "c"] --> true
        true in [1, true, "c"] --> true
        [2, 3] in [1, [2,3], "c"] --> true
        {"a": 2, "b": false} in [1, {"b": false, "a": 2}, "c"] --> true
        "x" in {"x": 3, "y": 10} --> true
        {"x": 3} in {"x": 3, "y": 10} --> true
        {"x": 3, "y": 10} in {"x": 3, "y": 10} --> true
        "dog" in "cat&dog&bird" --> true
        "23" in "123" --> true
        23 in "123" --> ERROR
        1 in 5 --> ERROR
        [1, 2, "c"] in 1 --> ERROR
        true in true --> ERROR
        null in null --> ERROR

        Raises:
            EvaluateError: It is happen if illegal values are given.
        """
        if isinstance(left, dict) and isinstance(right, dict):
            for name, value in left.items():
                if name not in right or right[name] != value:
                    return False
            return True
        if isinstance(right, str) and not isinstance(left, str):
            raise Error.EvaluateError()
        if isinstance(right, (dict, list, str)):
            return left in right
        raise Error.EvaluateError()

    @staticmethod
    def _remove_element_from_array(elements: list, element):
        """Remove the given element from array."""
        while True:
            try:
                elements.remove(element)
            except ValueError:
                break

    @staticmethod
    def is_truthy(value) -> bool:
        """Evaluate as boolean.

        Args:
            value (Any): A value that is evaluated as boolean.

        Returns:
            bool: The evaluated result
                  - None, False, 0, 0.0 --> False
                  - Other --> True
                    (Note that "0" is True.)
        """
        if value is None:
            return False
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != 0
        return True

    @staticmethod
    def _is_same_both_type(left, right) -> bool:
        return type(left) == type(right)  # pylint: disable=C0123

    @staticmethod
    def _is_number(value) -> bool:
        # Note that isinstance(True, int) and isinstance(False, int) is True.
        # So we must check that the given value is not bool.
        return not isinstance(value, bool) and isinstance(value, (int, float))

    @staticmethod
    def _is_numbers(left, right) -> bool:
        return Evaluator._is_number(left) and Evaluator._is_number(right)

    @staticmethod
    def _make_sure_numbers(left, right):
        """Make sure that the arguments are number.

        When the arguments, left and right, aren't number, EvaluateError
        is raised.

        Raises:
            EvaluateError: Exception
        """
        if not Evaluator._is_numbers(left, right):
            raise Error.EvaluateError()

    @staticmethod
    def _make_str_array(values, config=None, is_member=False):
        """Make an array of string with Evaluator.make_str.

        Args:
            values (list[Any]: An array of values.
            config (Config or NoneType, optional): Configuration if
                                                   needed.
            is_member (bool, optional): True if the above value is a
                                        member of block or array,
                                        False otherwise.
                                        The default is False.

        Returns:
            list[str]: an array of string

        Raises:
            EvaluateError: It is happen if number is Infinity or NaN
                           without permission of Configuration.
        """
        strings = []
        for value in values:
            string = Evaluator.make_str(value, config, is_member)
            strings.append(string)
        return strings

    @staticmethod
    def _make_escape_sequence(value: str) -> str:
        """Make escape sequence in string.
        
        Args:
            value (str): The original string

        Returns:
            str: The modified string
        """
        string = value
        index = 0
        length = len(value)
        while index < length:
            letter = string[index]
            if letter in Evaluator._REPLACED_LETTERS:
                string = string[:index] \
                         + '\\' + Evaluator._REPLACED_LETTERS[letter] \
                         + string[index+1:]
                index += 1
                length += 1
            index += 1
        return string

    @staticmethod
    def make_str(value, config=None, is_member=False, is_escape=True
                 ): # pylint: disable=R0911
        """Make string from any value.

        In this class, values are treated as Python native values.
        There are the following difference between VivJson and
        Python.
            - null : None
            - true : True
            - false : False
        Thus, this method is used instead of str function of Python.

        Args:
            value (Any): A value for converting to string.
                         int, float, bool, str, list, dict, None, or
                         Statement.
            config (Config or NoneType, optional): Configuration if
                                                   needed.
            is_member (bool, optional): True if the above value is a
                                        member of block or array,
                                        False otherwise.
                                        The default is False.
            is_escape (bool, optional): True if escape sequence is
                                        enabled, False otherwise.
                                        When this is True, control
                                        character, the double
                                        quotation mark, or reverse
                                        solidus is modified as
                                        escape sequence.
                                        The default is True.

        Returns:
            str: The given value as string

        Raises:
            EvaluateError: It is happen if number is Infinity or NaN
                           without permission of Configuration.
        """
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return 'true' if value else 'false'
        if isinstance(value, (list, tuple)):
            data = Evaluator._make_str_array(value, config, True)
            return f'[{", ".join(data)}]'
        if isinstance(value, dict):
            text = ''
            delimiter = ''
            for name, data in value.items():
                name = Evaluator.make_str(name, config, True)
                data = Evaluator.make_str(data, config, True)
                text = f'{text}{delimiter}{name}: {data}'
                delimiter = ', '
            return f'{{{text}}}'
        if isinstance(value, str):
            if is_escape:
                value = Evaluator._make_escape_sequence(value)
            return f'"{value}"' if is_member else value
        if isinstance(value, float):
            if isinf(value):
                infinity = Config.get_infinity_alt(config)
                if isinstance(infinity, str):
                    sign = '-' if value == float('-inf') else ''
                    return f'{sign}{infinity}'
                raise Error.EvaluateError()
            if isnan(value):
                nan = Config.get_nan_alt(config)
                if nan is not None:
                    return nan
                raise Error.EvaluateError()
        return str(value)
