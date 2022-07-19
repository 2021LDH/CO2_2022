def Q1(): #1902번 수 찾기
    import sys

    N = int(input())
    A = sorted(list(map(int, sys.stdin.readline().split())))
    M = int(input())
    B = list(map(int, sys.stdin.readline().split()))
    
    for i in range(M):    
        start, end = 0, N - 1
        while True:
            mid = (start + end) // 2
            if B[i] == A[mid]:
                print(1)
                break
            elif B[i] > A[mid]:
                start = mid + 1
                if start > end:
                    print(0)
                    break
            else:
                end = mid - 1
                if start > end:
                    print(0)
                    break

def Q2(): #10816번 숫자 카드 2, 이분 탐색 안 씀....
    import sys

    N = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    M = int(input())
    B = list(map(int, sys.stdin.readline().split()))

    count = [0] * 20000001
    for i in range(N):
        count[A[i]] += 1

    for i in range(M):
        print(count[B[i]], end = " ")

def Q3(): #1654번 랜선 자르기
    import sys

    k, n = map(int, sys.stdin.readline().split())
    lan = [0] * k
    for i in range(k):
        lan[i] = int(sys.stdin.readline())
    
    start, end = 1, max(lan)

    while True:
        mid, sum = (start + end) // 2, 0
        for i in range(k):
            sum += lan[i] // mid
        if sum >= n:
            start = mid + 1
            if start > end:
                break
        else:
            end = mid - 1
            if start > end:
                break
    print(end)

def Q4(): #2805번 나무 자르기
    import sys

    NumOfTree, Need = map(int,input().split())
    
    Tree = list(map(int, sys.stdin.readline().split()))

    start, end = 0, max(Tree)

    
    while start <= end:
        mid = (start + end) // 2
        summary = 0
        summary = sum(i - mid if i > mid else 0 for i in Tree)
        if summary >= Need:
            start = mid + 1
        else:
            end = mid - 1
    print(end)

def Q5(): #2110번 공유기 설치
    import sys

    n, c = map(int, input().split())
    A = [0] * n

    for i in range(n):
        A[i] = int(sys.stdin.readline())
    A.sort()

    start, end = 1, A[-1] - A[0]

    while True:
        mid = (start + end) // 2
        count, old = 1, A[0]
        for i in range(n):
            if A[i] - old >= mid:
                old = A[i]
                count += 1
        if count >= c:
            start = mid + 1
            if start > end:
                break
        else:
            end = mid - 1
            if start > end:
                break
    print(end)

def Q6(): #1300번 K번째 수 완벽하게 이해하지 못했음...
    a = int(input())
    b = int(input())
    
    start, end = 1, a * a
    while True:
        sum, mid = 0, (start + end) // 2
        for i in range(1, a + 1):
            sum += min(mid // i, a)
        if sum >= b:
            end = mid - 1
            if start > end:
                break
        else:
            start = mid + 1
            if start > end:
                break
    print(start)

def Q7(): #12015번 가장 긴 증가하는 부분 수열 2 아직 이해 못함...
    n = int(input())
    array = list(map(int, input().split()))
    stack = [0]
    
    
    def binary_search(target, start, end):
        while start <= end:
            mid = (start + end) // 2
    
            if stack[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start
    
    
    for i in array:
        if stack[-1] < i:
            stack.append(i)
        else:
            stack[binary_search(i, 0, len(stack) - 1)] = i
    
    print(len(stack) - 1)