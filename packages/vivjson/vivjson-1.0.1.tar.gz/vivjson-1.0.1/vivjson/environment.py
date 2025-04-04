"""Environment for VivJson

- Environment: Constructor.
- Environment#get
    - Get a variable's value if argument is variable name.
    - Get a block if argument is empty.
      A block has all variable without variables of the prefix "_"
      and definitions of pure function or closure.
    - Get a result value that is given with ":=" statement.
      It is returned if argument is empty and a result value is
      registered.
- Environment#set: Set a variable.
- Environment#remove: Remove a variable.

The following types are stored.

- Host native literal (str, int, float, bool, None)
- Host native array (list)
- Host native block (dict)
- Definition of pure function or closure (CalleeRegistry)
- Variable whose value is standard library's function (Identifier)
- Alias (Get)

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

from .statement import CalleeRegistry

class Environment:
    """Environment class

    Attributes:
        _enclosing (Environment or NoneType): The parent environment.
                                              None is given when this
                                              instance is root.
        _variables (dict): Variable name and value are stored.
        UNDEFINED (tuple): It is used to represent undefined variable.
        RESULT_NAME (str): It is used to assign particular value as
                           result by ':='.
        FUNCTION_RETURN_NAME (str): It is used for "return" statement.
                            Firstly, when anonymous/pure function
                            starts, it creates this variable whose
                            value is UNDEFINED.
                            Secondly, "return" statement sets value
                            and evaluation goes back until finishing
                            function. When the returned value is
                            given like "return(xxxx)", its value is
                            set. Otherwise, this name is set as
                            value.
                            For example, the function "test" creates
                            this variable. Then "return 'zero'" sets
                            "zero" into this variable and evaluation
                            goes back to assignment of "x".
                              function test(a) {
                                  if (a == 0) {
                                      return 'zero'
                                  }
                                  :
                                  :
                              }

                              x = test(0)
        BREAK_NAME (str): It is used for "break" statement.
                          Firstly, when loop starts, it creates this
                          variable whose value is UNDEFINED.
                          Secondly, "break" statement sets any value
                          and evaluation goes back until finishing
                          loop.
        CONTINUE_NAME (str):  It is used for "continue" statement.
                          Firstly, when loop starts, it creates this
                          variable whose value is UNDEFINED.
                          Secondly, "continue" statement sets any
                          value and evaluation goes back until
                          starting loop.
    """
    UNDEFINED = ()
    RESULT_NAME = '___#RESULT#___'
    FUNCTION_RETURN_NAME = '___#RETURN#___'
    BREAK_NAME = '___#BREAK#___'
    CONTINUE_NAME = '___#CONTINUE#___'

    def __init__(self, enclosing=None):
        """Initialize class.

        Args:
            enclosing (Environment or NoneType, optional): The parent
                                environment. None is given when this
                                instance is root.
                                The default is None.
        """
        self._enclosing = enclosing
        self._variables = {}

    def get(self, name=None, only_this_scope=False):
        """Get variable's value.

        Get variable's value.
        When it is not existed in this scope, it is tried in the parent
        scope.
        None is returned if it is not existed in the whole scope.

        When name is None, the whole values are returned as dict.
        However it is excluded when the prefix of variable is "_" or
        value is the definition of function (CalleeRegistry).
        Note that a result value of ":=" statement had been registered,
        it is returned.

        Args:
            name (str, optional): Variable name.
                                  When this is None, the whole values
                                  are returned as dict. However it is
                                  excluded when the prefix of variable
                                  is "_" or value is the function
                                  (CalleeRegistry).
                                  Note that a result value of ":="
                                  statement had been registered, it is
                                  returned.
                                  The default is None.
            only_this_scope (bool, optional): When it is True, getting
                                            scope is limited only here.
                                            The default is False.

        Returns:
            Any: Its value.
                 Environment.UNDEFINED is returned if the given name's
                 variable is not existed.
        """
        if name is None:
            # :=
            if Environment.RESULT_NAME in self._variables:
                return self._variables[Environment.RESULT_NAME]

            # Whole values
            result = {}
            for key, value in self._variables.items():
                if key[0] == '_':
                    continue
                if isinstance(value, CalleeRegistry) \
                        and not value.is_reference:
                    continue
                result[key] = value
            return result

        # Try to get from current scope.
        if not isinstance(name, str):
            return Environment.UNDEFINED
        if name in self._variables:
            return self._variables[name]

        # Try to get from parent scope.
        if not only_this_scope and self._enclosing is not None:
            return self._enclosing.get(name)

        return Environment.UNDEFINED

    def set(self, name, value, only_this_scope=False):
        """Set a variable.

        Modify/Assign a variable.
        Firstly, modifying is tried. When the given variable is not
        existed in this scope, it is tried in the parent scope.
        When it is not existed in the whole scope, it is assigned in
        this scope newly.

        Args:
            name (str or NoneType): Variable name.
                                    When None is given, value is set
                                    as the returned value.
            value (Any): Its value
            only_this_scope (bool, optional): When it is True, setting
                                            scope is limited only here.
                                            The default is False.
        """
        if name is None:
            name = Environment.RESULT_NAME  # :=
        elif not isinstance(name, str):
            return

        if not only_this_scope:
            is_completed = self.modify(name, value)
            if is_completed:
                return
        self._variables[name] = value  # New assignment

    def modify(self, name, value):
        """Modify a variable.

        Modify a variable.
        When the given variable is not existed in this scope, it is
        tried in the parent scope.

        Args:
            name (str): Variable name
            value (Any): Its value

        Returns:
            bool: True if modifying is completed,
                  False otherwise.
        """
        if name in self._variables:
            self._variables[name] = value  # Modify
            return True

        if self._enclosing is not None:
            return self._enclosing.modify(name, value)

        return False

    def remove(self, name, only_this_scope=False):
        """Remove a variable.

        Args:
            name (str): Variable name.
            only_this_scope (bool, optional): When it is True, removing
                                            scope is limited only here.
                                            The default is False.

        Returns:
            bool: True if removing is completed,
                  False otherwise.
        """
        if name in self._variables:
            del self._variables[name]
            return True

        if not only_this_scope and self._enclosing is not None:
            return self._enclosing.remove(name)

        return False

    def get_enclosing(self):
        """Get enclosing.

        Returns:
            Environment or NoneType: enclosing that is the parent
                                     Environment.
                                     None if enclosing is not
                                     available. In other words,
                                     this is root Environment
                                     if None is returned.
        """
        return self._enclosing
