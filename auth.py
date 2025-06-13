import json

class SignUp : 
    # inf = {'admin':'admin1234'} 
    def __init__(self, manager_inf, user_inf) :
        self.manager_inf = manager_inf
        self.user_inf = user_inf
        
    # @staticmethod
    def first(self) :
        print()
        print('- 회원가입 -')
        #아이디
        while True:
            a = input('아이디 : ')
            if self.user_inf and a in self.user_inf:
                print('이미 존재하는 아이디입니다. 다시 입력해주세요.')
            elif self.manager_inf and a in self.manager_inf:
                print('이 아이디는 사용할 수 없습니다.')
            else:
                break
                
        #비밀번호
        b = input('비밀번호 : ')
        self.user_inf[a] = b
        #user_data.jsond을 열고, w쓰기, encoding='utf-8'한글이 깨지지 않게
        with open('user_data.json', 'w', encoding='utf-8') as f:
            #json.dump딕셔너리를 json형식으로, self.user_inf저장할 파일
            #ensure_ascii=False한글이 깨지지 않게, indent=4들여쓰기
            json.dump(self.user_inf, f, ensure_ascii=False, indent=4)
        print('회원가입이 완료 되었습니다.')
        return 0

class Login(SignUp) :
    
    def first(self) :
        print()
        print('- 로그인 -')
        
        while True :
            a = input('아이디 : ')
            if a in self.user_inf.keys() :
                b = input('비밀번호 : ')
                if b == self.user_inf[a] :
                    print('로그인 완료')
                    return a, 0
                elif b != self.user_inf[a] :
                    print('로그인 실패! 아이디와 비밀번호가 맞지 않습니다.')
                elif a in self.manager_inf.keys() and b == self.manager_inf[a] :
                    print('관리자 로그인 완료')
                    return a, 1
            else :
                print('존재하지 않는 아이디입니다.')