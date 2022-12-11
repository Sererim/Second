"""
    Input: 6782
    Output: 23
    
    Input: 0.56
    Output: 11
"""
from Utils import Utils

numbers: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.') # [0,10], len = 11


def main():
    enter: str = "NULL"
    num: int = 0
    
    while True:
        print(Utils.message(2))
        print(Utils.message(4))
        enter = str(input())
        for i in enter:
            for x in numbers:
                if i == x:
                    num += int(x)
                elif i not in numbers:
                    print(f"{Errors.message(0)}")
                    main()
        print(f"Sum of numbers in the number entered is: {num}")
        if Utils.end_program():
            break
        else:
            main()
    return 0


if __name__ == "__main__":
    main()    
    