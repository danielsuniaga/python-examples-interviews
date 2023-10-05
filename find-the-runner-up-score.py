""" routine that analyzes a number of notes, the first input performs sets the number of notes and the second input writes the notes. """

n = int(input()) 

arr = map(int, input().split()) 

arr=set(arr)

print(arr)

arr.remove(max(arr)) 

print(max(arr))