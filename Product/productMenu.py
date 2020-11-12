import Product.productService as service


class Menu:
    def __init__(self):
        self.service = service.Service()

    def run(self):
        prompt = """1. 추가\n2. 검색\n3. 수정\n4. 삭제\n5. 전체목록\n6. 종료"""
        while True:
            print(prompt)
            nummber = int(input("숫자 입력 :"))
            if nummber == 1:
                self.service.addProduct()
            elif nummber == 2:
                self.service.getProduct()
            elif nummber == 3:
                self.service.editProduct()
            elif nummber == 4:
                self.service.delProduct()
            elif nummber == 5:
                self.service.printAll()
            elif nummber == 6:
                break