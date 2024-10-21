def task3():
    alg1 = 0
    alg2 = 0

    n = 1
    flag = False

    while flag == False:
        alg1 = 0.0045 * (n**3)

        alg2 = (0.36 * (n**2)) + (0.15*n)

        if alg1 > alg2:
            flag = True
            print(f"The amount of iterations is:", n)
        else:
            n+=1


task3()