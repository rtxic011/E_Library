from auth import Login, SignUp

class Main() :
    def intro(self) :
        print('전자도서관입니다.')
        a = input('1.로그인  2.회원가입  0.종료\n')
        if a == '1' :
            Login.first()
        if a == '2' :
            SignUp.first()

ma = Main()
ma.intro()