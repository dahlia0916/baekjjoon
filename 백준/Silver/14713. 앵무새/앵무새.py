import sys
bird = []
dap = list()
n = int(sys.stdin.readline())
for _ in range(n):
    bird.append(list(map(str,sys.stdin.readline().split())))
dap = list(map(str,sys.stdin.readline().split()))

for item in dap:
    correct = False
    for idx in range(n):
        if len(bird[idx]) != 0:
            if item == bird[idx][0]:
                bird[idx].pop(0)
                correct=True
                break
    if not correct:
        break

left = 0
for line in bird:
    left += len(line)
if correct and left==0:
    print("Possible")
else:
    print("Impossible")