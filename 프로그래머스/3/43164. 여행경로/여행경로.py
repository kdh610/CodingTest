from collections import *
import copy
def solution(tickets):
    dict = defaultdict(list)

    for i,ticket in enumerate(tickets):
        a,b = ticket[0], ticket[1]
        dict[a].append([b,i])



    n = len(tickets)
    visit = [False] * n

    answer= []
    result = ['ICN']


    def dfs(start, result, cnt):


        if cnt == n:
            temp = copy.deepcopy(result)
            answer.append(temp)
            return

        for city, ticket in dict[start]:
            if not visit[ticket]:

                visit[ticket]=True
                result.append(city)
                dfs(city, result, cnt+1)
                visit[ticket] = False
                result.pop()


    dfs('ICN', result, 0)
    answer.sort()
    return answer[0]