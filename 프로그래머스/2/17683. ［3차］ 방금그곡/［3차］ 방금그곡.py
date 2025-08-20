def solution(m, musicinfos):
    answer='(None)'
    max_time = 0
    m=(m.replace('C#', 'V')
        .replace('D#', 'W')
        .replace('F#', 'X')
        .replace('G#', 'Y')
        .replace('A#', 'Z')
      .replace('B#', 'F'))


    for i in musicinfos:
        info = i.split(",")
        start_h = info[0].split(":")[0]
        start_m = info[0].split(":")[1]
        start_time = int(start_h)*60 + int(start_m)

        end_h = info[1].split(":")[0]
        end_m = info[1].split(":")[1]
        end_time = int(end_h) * 60 + int(end_m)
        title = info[2]
        notes = (info[3]
                 .replace('C#', 'V')
                 .replace('D#', 'W')
                 .replace('F#', 'X')
                 .replace('G#', 'Y')
                 .replace('A#', 'Z') .replace('B#', 'F'))

        play_time = end_time - start_time
        music_length = len(notes)


        music = notes * (play_time//music_length) + notes[:(play_time%music_length)]

        if m in music:
            if max_time < play_time:
                max_time = play_time
                answer = title

    return answer