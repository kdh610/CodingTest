
def solution(m, musicinfos):
    note= {'A#':'H', 'B#':'I','C#':'J', 'D#':'K', 'F#':'L', 'G#':'M'}

    def replace_note(music):
        for k,v in note.items():
            music = music.replace(k,v)

        return music


    new_info = []

    for i,music in enumerate(musicinfos):
        start, end, title, score = music.split(',')

        start_H, start_M = start.split(':')
        start = int(start_H)*60 + int(start_M)

        end_H, end_M = end.split(':')
        end = int(end_H) * 60 + int(end_M)

        time = end-start
        score = replace_note(score)

        full_score = ''
        for j in range(time):
            full_score+=score[j%len(score)]

        new_info.append((time,i,title,full_score))

    m=replace_note(m)

    answer=[]
    for music in new_info:
        if m in music[3]:
            answer.append(music)


    answer.sort(key=lambda x:[-x[0],x[1]])

    if not answer:
        return '(None)'
    else:
        return answer[0][2]