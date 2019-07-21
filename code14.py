N,Q=map(int,input().split())
l=list(map(int,input().split()[:N]))
final=[]
for i in range (Q):
    s=list(map(int,input().split())) 
    final.append(s)
for j in final:
    o=0
    for k in range (j[0]-1,j[1]):
        o=o^l[k]
    print(o)
