""" routine that obtains a string, separates it with split and joins it with join. """

def split_and_join(line):
    
    ans=line.split() 
    
    return '-'.join(ans)
    
    # write your code here


line = input()

result = split_and_join(line)

print(result)