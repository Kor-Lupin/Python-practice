# 한 반의 반장 선거(반의 총 인원수 : All_cnt명 일 때)
vote_dict = {}
All_cnt = 10
Left_cnt = All_cnt
while True :
    print('\n남은 인원 : {}'.format(Left_cnt), end = '')
    msg = input('반장으로 뽑을 한 사람을 적어주세요 : ')
    Left_cnt -= 1
    if msg not in vote_dict:
            vote_dict[msg] = 1
            if Left_cnt ==  0 :
                print('모든 학생이 투표를 했습니다')
                print('이름 \t 총 득표 수 \t 등수')
                print('-------------------------')
                result = sorted(vote_dict.items(), key=lambda x: x[1], reverse = True)
                totalrank = 0
                for i in range(len(result)) :
                    totalrank += 1
                    print(result[i][0],'\t\t ',result[i][1],' \t ', str(totalrank)+'등')
                break
            
            else:
                print(vote_dict)
            
    else:
        vote_dict[msg] = vote_dict[msg] + 1
        if Left_cnt ==  0 :
            print('모든 학생이 투표를 했습니다')
            result = sorted(vote_dict.items(), key=lambda x: x[1], reverse = True)
            totalrank = 0
            print('이름 \t 총 득표 수 \t 등수')
            print('-------------------------')
            for i in range(len(result)) :
                totalrank += 1
                print(result[i][0],'\t\t ',result[i][1],' \t ', str(totalrank)+'등')
            break
        else:
            print(vote_dict)
       
        

        

