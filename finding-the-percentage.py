n = int(input())

import statistics

student_marks = {}

for _ in range(n):
    
    name, *line = input().split()
    
    scores = list(map(float, line))
    
    student_marks[name] = scores
    
query_name = input()

mean = statistics.mean(student_marks[query_name])

print(format(mean,'.2f'))

