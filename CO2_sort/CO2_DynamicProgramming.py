def Q1(): #15989번 1, 2, 3 더하기 4
	MAX = 10001
	arr = [[0,0,0,0] for _ in range(MAX)]
	arr[1][1] = 1
	arr[2][1] = 1
	arr[2][2] = 1
	arr[3][1] = 1
	arr[3][2] = 1
	arr[3][3] = 1

	for i in range(4,MAX):
		arr[i][1] = arr[i-1][1]
		arr[i][2] = arr[i-2][1] + arr[i-2][2]
		arr[i][3] = arr[i-3][1] + arr[i-3][2]+ arr[i-3][3]
		
	n = int(input())
	for _ in range(n):
		a = int(input())
		print(sum(arr[a]))

def Q2(): #1010번 다리 놓기
	import math

	n = int(input())
	for i in range(n):
		a, b = map(int, input().split())
		ans = math.factorial(b)/(math.factorial(b-a)*math.factorial(a))
		print(int(ans))
Q2()