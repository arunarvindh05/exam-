n,q=map(int,input().split())
l=list(map(int,input().split()[:n]))
final=[]
for i in range (q):
    s=list(map(int,input().split())) 
    final.append(s)
for j in final:
    o=0
    for k in range (j[0]-1,j[1]):
        o=o^l[k]
    print(o)
