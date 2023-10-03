
"""function that concatenates sequence numbers according to the parameter sent"""

def personalized_print(n):

    _result = ""

    for i in range(1,n+1):

        _result += str(i)

    return _result

n = int(input())

print(personalized_print(n))