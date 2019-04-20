# Notice the prompt displaying the user's input on the same line
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

# Not exactly the same but corrected for the last comma.
print(f"So, you're {age} old, {height} tall, and {weight} heavy.")

print("First num:", end=' ')
num1 = float(input())
print("Second num:", end=' ')
num2 = float(input())
print("Sum is: {}".format(num1 + num2))
