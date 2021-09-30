"""
Test pep8
A test file to see what the pep8 command (pep8 test_pep8.py) will pick up on.
Created: 30.09.21;    Author: SL
The "module docstring", documenting the file contents. pylint gets sad without.
"""

VAR_1 = 123  # Constants are named with UPPER_CASE naming style. -30.09.21
VAR_2 = 555

VAR_3 = VAR_1*VAR_2
VAR_3 = VAR_3 % 5

print('VAR_3 is now', VAR_3)

VAR_3 = 5
# Note: Command is now pycodestyle test_pep8.py - 30.09.21
# Note: See pylint (pylint test_pep8.py) which scores code. -30.09.21
