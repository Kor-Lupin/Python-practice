import random
import time

Num = []
i = 1
while True:
    Que = int(input('{}번째 로또 번호를 입력해주세요 : '.format(i)))
    if Que <= 9 and Que >= 0 :
        if Que in Num:
            print('중복된 숫자입니다. 다시 입력해주세요')
            pass
            i == i 
        else:
            Num.append(Que)
            i += 1
    else:
        pass
        print('0~9숫자중에 하나를 입력해주세요.')
        i == i 
    if len(Num) == 6:
        print('==========================')
        print('당신이 입력한 Lotto번호 : \n')
        print(Num)
        print('==========================')
        Que1 = int(input('1.이 번호로 저장하기\n2.수정하기\n번호 :'))
        if Que1 == 2:
            Num = []
            i = 1
            pass
        elif Que1 == 1:
            print('\n당신의 최종 Lotto번호는 \n{} 입니다.'.format(Num))
            break

time.sleep(3)        
print('\n\nLotto번호 뽑기를 시작하겠습니다!')
time.sleep(2)
pot = [n for n in range(0,10)]
jackpot = []
for a in range(1,7):
    random.shuffle(pot)
    pick = pot.pop()
    print('{} 번째 당첨 번호는 {}입니다.'.format(a,pick))
    jackpot.append(pick)
    time.sleep(2)

print('이번 당첨 번호는 {} 입니다.'.format(jackpot))
time.sleep(4)
print('당첨 번호 조회를 시작하겠습니다.\n')
time.sleep(3)
# Num -> 내가 입력한 로또
# jackpot -> 로또번호
Check = []
for i in Num:
    if i in jackpot:
        Check.append(i)

print('당첨된 숫자는 {} 입니다.'.format(Check))
if len(Check) == 0:
    print('꽝!! 다음 기회에...')
if len(Check) == 1:
    print('1개 맞았습니다! 6등')
if len(Check) == 2:
    print('--------------------------------')
    print('축하합니다! 2개 맞았습니다! 5등')
    print('-------------------------------')
if len(Check) == 3:
    print('===============================')
    print('축하합니다!! 3개 맞았습니다! 4등')
    print('===============================')
if len(Check) == 4:
    print('★★★★★★★★★★★★★★★★★★★★★★')                                
    print('축하합니다!!! 4개 맞았습니다! 3등')
    print('★★★★★★★★★★★★★★★★★★★★★★')
if len(Check) == 5:
    print('★★★★★★★★★★★★★★★★★★★★★★')                                
    print('축하합니다!!! 5개 맞았습니다! 2등')
    print('★★★★★★★★★★★★★★★★★★★★★★')
if len(Check) == 6:
    print('★★★★★★★★★★★★★★★★★★★★★★')
    print('★★★★★★★★★★★★★★★★★★★★★★')
    print('와우!!!!! 이럴수가! 다 맞았습니다 1등 당첨!!')
    print('★★★★★★★★★★★★★★★★★★★★★★')
    print('★★★★★★★★★★★★★★★★★★★★★★')


