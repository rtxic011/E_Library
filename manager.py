from auth import SignUp, Login
from main import Main, get_book

class Manager(SignUp, Login) :
    def __init__ (self) :
        self.ID = 'none'    
        self.book = get_book()
        
    def first(self, name) :
        self.ID = name
        print(f'오신 걸 환영합니다, {name}님.')
        self.second()
    
    def second(self) :
        print('[ 1.도서추가  2.도서삭제 3.도서정보수정  4.현재대출목록  0.종료 ]')
        a = input('메뉴를 선택해, 번호를 입력해주세요. : ')