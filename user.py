# from auth import SignUp, Login
# from main import Main, get_book
# from main import get_book
import datetime
import random
import json

class User() :
    
    def __init__ (self, books) :
        self.ID = 'none'
        self.check = True
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
            print(f'{title} :\n 작가: {info[0]}.  출간일: {info[1]}.  출판사: {info[2]}.')
            print()
            
        print('-'*40)
        self.second()
        
    def che(self) :
        q = {}
        for title, info in self.book.items() :
            if info[-1] == self.ID :
                q[title] = info[0]
        overdue_days = {}
        for title, info in q.items() :
                due_str = info[-2]
                due_date = datetime.datetime.strptime(due_str, '%Y.%m.%d')
                today = datetime.datetime.now()
                if today > due_date :
                    days_overdue = (today - due_date).days
                    overdue_days[title] = days_overdue
                    self.check = False
                else : 
                    self.check = True
    
    def second(self) :
        print()
        while True :
            print('[ 1.도서조회  2.대출  3.반납  4.현재대출목록  0.로그아웃 ]')
            a = input('메뉴를 선택해, 번호를 입력해주세요. : ')
            if a == '1' :
                self.search()
                break
            elif a == '2' :
                self.bor()
                break
            elif a == '3' :
                self.retu()
                break
            elif a == '4' :
                self.list()
                break
            elif a == '0' :
                self.logout()
                print()
                break
            else : 
                print('잘못된 입력입니다. 다시 시도해주세요.')
    
    def search(self) :
        print()
        print('- 도서조회 -')
        # q = self.sear()
        self.sear()
        self.second()
        
        
    def sear(self) :
        q = {}
        while True :
            print('찾고 있는 책의 제목, 작가등을 입력해주세요.')
            print('모든 책 목록을 보시려면 엔터를 누르시면 됩니다.')
            a = input('입력하기 : ')
            i = 1
            print()
            print('[ 검색 결과 ]')
            a = a.lower()
            f, i = self.se(a, q, False, i)
            a = a.upper()
            f, i = self.se(a, q, f, i)
            # f = self.se(a, q)
    
    def se(self, a, q, f, i) :
        f = bool(f)
        i = i
        for title, inf in self.book.items():
                info = inf[:3]
                if a in title or a in info:
                    if info[-1] == 'true' :
                        ch = '대출 가능'
                    else :
                        ch = '대출 불가능'
                    print(f'{i}. {title} : {info[0]} [{ch}]')
                    q[title] = info
                    i += 1
                    f = True
        if f == False :
                print('검색 결과가 없습니다. 다시 시도해주세요.')
        elif f == True :
            return q

    def bor(self) :
        print()
        print('- 대출 -')
        borrowed_count = sum(1 for info in self.book.values() if info[-1] == self.ID)
        if borrowed_count >= 5 :
            print('현재 대출 중인 책이 5권 이상입니다. 더 이상 대출할 수 없습니다.')
            self.second()
            return
        if self.check == False :
            print('현재 연체중입니다. 반납 후 다시 시도해주세요.')
            self.second()
            return
        while True :
            # print('대출 할 책을 골라주세요.')
            q = self.sear()
            print()
            a = input('대출할 책의 번호를 입력해주세요. : ')
            if a.isdigit() :
                a = int(a)
                if 0 < a <= len(q) :
                    key = list(q.keys())[a-1]
                    # c, h = self.search(1)
                    if q[key][-1] == 'true' :
                        b = input(f'[ {key} : {q[key][0]} ]'+'를 대출 하시겠습니까?(y/n) : ')
                        if b in ['y', 'Y', 'ㅛ'] :
                            now = datetime.datetime.now()
                            date = now + datetime.timedelta(days=7)
                            print(f'{now.month}월 {now.day}일, 대출되었습니다.')
                            print(f'{date.month}월 {date.day}일까지 반납 부탁드립니다.')
                            #book.json 파일 수정
                            self.book[key][-1] = self.ID
                            self.book[key][-2] = f'{date.year}.{date.month}.{date.day}'
                            with open('books.json', 'w', encoding='utf-8') as f:
                                json.dump(self.book, f, ensure_ascii=False, indent=4)
                            break
                    else :
                        print(f'[ {key} : {q[key][0]} ]는 현재 대출 중 입니다.')
        self.second()
    
    def retu(self) :
        print()
        print('- 반납 -')
        q = {}
        j = 0
        for title, info in self.book.items() :
            if info[-1] == self.ID :
                # q[title] = info[0]
                q[title] = info
        overdue_days = {}
        
        if len(q) >=1 :
            print('[대출 목록]')
            i = 1
            for title, info in q.items() :
                due_str = info[-2]
                # due_date = datetime.datetime.strptime(due_str, '%Y.%m.%d')
                try:
                    due_date = datetime.datetime.strptime(due_str, '%Y.%m.%d')
                except ValueError:
                    print(f'{title} : 반납 날짜 형식이 잘못되어 연체 여부를 확인할 수 없습니다.')
                    continue
                today = datetime.datetime.now()
                if today > due_date :
                    days_overdue = (today - due_date).days
                    overdue_days[title] = days_overdue
                    status = f'현재 연체 중입니다. ({days_overdue}일 연체)'
                else : 
                    status = '정상 대출 중입니다.'
                print(f'{i}. {title} : {info[0]}. 기한 날짜: {due_str} → {status}')
                i += 1
            self.rn(q, j)
        else :
            print(f'현재 {self.ID}님이 대출한 책이 없습니다.')
            return
    
    def rn(self, q, j) :
        q = q
        i = 1
        j = j
        while True :
            print()
            a = input('반납 할 책의 번호를 입력해주세요. : ')
            if a.isdigit() :
                a = int(a)
                if 1 <= a <= len(q) :
                    name2 = list(q.keys())[a-1]
                    writer = q[name2][0]
                    b = input(f'{name2} : {writer}을(를) 반납하시겠습니까?(y/n) : ')
                    if b in ['y', 'Y', 'ㅛ'] :
                        #book.json 파일 수정
                        self.book[name2][-1] = "true"
                        self.book[name2][-2] = ""
                        with open('books.json', 'w', encoding='utf-8') as f:
                            json.dump(self.book, f, ensure_ascii=False, indent=4)
                        j += 1
                        del q[name2]
                        self.che()
                        c = input('추가적으로 반납을 진행하시겠나요?(y/n) : ')
                        if b in ['y', 'Y', 'ㅛ'] and j <= len(q) :
                            self.rn(q, j)
                            print('[대출 목록]')
                            for title, info in q.items() :
                                print(f'{i}. {title} : {info[0]}')
                                self.rn(q, j)
                                break
                        else :
                            self.second()
                            break
    
    def list(self) :
        print()
        print('- 현재 대출 목록 -')
        print()
        q = {}
        for title, info in self.book.items() :
            if info[-1] == self.ID :
                q[title] = info
        overdue_days = {}
        
        if len(q) >=1 :
            print(f'{self.ID}님의 대출 목록')
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
                print(status)
                print()
                print(f'{title} : {info[0]}. 반납 날짜: {due_str}')
        else :
            print(f'현재 {self.ID}님이 대출한 책이 없습니다.')
        self.second()
    
    def logout(self) :
        print()
        while True :
            a = input('로그 아웃 하시겠습니까?(y/n) :')
            if a in ['y', 'Y', 'ㅛ'] :
                print('로그아웃 되었습니다.')
                return 0
            else :
                self.second()
                break