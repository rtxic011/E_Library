class SignUp() :
    inf = {'admin':'admin1234'} #일단 관리자
    
    def first() :
        print('- 회원가입 -')
        #아이디
        while True :
            a = input('아이디 : ')
            if a in SignUp.inf.keys :
                    print('중복된 아이디 입니다. 다시 입력해주세요.')
            else : 
                break
        #비밀번호
        b = input('비밀번호 : ')
        SignUp.inf[a] = b
        print('회원가입이 완료 되었습니다.')

class Login(SignUp) :
    def first() :
        print('- 로그인 -')
        while True :
            a = input('아이디 : ')
            b = input('비밀번호 : ')
            if a in SignUp.inf.keys() and b == SignUp.inf[a] :
                print('로그인 완료')
                break