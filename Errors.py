# file with a class for handling errors also has colors in it

class Errors:
       
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
        answer: list = [f"NaN.\n{Errors.color(1)}Not a number was entered!{Errors.color(6)}"
                        f"{Errors.color(2)}Number should be more than zero{Errors.color(6)}"
                        f""
                        f""
                        f""
                        f""
                        f""
                        f""
                        f""]
        return answer[msg]
