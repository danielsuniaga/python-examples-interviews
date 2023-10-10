

info = []

marks = []

for _ in range(int(input())):

    name = input()

    score = float(input())

    info.append([name,score])

    marks.append(score)

smin = sorted(set(marks))[1]

for name, marks in sorted(info):

    if smin == marks:
        
        print(name)





