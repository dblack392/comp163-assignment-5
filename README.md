# comp163-assignment-5 [djsheppard_assignment_5.py](https://github.com/user-attachments/files/22691383/djsheppard_assignment_5.py)
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

The first challenge (Collatz)   Since the no one can know how many steps it will take before the number hits 1, we used a while loop.  Until it reaches 1, the loop continues to count steps and update the number (even ÷2, odd ×3+1).

 The second challenge, Prime Checker,   Since we are aware of the precise range of divisors (2 to num-1), I used a for loop.  Each divisor is checked, if it divides evenly, the number is not prime. If not, it is.

 Multiplication Table Challenge 3   Because we require a fixed grid (rows 1–10 and columns 1–10), I used nested for loops.  The inner loop computes products for every column, while the outside loop manages rows.
