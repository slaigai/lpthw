"""
1. True
2. False
3. False
4. True
5. True
6. True
7. False
8. True
9. False
10. False
11. True
12. False
13. True
14. False
15. False
16. False
17. True
18. True
19. False
20. False
"""

print("1.", True and True)
print("2.", False and True)
print("3.", 1 == 1 and 2 == 1)
print("4.", "test" == "test")
print("5.", 1 == 1 or 2 != 1)
print("6.", True and 1 == 1)
print("7.", False and 0 != 0)
print("8.", True or 1 == 1)
print("9.", "test" == "testing")
print("10.", 1 != 0 and 2 == 1)
print("11.", "test" != "testing")
print("12.", "test" == 1)
print("13.", not (True and False))
print("14.", not (1 == 1 and 0 != 1))
print("15.", not (10 == 1 or 1000 == 1000))
print("16.", not (1 != 10 or 3 == 4))
print("17.", not ("testing" == "testing" and "Zed" == "Cool Guy"))
print("18.", 1 == 1 and (not ("testing" == 1 or 1 == 0)))
print("19.", "chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print("20.", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))

print("Behavior of and, or, etc for returning vars")
print("AND returns first False operand found if False (0): ", 0 and "")
print("AND returns first False operand found if False (0): ", 1 and 0)
print("AND returns second operand if True (1): ", 1 and 1)
print("OR returns first True operand found if True (\"str1\"): ", "str1" or "str2")
print("OR returns first True operand found if True (\"nonempty string\"): ", "" or "nonempty string")
print("OR returns second operand if False (0): ", "" or 0)


