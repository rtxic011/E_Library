
class SignUp : 
    # inf = {'admin':'admin1234'} 
    # def __init__(self) :
    @staticmethod
    def first() :
        print('- 회원가입 -')
        #아이디
        while True :
            a = input('아이디 : ')
            with open('user_data.txt', 'r') as f:
                for line in f:
                    saved_id, _ = line.strip().split(',')
                    if saved_id == a:
                        print('이미 존재하는 아이디입니다.')
                        return
            break
        #비밀번호
        b = input('비밀번호 : ')
        SignUp.inf[a] = b
        # print('회원가입이 완료 되었습니다.')
        with open('user_data.txt', 'a') as f:
            f.write(f'{a},{b}\n')
        print('회원가입이 완료 되었습니다.')
        return 0

class Login(SignUp) :
    def first() :
        print('- 로그인 -')
        while True :
            a = input('아이디 : ')
            b = input('비밀번호 : ')
            if a in SignUp.inf.keys() and b == SignUp.inf[a] :
                print('로그인 완료')
                break
        return a