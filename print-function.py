
def personalized_print(n):

    _result = ""

    i=1

    for i in range(1,n+1):

        _result += str(i)

    return _result

n = int(input())

print(personalized_print(n))