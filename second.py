"""

    Input: 4
    Output: [1, 2, 6, 24]
    [1, 1 * 2, 1 * 2 * 3, 1 * 2 * 3 * 4]
"""

from Errors import Errors

numbers: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')

class Count:
    
    num: int = 0
    numbers: list = [1]
    
    def __init__(self, n: int):
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
    control: str = "NULL"
    num: int = 0
    while True:
        print("Program is running.")
        control = str(input("Enter a number.\n"))
        for i in control:
            if i not in numbers:
                print(f"{Errors.message(0)}")
                main()
                
        num = int(control)
        val = Count(num)
        print(f"{repr(val.calculate())}")
        
        control = input("Do you want to terminate the program Y/y ?\n")
        if control == 'Y' or control == 'y':
            break
        else:
            main()
    return 0
    
    
if __name__ == "__main__":
    main()