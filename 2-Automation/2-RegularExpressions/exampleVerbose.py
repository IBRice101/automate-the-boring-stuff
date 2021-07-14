import re

re.compile(r'''
\d\d\d      # area code
-
\d\d\d      # first three digits
-
\d\d\d\d    # last four digits
\sx\d(2,4)  # extension, like x1234
''', re.VERBOSE) # verbose means whitespace (i.e. newline) can be ignored

