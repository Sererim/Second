from Errors import Errors

class Count:
    
    num: int = 0
    numbers: list = [1]
    
    def __init__(self, n):
        self.num = n
    
    def calculate(self):
        if self.num <= 0:
            print(f"{Errors.message(1)}")
            return self.numbers
        for i in range(1, self.num + 1):
            self.numbers.append(self.numbers[i-1]*i)
        self.numbers = self.numbers[1:self.num + 1]
        return self.numbers
    
def main():
    val = Count(4)
    print(val.calculate())
    
    
if __name__ == "__main__":
    main()