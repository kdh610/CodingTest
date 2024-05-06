from itertools import *
def solution(users, emoticons):
    discounts = [10,20,30,40]


    products = list(product(discounts, repeat=len(emoticons)))

    answer = []

    for discount in products:

        sales = 0
        emti_plus=0
        for user in users:
            rate, cost = user
            total_cost = 0
            for i,d in enumerate(discount):
                if d>=rate:
                    total_cost+= emoticons[i] * ((100-d)/100)
            if total_cost>=cost:
                emti_plus+=1
                total_cost=0
            sales+=total_cost

        answer.append([emti_plus,sales])

    answer.sort(key=lambda x:[-x[0],-x[1]])
    return answer[0]