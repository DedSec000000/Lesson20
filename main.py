x = 1
while x < 10:
    print(x, "is smaller than 10")
    x += 1

t = 10
while t > 0:  # write a program that counts down from 10 to blastoff.
    print(t)
    t -= 1
print("blastoff")

N = int(input("N: "))
x = 1
print("Factors: ")
while x <= N:
    if N % x == 0:
        print(x)
    x += 1

x = int(input("Give me a number from 1 to 10: "))
while x < 1 or x > 10:
    print("No, that is not between 1 and 10.")
    x = int(input("Give me a number from 1 to 10."))

small = int(input("Give me small number:"))
large = int(input("Give me large number."))
remainder = large % small
while not remainder == 0:
    large = small
    small = remainder
    remainder = large & small
    print(small)
