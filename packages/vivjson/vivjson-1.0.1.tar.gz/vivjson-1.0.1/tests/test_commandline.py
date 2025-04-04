"""Unit-test for Command-line

Run `python3 -m pytest tests/test_commandline.py` in parent directory.

Environment:
- Python 3.9 or later
- pytest 8.3 or later

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
__date__ = '2025-03-26'

import subprocess

def test_commandline_basic():
    """Unit-test for basic Command-line"""
    cp = subprocess.run(['python3', '-m', 'vivjson', 'return(10)'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        check=False)
    result = cp.stdout.strip()
    assert result == '10'

    cp = subprocess.run(['python3', '-m', 'vivjson',
                         '3', '2', 'return(_[0] + _[1])'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        check=False)
    result = cp.stdout.strip()
    assert result == '5'

    cp = subprocess.run(['python3', '-m', 'vivjson',
                         '3', '2', 'return(_)'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        check=False)
    result = cp.stdout.strip()
    assert result == '[3, 2]'

    cp = subprocess.run(['python3', '-m', 'vivjson', '5', 'return(_ * 2)'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        check=False)
    result = cp.stdout.strip()
    assert result == '10'

    cp = subprocess.run(['python3', '-m', 'vivjson',
                         'for(i in [1,2,3]){print(i*5)};return("")'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        check=False)
    result = cp.stdout.strip()
    assert '5' in result
    assert '10' in result
    assert '15' in result

    cp = subprocess.run(['python3', '-m', 'vivjson', 'tests/call_6.viv'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        check=False)
    result = cp.stdout.strip()
    assert result == '6'

    cp = subprocess.run(['python3', '-m', 'vivjson',
                         'tests/a5b7c9.json', 'tests/axb-c.viv'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        check=False)
    result = cp.stdout.strip()
    assert result == '26'

    cp = subprocess.run(['python3', '-m', 'vivjson',
                         'tests/a5b7c9.json', 'return(a+b+c)'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        check=False)
    result = cp.stdout.strip()
    assert result == '21'

    cp = subprocess.run(['python3', '-m', 'vivjson',
                         'tests/dog2cat3.json',
                         'sum = 0; for (a in _) {sum += a.number}; return(sum)'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        check=False)
    result = cp.stdout.strip()
    assert result == '5'

def test_commandline_usage():
    """Unit-test for usage"""
    cp = subprocess.run(['python3', '-m', 'vivjson', 'a=3/0'],
                        encoding='utf-8', stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, check=False)
    error = cp.stderr.strip()
    assert 'Error: Cannot evaluate' in error

    for option in [None, '-help', '--invalid']:
        command = ['python3', '-m', 'vivjson']
        if option is not None:
            command.append(option)

        cp = subprocess.run(command,
                            encoding='utf-8', stdout=subprocess.PIPE,
                            check=False)
        result = cp.stdout.strip()
        assert 'file extension' in result
        assert 'Example 1' in result

def test_commandline_stdin():
    """Unit-test for stdin"""
    for option in ['-i', '--stdin']:
        for stdin in ['a=3', '{"a": 3}']:
            command = \
                f'echo "{stdin}" | python3 -m vivjson {option} "return(a*2)"'
            cp = subprocess.run(command,
                                encoding='utf-8', stdout=subprocess.PIPE,
                                shell=True, check=False)
            result = cp.stdout.strip()
            assert result == '6'

    command = 'echo "3" | python3 -m vivjson -i=a "return(a+2)"'
    cp = subprocess.run(command,
                        encoding='utf-8', stdout=subprocess.PIPE,
                        shell=True, check=False)
    result = cp.stdout.strip()
    assert result == '5'

    command = 'echo "3" | python3 -m vivjson -i="" "return(a+2)"'
    cp = subprocess.run(command,
                        encoding='utf-8', stdout=subprocess.PIPE,
                        shell=True, check=False)
    result = cp.stdout.strip()
    assert result == '2'

    command = 'echo "3" | python3 -m vivjson -i= "return(a+2)"'
    cp = subprocess.run(command,
                        encoding='utf-8', stdout=subprocess.PIPE,
                        shell=True, check=False)
    result = cp.stdout.strip()
    assert result == '2'

    for option in ['-i', '--stdin']:
        for quotation in ['"', "'", ""]:
            command = 'cat tests/dog2cat3.json | ' \
                f'python3 -m vivjson {option}={quotation}values{quotation} ' \
                '"result = {}, ' \
                'for(value in values){result[value.name] = value.number}, ' \
                'return(result)"'
            cp = subprocess.run(command,
                                encoding='utf-8', stdout=subprocess.PIPE,
                                shell=True, check=False)
            result = cp.stdout.strip()
            assert result == '{"dog": 2, "cat": 3}'

    cp = subprocess.run('cat tests/call_6.viv | python3 -m vivjson -i',
                        encoding='utf-8', stdout=subprocess.PIPE,
                        shell=True, check=False)
    result = cp.stdout.strip()
    assert result == '6'

    cp = subprocess.run('python3 -m vivjson -i tests/call_6.viv',
                        encoding='utf-8', stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, shell=True, check=False)
    result = cp.stdout.strip()
    assert result == ''
    error = cp.stderr.strip()
    assert 'Error: Cannot read from stdin.' in error

    command = 'cat tests/array_escaped_str.json | ' \
              'python3 -m vivjson -i=x "return(x)"'
    cp = subprocess.run(command,
                        encoding='utf-8', stdout=subprocess.PIPE,
                        shell=True, check=False)
    result = cp.stdout.strip()
    # Note that U+2028 (LINE SEPARATOR) and U+2029 (PARAGRAPH SEPARATOR) are
    # included.
    assert result == '["あいうえおか", "x\\ny", "x\\by", "x y", "x y"]'

    command = 'cat tests/array_escaped_str.json | ' \
              'python3 -m vivjson -i=x "print(x), return(\'\')"'
    cp = subprocess.run(command,
                        encoding='utf-8', stdout=subprocess.PIPE,
                        shell=True, check=False)
    result = cp.stdout.strip()
    # Note that U+2028 (LINE SEPARATOR) and U+2029 (PARAGRAPH SEPARATOR) are
    # included.
    assert result == '["あいうえおか", "x\\ny", "x\\by", "x y", "x y"]'

    command = 'cat tests/array_escaped_str.json | ' \
              'python3 -m vivjson -i=x "print(x[0], x[1], x[2], x[3], x[4]), return(\'\')"'
    cp = subprocess.run(command,
                        encoding='utf-8', stdout=subprocess.PIPE,
                        shell=True, check=False)
    result = cp.stdout.strip()
    # Note that U+2028 (LINE SEPARATOR) and U+2029 (PARAGRAPH SEPARATOR) are
    # included.
    assert result == 'あいうえおか, x\ny, x\by, x y, x y'

def test_commandline_version():
    """Unit-test for version"""
    for option in ['-v', '--version']:
        command = ['python3', '-m', 'vivjson']
        command.append(option)

        cp = subprocess.run(command,
                            encoding='utf-8', stdout=subprocess.PIPE,
                            check=False)
        result = cp.stdout.strip()
        assert 'specification version' in result
        assert 'interpreter version' in result
