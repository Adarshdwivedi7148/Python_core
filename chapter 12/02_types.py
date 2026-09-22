from typing import Tuple
person: Tuple[str,int] = ("Alice", 30)

# variable type hints
n : int = 5     
name : str = "Messi"

# function type hints
def add_numbers(a: int, b: int) -> int:  
    sum_result = a+b
    return sum_result

cd = add_numbers(2,3)
print(cd)

