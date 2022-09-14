from distutils.util import execute
import io
from contextlib import redirect_stdout

# ------------------------------------------------------------------------------

def message_to_exec(message: str):
    """Takes a discord message input and returns a string
    that is able to be used with the exec() function. 
    This is a python only solution."""
    language = ''
    arguments = ''
    code = ''
    inCodeSection = False
    for line in message.split('\n'):
        linesplit = line.split()
        if (not inCodeSection):   
            for j in range(0, len(linesplit)):
                if (j == 0):
                    pass
                elif (j == 1):
                    language += linesplit[j]
                elif (j > 1):
                    arguments += (linesplit[j] + ' ')
            inCodeSection = True
        elif (inCodeSection & (len(line) != 0)):
            if ((line[0] != '`')):
                code += line + '\n'
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        exec(code)
    out = stdout.getvalue()
    return out