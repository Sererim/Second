# file with a class for handling errors, generic messages and colors.

numbers: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.') # [0,10], len = 11

class Utils:
       
    @staticmethod
    def color(col: int):
        colors = ('\033[95m', #Header 0
                  '\033[94m', #Blue 1
                  '\033[96m', #Cyan 2
                  '\033[92m', #Green 3
                  '\033[93m', #Warning 4
                  '\033[91m', #Fail 5
                  '\033[0m', #ENDC 6
                  '\033[1m', #Bold 7
                  '\033[4m', #Underline 8
                  )
        return colors[col]

    @staticmethod
    def message(msg: int):
        answer: list = [f"NaN.\n{Utils.color(1)}Not a number was entered!{Utils.color(6)}",
                        f"{Utils.color(2)}Number should be more than zero{Utils.color(6)}",
                        f"Program is running.\n",
                        f"Do you want to terminate the program Y/y ?\n",
                        f"Enter a number.\n"]
        return answer[msg]

    @staticmethod
    def end_program() -> bool:
        enter: str = "NULL"
        print(Utils.message(3))
        enter = input()
        if enter == 'Y' or enter == 'y':
            return True
        else:
            return False
        
    @staticmethod
    def isanumber(enter: str) -> bool:
        for i in enter:
            if i not in numbers:
                print(f"{Utils.message(0)}")
                return False
        return True
    
    @staticmethod
    def isanumber_lst(enter: list) -> bool:
        for i in enter:
            if i not in numbers:
                print(f"{Utils.message(0)}")
                return False
        return True