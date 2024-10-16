percentage = float(input("Enter your percentage: "))
if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Not good")

#nomer 2
# Input: Three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1, num2, num3)  # Use the max() function
print(f"The largest number is: {largest}")

#nomer 3
def fibonacci(n):
    a,b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
n = int(input("Masukkan deret fibonacci: "))
fibonacci(n)



#nomer 4
n = int(input("Masukkan nilai n untuk bilangan ganjil: "))
for steps in range(1, n, 2) :
    print(steps)


#nomer 5
# Function to print the pattern
def print_pattern(n):
    for i in range(1, n+1):
        # Print the current number i, repeated i times, with space between
        print(" ".join([str(i)] * i))

# Input value for n
n = int(input("Enter a number n to generate the pattern: "))

# Print the pattern
print_pattern(n)

