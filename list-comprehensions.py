
"""method that generates a three-dimensional matrix according to the parameters and where the sum of them will be different from the 4 parameter."""

def develop_list(x,y,z,n):

    List = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in   range(z+1) if i+j+k != n]

    return List

x = int(input())

y = int(input())

z = int(input())

n = int(input())

print(develop_list(x,y,z,n))
