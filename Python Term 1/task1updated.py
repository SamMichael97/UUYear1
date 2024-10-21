def task1():
    value = int(input('Enter the number you want to sum'))
    total = 0
    mlist = list(range(value + 1))
    elist = []

    for number in mlist:
        if number % 2 == 0:
            total += number
            elist.append(number)

    elist.pop(0)

    print(f"The total sum of even numbers up to", value, "is", total)

task1()



