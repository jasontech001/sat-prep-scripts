import math

print("➗ Fraction Simplifier")
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

gcd = math.gcd(numerator, denominator)
simple_num = numerator // gcd
simple_den = denominator // gcd

print(f"Simplified fraction: {simple_num}/{simple_den}")
