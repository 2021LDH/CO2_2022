def Q1(): #2750번 수 정렬하기
    n = int(input())
    arr = []
    
    for i in range(n): 
        arr.append(int(input()))
    
    arr.sort()
    
    for i in range(n):
        print(arr[i])

def Q2(): #2751번 수 정렬하기 2
    import sys
    
    n = int(sys.stdin.readline())
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
    
    arr.sort()
    
    for i in range(n):
        print(arr[i])

def Q3(): #10989번 수 정렬하기 3
    import sys

    n = int(sys.stdin.readline())
    count = [0] * 10001

    for i in range(n):
        count[int(sys.stdin.readline())] += 1

    for i in range(10001):
        for j in range(count[i]):
            print(i)

def Q4(): #2108번 통계학
    import sys
  
    n = int(sys.stdin.readline())
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline()))
  
    arr.sort()
  
    count = [0] * 8001
    for i in range(n):
        count[arr[i] + 4000] += 1

    NumOfMax = 0
    for i in range(8001):
        if max(count) == count[i]:
            NumOfMax += 1
  
    a = 0
    b = 0
    if NumOfMax == 1:
        b = count.index(max(count)) - 4000
    else:
        for i in range(8001):
            if count[i] == max(count) and a == 1:
                b = i - 4000    
            if count[i] == max(count):
                a += 1
  
    print(round(sum(arr)/n))
    print(arr[n//2])
    print(b)
    print(arr[n - 1] - arr[0])

def Q5(): #1427번 소트인사이드
    n = int(input())

    for i in range(1, 11):
        if n // (10 ** i) == 0:
            break

    arr = [0] * i

    for j in range(i):
        arr[j] = n % 10
        n = n // 10

    arr.sort()

    result = 0
    for j in range(i):
        result += arr[j] * (10 ** j)
    print(result)

def Q6(): #11650번 좌표 정렬하기
    n = int(input())

    x_y = []
    for i in range(n):
        x, y = map(int, input().split())
        x_y.append([x, y])
    x_y.sort(key = lambda x : (x[0], x[1]))
    for i in range(n):
        print(x_y[i][0], x_y[i][1])

def Q7(): #11651번 좌표 정렬하기 2
    n = int(input())

    x_y = []
    for i in range(n):
        x, y = map(int, input().split())
        x_y.append([x, y])
    x_y.sort(key = lambda x : (x[1], x[0]))
    for i in range(n):
        print(x_y[i][0], x_y[i][1])

def Q8(): #	1181번 단어 정렬
    n = int(input())

    word = []
    for i in range(n):
        word.append(str(input()))

    word.sort()
    word.sort(key = lambda x : len(x))
    
    arr = []
    for i in range(n):
        if i == 0 or word[i - 1] != word[i]:
            arr.append(word[i])
        elif word[i - 1] == word[i]:
            pass

    for i in range(len(arr)):
        print(arr[i])


def Q9(): #10814번 나이순 정렬
    n = int(input())

    people = []
    
    for i in range(n):
        age, name = input().split()
        people.append([int(age), name])
    
    people.sort(key = lambda x : x[0])
    
    for i in range(n):
        print(people[i][0], people[i][1])

def Q10(): #18870번 좌표 압축
    n = int(input())

    x = list(map(int,input().split()))
    x_y = []
    for i in range(n):
        x_y.append([x[i], i])

    x_y.sort(key = lambda x : x[0])
    
    result = []
    for i in range(n):
        result.append([0, 0])
    
    result[0][1] = x_y[0][1]
    for i in range(1,n):
        if x_y[i][0] == x_y[i - 1][0]:
            result[i][0] = result[i - 1][0]
            result[i][1] = x_y[i][1]
        else:
            result[i][0] = result[i - 1][0] + 1
            result[i][1] = x_y[i][1]

    
    result.sort(key = lambda x : x[1])
    for i in range(n):
        print(result[i][0], end = " ")