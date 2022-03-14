# Strings can be entered in "  " or '  '
from operator import mul


single_string = 'data analysis'
double_string = "data analysis"

# special characters in strings are enclosed with a backslash:
tab_string = "\t" # tab character symbol
print(tab_string)
len(tab_string) # length of string
print(len(tab_string))

# to put a backslash in a string (e.g. when specifying folder names in Windows) you can create a raw string and use the r "" notation
not_tab_string = r"\t" # a string containing the slash character and the letter t
print(not_tab_string)
len(not_tab_string)
print(len(not_tab_string))

# Python also supports multi-character strings defined with triple quotes:
multi_line_string = """ This is the first line, 
 this is the second line, 
 this is the third line"""

print(multi_line_string)