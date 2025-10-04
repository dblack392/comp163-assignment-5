#Test Case Number 1
print("=== Challenge 1: Collatz Conjecture ===")

#Geting a starting number from the user with an input
current_number = int(input("Enter starting number: "))
step_count = 0   # count how many steps it takes

#Print the sequence starting with the given number
print("Sequence:", current_number, end=" ")

#Loop until the number reaches 1
while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = (current_number * 3) + 1
    print(current_number, end=" ")
    step_count += 1

print("\n")
print(f"Steps: {step_count}")
print()


#Test Case Number 2
print("=== Challenge 2: Prime Number Checker ===")
num = int(input("Enter a number: "))

if num > 1:
    print(f"Testing divisors from 2 to {num - 1}...")
    for i in range(2, num):  #check divisibility properly
        if num % i == 0:
            print(f"{num} is not prime (divisible by {i})")
            break
    else:
        print(f"{num} is prime")
else:
    print(f"{num} is not prime")

print()


#Test Case Number 3
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

#Prints header row
print("    ", end="")
for header in range(1, 11):
    print(f"{header:4}", end="")
print()

#Prints each row in table
for row in range(1, 11):
    print(f"{row:2} ", end="")  #row label aligned
    for col in range(1, 11):
        table_value = row * col
        print(f"{table_value:4}", end="")
    print()  #new line at the end of the row

