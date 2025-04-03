"""Command-line client for VivJson

Usage: vivjson [ [option] <code or file> ... ]
         or
       python3 -m vivjson [ [option] <code or file> ... ]

option: - "+" is concatenated the previous code and
          the following code, such as
            "a=" + "[1, 2]" "return(a[0]+a[1])"
        - "-i" or "--stdin" reads from PIPE.
          For example, the following command shows "6".
            echo '{"a":3}' | vivjson -i "return(a*2)"
          "-i=<name>" or "--stdin=<name>" gives variable name for
          value that read from PIPE.
          For example, the following command shows
          {"dog": 2, "cat": 3}.
            echo '[{"x":"dog","y":2},{"x":"cat","y":3}]' | \
            vivjson -i=data "z={},for(v in data){z[v.x]=v.y},print(z)"
        - "-j" or "--json" indicates that the following code is JSON.
          For example, error occurs because the following value is
          invalid as JSON.
            vivjson -j '{"a":1+2}'
        - "-v" or "--version" shows version.

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
__date__ = '2025-03-28'

import sys
from .viv import Viv, Json
from .config import Config

def show_usage():
    """Show usage of VivJson in command line."""
    print(
        'VivJson\n'
        'Usage: vivjson [ [option] [ <code or file> ] ] ...\n'
        '         or\n'
        '       python3 -m vivjson [ [option] [ <code or file> ] ] ...\n'
        '\n'
        'option: - "+" is concatenated the previous code and the following\n'
        '          code, such as\n'
        '            "a=" + "[1, 2]" "return(a[0]+a[1])"\n'
        '        - "-i" or "--stdin" reads from PIPE.\n'
        '          For example, the following command shows "6".\n'
        '            echo \'{"a":3}\' | vivjson -i "return(a*2)"\n'
        '          "-i=<name>" or "--stdin=<name>" gives variable name for\n'
        '          value that read from PIPE.\n'
        '          For example, the following command shows\n'
        '          {"dog": 2, "cat": 3}.\n'
        '            echo \'[{"x":"dog","y":2},{"x":"cat","y":3}]\' | \\\n'
        '            vivjson -i=data "z={},for(v in data){z[v.x]=v.y},print(z)"\n'
        '        - "-j" or "--json" indicates that the following code is JSON.\n'
        '          For example, error occurs because the following value is\n'
        '          invalid as JSON.\n'
        '            vivjson -j \'{"a":1+2}\'\n'
        '        - "-v" or "--version" shows version.\n'
        '\n'
        '       Note that the file extension must be '
                  f'"{Viv.EXTENSIONS[0]}" or "{Viv.EXTENSIONS[1]}".\n'
        '\n'
        'Example 1. The following codes show same result (5).\n'
        '           - vivjson "a:3,b:2,return(a+b)"\n'
        '           - vivjson "{a:3,b:2,return(a+b)}"\n'
        '           - vivjson "{a:3,b:2}" "{return(a+b)}"\n'
        '           - vivjson "{a:3,b:2}" "return(a+b)"\n'
        '           - vivjson "x=" + "{a:3,b:2}" "return(x.a+x.b)"\n'
        '           - vivjson "3,2" "return(_[0]+_[1])"\n'
        '           - vivjson 3 2 "return(_[0]+_[1])"\n'
        '           - vivjson 3 "return(_ + 2)"\n'
        'Example 2. Using file.\n'
        '           - vivjson test.viv\n'
        '           - vivjson data.json calc.viv\n'
        'Example 3. Using code and file.\n'
        '           - vivjson "{a:3,b:2}" calc.viv\n'
        'Example 4. Using PIPE.\n'
        '           - echo "return(3*5)" | vivjson -i\n'
        '           - echo "a=3" | vivjson -i "return(a*2)"\n'
        '           - echo \'{"a":3}\' | vivjson -i "return(a*2)"\n'
        '           - cat test.viv | vivjson -i\n'
        '           - cat data.json | vivjson -i "return(a*b)"\n'
        'Example 5. Parsing data as JSON.\n'
        '           - vivjson -j \'{"a":3,"b":2}\' "return(a+b)"\n'
        '           - echo \'{"a":3,"b":2}\' | vivjson -j -i "return(a+b)"\n'
        '\n'
        '       Note that the combined option, such as "-ji", isn\'t allowed.'
    )

def show_version():
    """Show version of VivJson in command line."""
    print(
        "VivJson's\n"
        f'    specification version: {Config.SPEC_VERSION}\n'
        f'    interpreter version:   {Config.INTERPRETER_VERSION}'
    )

def get_stdin():
    """Get data or command from stdin.

    Returns:
        str or NoneType: data/command if it is given,
                         None otherwise.
    """
    data = []
    try:
        while True:
            line = input().strip()
            data.append(line)
    except EOFError:
        pass

    if len(data) == 0:
        return None
    return '\n'.join(data)

def is_number(text: str) -> bool:
    """Detect whether the given text is number or not.

    Args:
        text (str): A text that may be number

    Returns:
        bool: True if the given text is number, False otherwise
    """
    try:
        float(text)
    except (ValueError, OverflowError):
        return False
    return True

def main():  # pylint: disable=R0912
    """Main function for command line."""
    if len(sys.argv) < 2:
        show_usage()
        return

    arguments = sys.argv.copy()
    arguments.pop(0)

    for argument in arguments:
        if argument in ('-v', '--version'):
            show_version()
            return

    stdin_index = -1
    stdin_name = None
    for index, argument in enumerate(arguments):
        for option in ('-i', '--stdin'):
            if argument.find(option) == 0:
                stdin_index = index
                if '=' in argument:
                    data = argument.split('=')
                    if len(data) == 2 and len(data[1]) > 0:
                        stdin_name = data[1]
                break
    if stdin_index >= 0:
        arguments.pop(stdin_index)

        stdin = get_stdin()
        if not isinstance(stdin, str):
            error_message = Viv.report_error('Cannot read from stdin.')
            print(error_message, file=sys.stderr)
            return
        if stdin_name is not None:
            stdin = f'{stdin_name}={stdin}'
        arguments.insert(0, stdin)  # #1

    # | Original | Stdin | arguments     | stdinIndex | array as Result |
    # |----------|-------|---------------|------------|-----------------|
    # | "a:3"    | ----  | ["a:3"]       | -1         | ["a:3"]         |
    # | -j "a:3" | ----  | ["-j", "a:3"] | -1         | [Json("a:3")]   |
    # | -i       | "a:3" | ["a:3"]       |  0         | ["a:3"]         |
    # | -j -i    | "a:3" | ["a:3", "-j"] |  1         | [Json("a:3")]   |
    array = []
    index = -1
    while (index := index + 1) < len(arguments):
        if len(argument) >= 1 and argument[0] == '#':
            break

        argument = arguments[index]
        if argument in ('-j', '--json'):
            if index == stdin_index:
                if index == 0:
                    error_message = Viv.report_error('Unexpected behavior.')
                    print(error_message, file=sys.stderr)
                    return
                array[0] = Json(arguments[0])  # #1
                continue
            if index + 1 < len(arguments):
                index += 1
                array.append(Json(arguments[index]))
                continue
        array.append(argument)

    if len(array) == 1 and isinstance(array[0], str) \
            and (len(array[0]) == 0
                 or (array[0][0] == '-' and not is_number(array[0]))):
        show_usage()
        return

    result, error_message = Viv.run(array)
    if error_message != '':
        print(error_message, file=sys.stderr)
        return

    print(Viv.make_string(result))

if __name__ == '__main__':
    main()
