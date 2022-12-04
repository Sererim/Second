"""

Input: 3
Output: Dict = {1: 2, 2: 2.25; 3: 2.37, ..., n: (1 + (1/n))**n}, : n - key for dict, (1 + (1/n))**n i value.

"""
from Errors import Errors

numbers: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.') # [0,10], len = 11


def main() -> int:
    control: str
    num: int
    full = {1:1}
    small = {1:1}
    while True:
        print("Program is running.")
        control = str(input("Enter a number.\n"))
        for i in control:
            if i not in numbers:
                print(f"{Errors.message(0)}")
                main()
                
        num = int(control)
        full.clear()
        for i in range(1, num + 1):
            small.clear()
            
            small = {i: (1 + (1/i))**i}
            full.update(small)
        print("{}".format(full))
        
        control = input("Do you want to termiate the program Y/y ?\n")
        if control == 'Y' or control == 'y':
            break
        else:
            main()
    return 0
    
    
if __name__ == "__main__":
    main()