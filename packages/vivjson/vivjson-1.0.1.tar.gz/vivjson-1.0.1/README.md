# VivJson for Python

## Overview

- Deserialize/serialize JSON.
- Tiny language
    - The embedded scripting language 
    - Dynamically typing
    - Lightweight language
- The extension of JSON (JSON's object is valid statements as script.)


## Use-case

- In Python Application
    - Read/Write JSON's value.
    - Change the behavior of Application with downloaded script.
    - Change the operation of data with embedded script within data.
- In command line
    - Manipulate JSON's value with script.


## Example

In Python,

```python
from vivjson.viv import Viv, Json, Method

data = '{"foo": 10, "bar": 30, "baz": 20}'

# JSON's object will be dict.
value, error_message = Viv.run(data)
print(value)  # {'foo': 10, 'bar': 30, 'baz': 20}
print(type(value))  # <class 'dict'>

# The specific variable's value
value, error_message = Viv.run(data, 'return(foo)')
print(value)  # 10
print(type(value))  # <class 'int'>

# The undefined value is evaluated as null (None).
value, error_message = Viv.run(data, 'return(qux)')
print(value)  # None
print(type(value))  # <class 'NoneType'>
# The existence can be checked with "in" operator.
# Note that "." of the right hand side indicates the whole scope.
# "." as the operand is permitted only the right hand side of
# "in" operator.
# Carefully, it can't check about the variable whose prefix is "_".
value, error_message = Viv.run(data, 'return("qux" in .)')
print(value)  # False
print(type(value))  # <class 'bool'>

# The calculated value
value, error_message = Viv.run(data, 'return(foo + bar + baz)')
print(value)  # 60

# Find maximum value.
# 1. Assignment: pairs = {"foo": 10, "bar": 30, "baz": 20}
# 2. for-loop with iterator: for (pair in pairs) {...}
#    - pair[0] is the above key.
#    - pair[1] is the above value.
# 3. Update max.
# 4. Return it.
code = 'max=-1, for (pair in pairs) {if (max < pair[1]) {max = pair[1]}}, return(max)'
value, error_message = Viv.run('pairs = ', '+', data, code)
print(value)  # 30
# Note that "+" of arguments is concatenation. Of course, the following 
# representation can be accepted.
value, error_message = Viv.run('pairs = ' + data, code)
print(value)  # 30
# This is realized as below. However, such code may generate the unexpected
# result because "." represents this block that has the variable "max".
code = 'max=-1, for (pair in .) {if (max < pair[1]) {max = pair[1]}}, return(max)'
value, error_message = Viv.run(data, code)
print(value)  # 30
# When "_max" is used instead of "max", it is improved.
# Because "." does not treat the variable whose prefix is "_".
code = '_max=-1, for (pair in .) {if (_max < pair[1]) {_max = pair[1]}}, return(_max)'
value, error_message = Viv.run(data, code)
print(value)  # 30

# In default, both of script's code and JSON value are accepted.
# Json class is useful if you want to accept as JSON value rather
# than script's code.
data = '{"foo": 3}'
code = 'return(foo)'
value, error_message = Viv.run(Json(data), code)
print(value)  # 3

# Using class instance, implicit variable, and member's access
# - When the given value is not JSON object (key-value pairs),
#   it is assigned into implicit variable.
#   The implicit variable is "_" if there is one value. Otherwise,
#   "_[0]", "_[1]", ... are used.
# - A class member is selected like foo.bar and foo['bar'].
#   In the following example, "_.2" and "_[2]".
data = '["foo", 10, [{"bar": null, "baz": "test"}, false]]'
instance, error_message = Viv.make_instance(data)
value, error_message = Viv.run(instance, "return(_[2][0]['bar'])")
print(value)  # None (null is represented as None in Python.)
value, error_message = Viv.run(instance, "return(_.2.-2.baz)")
print(value)  # test
# Calling class method
# - Method object has 2 elements.
#     - 1st element is method name as str.
#     - 2nd element is its arguments as list/tuple.
#   In the following example, Method('add', [10, 20]).
#   It is equivalent to "return(add(10, 20))".
code = 'function add(a, b) {' \
        '  return(a + b)' \
        '}'
instance, error_message = Viv.make_instance(code)
value, error_message = Viv.run(instance, Method('add', [10, 20]))
print(value)  # 30
value, error_message = Viv.run(instance, 'return(add(10, 20))')
print(value)  # 30
```

In command-line,

```shell
# The specific variable's value
vivjson '{"foo": 10, "bar": 30, "baz": 20}' 'return(foo)'  # 10
# or
python3 -m vivjson '{"foo": 10, "bar": 30, "baz": 20}' 'return(foo)'  # 10

# Using PIPE (-i option)
echo '{"foo": 10, "bar": 30, "baz": 20}' | vivjson -i 'return(foo)'  # 10

# The calculated value
echo '{"foo": 10, "bar": 30, "baz": 20}' | \
vivjson -i 'return(foo + bar + baz)'  #60

# Find maximum value.
echo '{"foo": 10, "bar": 30, "baz": 20}' | vivjson -i=pairs \
'max=-1, for (pair in pairs) {if (max < pair[1]) {max = pair[1]}}, return(max)'  # 30

# Find maximum value without PIPE.
vivjson "pairs=" + '{"foo": 10, "bar": 30, "baz": 20}' \
'max=-1, for (pair in pairs) {if (max < pair[1]) {max = pair[1]}}, return(max)'  # 30
# Note that "+" of arguments is concatenation. Of course, the following 
# representation can be accepted.
vivjson 'pairs={"foo": 10, "bar": 30, "baz": 20}' \
'max=-1, for (pair in pairs) {if (max < pair[1]) {max = pair[1]}}, return(max)'  # 30

# Getting member's value
# "return(foo.bar)" and "return(foo['bar'])" are equivalent.
vivjson '{"foo": [1, {"bar": true}, "test"]}' 'return(foo[0])'  # 1
vivjson '{"foo": [1, {"bar": true}, "test"]}' 'return(foo.1.bar)'  # true
vivjson '{"foo": [1, {"bar": true}, "test"]}' 'return(foo.-1)'  # test

# Using implicit variable
# When the given value is not JSON object (key-value pairs),
# it is assigned into implicit variable.
# The implicit variable is "_" if there is one value. Otherwise,
# "_[0]", "_[1]", ... are used.
vivjson 1.5 'return(_)'  # 1.5
vivjson 1.5 2 'return(_[0] + _[1])'  # 3.5
echo '[{"name": "dog", "number": 2}, {"name": "cat", "number": 3}]' | \
vivjson -i 'result = {}' \
'for (data in _) {result[data.name] = data.number}' \
'return(result)'  # {"dog": 2, "cat": 3}

# Help
vivjson
```


## Installation

Python version: >= 3.9

```shell
python3 -m pip install vivjson
```


## API

| Pattern                                                                 | Consumed memory | Next running speed |
|-------------------------------------------------------------------------|-----------------|--------------------|
| [Direct running](#direct_running)                                       | Low             | Slow               |
| [Parsing and Running](#parsing_and_running)                             | Middle          | Middle             |
| [Making class instance and Running](#making_class_instance_and_running) | High            | Fast               |

When class instance is made, class method can be called and member's variable can be updated.


<a id="direct_running"></a>

### Direct running

It is suitable if running times is only one.

```
            +--------------------+
            |                    |
            | Viv                |
            |                    |
            |  +--------------+  |
Java's      |  |              |  |     Java's
value   ------>| run          |------> value
            |  |              |  |       or
JSON's      |  |              |  |     JSON's
value   ------>|              |  |     value 
            |  |              |  |
Script      |  |              |  |
code    ------>|              |  |
            |  +--------------+  |
            |                    |
            +--------------------+
```

For example,

```python
value, error_message = Viv.run('{"foo": 3, "bar": 2}', "return(foo + bar)")
print(value)  # 5
```


<a id="parsing_and_running"></a>

### Parsing and Running

It is suitable that same running is repeated.  
Because parsing is done only one time.

```
            +--------------------+              +--------------------+
            |                    |              |                    |
            | Viv                |              | Viv                |
            |                    |              |                    |
            |  +--------------+  |  Parsed      |  +--------------+  |
Java's      |  |              |  |  value/code  |  |              |  |     Java's
value   ------>| parse,       |------------------->| run          |------> value
            |  | parse_file,  |  |              |  |              |  |       or
JSON's      |  | parse_text   |  |  Additional  |  |              |  |     JSON's
value   ------>|              |  |  Java/JSON's |  |              |  |     value 
            |  |              |  |  value   ------>|              |  |
Script      |  |              |  |              |  |              |  |
code    ------>|              |  |  Additional --->|              |  |
            |  +--------------+  |  Script code |  +--------------+  |
            |                    |              |                    |
            +--------------------+              +--------------------+
```

For example,

```python
parsed, error_message = Viv.parse("return(foo + bar)")
value, error_message = Viv.run('{"foo":3, "bar": 2}', parsed)
print(value);  # 5
```

<a id="making_class_instance_and_running"></a>

### Making class instance and Running

It is suitable that same running is repeated.  
Because parsing and initialization are done only one time.

```
            +---------------------+              +--------------------+
            |                     |              |                    |
            | Viv                 |              | Viv                |
            |                     |              |                    |
            |  +---------------+  |              |  +--------------+  |
Java's      |  |               |  |  Instance    |  |              |  |     Java's
value   ------>| make_instance |------------------->| run          |------> value
            |  |               |  |              |  |              |  |       or
JSON's      |  |               |  |  Additional  |  |              |  |     JSON's
value   ------>|               |  |  Java/JSON's |  |              |  |     value 
            |  |               |  |  value   ------>|              |  |
Script      |  |               |  |              |  |              |  |
code    ------>|               |  |  Additional --->|              |  |
            |  +---------------+  |  Script code |  |              |  |
            |                     |              |  |              |  |
            +---------------------+  Calling ------>|              |  |
                                     Method      |  +--------------+  |
                                                 |                    |
                                                 +--------------------+

```

For example,

```python
code = "function add(a, b) {" \
       "  return(a + b)" \
       "}" \
       "c = [20, false]"
instance, error_message = Viv.make_instance(code)

value, error_message = Viv.run(instance, '{"foo":3, "bar": 2}', 'return(add(foo, bar))')
print(value)  # 5
value, error_message = Viv.run(instance, Method("add", [3, 2]))
print(value)  # 5

value, error_message = Viv.run(instance, "return(c[0])")
print(value)  # 20
```


### Viv class

The following methods are available.

- Running/Deserialization function
    - `run` : Run VivJson's code or deserialize JSON objects.
    - `parse` : Parse VivJson's code and JSON object.
    - `parse_file` : Parse a file that contains VivJson's code or JSON object.
    - `parse_text` : Parse a text that is VivJson's code or JSON object.
    - `make_instance` : Makes a class instance.
- String conversion
    - `make_string` : Convert into String. Serialize into JSON string.

The following arguments can be given into all methods except `make_string`.  
Note that `make_string`'s argument is Any value.

| Argument type                                | Python object type | Example                                                         |
|----------------------------------------------|--------------------|-----------------------------------------------------------------|
| A VivJson's code                             | `str`              | `'foo = bar / 2'`, `'result = test(100)'`                       |
| A JSON value                                 | `str`              | `'{"foo": 10, "bar": true}'`, `'[1, 2]'`, `'dog'`, `'null'`     |
| A JSON value                                 | `Json`             | `Json('{"foo": 10, "bar": true}')`, `Json('[1, 2]')`, `Json('dog')`, `Json('null')` |
| A file path                                  | `str`              | `'data/events.json'`, `'calc.viv'`                              |
| Some VivJson's codes, JSON values, file paths, variables, Parsed objects | `list` or `tuple` | `[Json('{"foo": 10, "bar": 1.5}'), 'baz = foo + bar', 'return(baz)']` |
| Some variables (name/value pairs)            | `dict`             | `{"foo": "alpha", "bar": true}`                                 |
| Some configurations                          | `Config`           | `Config(infinity="Infinity", nan="NaN")`                        |
| Some parsed statements                       | `Parsed`           | `Viv.parse('return(a+b)')`                                      |
| A class instance                             | `Instance`         | `Viv.make_instance('{"a": 3, "b": 2}')`                         |
| A calling class-method                       | `Method`           | `Method('add', [100, -10])`<br> The 1st element is the method name as `str`. The following list is its arguments. |

The calling class-method needs class instance in arguments.

```python
code = 'function add(a, b) {' \
        '  return(a + b)' \
        '}'
instance, error_message = Viv.make_instance(code)
value, error_message = Viv.run(instance, Method('add', [100, -10]))
print(value)  # 90
```

Multiple arguments can be given into all methods except `make_string`.  
Furthermore, an array of arguments can be given too.
For example, `value, error_message = Viv.run('{a:3,b:2}', 'return(a+b)')` is equivalent to
`value, error_message = Viv.run(['{a:3,b:2}', 'return(a+b)'])`.

There are two value as the returned value except `make_string`.  
Note that `make_string`'s returned value is `str`.

| Method          | First value if succeeded | First value if failed | Second value if succeeded | Second value if failed |
|-----------------|--------------------------|-----------------------|---------------------------|------------------------|
| `run`           | `bool`, `int`, `float`, `str`, `list`, `dict`, `None` | `None` | `""` (empty) | Error message         |
| `parse`         | `Parsed`                 | `None`                | `""` (empty)              | Error message          |
| `parse_file`    | `Parsed`                 | `None`                | `""` (empty)              | Error message          |
| `parse_text`    | `Parsed`                 | `None`                | `""` (empty)              | Error message          |
| `make_instance` | `Instance`               | `None`                | `""` (empty)              | Error message          |

`dict`'s key is `str`. Its value is `bool`, `int`, `float`, `str`, `list`, `dict`, or `None`.  
`list`'s element is also `bool`, `int`, `float`, `str`, `list`, `dict`, or `None`.


### Config class

The following configurations are available.

| Name              | Object type     | Default value | Description                                                   |
|-------------------|-----------------|---------------|---------------------------------------------------------------|
| enable_stderr     | `bool`          | `False`       | When `True` is given, error message is outputted into stderr. |
| enable_tag_detail | `bool`          | `False`       | When `True` is given, error message's tag contains either of "Lexer", "Parser", or "Evaluator". |
| enable_only_json  | `bool`          | `False`       | When `True` is given, the given data is parsed as JSON. In other words, script is disabled.     |
| infinity          | `str` or `None` | `None`        | When string is given, Infinity is allowed in JSON. Then the given string is used to input/output Infinity from/to JSON. (Note that it is not surrounded with quotation mark.)<br>When `None` is given and Infinity is happen, error is occurred. |
| nan               | `str` or `None` | `None`        | When string is given, NaN (Not a Number) is allowed in JSON. Then the given string is used to input/output NaN from/to JSON. (Note that it is not surrounded with quotation mark.)<br>When `None` is given and NaN is happen, error is occurred. |
| max_array_size    | `int`           | `1000`        | Maximum array/block size.                                   |
| max_depth         | `int`           |  `200`        | Maximum recursive called times of evaluate method.          |
| max_loop_times    | `int`           | `1000`        | Maximum loop times of "for", "while", and so on.            |

Each configuration is set/gotten with the following method.  
On the other hand, each configuration can be given as an argument of constructor.

| Name              | get method            | set method         |
|-------------------|-----------------------|--------------------|
| enable_stderr     | get_enable_stderr     | enable_stderr      |
| enable_tag_detail | get_enable_tag_detail | enable_tag_detail  |
| enable_only_json  | get_enable_only_json  | enable_only_json   |
| infinity          | get_infinity          | set_infinity       |
| nan               | get_nan               | set_nan            |
| max_array_size    | get_max_array_size    | set_max_array_size |
| max_depth         | get_max_depth         | set_max_depth      |
| max_loop_times    | get_max_loop_times    | set_max_loop_times |

For example,

```python
config = Config(max_array_size=10)
config.set_infinity("Infinity")
config.set_nan("NaN")
value, error_message = Viv.run(Json(text), code, config)
```

By the way, the following JSON object is invalid because JSON's number can't treat Infinity and NaN. (See [RFC 8259 Section 6][RFC 8259 Section 6])  
However, VivJson can treat it using `Config#set_infinity` and `Config#set_nan`.

```json
{
    "normal": 1.5,
    "inf": Infinity,
    "negative_inf": -Infinity,
    "nan": NaN,
    "str": "1.5"
}
```

[RFC 8259 Section 6]:https://datatracker.ietf.org/doc/html/rfc8259#section-6


## Implementation

### Diagram

```
            +-----------------------------------------------------+
            |                                                     |
            | Viv                                                 |
            |                             +-------------+         |
Python's -------------+------------------>|             |         |
value       |         |                   | Evaluator   |         |
            |         V                   |             |         |
            |  +-------------+            |             |         |
JSON's  ------>|             |            |             |         |     Python's
value       |  | Parser      | Statements |             |         |     value
            |  |             |----------->|             |------------->   or
            |  |  +-------+  |            |             |         |     JSON's
Script  ------>|  |       |  |            +-------------+         |     value
code        |  |  | Lexer |  |              |      |              |
            |  |  |       |  |    Variables |      | Function     |
            |  |  +-------+  |              |      | call         |
Other   ------>|             |              |      |              |
            |  +-------------+              |      |              |
            |                               V      V              |
            |  +-------------+  +-------------+  +-------------+  |
            |  |             |  |             |  |             |  |
            |  | Config      |  | Environment |  | Standard    |  |
            |  |             |  |             |  |             |  |
            |  +-------------+  +-------------+  +-------------+  |
            +-----------------------------------------------------+
```


### Class

- **Viv**: API
    - **Json**: JSON data class. In default, both of script's code and JSON value are accepted. This class is used if you want to accept as JSON value rather than script's code.
    - **Parsed**: Parsed data class. This is used as the returned value of `parse*`.
    - **Instance**: Instance data class. This is used as the returned value of `make_instance`.
    - **Method**: Method data class. This is used to call class method.
- **Lexer**: Source code is resolved into some tokens.
- **Parser**: Then statements are built from several tokens. One statement represents a unit of processing.
- **Evaluator**: Statements are operated.
- **Environment**: Variable's value and the definition of function are stored.
    1. New block (includes function) creates new instance of Environment as new scope.
    2. The basic value (number, string, boolean, and null) is stored as host language native literal.
- **Token**: Its instance is created from source code in Lexer.
- **Statement**: Mostly, its instance is created from tokens in Parser.
    - **Array**: Array data class
    - **Binary**: Binary data class. For example, `3 * 2` are stored into left, operator, and right.
    - **Blank**: Blank data class.
    - **Block**: Block data class. For example,
        1. anonymous: `x = {a: 3, b: 2}`
        2. pure: `function test() {return(10)}`
        3. limited: `if (i > 10) {x="+"} else {x="-"}`
    - **Call**: Call data class. This is used to call function, such as `len("abc")`.
    - **Callee**: Callee data class. This is used to define function entity.
    - **CalleeRegistry**: Callee Registry data class. This is made in Evaluator. This is not used in Parser.
    - **Get**: Get data class. For example, `x["y"]["z"]` and `x.y.z` are represented as `["x", "y", "z"]`.
    - **Identifier**: Identifier data class. It is used as name of variable, function, and class.
    - **Injection**: Injection data class. Set host language's variable.
    - **Keyword**: Keyword data class. It is used as return, break, and so on.
    - **Literal**: Literal data class. string, number (int and float), true, false, and null are accepted.
    - **Loop**: Loop data class.
    - **Parameter**: Parameter data class. This is used to assist the definition of function entity.
    - **Remove**: Remove data class. For example, `remove(x["y"]["z"])`, `remove(x.y.z)`
    - **Return**: Return data class. `"return" [ "(" value ")" ]`
    - **Set**: Set data class. For example, `x["y"]["z"] = 3` is represented.
    - **Value**: Value data class. Set host language's value.
- **Standard**: Standard library
- **Config**: Configuration of runtime
- **Error**: Exception and report
    - **LexError**: Exception for Lexer
    - **ParseError**: Exception for Parser
    - **EvaluateError**: Exception for Evaluator


## Related links

- [VivJson](https://github.com/benesult/vivjson-spec)
    - [VivJson's quick reference](https://github.com/benesult/vivjson-spec/blob/main/quick_reference.md)
    - [VivJson's specification](https://github.com/benesult/vivjson-spec/blob/main/specification.md)
    - [VivJson's sample code](https://github.com/benesult/vivjson-spec/blob/main/sample_codes.md)
- [VivJson for Java](https://github.com/benesult/vivjson-java)
- [VivJson for Python in PyPI](https://pypi.org/project/vivjson/)
