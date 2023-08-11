# Recursive
# https://www.acmicpc.net/problem/5568

N = int(input())
K = int(input())
C = [input() for _ in range(N)]

S = [[0 for _ in range(N)] for _ in range(K)]
integers = []


def get_integer(no):
    if no == K:
        integer = ''.join([selected(i) for i in range(K)])
        if not integer in integers:
            integers.append(integer)
        return
    for i in range(len(C)):
        if is_selected(i):
            continue
        S[no][i] = 1
        get_integer(no+1)
        S[no][i] = 0


def is_selected(idx):
    for i in range(K):
        if S[i][idx] == 1:
            return True
    return False


def selected(no):
    for i in range(len(S[no])):
        if S[no][i] == 1:
            return C[i]


get_integer(0)
print(len(integers))
