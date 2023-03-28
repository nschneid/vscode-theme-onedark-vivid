
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we will need
from email.mime.text import MIMEText

# Open a plain text file for reading.
msg = {}
with open('myfile.txt') as fP:
    text = fP.read().strip()
    msg['Subject'] = text.splitlines()[0]
    for i in range(10):
        msg[i,i+1] = msg[0][i:i+1]

def myfun(myvar: int=2, *args, **kwargs):
    """
    Multiply the provided integer
    by an approximation of pi.
    """
    PI = 3.14
    return myvar*PI

@classmethod
def someMethod(foo, bar='bar\nbar'):
    print(f'{foo} {bar!r}')
    if foo is not None and 'bar' in bar:
        myfun(1, "2", bar=foo)

foo = list()

@my_decorator('some_str', my_list=['str', 1])
def my_func(args):
    pass

const = 42
PI = 3.14
langConst = True
NOTHING = None


from numpy import ndarray


if __name__ is '__main__' and not None:
    pass