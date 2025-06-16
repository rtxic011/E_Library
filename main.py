import json
from auth import SignUp, Login
from user import User
from manager import Manager
import time

with open('books.json', 'r', encoding='utf-8') as f:
    get_book =json.load(f) 


with open('manager_data.json', 'r', encoding='utf-8') as f:
    get_manager = json.load(f)


with open('user_data.json', 'r', encoding='utf-8') as f:
    get_user = json.load(f)


class Main() :
    # def __init__(self):
    
    def intro(self) :
        print('전자도서관입니다.')
        # time.sleep(0.8)
        print('-'*40)
        print('전자도서관에 오신 것을 환영합니다. \n번호를 입력하여 다음 메뉴로 이동하세요.')
        print('-'*40)
        # time.sleep(0.8)
        while True :
            a = input('1.로그인  2.회원가입  0.종료\n')
            if a == '1' :
                name, check = login.first()
                if check == 0 :
                    User.first(name)
                if check == 1 :
                    Manager.first(name)
                elif check == '2' :
                    SignUp.first()
                    name, check = login.first()
                    if check == 0 :
                        User.first(name)
                    if check == 1 :   
                        Manager.first(name)
                
            elif a == '2' :
                SignUp.first()
                name, check = login.first()
                if check == 0 :
                    User.first(name)
                #if check == 1 :
                    #매니저 코드 실행
            elif a == '0' :
                print()
                print('이용해주셔서 감사합니다.')
                return 0
            else :
                print('잘못된 입력입니다. 다시 시도해주세요.')

User = User(get_book)
Manager = Manager(get_book)
SignUp = SignUp(get_manager, get_user)
login = Login(get_manager, get_user)

ma = Main()
ma.intro()