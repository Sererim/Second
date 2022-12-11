"""

Input: N generates a list [-N; N]
Output: list into a file.txt 

"""
from Utils import Utils


numbers: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.') # [0,10], len = 11



def main() -> int:
    num: int
    control: str
    nums = []
    while True:
        print("Program is running.")
        control = str(input("Enter a number.\n"))
        for i in control:
            if i not in numbers:
                print(f"{Errors.message(0)}")
                main()
        num = int(control)
        
        for i in range(-num, num + 1):
            nums.append(i)
        print(f"{nums}")
        break
    
    return 0
    
    
if __name__ == "__main__":
    main()