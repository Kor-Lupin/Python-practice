#%% mini lotto
import numpy as np
Num = []
while True :
    My_Lotto = int(input('0~9번호 중 하나를 5개 자리로 넣어주세요\n예) 3\n입력 : '))
    if My_Lotto >= 0 and My_Lotto < 10:
        Num.append(My_Lotto)
        if len(Num) == 5:
            print('==========================')
            print('당신이 입력한 Lotto번호 : \n')
            print(Num)
            print('==========================')
            Que = int(input('1.이 번호로 저장하기\n2.수정하기\n번호 :'))
            if Que == 2:
                Num = []
                My_Lotto = int(input('0~9번호 중 하나를 5개 자리로 넣어주세요\n예) 3\n입력 : '))
                if My_Lotto >= 0 and My_Lotto < 10:
                    Num.append(My_Lotto)
                    if len(Num) == 5:
                        print('========================')
                        print('당신이 입력한 Lotto번호 : \n')
                        print(Num)
                        print('========================')
                else :
                    pass
                    print('다시 입력해 주세요')
        
            if Que == 1 :
                print('\n당신의 최종 Lotto번호는 \n{} 입니다.'.format(Num))
                Choice = int(input('1. 로또번호 뽑기\n입력 : '))
                Lotto_1 = np.random.randint(10)
                Lotto_2 = np.random.randint(10)
                Lotto_3 = np.random.randint(10)
                Lotto_4 = np.random.randint(10)
                Lotto_5 = np.random.randint(10)
                Lotto_Num = [0,0,0,0,0]
                while True :
                    if Choice == 1:
                        Lotto_Num[0] = Lotto_1
                        Lotto_Num[1] = Lotto_2
                        Lotto_Num[2] = Lotto_3
                        Lotto_Num[3] = Lotto_4
                        Lotto_Num[4] = Lotto_5
                        Result = int(input('1.로또 등수 확인하기\n입력 : '))
                        if Result == 1 :
                            Rank = []
                            for i in range(len(Num)):
                                if Num[i] in Lotto_Num:
                                        Rank.append(Num[i])
                            if len(Rank) == 0 :
                                print('꽝!! 다음 기회에...')
                                
                            elif len(Rank) == 1:
                                print('1개 맞았습니다! 5등')
                                
                            elif len(Rank) == 2:
                                print('--------------------------------')
                                print('축하합니다! 2개 맞았습니다! 4등')
                                print('-------------------------------')
                                
                            elif len(Rank) == 3:
                                print('===============================')
                                print('축하합니다!! 3개 맞았습니다! 3등')
                                print('===============================')
                                
                            elif len(Rank) == 4:
                                print('★★★★★★★★★★★★★★★★★★★★★★')                                
                                print('축하합니다!!! 4개 맞았습니다! 2등')
                                print('★★★★★★★★★★★★★★★★★★★★★★')
                                
                            elif len(Rank) == 5:
                                print('★★★★★★★★★★★★★★★★★★★★★★')
                                print('★★★★★★★★★★★★★★★★★★★★★★')
                                print('와우!!!!! 이럴수가! 다 맞았습니다 1등 당첨!!')
                                print('★★★★★★★★★★★★★★★★★★★★★★')
                                print('★★★★★★★★★★★★★★★★★★★★★★')
                        break
                    break
                break
                    
    else :
        pass
        print('다시 입력해 주세요')
        
        
        


        

        
        
        
        
        
        
        
    
         
        
