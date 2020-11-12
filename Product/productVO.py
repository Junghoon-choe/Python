class Product:
    cnt = 0  # 클래스 변수. 제품의 개수 카운팅

    def __init__(self, name, price, amount):  # 객체가 생성 될때마다 호출된다.
        Product.cnt += 1  # 중복되지 않게 카운트해준다.
        self.num = Product.cnt
        self.name = name
        self.price = price
        self.amount = amount

    def printProduct(self):
        print('num:', self.num)
        print('name:', self.name)
        print('price:', self.price)
        print('amount:', self.amount)