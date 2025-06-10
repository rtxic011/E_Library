import json
from auth import Login, SignUp

with open('books.json', 'r', encoding='utf-8') as f:
    book = json.load(f) 

def get_book() :
    return book

class Main() :
    # def __init__(self):
    
    def intro(self) :
        print('전자도서관입니다.')
        a = input('1.로그인  2.회원가입  0.종료\n')
        if a == '1' :
            Login.first()
        if a == '2' :
            SignUp.first()

ma = Main()
ma.intro()