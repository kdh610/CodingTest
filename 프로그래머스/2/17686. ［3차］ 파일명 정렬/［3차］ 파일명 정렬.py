import re
def solution(files):
    p = re.compile('(\D*)(\d*)(.*)')

    fileName = []

    for i,file in enumerate(files):
        m = list(p.findall(file)[0])
        m.append(i)
        m[0] = m[0].lower()
        m[1] = int(m[1])
        m[2] = m[2].lower()
        fileName.append(m)

    fileName.sort(key=lambda x:[x[0],x[1],x[3]])

    answer=[]
    for name in fileName:
        num = name[3]
        answer.append(files[num])

    return answer