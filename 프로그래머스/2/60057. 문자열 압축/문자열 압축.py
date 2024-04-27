def solution(s):
    answer = len(s)
    for i in range(1,len(s)):
        result=''
        string = s[0:i]
        cnt=1
        for j in range(i,len(s),i):

            if string!=s[j:j+i]:
                if cnt>1:
                    result+=(str(cnt) + string)

                else:
                    result+=string
                string = s[j:j+i]
                cnt=1
            else:
                cnt+=1

            if j==len(s)-i or len(string)<i:
                string = s[j:]
                if cnt > 1:
                    result += (str(cnt) + string)
                else:
                    result += string

        answer = min(answer,len(result))
    return answer