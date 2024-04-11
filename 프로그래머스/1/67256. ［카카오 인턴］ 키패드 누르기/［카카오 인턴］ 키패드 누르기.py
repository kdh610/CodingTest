from collections import *
def solution(numbers, hand):
    keypad = {1:(0,0), 2:(0,1), 3:(0,2),
              4:(1,0), 5:(1,1), 6:(1,2),
              7:(2,0), 8:(2,1), 9:(2,2),
              '*':(3,0), 0:(3,1), '#':(3,2)}

    left_hand = '*'
    right_hand = '#'

    left_num = [1,4,7]
    right_num = [3,6,9]
    center_num = [2,5,8,0]
    answer =''

    for n in numbers:

        if n in left_num:
            answer+='L'
            left_hand = n
        elif n in right_num:
            answer+='R'
            right_hand = n
        else:
            ny = keypad[n][0]
            nx = keypad[n][1]

            left_dist = abs(keypad[left_hand][0] - ny) + abs(keypad[left_hand][1] - nx)
            right_dist = abs(keypad[right_hand][0] - ny) + abs(keypad[right_hand][1] - nx)

            if left_dist<right_dist:
                answer+='L'
                left_hand = n
            elif left_dist>right_dist:
                answer+='R'
                right_hand = n
            elif left_dist==right_dist:
                if hand=='left':
                    answer += 'L'
                    left_hand = n
                else:
                    answer += 'R'
                    right_hand = n
            
    
    
    
    return answer