# from auth import SignUp, Login
# from main import Main, get_book
from main import get_book
import datetime

class User() :
    
    def __init__ (self) :
        self.ID = 'none'
        self.book = get_book()

    def first(self, name) :
        self.ID = name
        print(f'오신 걸 환영합니다, {name}님.\n')
        print('-'*40)
        print('[ 도서 목록 ]')
        for title, info in self.book.items() :
            print(f'{title} : {", ".join(info)}')
        print('-'*40)
        self.second()
    
    def second(self) :
        print()
        print('[ 1.도서조회  2.대출  3.반납  4.현재대출목록  0.종료 ]')
        a = input('메뉴를 선택해, 번호를 입력해주세요. : ')
        if a == '1' :
            self.search(0)
    
    def search(self, n) :
        print()
        if n == 0 :
            print('- 도서조회 -')
        q = {}
        while True :
            a = input('찾고 있는 책의 제목, 작가등을 입력해주세요. \n')
            f = False
            for i, (title, info) in enumerate(self.book.items(), start=1):
                if a in title or a in info:
                    print(f'{i}. {title} : {", ".join(info)}')
                    q[title] = info
            if not f and n == 0 :
                print('검색 결과가 없습니다. 다시 시도해주세요.')
            elif n == 0:
                self.second()
                break
            elif n == 1:
                a = input('대출할 책의 번호를 입력해주세요. : ')
                key = list(q.keys())[a-1]
                return key, q[key]    
    
    def bor(self) :
        print()
        print('- 대출 -')
        while True :
            print('대출 할 책을 골라주세요.')
            c, h = self.search(1)
            a = input(f'[{c} : {", ".join(h)}]'+'를 대출 하시겠습니까?(y/n) : ')
            if a in ['y', 'Y', 'ㅛ'] :
                now = datetime.datetime.now()
                date = now + datetime.timedelta(days=7)
                print(f'{now.month}월 {now.day}일, 대출되었습니다.')
                print(f'{date.month}월 {date.day}일까지 반납 부탁드립니다.')
                break
        self.second()
    
    