""" Determines whether a character is lowercase or uppercase and inverts it"""

def swap_case(string):

    _result=''

    for i in string:

        if i.isupper():

            i = i.lower()

        else:

            i = i.upper()

        _result+="".join(i)

    return _result

string = input()