"""

    Input: 4
    Output: [1, 2, 6, 24]
    [1, 1 * 2, 1 * 2 * 3, 1 * 2 * 3 * 4]
"""

from Utils import Utils


class Count:
    
    num: int = 0
    numbers: list = [1]
    
    def __init__(self, n: int):
        self.num = n
    
    def calculate(self):
        if self.num <= 0:
            print(f"{Utils.message(1)}")
            return self.numbers
        for i in range(1, self.num + 1):
            self.numbers.append(self.numbers[i-1]*i)
        self.numbers = self.numbers[1:self.num + 1]
        return self.numbers
    
def main():
    control: str = "NULL"
    num: int = 0
    while True:
        print(Utils.message(2))
        print(Utils.message(4))
        control = str(input())
        if not Utils.isanumber(control):
            main()
                
        num = int(control)
        val = Count(num)
        print(f"{repr(val.calculate())}")
        
        if Utils.end_program():
            break
        else:
            main()
    return 0
    
if __name__ == "__main__":
    main()
