# Answers to questions from Study Drills of ex29
#
# 1. if-statment creates a branch in code. "If this Boolean expression is True, then run the code under it,
# otherwise skip it."
#
# 2. The colon at the end of the line will tell Python that you're starting a new block of code. Indenting four
# spaces tells Python what lines of code are in that block
#
# 3. Probably an error because python expects a level of indentation after a colon
#
# 4. Yeah you can
#
# 5. Okay

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("we still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
