# from auth import SignUp, Login
# from main import Main, get_book
# from main import get_book
import datetime
import random
import json

class User() :
    
    def __init__ (self, books) :
        self.ID = 'none'
        self.book = books
        self.sample_books = {}

    def first(self, name) :
        self.ID = name
        print(f'오신 걸 환영합니다, {name}님.\n')
        print()
        print('-'*40)
        print('[ 추천 도서 ]')
        for title, info in self.book.items() :
            if info[-1] == "true" :
                self.sample_books[title] = info[:-1]
        sample = random.sample(list(self.sample_books.items()), min(3, len(self.sample_books)))
        for title, info in sample:
            print(f'{title} : 작가,{info[0]}.  출간일,{info[1]}.  출판사,{info[2]}.')
            
        print('-'*40)
        self.second()
    
    def second(self) :
        print()
        print('[ 1.도서조회  2.대출  3.반납  4.현재대출목록  0.종료 ]')
        a = input('메뉴를 선택해, 번호를 입력해주세요. : ')
        if a == '1' :
            self.search('0')
    
    def search(self, n) :
        print()
        if n == '0' :
            print('- 도서조회 -')
        q = {}
        while True :
            a = input('찾고 있는 책의 제목, 작가등을 입력해주세요. \n')
            f = False
            i = 1
            print()
            print('[ 검색 결과 ]')
            for title, info in self.book.items():
                if a in title or a in info:
                    print(f'{i}. {title}', end='')
                    q[title] = info
                    i += 1
                    f = True
            if not f and n == 0 :
                print('검색 결과가 없습니다. 다시 시도해주세요.')
            elif n == '1':
                a = input('대출할 책의 번호를 입력해주세요. : ')
                key = list(q.keys())[a-1]
                return key, q[key][0]
            else :
                self.second()
                break
    
    def bor(self) :
        print()
        print('- 대출 -')
        borrowed_count = sum(1 for info in self.book.values() if info[-1] == self.ID)
        if borrowed_count >= 5:
            print('현재 대출 중인 책이 5권 이상입니다. 더 이상 대출할 수 없습니다.')
            self.second()
            return
        while True :
            print('대출 할 책을 골라주세요.')
            c, h = self.search(1)
            a = input(f'[ {c} : {h} ]'+'를 대출 하시겠습니까?(y/n) : ')
            if a in ['y', 'Y', 'ㅛ'] :
                now = datetime.datetime.now()
                date = now + datetime.timedelta(days=7)
                print(f'{now.month}월 {now.day}일, 대출되었습니다.')
                print(f'{date.month}월 {date.day}일까지 반납 부탁드립니다.')
                #book.json 파일 수정
                self.book[c][-1] = self.ID
                self.book[c][-2] = f'{date.year}.{date.month}.{date.day}'
                with open('books.json', 'w', encoding='utf-8') as f:
                    json.dump(self.book, f, ensure_ascii=False, indent=4)
                break
        self.second()
    
    def retu(self) :
        print()
        print('- 반납 -')
        q = {}
        i = 1
        for title, info in self.book.items() :
            if info[-1] == self.ID :
                q[title] = info
        overdue_days = {}
        
        if len(q) >=1 :
            print('대출한 책을 찾았습니다.')
            for title, info in q.items() :
                due_str = info[-2]
                due_date = datetime.datetime.strptime(due_str, '%Y.%m.%d')
                today = datetime.datetime.now()
                if today > due_date :
                    days_overdue = (today - due_date).days
                    overdue_days[title] = days_overdue
                    status = f'현재 연체 중입니다. ({days_overdue}일 연체)'
                else : 
                    status = '정상 대출 중입니다.'
                print(f'{i}. {title} : {info[0]}. 반납 날짜: {due_str} → {status}')
                i += 1