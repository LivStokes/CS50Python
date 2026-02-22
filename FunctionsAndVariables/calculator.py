# Various ways of printing calculations.
x = input("Whats x? ")
y = input("Whats y? ")
z = int(x) + int(y)
print(z)
# OR
x = int(input("Whats x? "))
y = int(input("Whats y? "))
print(x + y)
# OR
print(int(input("What's x? ")) + int(input("What's y? ")))
# OR
x = float(input("Whats x? "))
y = float(input("Whats y? "))
print(x + y)
x = float(input("Whats x? "))
y = float(input("Whats y? "))
print(round(x + y))
# Or
x = float(input("Whats x? "))
y = float(input("Whats y? "))
z = round(x + y)
print(z)
# OR
x = float(input("Whats x? "))
y = float(input("Whats y? "))
z = round(x + y)
print(f"{z}")
# OR
x = float(input("Whats x? "))
y = float(input("Whats y? "))
z = round(x + y)
print(f"{z:,}")
# Or
x = float(input("Whats x? "))
y = float(input("Whats y? "))
z = x / y
print(f"{z:.2f}")
# OR
def main():
        x = int(input("Whats x? "))
        print("x squared is", square(x))
def square(n)
    return n * n # n ** 2 # pow(n, 2)
main()