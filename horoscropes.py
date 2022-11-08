#%% 비밀번호 암호화 및 복호화
Kim_pw = str(input('비밀번호를 입력해 주세요 : '))
en_pw = ''
de_pw = ''

for i in Kim_pw:
    en_pw += chr(ord(i) * 9 + 15)
    
print('기존 비밀번호 : %s' %Kim_pw)
print('암호화된 비밀번호 : %s' %en_pw)

for i in en_pw:
    de_pw += chr((ord(i)- 15) // 9)

print('복호화된 비밀번호 : %s' %de_pw)


#%% 삼항 연산자
# =============================================================================
# 다음중 프로그래밍 언어가 아닌 것은?
# 1.JAVA
# 2.파이썬
# 3.C언어
# 4.망둥어
# =============================================================================

que = '다음중 프로그래밍 언어가 아닌 것은?'
num = '1.JAVA\n2.파이썬\n3.C언어\n4.망둥어\n정답 : '

while True:
    Que = int(input(que + '\n' + num))
    if Que == 4:
        print('정답입니다!')
        break
    elif Que < 4 and Que > 0 :
        print('오답입니다!')
    else: 
        print('잘못입력하셨습니다!')
    
#%% horoscopes
horoscopes = ['물병자리', '물고기자리', '양자리', '황소자리',
              '쌍둥이자리','게자리','사자자리','처녀자리',
              '천칭자리','전갈자리','사수자리','염소자리']
ErrMsg = '잘못 입력하셨습니다.'
result = ''
while True :
    que = int(input('1.생년월일 입력하기\n2.나가기\n입력하기 : '))
    if que == 1:
        month = int(input('당신이 태어난 월은?\n예)10\n입력하기 : '))
        date = int(input('당신이 태어난 일은?\n예)10\n입력하기 : '))
        if month == 1:
            if date <= 19 and date >= 1 :
                result = horoscopes[11]
            elif date >= 20 and date <= 31 :
                result = horoscopes[0]
            else:
                result = ErrMsg
        if month == 2:
            if date <= 18 and date >= 1 :
                result = horoscopes[0]
            elif date >= 19 and date <=29 :
                result = horoscopes[1]
            else: 
                result = ErrMsg
        if month == 3:
            if date >= 1 and date <= 20:
                result = horoscopes[1]
            elif date >= 21 and date <= 31:
                result = horoscopes[2]
            else:
                result = ErrMsg
        if month == 4:
            if date >=1 and date <=19:
                result = horoscopes[2]
            elif date >= 20 and date <= 30 :
                result = horoscopes[3]
            else:
                result = ErrMsg
        if month == 5 :
            if date >=1 and date <= 20:
                result = horoscopes[3]
            elif date >= 21 and date <=31:
                result = horoscopes[4]
            else :
                result = ErrMsg
        if month == 6:
            if date >=1 and date <= 21 :
                result = horoscopes[4]
            elif date >= 22 and date <= 30:
                result = horoscopes[5]
            else:
                result = ErrMsg
        if month == 7:
            if date >= 1 and date <= 22:
                result = horoscopes[5]
            elif date >= 23 and date <= 31:
                result = horoscopes[6]
            else:
                result = ErrMsg
        if month == 8:
            if date >= 1 and date <= 22 :
                result = horoscopes[6]
            elif date >= 23 and date <= 31:
                result = horoscopes[7]
            else:
                result = ErrMsg
        if month == 9:
            if date >= 1 and date <= 22 :
                result = horoscopes[7]
            elif date >= 23 and date <= 30:
                result = horoscopes[8]
            else :
                result = ErrMsg
        if month == 10:
            if date >= 1 and date <= 22 :
                result = horoscopes[8]
            elif date >= 23 and date <= 31:
                result = horoscopes[9]
            else:
                result = ErrMsg
        if month == 11:
            if date >= 1 and date <= 22:
                result = horoscopes[9]
            elif date >= 23  and date <= 30:
                result = horoscopes[10]
            else:
                result = ErrMsg
        if month == 12:
            if date >= 1 and date <=24:
                result = horoscopes[10]
            elif date >= 25 and date <= 31:
                result = horoscopes[11]
            else:
                result = ErrMsg
        print(result)
    elif que == 2:
        break
    else:
        result = ErrMsg
        print(result)
        

        
            
            
            
        
    


























