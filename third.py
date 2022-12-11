"""

Input: 3
Output: Dict = {1: 2, 2: 2.25; 3: 2.37, ..., n: (1 + (1/n))**n}, : n - key for dict, (1 + (1/n))**n i value.

"""
from Utils import Utils

numbers: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.') # [0,10], len = 11


def main() -> int:
    control: str
    num: int
    full = {1:1}
    small = {1:1}
    while True:
        print(Utils.message(2))
        print(Utils.message(4))
        control = str(input())
        if not Utils.isanumber(control):
            main()
                
        num = int(control)
        full.clear()
        for i in range(1, num + 1):
            small.clear()
            
            small = {i: (1 + (1/i))**i}
            full.update(small)
        print("{}".format(full))
        
        if Utils.end_program():
            break
        else:
            main()
    return 0
    
    
if __name__ == "__main__":
    main()
