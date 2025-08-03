n=int(input())
arr=list(map(int,input().split()))

arr1=sorted(set(arr),reverse=True)
print(arr1[1])