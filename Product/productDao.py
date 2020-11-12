class Dao:  # 저장소 : 저장, 검색, 수정, 삭제
    def __init__(self):  # 생성자로 리스트를 사용했다.
        self.prod = []

    def insert(self, p):  # 프로덕트
        print('제품추가. p는 Product 객체')
        self.prod.append(p)  # 파라메터로 받아온 프로덕트 객체를 추가해준다.

    def select(self, num):  # 제품번호로 검색하여 그 위치를 반환해준다.
        for p in self.prod:  # 반복문으로 제품의 인덱스와 내용을 가져올수 있게 선언해준다.
            if num == p.num:  # 파라메터값으로 받아온 숫자와 제품의 번호와 같으면
                return p  # 해당 인덱스를 리턴으로 반환해준다.

    def update(self, p):  # 제품 가격만 수정
        print('제품 p를 번호로 찾아서 새 정보로 수정')  # 제품이 있는가 확인하고, 있다면 수정이 가능하게 구현,
        res = self.select(p.num)
        if res != None:
            res.price = p.price
        else:
            print("없는 제품")

    def delete(self, num):
        print('제품 번호로 찾아서 삭제')
        res = self.select(num)
        if res != None:
            self.prod.remove(res)
        else:
            print("없는 제품")

    def selectAll(self):
        return self.prod