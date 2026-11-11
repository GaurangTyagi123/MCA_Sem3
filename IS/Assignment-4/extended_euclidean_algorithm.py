def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


if __name__ == "__main__":
    a:int = int(input("Enter a: "))
    b:int = int(input("Enter b: "))
    
    gcd,x,y = extended_gcd(a,b)
    print(f"coefficients: {x} {y}")
    print(f"equation : {a}({x}) + {b}({y}) = {gcd}")
