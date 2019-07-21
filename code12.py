n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))
l=[]
for i in range(m):
    p,q=list(map(int,input().split()))
    l.append(sum(arr[p-1:q]))
for i in l:
    print(i)
