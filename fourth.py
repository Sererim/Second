"""

Input: N generates a list [-N; N]
Output: list into a file.txt 

"""
from Utils import Utils


class Handle:

    def __init__(self) -> None:
        self.word = "NULL"
        self.temp = []
        self.position = []
        self.N = []
    
    def generate(self, n: int) -> None:
        for x in range(-n, n+1):
            self.N.append(x)
    
    def file_open(self) -> None:
        f = open("file.txt", 'r')
        self.word = f.read()
        self.temp = self.word.splitlines()
        f.close()
    
    def string_to_number(self) -> None:
        for i in range(len(self.temp)):
            self.position.append(int(self.temp[i]))

    def check_if_allowed(self) -> bool:
        for i in self.position:
            if 0 < i < len(self.N) - 1:
                return True
            else:
                return False

    def find_multiplication(self) -> int:
        num: int = 1
        for i in self.position:
            num *= self.N[i]
        return num
    
    def make_string_to_file(self):
        self.word = ""
        while True:
            print("Enter positional numbers")
            word = input()
            i = int(word)
            if not 0 < i < len(self.N) - 1:
                pass
            else:
                self.temp = word.splitlines()
                break
    
    def write_to_file(self):
        with open('file.txt', 'w') as f:
            for i in self.temp:
                f.write(f"{i}\n")
        f.close()
    
    def amend_a_file(self):
        with open("file.txt", 'a') as f:
            for i in self.temp:
                f.write(f"{i}\n")
        f.close()
        

def main() -> int:
    enter: str = "NULL"
    num: int = 0
    print(Utils.message(2))
    print(Utils.message(4))
    enter = str(input())        
    num = int(enter)
        
    work = Handle()
    work.generate(num)
    work.file_open()
    work.string_to_number()
    if not work.check_if_allowed():
        main()
    print(work.find_multiplication())
    while True:
        enter = input("Do you want to rewrite the file or amend it ?\n"
                      "Enter 1 to rewrite it.\nEnter 2 to amend it.\n"
                      "Enter Y or y to terminate the program.\n")
        if enter == "Y" or enter == "y":
            break
        elif enter == "1":
            work.write_to_file()
        elif enter == "2":
            work.amend_a_file()
        else:
            pass
    return 0
        

if __name__ == "__main__":
    main()
