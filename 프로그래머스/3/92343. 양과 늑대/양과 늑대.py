

from collections import *





def solution(info, edges):
    answer = 0

    tree = defaultdict(list)

    for parent, child in edges:
        tree[parent].append(child)

    return max_sheep([0], tree, info, 0,0)



def max_sheep(nodes, tree, info, sheep, wolf) :

    if not nodes:
        return sheep

    MAX_SHEEP = sheep

    for idx, node in enumerate(nodes):
        print('node',node)
        if info[node] == 0:
            MAX_SHEEP = max(MAX_SHEEP, max_sheep(nodes[:idx]+nodes[idx+1:] + tree[node], tree, info, sheep +1 , wolf))
        elif info[node]==1 and  wolf+1 < sheep:
            MAX_SHEEP = max(MAX_SHEEP, max_sheep(nodes[:idx]+nodes[idx + 1:] + tree[node], tree, info, sheep, wolf+1))


    return MAX_SHEEP
