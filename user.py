from auth import SignUp, Login
from main import Main, get_book

class User(SignUp, Login) :
    
    def __init__ (self) :
        self.ID = 'none'
        self.book = get_book()

    def first(self, name) :
        self.ID = name
        print(f'오신 걸 환영합니다, {name}님.')
        self.second()
    
    def second(self) :
        print('[ 1.도서조회  2.대출  3.반납  4.현재대출목록  0.종료 ]')
        a = input('메뉴를 선택해, 번호를 입력해주세요. : ')
        if a == '1' :
            self.search(0)
    
    def search(self, n) :
        if n == 0 :
            print('- 도서조회 -')
        q = []
        while True :
            a = input('찾고 있는 책의 제목, 작가등을 입력해주세요.')
            f = False
            for i, (title, info) in enumerate(self.book.items(), start=1):
                if a in title or a in info:
                    print(f'{i}. {title} : {", ".join(info)}')
                    q.append(title)
            if not f and n == 0 :
                print('검색 결과가 없습니다. 다시 시도해주세요.')
            elif n == 0:
                self.second()
                break
            elif n == 1:
                
                return q[i-1]
    
    def bor(self) :
        print('- 대출 -')
        while True :
            a = input('')