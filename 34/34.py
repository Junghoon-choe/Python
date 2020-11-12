class Product:
    num=0
    def __init__(self,name, price, amount):
        self.num = Product.num+1
        self.name = name
        self.price = price
        self.amount = amount

    def printProduct(self):
        print('num:', self.num)
        print('name:', self.name)
        print('price:', self.price)
        print('amount:', self.amount)

class Dao:
    def __init__(self):
        self.prod = []

    def insert(self, p):
        print('제품추가. p는 Product 객체')

    def select(self, num):
        for idx, p in enumerate(self.prod):
            if num == p.num:
                return idx

    def getProduct(self, idx):
        return self.prod[idx]

    def update(self, p):#제품 가격만 수정
        print('제품 p를 번호로 찾아서 새 정보로 수정')

    def delete(self, num):
        print('제품 번호로 찾아서 삭제')

    def selectAll(self):
        return self.prod

class Service:
    def __init__(self):
        self.dao = Dao()

    def addProduct(self):
        print('제품명, 가격, 수량 입력받아 Product객체 생성 후 dao.insert()로 추가')

    def getProduct(self):
        print('검색할 번호 입력받아 dao.select()로 검색')

    def editProduct(self):
        print('수정할 제품 번호와 새 가격 입력받아 dao.update()로 수정')

    def delProduct(self):
        print('삭제할 제품 번호 입력받아 dao.delete()로 삭제')

    def printAll(self):
        print('dao.selectAll()로 전체 검색한 결과 출력')

class Menu:
    def __init__(self):
        self.service = Service()

    def run(self):
        while True:
            x = int(input('1.제품추가 2.제품검색 3.제품수정 4.제품삭제 5.전체목록 6.종료'))
            if x==1:
                self.service.addProduct()
            elif x==2:
                self.service.getProduct()
            elif x==3:
                self.service.editProduct()
            elif x==4:
                self.service.delProduct()
            elif x==5:
                self.service.printAll()
            elif x==6:
                break

def main():
    m = Menu()
    m.run()

main()