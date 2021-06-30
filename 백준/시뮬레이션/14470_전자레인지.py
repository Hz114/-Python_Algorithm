A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

answer = 0
if A < 0:
    answer += -1 * (A * C)
    answer += D
    answer += B * E
elif A == 0:
    answer += D
    answer += B * E
else:
    answer += (B - A) * E

print(answer)
