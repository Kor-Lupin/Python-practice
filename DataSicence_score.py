title = '데이터사이언스 중간성적을 입력해주세요.(30점 만점)\n'
Msg = '1.추가\n2.수정\n3.삭제\n4.목록\n5.나가기\n번호: '
errMsg = '다시 입력해 주세요.'

studentDict = {}

while True :
    choice = int(input(title + Msg))
    if choice == 1:
        name = input('학생이름 : ')
        if name not in studentDict :
            studentDict[name] = int(input('성적을 입력해주세요 : '))
        else :
            print('이미 등록되어 있는 학생입니다.')
        print(studentDict)
        
    elif choice == 2:
        choice = int(input('1.학생명 수정\n2.점수 수정\n번호 : '))
        name = input('수정 할 학생명 : ')
        if choice == 1 :
            if name in studentDict :
                new = input('새로운 학생명 : ')
                score = studentDict[name]
                del studentDict[name]
                studentDict[new] = score
            else :
                print('존재하지 않는 학생입니다.')
        elif choice == 2:
            studentDict[name] = input('새로운 점수 :')
            
    elif choice == 3:
        name = input('삭제할 학생명 : ')
        if name in studentDict:
            del studentDict[name]
        else :
            print('존재하지 않는 학생입니다.')
            
    elif choice == 4:
        print('데이터 사이언스 중간고사 성적')
        studentTuple = sorted(studentDict.items())
        print(studentTuple)
        print('----------------------------')
        print('이름 \t 성적\t 등수')
        totalRank = 0
        for i in range(len(studentTuple)):
            totalRank += 1
            print(studentTuple[i][0],'\t', studentTuple[i][1],'\t', str(totalRank) + '위')
         
    elif choice ==5 :
        break
    
    else:
        print(errMsg)
            
            
                
                
                
                
                
                
                
                
                
                
                
            
                
        