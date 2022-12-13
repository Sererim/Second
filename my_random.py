"""

Create a random number generator.    

Generates a pseudo-random number form 0 to 10.


"""

from time import time_ns, sleep


class MyRandom:
    
    def __init__(self) -> None:
        
        numbers: list[int] = []
        new_numbers: list[int] = []
        
        for i in range(0,11):
            numbers.append(i)
            
        self.numbers = numbers
        self.new_numbers = new_numbers
        
    def knuth(self) -> int:
        
        n: int = 0
        k: int = 0
        
        while True:
            n = time_ns()
            sleep(0.005)
            k = int(repr(n)[-3])
            
            if k < len(self.numbers):
                self.new_numbers.append(self.numbers[k])
                self.numbers = self.numbers[:k] + self.numbers[k+1:]
                
            if len(self.numbers) == 0:
                break
            
        while True:
            n = time_ns()
            k = int(repr(n)[-3])
            
            if k < len(self.new_numbers) + 1:
                self.new_numbers = self.new_numbers[:k] + self.new_numbers[k+1:]
                
            if len(self.new_numbers) == 1:
                break
            
        return self.new_numbers[0]
        
        
def main() -> int:
    
    rand = MyRandom()
    print(f"| {rand.knuth()} |")
    return 0
    
    
if __name__ == "__main__":
    main()
