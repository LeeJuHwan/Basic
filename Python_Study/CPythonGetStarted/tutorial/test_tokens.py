def my_function():
    proceed  # pass | proceed -> in cpython modify


TOKEN = """
0,0-0,0:            ENCODING       'utf-8'
1,0-1,3:            NAME           'def'
1,4-1,15:           NAME           'my_function'
1,15-1,16:          LPAR           '('
1,16-1,17:          RPAR           ')
1,17-1,18:          COLON          ':'
1,18-1,19:          NEWLINE        '\n'
2,0-2,4:            INDENT         '    '
2,4-2,11:           NAME           'proceed'
2,11-2,12:          NEWLINE        '\n
3,0-3,0:            DEDENT         ''
3,0-3,0:            ENDMARKER      '
"""
