
# MIDTERM EXAMINATION

def match_a():
    print("Function match_a() \n")

    arnold1 = input("Enter 1st input:")
    arnold2 = input("Enter 2nd input:")
    arnold3 = input("Enter 3rd input:")

    arnold22 = []
    arnold33 = []
    arnold11 = []

    for i in arnold1:
        if len(i) != 1:  # exclude character
            if i == i[::-1]:  # Palindrome checker
                arnold11.append(i)

    for i in arnold2:
        if len(i) != 1:  # exclude character
            if i == i[::-1]:  # Palindrome checker
                arnold22.append(i)

    for i in arnold3:
        if len(i) != 1:  # exclude character
            if i == i[::-1]:  # Palindrome checker
                arnold33.append(i)

    print
    "1st output: ", len(arnold11)
    print
    "2nd output: ", len(arnold22)
    print
    "3rd output: ", len(arnold33)


match_a()
print("\n\n")


def front_x():
    print("Function front_x()\n")

    arnold1 = input("Enter 1st input:")
    arnold2 = input("Enter 2nd input:")
    arnold3 = input("Enter 3rd input:")

    arnold11 = []
    arnold111 = []
    arnold22 = []
    arnold222 = []
    arnold33 = []
    arnold333 = []

    for i in arnold1:
        if i.startswith('x'):  # new list of strings that starts with 'x' from others
            arnold11.append(i)
        else:
            arnold111.append(i)  # new list of other strings

    print
    "1st output: ", sorted(arnold11) + sorted(arnold111)  # to alphabetically arranged

    for i in arnold2:
        if i.startswith('x'):  # new list of strings that starts with 'x' from others
            arnold22.append(i)
        else:
            arnold222.append(i)  # new list of other strings

    print
    "2nd output: ", sorted(arnold22) + sorted(arnold222)  # to alphabetically arranged

    for i in arnold3:
        if i.startswith('x'):  # new list of strings that starts with 'x' from others
            arnold33.append(i)
        else:
            arnold333.append(i)  # new list of other strings

    print
    "3rd output: ", sorted(arnold33) + sorted(arnold333)  # to alphabetically arranged


front_x()