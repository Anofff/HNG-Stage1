def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    return sum(int(digit) ** len(str(n)) for digit in str(n)) == n

def classify_number(n: int):
    properties = []
    
    if is_armstrong(n):
        properties.append("armstrong")
    
    properties.append("odd" if n % 2 != 0 else "even")

    return {
        "number": n,
        "is_prime": is_prime(n),
        "is_perfect": is_perfect(n),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(n))
    }
