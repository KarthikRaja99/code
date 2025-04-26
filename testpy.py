def find(parent,node):
    if parent[node]!=node:
        parent[node]=find(parent,parent[node])
    return parent[node]
def union(parent,node1,node2):
    root1=find(parent,node1)
    root2=find(parent,node2)
    if root1!=root2:
        parent[root2]=root1
cities=input()
edges=[]
for i in range(int(input())):
    city1,city2,cost=input().split()
    edges.append((city1,city2,int(cost)))
mst=[]
parent={city:city for city in cities}
edges.sort(key=lambda x:x[2])
for city1,city2,cost in edges:
    if find(parent,city1)!=find(parent,city2):
        mst.append((city1,city2,cost))
        union(parent,city1,city2)
for city1,city2,cost in mst:
    print(f"{city1}:{city2} - {cost}")