#Test Case Number 1
print("=== Challenge 1: Colletz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", current_number, end=" ")
while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = (current_number * 3) + 1
    print(current_number, end=" ")
    step_count = step_count + 1

print()
print(f"Steps: {step_count}")
print()

#Test case number 2
print("=== Challenge 2: Prime Number Checker ===")
num = int(input("Enter a number: "))

if num > 1:
    print(f"Testing divisors from 2 to {num - 1}...")
    for i in range(2, num - 1):
        if num % 1 == 0:
            print(f"{num} is not prime (divisable by 3")
            break
    else:
        print(f"{num} is prime:")
else:
    print(f"{num} is not prime")

print()

