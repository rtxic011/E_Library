import json
from auth import SignUp, Login
from user import User
from manager import Manager

with open('books.json', 'r', encoding='utf-8') as f:
    get_book =json.load(f) 


with open('manager_data.json', 'r', encoding='utf-8') as f:
    get_manager = json.load(f)


with open('user_data.json', 'r', encoding='utf-8') as f:
    get_user = json.load(f)


user = User(get_book)
manager = Manager(get_book)
signup = SignUp(get_manager, get_user)
login = Login(get_manager, get_user)

class Main() :
    def intro(self):
        print('전자도서관입니다.')
        print('-' * 40)
        print('전자도서관에 오신 것을 환영합니다. \n번호를 입력하여 다음 메뉴로 이동하세요.')
        print('-' * 40)

        while True:
            a = int(input('1.로그인  2.회원가입  0.종료\n'))
            if a == 1:
                # print("qwe1")
                name, check = login.first()
                # print("qwe2")
                if check == 0:
                    user.first(name)
                    # print("wer3")
                    break
                elif check == 1:
                    manager.first(name)
                    break
                elif check == 2:
                    a = '2'
                    continue
            elif a == 2:
                signup.first()
            elif a == 0:
                print()
                print('이용해주셔서 감사합니다.')
                return 0
            else:
                print('잘못된 입력입니다. 다시 시도해주세요.')

ma = Main()
ma.intro()