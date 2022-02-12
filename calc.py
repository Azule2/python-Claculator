class calculator:
    def __init__(self,num1 = 0,num2 = 0):
        self.num1 = int (input('Enter First Number: '))
        self.num2 = int (input('Enter Second Number: '))
        self.run()

    def run(self):
        print('+ ,- ,* ,/ ')
        Selectnum = input('Select: ')
        while True:
            if Selectnum == '+':
                self.sum()
                break
            elif Selectnum == '-':
                self.sub()
                break
            elif Selectnum == '*':
                self.mul()
                break
            elif Selectnum == '/':
                self.div()
                break



    def sum(self):
        sum1 = self.num1 + self.num2
        print(sum1)

    def sub(self):
        sub1 = self.num1 - self.num2
        print(sub1)

    def div(self):
        div1 = self.num1 / self.num2
        print(div1)

    def mul(self):
        mul1 = self.num1 * self.num2
        print(mul1)

run = calculator()
