from collections import *
import sys
sys.setrecursionlimit(10**6)
def insert(tree,cur, val):
    if tree[cur[2]][0]==-1 and  cur[0] > val[0]:
        tree[cur[2]][0] =val
        return cur
    elif tree[cur[2]][1]==-1 and cur[0] < val[0]:
        tree[cur[2]][1] = val
        return cur
    else:
        if cur[0] > val[0]:
            tree[cur[2]][0] = insert(tree,tree[cur[2]][0], val)
        else:
            tree[cur[2]][1] = insert(tree,tree[cur[2]][1],val)

    return cur

def pre_order(tree,pre,node):
    pre.append(node)
    if tree[node][0]!=-1:
        pre_order(tree,pre,tree[node][0][2])
    if tree[node][1]!=-1:
        pre_order(tree,pre,tree[node][1][2])
        
def post_order(tree,post,node):
    if tree[node][0]!=-1:
        post_order(tree,post,tree[node][0][2])
    if tree[node][1]!=-1:
        post_order(tree,post,tree[node][1][2])
    post.append(node)


def solution(nodeinfo):
    tree = defaultdict(list)
    for i,v in enumerate(nodeinfo):
        nodeinfo[i] = v+[i+1]
        tree[nodeinfo[i][2]] = [-1,-1]
    nodeinfo.sort(key=lambda x: [-x[1],x[0]])
    root = nodeinfo[0]
    
    for i in range(1,len(nodeinfo)):
        insert(tree,root, nodeinfo[i])
    pre= []
    post = []
    pre_order(tree,pre,root[2])
    post_order(tree,post,root[2])

    answer= [pre,post]

    return answer