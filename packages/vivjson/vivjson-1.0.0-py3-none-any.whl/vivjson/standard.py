"""Standard library for VivJson

- std_if: if (condition) { operations }
- std_do: do { operations }
- std_while: while (condition) { operations }
- std_for: for ( ... ) { operations }
- std_int: int(value)
- std_float: float(value)
- std_string: string(value)
- std_len: len(value)
- std_insert: insert(array, index, value)
- std_strip: strip(value)
- std_type: type(value)
- std_print: print(value [, value, ...])

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

from .config import Config
from .environment import Environment
from .error import Error
from .tokens import Token
from .statement import Array, Binary, Block, CalleeRegistry, \
                       Identifier, Literal, Loop

class Standard:
    """Standard library class

    Attributes:
        PREFIX (str): The prefix of method. It is defined as "std_".
                      Almost methods of this library have general name like
                      "print", "if", and so on. It is confused host language's
                      functions and statements.
                      So this prefix is added: std_print, std_if, ...
    """
    PREFIX = 'std_'

    @staticmethod
    def std_if(evaluator, call, config=None):  # pylint: disable=W0613, R1711
        """if/elseif/else

        if (...) {...} [ elseif (...) {...} ... ] else {...}

        For example,
            if (...) {...}
               ----- -----
                 |     |
                 |   call.arguments.values[1]
               call.arguments.values[0]

            if (...) {...} else {...}
               ----- -----      -----
                 |     |          |
                 |     |        call.arguments.values[3]
                 |     |    call.arguments.values[2] is always true.
                 |   call.arguments.values[1]
               call.arguments.values[0]

            if (...) {...} elif (...) {...} else {...}
               ----- -----      ----- -----      -----
                 |     |          |     |          |
                 |     |          |     |      call.arguments.values[5]
                 |     |          |     |  call.arguments.values[4] is
                 |     |          |     |  always true.
                 |     |          |   call.arguments.values[3]
                 |     |        call.arguments.values[2]
                 |   call.arguments.values[1]
               call.arguments.values[0]

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         2 x n statements.
                            2 x n: condition
                            2 x n + 1: A list of operations as Block
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            Any: Result of Block evaluation

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        length = len(statements)
        if length == 0 or length % 2 != 0:
            raise Error.EvaluateError()

        for index in range(0, length, 2):
            is_satisfied = evaluator.evaluate(statements[index])
            if evaluator.is_truthy(is_satisfied):
                return evaluator.evaluate(statements[index + 1])
        return None

    @staticmethod
    def std_do(evaluator, call, config=None): # pylint: disable=W0613
        """do { operations }

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         1 statement.
                            1st (Block): A list of operations as Block
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            Any: Result of Block evaluation

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        if len(statements) != 1 or not isinstance(statements[0], Block):
            raise Error.EvaluateError()

        true = Literal(Token(Token.Type.TRUE))

        continuous = [Binary(
            Identifier(Token(Token.Type.IDENTIFIER,
                             lexeme=Environment.CONTINUE_NAME)),
            Token(Token.Type.EQ),
            true
        )]

        loop = Loop(call, [true], continuous, statements[0].values,
                    None, None)
        return evaluator.evaluate(loop)

    @staticmethod
    def std_while(evaluator, call, config=None): # pylint: disable=W0613
        """while (condition) { operations }

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         2 statements.
                            1st (Statement): condition
                            2nd (Block): A list of operations as Block
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            Any: Result of Block evaluation

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        if len(statements) != 2 or not isinstance(statements[1], Block):
            raise Error.EvaluateError()

        loop = Loop(call, [statements[0]], [statements[0]],
                    statements[1].values, None, None)
        return evaluator.evaluate(loop)

    @staticmethod
    def std_for(evaluator, call, config=None):
        """for ( ... ) { operations }

        Example:
        - for (init; condition; update) { operations }
        - for (; condition; update) { operations }
        - for (;; update) { operations }
        - for (;;) { operations }
        - for () { operations }
        - for (value in list) { operations }
        - for (init; condition; update; { operations })

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         statements.
                         When a list has 4 statements:
                             1st (Statement): initial operation
                             2nd (Statement): condition
                             3rd (Statement): update operation
                             4th (Block): A list of operations as Block
                         When a list has 2 statements:
                             1st (Binary): value in list
                             2nd (Block): A list of operations as Block
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            Any: Result of Block evaluation

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        loop = None
        if len(statements) == 2:
            if not isinstance(statements[0], Binary) \
                    or not isinstance(statements[0].left, Identifier) \
                    or statements[0].operator.type != Token.Type.IN:
                raise Error.make_evaluate_error(
                    f'{statements[0]} is invalid', statements[0], config)
            if not isinstance(statements[1], Block):
                raise Error.make_evaluate_error(
                    f'{statements[1]} is invalid', statements[1], config)
            data = evaluator.evaluate(statements[0].right)
            condition = Literal(Token(Token.Type.TRUE))
            initial = [condition]
            continuous = [condition]
            operations = statements[1].values
            loop = Loop(call, initial, continuous, operations,
                        statements[0].left, data)
        elif len(statements) == 4:
            if not isinstance(statements[3], Block):
                raise Error.make_evaluate_error(
                    f'{statements[3]} is invalid', statements[3], config)
            initial = [statements[0], statements[1]]
            continuous = [statements[2], statements[1]]
            operations = statements[3].values
            loop = Loop(call, initial, continuous, operations, None, None)
        else:
            raise Error.EvaluateError()
        return evaluator.evaluate(loop)

    @staticmethod
    def std_int(evaluator, call, config=None):  # pylint: disable=W0613
        """int(value)

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         1 statement.
                            1st: A number whose type is int, float,
                                 or string.
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            int: Number whose type is converted to int.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        while len(statements) == 1:  # It isn't loop. It is used for break.
            value = evaluator.evaluate(statements[0])
            if isinstance(value, str):
                try:
                    value = float(value)
                except (ValueError, OverflowError):
                    break
            if isinstance(value, bool) \
                    or not isinstance(value, (int, float)):
                break
            result = 0
            try:
                result = int(value)
            except (ValueError, OverflowError):
                break
            return result
        raise Error.EvaluateError()

    @staticmethod
    def std_float(evaluator, call, config=None): # pylint: disable=W0613
        """float(value)

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         1 statement.
                            1st: A number whose type is int, float,
                                 or string.
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            float: Number whose type is converted to float.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        if len(statements) == 1:
            value = evaluator.evaluate(statements[0])
            if not isinstance(value, bool) \
                    and isinstance(value, (int, float, str)):
                try:
                    return float(value)
                except (ValueError, OverflowError):
                    pass
        raise Error.EvaluateError()

    @staticmethod
    def std_string(evaluator, call, config=None):
        """string(value)

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         1 statement.
                            1st: Any value
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            str: Text that is converted from the given value.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        if len(statements) == 1:
            value = evaluator.evaluate(statements[0])
            return evaluator.make_str(value, config=config)
        raise Error.EvaluateError()

    @staticmethod
    def std_len(evaluator, call, config=None):  # pylint: disable=W0613
        """len(value)

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         1 statement.
                            1st: An array, a block, or a string.
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            int: Length of array, block, or string.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        if len(statements) == 1:
            if isinstance(statements[0], (Array, Block)):
                return len(statements[0].values)
            value = evaluator.evaluate(statements[0])
            if isinstance(value, (dict, list, str)):
                return len(value)
        raise Error.EvaluateError()

    @staticmethod
    def std_insert(evaluator, call, config=None):
        """insert(array, index, value)

        Insert a value into the array.
        Inserted position can be given with "index".

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         3 statements.
                            1st (Array): An array
                            2nd (Statement): An index
                            3rd (Statement): A value
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            NoneType: It is always None.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        if len(statements) >= 3:
            array = evaluator.evaluate(statements[0])
            if not isinstance(array, list):
                raise Error.make_evaluate_error('insert() needs array',
                                                statements[0], config)
            length = len(array)
            if length + 1 <= Config.get_max_array_size_alt(config):
                index = evaluator.evaluate(statements[1])
                if isinstance(index, float):
                    index = int(index)
                if isinstance(index, bool) or not isinstance(index, int):
                    raise Error.make_evaluate_error(
                                    'index of insert() must be number',
                                    statements[1], config)
                if index < -1 * length or index > length:
                    raise Error.make_evaluate_error('out of range',
                                                    statements[1], config)
                value = evaluator.evaluate(statements[2])
                array.insert(index, value)
                return None
        raise Error.EvaluateError()

    @staticmethod
    def std_strip(evaluator, call, config=None): # pylint: disable=W0613
        """strip(value)

        Remove white-space and new line code from the head/tail.
        Double-byte space (Full-width space) is also removed.

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         1 statement.
                            1st: A string.
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            str or NoneType: Type is represented as text format.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        statements = call.arguments.values
        if len(statements) == 1:
            value = evaluator.evaluate(statements[0])
            if isinstance(value, str):
                return value.strip()
        raise Error.EvaluateError()

    @staticmethod
    def std_type(evaluator, call, config=None): # pylint: disable=W0613, R0911
        """type(value)

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         1 statement.
                            1st: Any value.
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            str or NoneType: Type is represented as text format.
                             - "int"
                             - "float"
                             - "string"
                             - "boolean"
                             - "null"
                             - "array"
                             - "block"
                             - "function"
                             None is returned for other type.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        if len(call.arguments.values) != 1:
            raise Error.EvaluateError()
        value = call.arguments.values[0]
        if isinstance(value, Array):
            return "array"
        if isinstance(value, Block):
            return "block"
        value = evaluator.evaluate(value)
        if value is None:
            return "null"
        if isinstance(value, Identifier) \
                and Standard.get_method(value.name.lexeme) is not None:
            return "function"
        if isinstance(value, CalleeRegistry):
            return "function"
        if isinstance(value, list):
            return "array"
        if isinstance(value, dict):
            return "block"
        if isinstance(value, bool):
            return "boolean"
        if isinstance(value, int):
            return "int"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "string"
        return None

    @staticmethod
    def std_print(evaluator, call, config=None):  # pylint: disable=R1711
        """print(value [, value, ...])

        Args:
            evaluator (Evaluator): Evaluator instance
            call (Call): The information of calling.
                         call.arguments.values is a list of
                         statements that have printable values.
            config (Config or NoneType, optional): Configuration if
                                                   needed.

        Returns:
            NoneType: It is always None.

        Raises:
            EvaluateError: It is happen if evaluation is failed.
        """
        texts = []
        for statement in call.arguments.values:
            text = evaluator.make_str(evaluator.evaluate(statement),
                                      config=config, is_escape=False)
            texts.append(text)
        whole_text = ", ".join(texts)
        print(whole_text)
        return None

    @staticmethod
    def get_method(name: str):
        """Get standard library's method.

        Args:
            name (str): Method name

        Returns:
            function or NoneType: Standard library's method if it is
                                  available, None otherwise.
        """
        try:
            method_name = Standard.PREFIX + name
            return getattr(Standard, method_name)
        except AttributeError:
            pass
        return None
