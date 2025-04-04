"""API of VivJson

- Viv.run: Run VivJson's code or deserialize JSON objects.
- Viv.parse: Parse VivJson's code and JSON object.
- Viv.parse_file: Parse a file that contains VivJson's code or JSON object.
- Viv.parse_text: Parse a text that is VivJson's code or JSON object.
- Viv.make_instance: Make a class instance.
- Viv.make_string: Convert into String. Serialize into JSON string.

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

# pylint: disable=W0718, W4901, C0411

from dataclasses import dataclass
import os
from typing import Optional, TypeVar
from .config import Config
from .environment import Environment
from .error import Error
from .evaluator import Evaluator
from .parser import Parser
from .statement import Array, Blank, Block, Call, CalleeRegistry, \
                       Identifier, Injection, Literal, Return, \
                       Set, Statement, Value
from .tokens import Token

class Viv:
    """Viv class

    Attributes:
        EXTENSIONS (tuple[str]): The effective file extensions.
    """
    EXTENSIONS = ('.viv', '.json')

    @staticmethod
    def run(*parameters):
        """Run VivJson's code or deserialize JSON objects.

        For example,
        - run("a:3,b:2,return(a+b)")
        - run(["{a:3,b:2}", "{return(a+b)}"])
        - run(["x=", "+", "{a:3,b:2}", "return(x.a+x.b)"])
        - run("test.viv")
        - run(["test.viv"])
        - run("data.json", "calc.viv")
        - run(["data.json", "calc.viv"])
        - run("{a:3,b:2}", "calc.viv")
        - run("x/", Config(enable_stderr=True))  # Error at run-time
        - run({"x":[1,2],"y":True},"return(if(y){:=x[0]}else{:=x[1]})")

        Args:
            parameters (Any): VivJson's codes, JSON values,
                              file paths, variables,
                              Parsed objects, a class instance,
                              a method object, or a Configuration.
                            str: A VivJson's code, a JSON value, or
                                 a file path
                            list[Any] or tuple[Any]: Some VivJson's
                                                codes, JSON values,
                                                some file paths,
                                                variables, or
                                                Parsed objects
                            dict: Some variables that are name/value
                                  pairs.
                            Json: JSON object
                            Parsed: The parsed object that is generated
                                    with Viv.parse, Viv.parse_text, or
                                    Vir.parse_file method.
                            Instance: Class instance. It is passed
                                      through toward output.
                            Method: Calling class method.
                                    This object has 2 members.
                                    "name" is class method name.
                                    "arguments" is its arguments.
                            Config: Configuration

        Returns:
            Any, str: Result and Error message.
                      1st value: Result of the given codes if success,
                                 None otherwise
                      2nd value: "" if success,
                                 Error message otherwise.
        """
        # Multiple parameters are represented as tuple.
        # | Caller of this method   | parameters            |
        # |-------------------------|-----------------------|
        # | run("x = 3")            | ("x = 3",)            |
        # | run("x = 3", "y = 5")   | ("x = 3", "y = 5")    |
        # | run(["x = 3", "y = 5"]) | (["x = 3", "y = 5"],) |
        parsed, config, error_message = Viv._parse_internal(parameters)
        if error_message != '':
            return None, error_message

        # Evaluate.
        value, error_message = Viv._run_internal(parsed, config)
        if error_message != '':
            return None, error_message
        value = Viv._collect_only_valid_elements(value)
        if value == Environment.UNDEFINED:
            return None, Viv.report_error('The returned value is invalid')
        return value, ''

    @staticmethod
    def parse(*parameters):
        """Parse VivJson's code and JSON object.

        For example,
        - parse("a:3,b:2,return(a+b)")
        - parse(["{a:3,b:2}", "{return(a+b)}"])
        - parse(["x=", "+", "{a:3,b:2}", "return(x.a+x.b)"])
        - parse("test.viv")
        - parse(["test.viv"])
        - parse("data.json", "calc.viv")
        - parse(["data.json", "calc.viv"])
        - parse("{a:3,b:2}", "calc.viv")
        - parse("x/", Config(enable_stderr=True))  # Error at run-time
        - parse({"x":[1,2],"y":True},"return(if(y){:=x[0]}else{:=x[1]})")

        Args:
            parameters (Any): VivJson's codes, JSON values,
                              file paths, variables,
                              Parsed objects, a class instance,
                              a method object, or a Configuration.
                            str: A VivJson's code, a JSON value, or
                                 a file path
                            list[Any] or tuple[Any]: Some VivJson's
                                                codes, JSON values,
                                                some file paths,
                                                variables, or
                                                Parsed objects
                            Json: JSON object
                            dict: Some variables that are name/value
                                  pairs.
                            Parsed: The parsed object that is generated
                                    with this method. It is passed
                                    through toward output.
                            Instance: Class instance. It is passed
                                      through toward output.
                            Method: Class method information. It is
                                    passed through toward output.
                            Config: Configuration

        Returns:
            Parsed or NoneType, str: Parsed object of script and
                                     Error message.
                                   1st value: Parsed object if success,
                                              None otherwise
                                              Parsed object has
                                              statements of the given
                                              codes 
                                   2nd value: "" if success,
                                              Error message otherwise.
        """
        # Multiple parameters are represented as tuple.
        # | Caller of this method     | parameters            |
        # |---------------------------|-----------------------|
        # | parse("x = 3")            | ("x = 3",)            |
        # | parse("x = 3", "y = 5")   | ("x = 3", "y = 5")    |
        # | parse(["x = 3", "y = 5"]) | (["x = 3", "y = 5"],) |
        parsed, _, error_message = Viv._parse_internal(parameters)
        return parsed, error_message

    @staticmethod
    def _parse_internal(parameters):  # pylint: disable=R0912, R0914, R0915
        """Parse VivJson's code and JSON object.

        Args:
            parameters (list or tuple): VivJson's codes, JSON values,
                                        file paths, variables, Parsed
                                        objects, a class instance,
                                        a method object,
                                        or a Configuration.

        Returns:
            Parsed or NoneType, Config or NoneType, str:
                        Parsed object of script, Configuration, and
                        Error message.
                        1st value: Parsed object if paring is success,
                                   None otherwise.
                                   Parsed object has statements of
                                   the given codes 
                        2nd value: Configuration if it is given,
                                   None otherwise
                        3rd value: "" if success,
                                   Error message otherwise.
        """
        extracted_parameters, instance, config = \
                                        Viv._extract_parameters(parameters)
        if extracted_parameters is None:
            return None, config, Viv.report_error('Invalid parameter')

        # Concatenate if + option is given.
        targets, error_message = \
                        Viv._concatenate_parameters(extracted_parameters)
        if error_message != '':
            return None, config, error_message

        # Parse the given target.
        statements_array = []
        for target in targets:
            # target[0]: index of the given argument
            # target[1]: parameter
            statements = None
            error_message = ''
            if isinstance(target[1], dict):
                location = Viv._get_argument_text(target[0])
                statements = []
                for name, value in target[1].items():
                    if not isinstance(name, str) \
                            or not Viv._is_valid_type(value):
                        return None, config, Viv.report_error(
                                    f'Invalid parameter "{name}: {value}"')
                    statements.append(Injection(name, value, location))
            elif isinstance(target[1], Parsed):
                statements = target[1].statements
            elif Viv._get_file_extension(target[1]) is not None:
                parsed, error_message = Viv.parse_file(target[1], config)
                if parsed is not None:
                    statements = parsed.statements
            else:
                argument_index = None if len(targets) == 1 else target[0]
                text = None
                config_ext = None
                if isinstance(target[1], Json):
                    text = target[1].value
                    config_ext = Config() if config is None \
                                 else config.clone()
                    config_ext.enable_only_json()
                else:
                    text = target[1]
                    config_ext = config
                parsed, error_message = \
                        Viv.parse_text(text, config_ext, argument_index)
                if parsed is not None:
                    statements = parsed.statements
            if error_message != '':
                return None, config, error_message
            if not isinstance(statements, list):
                return None, config, Viv.report_error('No statement')
            statements_array.append(statements)

        # Collect implicit variables and fix them.
        implicit_variables = []
        for index, statements in enumerate(statements_array):
            if Viv._is_setting_implicit_variable(statements):
                implicit_variables.append(index)
        count = len(implicit_variables)
        if count >= 2:
            new_index = 0
            for index, statements in enumerate(statements_array):
                if index in implicit_variables:
                    Viv._fix_setting_implicit_variable(statements, new_index)
                    new_index += 1

            # Insert "_ = [null, ...]" before each assignment,
            # such as "_[0] = 1".
            identifier = Identifier(Token(Token.Type.IDENTIFIER, lexeme='_'))
            value = Array([Literal(Token(Token.Type.NULL))] * count)
            statements = [Set([identifier], Token(Token.Type.SET), value)]
            statements_array.insert(0, statements)

        # Concatenate statements.
        whole_statements = []
        for statements in statements_array:
            whole_statements.extend(statements)

        # Viv.print_statements(whole_statements)

        return Parsed(whole_statements, instance), config, ''

    @staticmethod
    def parse_file(file_path: str, config=None):
        """Parse a file.

        JSON value and VivJson's code can be parsed.

        Args:
            file_path (str): The path of file that has JSON value or
                             VivJson's code
            config (Config or NoneType, optional): Configuration if
                                                   needed,
                                                   None otherwise.

        Returns:
            Parsed or NoneType, str: Parsed object of script and
                                     Error message.
                                   1st value: Parsed object if success,
                                              None otherwise.
                                              Parsed object has
                                              statements of the given
                                              codes 
                                   2nd value: "" if success,
                                              Error message otherwise.
        """
        extension = Viv._get_file_extension(file_path)
        if extension is None:
            return None, Viv.report_error(f'"{file_path}" is invalid.')
        file_name = os.path.basename(file_path)

        code = None
        with open(file_path, encoding='utf-8') as file:
            code = file.read()

        if code is None:
            return None, Viv.report_error(
                                    f'Cannot read code from "{file_name}".')

        if extension == '.json':
            config_ext = Config() if config is None else config.clone()
            config_ext.enable_only_json()
            config = config_ext

        parser = Parser(code, file_name, config)
        error_message = ''
        try:
            statements = parser.parse()
            return Parsed(statements, None), ''
        except (Error.LexError, Error.ParseError) as e:
            error_message = str(e)
        except Exception as e:
            error_message = Viv.report_error(str(e))
        return None, error_message

    @staticmethod
    def parse_text(text: str, config=None, argument_index=None):
        """Parse a text.

        JSON value and VivJson's code can be parsed.

        Args:
            text (str): Text that is JSON value or VivJson's code
            config (Config or NoneType, optional): Configuration if
                                                   needed,
                                                   None otherwise.
            argument_index (int, optional): Argument index (0~)

        Returns:
            Parsed or NoneType, str: Parsed object of script and
                                     Error message.
                                   1st value: Parsed object if success,
                                              None otherwise
                                              Parsed object has
                                              statements of the given
                                              codes 
                                   2nd value: "" if success,
                                              Error message otherwise.
        """
        if not isinstance(text, str):
            return None, Viv.report_error(f'"{text}" is not string.')

        medium = None if argument_index is None \
                    else Viv._get_argument_text(argument_index)
        parser = Parser(text, medium, config)
        error_message = ''
        try:
            statements = parser.parse()
            return Parsed(statements, None), ''
        except (Error.LexError, Error.ParseError) as e:
            error_message = str(e)
        except Exception as e:
            error_message = Viv.report_error(str(e))
        return None, error_message

    @staticmethod
    def make_instance(*parameters):
        """Make a class instance.

        This method runs the given parameters as Constructor.
        Then its result will be class instance.

        For example, a class method is called as below.

        code = "function test(x, y) {" \
               "  z = x.a + x.b.1 + y" \
               "  return(z)" \
               "}"
        map_x = {"a": 100, "b": [1.0, 2.0]}
        instance, error_message = Viv.make_instance(code)
        result, error_message = \
                Viv.run(instance, Method("test", [map_x, 3]))
        print(result)  // 105.0

        Args:
            parameters (Any): VivJson's codes, JSON values,
                              file paths, variables,
                              Parsed object, or a Configuration
                            str: A VivJson's code, a JSON value, or
                                 a file path
                            list[Any] or tuple[Any]: Some VivJson's
                                                codes, JSON values,
                                                some file paths,
                                                variables, or
                                                Parsed objects
                            Json: JSON object
                            dict: Some variables that are name/value
                                  pairs.
                            Parsed: The parsed object that is generated
                                    with this method. It is passed
                                    through toward output.
                            Config: Configuration

                            Even if the class instance is contained,
                            it is ignored.
        Returns:
            Instance or NoneType, str: Class instance and Error message
                                1st value: Class instance if success,
                                           None otherwise.
                                2nd value: "" if success,
                                           Error message otherwise.
        """
        # Multiple parameters are represented as tuple.
        # | Caller of this method             | parameters            |
        # |-----------------------------------|-----------------------|
        # | make_instance("x = 3")            | ("x = 3",)            |
        # | make_instance("x = 3", "y = 5")   | ("x = 3", "y = 5")    |
        # | make_instance(["x = 3", "y = 5"]) | (["x = 3", "y = 5"],) |
        parsed, config, error_message = Viv._parse_internal(parameters)
        if error_message != '':
            return None, error_message

        if parsed is None or not isinstance(parsed.statements, list):
            return None, Viv.report_error('Invalid statement/value')
        block = Block(parsed.statements, Block.CLASS_CONSTRUCTOR)

        evaluator = Evaluator(config)
        try:
            evaluator.evaluate(block)
        except Error.EvaluateError as e:
            return None, str(e)
        except Exception as e:
            return None, Viv.report_error(str(e))
        return Instance(evaluator), ''

    @staticmethod
    def _run_internal(parsed, config=None):
        """Run VivJson with statements.

        Args:
            parsed (Parsed): Parsed object
            config (Config or NoneType, optional): Configuration if
                                                   needed,
                                                   None otherwise.

        Returns:
            Any, str: Returned value of script and Error message.
                      1st value: Returned value if success,
                                 None otherwise. (None may be
                                 returned even if success.)
                      2nd value: "" if success,
                                 Error message otherwise.
        """
        if parsed is None or not isinstance(parsed.statements, list):
            return None, Viv.report_error('Invalid statement/value')
        block = Block(parsed.statements, Block.ANONYMOUS_FUNCTION)

        evaluator = None
        if isinstance(parsed.instance, Instance) \
                and isinstance(parsed.instance.evaluator, Evaluator):
            evaluator = parsed.instance.evaluator
        else:
            evaluator = Evaluator(config)

        result = None
        try:
            result = evaluator.evaluate(block)
        except Error.EvaluateError as e:
            evaluator.rewind_after_abort()
            return None, str(e)
        except Exception as e:
            evaluator.rewind_after_abort()
            return None, Viv.report_error(str(e))
        return result, ''

    @staticmethod
    def print_statements(statements, add_class_name=False, config=None):
        """Print statements.

        Args:
            statements (list[Statement] or Block): Statements of script
            add_class_name (bool, optional): Class name is added to
                                        each statement if this is True.
                                        The default is False.
            config (Config or NoneType, optional): Configuration if
                                                   needed,
                                                   None otherwise.
        """
        if isinstance(statements, Block):
            statements = statements.values
        if not isinstance(statements, list):
            return

        for statement in statements:
            if isinstance(statement, Block):
                Viv.print_statements(statement)
                continue
            if isinstance(statement, Blank):
                continue

            string = Viv.make_string(statement, config=config)

            if isinstance(add_class_name, bool) and add_class_name:
                string = f'{statement.__class__.__name__}({string})'

            print(string)

    @staticmethod
    def make_string(value, config=None):
        """Convert a value into string. Serialize a value into JSON string.

        Configuration is available for Infinity and NaN (Not a Number).
        When it is not setting, "" (empty) is returned.

        Args:
            value (Any): Value
            config (Config or NoneType, optional): Configuration if
                                                   needed,
                                                   None otherwise.

        Returns:
            str: Converted value
        """
        string = ''
        try:
            string = Evaluator.make_str(value, config=config)
        except (Error.EvaluateError, Exception):
            pass
        return string

    @staticmethod
    def report_error(error_message: str, enable_stderr=False) -> str:
        """Reports Error.
   
        The formatted error is returned.
        The formatted error contains Tag looks like [xxxx].
        It is outputted into stderr when the argument "enableStderr" is
        true. 

        Args:
            error_message (str): Error message
            enable_stderr (bool, optional): Enablement of stderr. When
                                            it is true, the formatted
                                            error is outputted into
                                            stderr.
                                            The default is False.

        Returns:
            str: The formatted error
        """
        config = Config(enable_stderr=enable_stderr)
        return Error.report("", error_message, config=config)

    @staticmethod
    def _get_file_extension(word):
        """Get file extension if the given word is file path.

        Args:
            word (str): The file path or code

        Returns:
            str or NoneType: a file extension (one of the EXTENSIONS)
                             if the given word is file path,
                             None otherwise
        """
        if not isinstance(word, str):
            return None
        _, ext = os.path.splitext(word)
        ext = ext.lower()
        if ext not in Viv.EXTENSIONS:
            return None
        if not os.path.exists(word):
            return None
        return ext

    @staticmethod
    def _get_argument_text(index: int) -> str:
        """Get text message of argument index.

        Args:
            index (int): Argument index

        Returns:
            str: Text message of the given argument index
        """
        suffixes = ('st', 'nd', 'rd')
        suffix = suffixes[index] if index < len(suffixes) else 'th'
        index += 1
        return f'{index}{suffix} argument'

    @staticmethod
    def _extract_parameters(parameters):  # pylint: disable=R0912
        """Extract parameters.

        Args:
            parameters (list or tuple): VivJson's codes, JSON values,
                              file paths, variables,
                              Parsed objects, a class instance,
                              a method object, or a Configuration.

        Returns:
            list or NoneType, Instance or NoneType, Config or NoneType:
                        Extracted parameters and Configuration.
                        1st value: Extracted parameters if success,
                                   None otherwise.
                        2nd value: Class instance if it is given,
                                   None otherwise
                        3rd value: Configuration if it is given,
                                   None otherwise
        """
        instance = None
        for parameter in parameters:
            if isinstance(parameter, Instance):
                instance = parameter
                break

        extracted_parameters = []
        config = None
        for parameter in parameters:  # pylint: disable=R1702
            if isinstance(parameter, Instance):
                pass
            elif isinstance(parameter, (list, tuple)):
                extracted_parameters.extend(parameter)
            elif isinstance(parameter, (str, dict, Json, Parsed)):
                extracted_parameters.append(parameter)
            elif isinstance(parameter, Config):
                config = parameter
            elif isinstance(parameter, Method):
                ret = None
                if instance is not None and instance.evaluator is not None \
                        and isinstance(parameter.name, str) \
                        and parameter.name[0] != "_" \
                        and isinstance(parameter.arguments, (list, tuple)):
                    try:
                        value = instance.evaluator.get(parameter.name)
                        if isinstance(value, CalleeRegistry):
                            call = Viv._make_call(parameter)
                            if call is not None:
                                ret = Return(Token(Token.Type.RETURN), call)
                    except Error.EvaluateError:
                        pass
                if ret is None:
                    return None, None, config
                extracted_parameters.append(Parsed([ret], None))
            else:
                return None, None, config
        return extracted_parameters, instance, config

    @staticmethod
    def _concatenate_parameters(parameters):
        """Concatenate if + option is given.

        Args:
            parameters (list): Parameters that may be have "+".

        Returns:
            list[tuple] or NoneType, str: Concatenated parameters and
                                    "" if success,
                                    None and Error message otherwise.
                                    Each concatenated parameter is
                                    a tuple that has index (0-) and 
                                    parameter.
        """
        concatenated = []  # list[tuple], each tuple has index and parameter.
        ahead = None  # NoneType or list[tuple]
        for index, parameter in enumerate(parameters):
            if parameter == '+':
                try:
                    ahead = concatenated.pop()
                except IndexError:
                    return None, Viv.report_error(
                                            'No statement before + option')
                continue
            if ahead is not None:
                if not isinstance(parameter, str):
                    return None, Viv.report_error('Bad data after + option')
                index = ahead[0]
                parameter = ahead[1] + parameter
                ahead = None
            concatenated.append((index, parameter))
        if ahead is not None:
            return None, Viv.report_error('No statement after + option')
        return concatenated, ''

    @staticmethod
    def _make_call(method):
        """Make Call statement.

        Args:
            method (Method): Calling class method.
                             This object has 2 members.
                             "name" is class method name.
                             "arguments" is its arguments.

        Returns:
            Call or NoneType: Call statement if success, None otherwise
        """
        name = Identifier(Token(Token.Type.IDENTIFIER, lexeme=method.name))

        values = []
        for index, argument in enumerate(method.arguments):
            if not Viv._is_valid_type(argument):
                return None
            value = Value(argument, Viv._get_argument_text(index))
            values.append(value)
        return Call(name, Array(values))

    @staticmethod
    def _collect_only_valid_elements(value):
        """Collect only valid elements.

        Valid type: None, bool, int, float, str, list, dict

        Note that tuple is invalid.
        Note that key of dict must be str.

        Args:
            value (Any): Value

        Returns:
            Any: value if success, Environment.UNDEFINED otherwise
        """
        if value is None or isinstance(value, (bool, int, float, str)):
            return value
        if isinstance(value, list):
            fixed = []
            for element in value:
                element = Viv._collect_only_valid_elements(element)
                if element != Environment.UNDEFINED:
                    fixed.append(element)
            return fixed
        if isinstance(value, dict):
            fixed = {}
            for k, v in value.items():
                if not isinstance(k, str):
                    continue
                v = Viv._collect_only_valid_elements(v)
                if v != Environment.UNDEFINED:
                    fixed[k] = v
            return fixed
        return Environment.UNDEFINED

    @staticmethod
    def _is_valid_type(value):  # pylint: disable=R0911
        """Judge whether the given value is valid or not.

        Valid type: None, bool, int, float, str, list, dict

        Note that tuple is invalid.
        Note that key of dict must be str.

        Args:
            value (Any): Value

        Returns:
            bool: True if valid, False otherwise.
        """
        if value is None or isinstance(value, (bool, int, float, str)):
            return True
        if isinstance(value, list):
            for element in value:
                is_valid = Viv._is_valid_type(element)
                if not is_valid:
                    return False
            return True
        if isinstance(value, dict):
            for k, v in value.items():
                if not isinstance(k, str):
                    return False
                is_valid = Viv._is_valid_type(v)
                if not is_valid:
                    return False
            return True
        return False

    @staticmethod
    def _is_setting_implicit_variable(statements):
        """Judge whether it is setting implicit variable or not.

        The implicit variable is "_". Its setting is "_ = ...".

        Args:
            statements (list[Statement]): Statements of script

        Returns:
            bool: True if setting implicit variable,
                  False otherwise.
        """
        return isinstance(statements, list) and len(statements) == 1 \
                and isinstance(statements[0], Set) \
                and isinstance(statements[0].members[0], Identifier) \
                and statements[0].members[0].name.lexeme == '_'

    @staticmethod
    def _fix_setting_implicit_variable(statements, index):
        """Fix implicit variable.

        The original implicit variable is "_". It is fixed as
        "_[index]".

        Args:
            statements (list[Statement]): Statements of script
            index (int): The index of implicit variable.
                         It starts from 0.
        """
        selector = Literal(Token(Token.Type.NUMBER, lexeme=str(index)))
        statements[0].members.insert(1, selector)

@dataclass(frozen=True)
class Json:
    """JSON data class"""
    value: str

@dataclass(frozen=True)
class Instance:
    """Instance data class"""
    evaluator: Evaluator

METHODARG = TypeVar("METHODARG", list, tuple)

@dataclass(frozen=True)
class Method:
    """Method data class"""
    name: str
    arguments: METHODARG

@dataclass(frozen=True)
class Parsed:
    """Parsed data class"""
    statements: list[Statement]
    instance: Optional[Instance]
