input("What's your name? ")
print("hello, Olivia.")

# Another alternative
# Gradual state of print() function from worst to best solution of the most efficient output.
name = input("Whats your name? ")
print("hello, name")
# Or
name = input("Whats your name? ")
print("hello, " + name)
# Or
name = input("Whats your name? ")
print("hello,", name)
# Or
name = input("Whats your name? ")
print("hello, ")
print(name)
# Or
name = input("Whats your name? ")
print(f"hello, {name}")
# Or
name = input("Whats your name? ")
name = name.strip()
print(f"hello, {name}")
# Or
name = input("Whats your name? ")
name = name.strip()
name = name.title()
print(f"hello, {name}")
# Or
name = input("Whats your name? ")
name = name.strip.title()
print(f"hello, {name}")
# Or
name = input("Whats your name? ").strip().title()
print(f"hello, {name}")
#OR
def hello(to)
    print("hello, ", to)
name = input("Whats your name? ")
hello(name)
# OR
def hello(to="world"):
    print("hello, ", to)
name = input("Whats your name? ")
hello(name)
# OR
def main()
    name = input("Whatas your name? ")
    hello(name)

def hello(to="world"):
    print("hello," to)

main()