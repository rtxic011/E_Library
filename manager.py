# from auth import SignUp, Login
# from main import Main, get_book

import json

class Manager() :
    def __init__ (self, books) :
        self.ID = 'none'    
        self.book = books
        
    def first(self, name) :
        self.ID = name
        print(f'오신 걸 환영합니다, 관리자님.')
        self.second()
    
    def second(self) :
        print()
        print('[ 1.도서추가  2.도서삭제 3.도서정보수정  0.종료 ]')
        a = input('메뉴를 선택해, 번호를 입력해주세요. : ')
        if a == '1' :
            self.add()
        elif a == '2' :
            self.delete()
        elif a == '3' :
            self.edit()
        elif a == '0' :
            return 0  

    def add(self):
        print()
        print('- 도서 추가 -')
        title = input('책 제목을 입력하세요: ')
        if title in self.book:
            print('이미 존재하는 책입니다.')
            return
        author = input('저자를 입력하세요: ')
        pubdate = input('출간일(예: 2023.01.15): ')
        publisher = input('출판사를 입력하세요: ')
        self.book[title] = [author, pubdate, publisher, "", "true"]
        with open('books.json', 'w', encoding='utf-8') as f:
            json.dump(self.book, f, ensure_ascii=False, indent=4)
        print(f'"{title}" 도서가 추가되었습니다.')

    def delete(self):
        print()
        print('- 도서 삭제 -')
        title = input('삭제할 책 제목을 입력하세요: ')
        if title in self.book:
            del self.book[title]
            with open('books.json', 'w', encoding='utf-8') as f:
                json.dump(self.book, f, ensure_ascii=False, indent=4)
            print(f'"{title}" 도서가 삭제되었습니다.')
        else:
            print('해당 책이 존재하지 않습니다.')

    def edit(self):
        print()
        print('- 도서 정보 수정 -')
        title = input('수정할 책 제목을 입력하세요: ')
        if title not in self.book:
            print('해당 책이 존재하지 않습니다.')
            return
        print(f'현재 정보: {self.book[title]}')
        author = input('새 저자 (엔터 시 변경 없음): ')
        pubdate = input('새 출간일 (엔터 시 변경 없음): ')
        publisher = input('새 출판사 (엔터 시 변경 없음): ')
        if author:
            self.book[title][0] = author
        if pubdate:
            self.book[title][1] = pubdate
        if publisher:
            self.book[title][2] = publisher
        with open('books.json', 'w', encoding='utf-8') as f:
            json.dump(self.book, f, ensure_ascii=False, indent=4)
        print(f'"{title}" 도서 정보가 수정되었습니다.')

    def loan(self):
        print()
        print('- 현재 대출 목록 -')
        i = 1
        found = False
        for title, info in self.book.items():
            if info[-1] != 'true':
                print(f'{i}. {title} : {info[0]} - 대출자: {info[-1]}, 반납기한: {info[-2]}')
                i += 1
                found = True
        if not found:
            print('현재 대출 중인 도서가 없습니다.')