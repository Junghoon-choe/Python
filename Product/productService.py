import Product.productDao as dao
import Product.productVO as prod
# 4번. init 클래스파일 참조.

class Service:
    def __init__(self):
        self.dao = dao.Dao()

    def addProduct(self):
        print('제품명, 가격, 수량 입력받아 Product객체 생성 후 dao.insert()로 추가')
        name = input("제품명 :")
        price = int(input("가격 :"))
        a = int(input("수랑 :"))

        self.dao.insert(prod.Product(name, price, a))

    def getProduct(self):
        print('검색할 번호 입력받아 dao.select()로 검색')
        num = int(input("num :"))  # 제품 입력받아서
        res = self.dao.select(num)  # dao에서 찾을 수 있도록 .
        # 제품이 있는지 확인.
        if res == None:
            print('없는 제품')
        else:
            res.printProduct()

    def editProduct(self):
        print('수정할 제품 번호와 새 가격 입력받아 dao.update()로 수정')
        num = int(input("num :"))  # 제품 입력받아서
        price = int(input("new price :"))
        p = prod.Product('', price, 0)
        p.num = num
        self.dao.update(p)

    def delProduct(self):
        print('삭제할 제품 번호 입력받아 dao.delete()로 삭제')
        num = int(input("num :"))  # 제품 입력받아서
        self.dao.delete(num)

    def printAll(self):
        print('dao.selectAll()로 전체 검색한 결과 출력')
        datas = self.dao.selectAll()
        for p in datas:
            p.printProduct()
