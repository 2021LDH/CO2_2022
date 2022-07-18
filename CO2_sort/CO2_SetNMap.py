def Q1(): #10815번 숫자 카드
    a = input()
    arr = set(map(int, input().split()))
    b = input()
    for i in map(int, input().split()):
        if i in arr:
            print(1, end=' ')
        else:
            print(0, end=' ')

def Q2(): #14425번 문자열 집합
    a, b = map(int, input().split())
    arr1 = set()
    arr2 = []
    for i in range(a):
        arr1.add(input())
    for i in range(b):
        arr2.append(input())
    
    count = 0
    for i in arr2:
        if i in arr1:
            count += 1
    print(count)

def Q3(): #1620번 나는야 포켓몬 마스터 이다솜
    import sys

    a, b = map(int, sys.stdin.readline().split())
    data = dict()
    for i in range(a):
        temp = sys.stdin.readline().rstrip()
        data[i + 1] = temp
        data[temp] = i + 1
    for i in range(b):
        Q = sys.stdin.readline().rstrip()
        if Q.isdigit():
            print(data[int(Q)])
        else:
            print(data[Q])

#4번 #10816번 숫자 카드 2는 브루트 포스에 포함되어 있으므로 패스

def Q5(): #1764번 듣보잡
    import sys

    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr1 = set()
    for i in range(a):
        arr1.add(sys.stdin.readline().rstrip())
    
        arr2 = list()
    for i in range(b):
        arr2.append(sys.stdin.readline().rstrip())

    result = list()
    for i in arr2:
        if i in arr1:
            result.append(i)
    result.sort()
    print(len(result))
    for i in range(len(result)):
        print(result[i])

def Q6(): #1269번 대칭 차집합
    import sys

    n, m = sys.stdin.readline().split()
    A = set(map(int, sys.stdin.readline().rstrip().split()))
    B = set(map(int, sys.stdin.readline().rstrip().split()))
    print(len(A ^ B))

def Q7(): #11478번 서로 다른 부분 문자열의 개수
    import sys

    arr = input()
    result = set()
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            result.add(arr[i:j + 1])
    print(len(result))
Q7()