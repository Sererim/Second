"""
    Input: 6782
    Output: 23
    
    Input: 0.56
    Output: 11
"""
from Errors import Errors

numbers: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.') # [0,10], len = 11


def main():
    enter: str = "NULL"
    num: int = 0
    
    while True:
        print("Program is running.\n")
        enter = str(input("Enter a number.\n"))
        for i in enter:
            for x in numbers:
                if i == x:
                    num += int(x)
                elif i not in numbers:
                    print(f"{Errors.message(0)}")
                    main()
        print(f"Sum of numbers in the number entered is: {num}")
        enter = input("Do you want to terminate the program Y/y ?\n")
        if enter == 'Y' or enter == 'y':
            break
        else:
            main()
    return 0


if __name__ == "__main__":
    main()    
    