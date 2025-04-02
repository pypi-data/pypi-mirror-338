import random
from string import ascii_letters

def genInteger(min: int=1, max: int=5) -> int:
    """
    Generate a random integer between min and max.
    """
    return random.randint(min, max)

def genDecimal(min: float=2, max: float=5) -> float:
    """
    Generate a random float between min and max.
    """     
    return random.uniform(min, max)

def genString(length: int=10) -> str:
    """
    Generate a random string of fixed length.
    """
    result = '' if length == 0 else ''.join(random.choice(ascii_letters) for i in range(length))
    return result

def genBool() -> bool:
    """
    Generate a random boolean value.
    """
    return random.choice([True, False])
