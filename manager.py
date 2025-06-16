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
        print('[ 1.도서추가  2.도서삭제  3.도서정보수정  4.도서상태수정  5.도서조회 0.종료 ]')
        a = input('메뉴를 선택해, 번호를 입력해주세요. : ')
        if a == '1' :
            self.add()
        elif a == '2' :
            self.delete()
        elif a == '3' :
            self.edit()
        elif a == '4':
            self.edit_status()
        elif a == '0' :
            return 0
        
    
    def search(self):
        print()
        print('- 도서 조회 -')
        q = {}
        while True:
            print('찾고 있는 책의 제목, 작가 등을 입력해주세요.')
            print('모든 책 목록을 보시려면 엔터를 누르시면 됩니다.')
            a = input('입력하기 : ')
            i = 1
            print()
            print('[ 검색 결과 ]')
            a = a.lower()
            q, i = self.sear(a, q, False, i)
            a = a.upper()
            q, i = self.sear(a, q, True, i)
            if q:
                break

    def sear(self, a, q, f, i):
        for title, inf in self.book.items():
            info = inf[:3]
            if a in title or a in info:
                if inf[-1] == 'true':
                    ch = '대출 가능'
                else:
                    ch = '대출 중'
                print(f'{i}. {title} : {info[0]} [{ch}]')
                q[title] = info
                i += 1
                f = True
        if not f:
            print('검색 결과가 없습니다. 다시 시도해주세요.')
        return q, i

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
        while True:
            confirm = input(f'{title} : 작가, {author}.  출판일, {pubdate}. 출판사, {publisher}. 도서를 추가하시겠습니까? (y/n): ')
            if confirm in ['y', 'Y', 'ㅛ']:
                self.book[title] = [author, pubdate, publisher, "", "true"]
                with open('books.json', 'w', encoding='utf-8') as f:
                    json.dump(self.book, f, ensure_ascii=False, indent=4)
                print(f'"{title}" 도서가 추가되었습니다.')
                break
            elif confirm == 'n':
                print('도서 추가가 취소되었습니다.')
                break
            else:
                print("y 또는 n을 입력해주세요.")

    def delete(self):
        print()
        print('- 도서 삭제 -')
        title = input('삭제할 책 제목을 입력하세요: ')
        if title in self.book:
            while True:
                confirm = input(f'"{title}" 도서를 삭제하시겠습니까? (y/n): ')
                if confirm in ['y', 'Y', 'ㅛ']:
                    del self.book[title]
                    with open('books.json', 'w', encoding='utf-8') as f:
                        json.dump(self.book, f, ensure_ascii=False, indent=4)
                    print(f'"{title}" 도서가 삭제되었습니다.')
                    break
                elif confirm == 'n':
                    print('도서 삭제가 취소되었습니다.')
                    break
                else:
                    print("y 또는 n을 입력해주세요.")
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
        while True:
            confirm = input(f'"{title}" 도서 정보를 수정하시겠습니까? (y/n): ')
            if confirm in ['y', 'Y', 'ㅛ']:
                if author:
                    self.book[title][0] = author
                if pubdate:
                    self.book[title][1] = pubdate
                if publisher:
                    self.book[title][2] = publisher
                with open('books.json', 'w', encoding='utf-8') as f:
                    json.dump(self.book, f, ensure_ascii=False, indent=4)
                print(f'"{title}" 도서 정보가 수정되었습니다.')
                break
            elif confirm == 'n':
                print('도서 정보 수정이 취소되었습니다.')
                break
            else:
                print("y 또는 n을 입력해주세요.")
    
    def edit_status(self):
        print()
        print('- 도서 상태 수정 -')
        title = input('상태를 수정할 책 제목을 입력하세요: ')
        if title not in self.book:
            print('해당 책이 존재하지 않습니다.')
            return
        info = self.book[title]
        status = "대출 가능" if info[-1] == "true" else "대출 중"
        borrower = "-" if info[-1] == "true" else info[-1]
        print(f'\n→ 현재 도서 상태: {status}, 대출자: {borrower}, 반납 기한: {info[-2]}')

        new_due = input('새 반납 기한 (예: 2024.06.30, 엔터 시 변경 없음): ')
        new_borrower = input('새 대출자 이름 (예: 사용자 ID, 또는 "true"로 설정, 엔터 시 변경 없음): ')

        print(f'→ 변경 예정: 반납 기한: {new_due if new_due else info[-2]}, 대출자: {new_borrower if new_borrower else info[-1]}')

        while True:
            confirm = input(f'"{title}" 도서 상태를 위와 같이 수정하시겠습니까? (y/n): ')
            if confirm.lower() in ['y', 'ㅛ']:
                if new_due:
                    info[-2] = new_due
                if new_borrower:
                    info[-1] = new_borrower
                self.book[title] = info
                with open('books.json', 'w', encoding='utf-8') as f:
                    json.dump(self.book, f, ensure_ascii=False, indent=4)
                print(f'"{title}" 도서 상태가 수정되었습니다.')
                break
            elif confirm.lower() == 'n':
                print('도서 상태 수정이 취소되었습니다.')
                break
            else:
                print("y 또는 n을 입력해주세요.")